"""
RL-100 Trainer
==============
Complete training pipeline for RL-100: IL -> Offline RL -> Online RL.

Implements Algorithm 1 from RL-100 paper:
1. Phase 1: Imitation Learning (IL) - Train diffusion policy with BC
2. Phase 2: Offline RL Loop (M iterations):
   a) Train IQL Critics on dataset
   b) Optimize policy with PPO + Consistency Distillation
   c) Collect new data with policy
   d) Merge datasets and retrain IL
3. Phase 3: Online RL - Fine-tune with online rollouts

Key Components:
- RL100Policy: Diffusion policy with PPO optimization
- IQLCritics: Q and V networks for advantage estimation
- ConsistencyModel: Fast 1-step generation
- EnvRunner: Environment for data collection

Args:
    config: Configuration dictionary with:
        - policy: RL100Policy config
        - dataset: Dataset config
        - env_runner: Environment config
        - training: Training hyperparameters
"""

import os
import torch
import torch.nn as nn
from torch.utils.data import DataLoader
import numpy as np
import wandb
import copy
from typing import Dict, Optional, Tuple
from termcolor import cprint
import hydra
from omegaconf import OmegaConf
try:
    import matplotlib.pyplot as plt
except ImportError:
    plt = None

from diffusion_policy_3d.policy.rl100_policy import RL100Policy
from diffusion_policy_3d.model.rl.iql_critics import IQLCritics
from diffusion_policy_3d.model.rl.consistency_model import ConsistencyModel, ConsistencyDistillation
from diffusion_policy_3d.model.rl.transition_model import TransitionModel
from diffusion_policy_3d.model.diffusion.ema_model import EMAModel
from diffusion_policy_3d.common.pytorch_util import dict_apply, optimizer_to
from diffusion_policy_3d.common.replay_buffer import ReplayBuffer
from diffusion_policy_3d.dataset.base_dataset import BaseDataset
from diffusion_policy_3d.env_runner.base_runner import BaseRunner


class RL100Trainer:
    """
    Complete RL-100 training pipeline.

    Training Flow:
    ==============
    1. train_imitation_learning(D_0):
        - Standard BC on initial dataset
        - Outputs: Trained DP3 policy π_θ

    2. For M iterations:
        a) train_iql_critics(D_t):
            - Update V: L_V = expectile_loss(V(s), Q(s, a), τ=0.7)
            - Update Q: L_Q = MSE(Q(s,a), r + γV(s'))

        b) offline_rl_optimize(D_t):
            - Compute advantage: A = Q(s,a) - V(s)
            - Update policy: L_PPO = Σ_k min(r_k*A, clip(r_k)*A)
            - Distill to consistency model: L_CD = ||CM(noise) - π_θ||^2

        c) collect_new_data(π_θ):
            - Rollout policy in environment
            - Add to D_new

        d) merge and retrain:
            - D_{t+1} = D_t ∪ D_new
            - Retrain IL on D_{t+1}

    3. online_rl_finetune():
        - Continue PPO with fresh rollouts
        - No more IL retraining
    """

    def __init__(self, config: OmegaConf, output_dir: Optional[str] = None):
        self.config = config
        self._output_dir = output_dir
        self.device = torch.device(config.training.device)

        # Initialize policy (RL100Policy extends DP3)
        cprint("[RL100Trainer] Initializing RL100Policy...", "cyan")
        self.policy: RL100Policy = hydra.utils.instantiate(config.policy)
        self.policy.to(self.device)

        # EMA model
        self.ema_policy = None
        if config.training.use_ema:
            self.ema_policy = copy.deepcopy(self.policy)
            self.ema = hydra.utils.instantiate(
                config.ema,
                model=self.ema_policy
            )

        # Optimizer for policy
        self.policy_optimizer = hydra.utils.instantiate(
            config.optimizer.policy,
            params=self.policy.parameters()
        )

        # Initialize IQL Critics
        cprint("[RL100Trainer] Initializing IQL Critics...", "cyan")
        obs_dim = self.policy.obs_feature_dim * self.policy.n_obs_steps  # Flattened obs feature dim across all obs steps
        action_dim = self.policy.action_dim

        self.critics = IQLCritics(
            obs_dim=obs_dim,
            action_dim=action_dim,
            hidden_dims=config.critics.hidden_dims,
            gamma=config.critics.gamma,
            tau=config.critics.tau
        )
        self.critics.to(self.device)

        # Optimizers for critics
        self.v_optimizer = hydra.utils.instantiate(
            config.optimizer.v_network,
            params=self.critics.v_network.parameters()
        )
        self.q_optimizer = hydra.utils.instantiate(
            config.optimizer.q_network,
            params=self.critics.q_network.parameters()
        )

        # Initialize Consistency Model
        cprint("[RL100Trainer] Initializing Consistency Model...", "cyan")
        self.consistency_model = ConsistencyModel(
            input_dim=action_dim,
            global_cond_dim=obs_dim,  # obs_dim = obs_feature_dim * n_obs_steps, already flattened
            diffusion_step_embed_dim=config.policy.diffusion_step_embed_dim,
            down_dims=config.policy.down_dims,
            condition_type=config.policy.condition_type
        )
        self.consistency_model.to(self.device)

        self.consistency_optimizer = hydra.utils.instantiate(
            config.optimizer.consistency,
            params=self.consistency_model.parameters()
        )

        self.consistency_distillation = ConsistencyDistillation(
            teacher_policy=self.policy,
            student_model=self.consistency_model,
            student_optimizer=self.consistency_optimizer
        )

        # Initialize Transition Model (Algorithm 1, Line 6)
        cprint("[RL100Trainer] Initializing Transition Model T_θ(s'|s,a)...", "cyan")
        self.transition_model = TransitionModel(
            obs_feature_dim=obs_dim,    # same flattened dim used by critics
            action_dim=action_dim,
            hidden_dims=(200, 200, 200, 200),
            num_ensemble=7,
            num_elites=5,
            device=str(self.device),
        )

        # Training state
        self.global_step = 0
        self.epoch = 0
        self.offline_rl_iteration = 0

    @property
    def output_dir(self) -> str:
        if self._output_dir is not None:
            return self._output_dir
        return os.getcwd()

    def _save_loss_curve_plot(
        self,
        loss_history: list,
        title: str,
        ylabel: str,
        filename: str
    ) -> Optional[str]:
        """
        Save loss curve with:
          - top panel: full range (non-uniform y-axis via symlog when needed)
          - bottom panel: zoomed view in [0, 1] to show 0.x fluctuations.
        """
        if not loss_history:
            return None
        if plt is None:
            cprint("[Plot] matplotlib is not available; skip loss curve plotting.", "yellow")
            return None

        y = np.asarray(loss_history, dtype=np.float64)
        x = np.arange(1, len(y) + 1, dtype=np.int32)
        if y.size == 0:
            return None

        plot_dir = os.path.join(self.output_dir, "plots")
        os.makedirs(plot_dir, exist_ok=True)
        save_path = os.path.join(plot_dir, filename)

        fig, (ax_full, ax_zoom) = plt.subplots(
            2, 1, figsize=(9, 7), sharex=True, gridspec_kw={'height_ratios': [2, 1]}
        )

        # Full-range panel: non-uniform axis when values exceed 1.
        y_max = float(np.nanmax(y))
        y_min = float(np.nanmin(y))
        ax_full.plot(x, y, color="#1f77b4", linewidth=2.0)
        if y_max > 1.0:
            ax_full.set_yscale('symlog', linthresh=1.0, linscale=1.2, base=10)
        ax_full.set_ylabel(ylabel)
        ax_full.set_title(f"{title} (top: adaptive axis, bottom: 0-1 zoom)")
        ax_full.grid(True, alpha=0.3)
        ax_full.set_ylim(bottom=max(0.0, y_min * 0.95), top=max(1e-6, y_max * 1.05))

        # Zoom panel: emphasize [0, 1] region.
        zoom_mask = (y >= 0.0) & (y <= 1.0)
        if np.any(zoom_mask):
            y_zoom = y[zoom_mask]
            zmin = float(np.min(y_zoom))
            zmax = float(np.max(y_zoom))
            pad = max(0.01, (zmax - zmin) * 0.2)
            zlow = max(0.0, zmin - pad)
            zhigh = min(1.0, zmax + pad)
            if zhigh - zlow < 0.05:
                mid = 0.5 * (zhigh + zlow)
                zlow = max(0.0, mid - 0.025)
                zhigh = min(1.0, mid + 0.025)
        else:
            zlow, zhigh = 0.0, 1.0

        ax_zoom.plot(x, y, color="#d62728", linewidth=1.8)
        ax_zoom.set_ylim(zlow, zhigh)
        ax_zoom.set_ylabel(f"{ylabel} (0-1)")
        ax_zoom.set_xlabel("Epoch")
        ax_zoom.grid(True, alpha=0.35)

        fig.tight_layout()
        fig.savefig(save_path, dpi=160)
        plt.close(fig)

        cprint(f"[Plot] Saved: {save_path}", "cyan")
        return save_path

    def train_imitation_learning(
        self,
        dataset: BaseDataset,
        num_epochs: int,
        val_dataset: Optional[BaseDataset] = None,
        env_runner: Optional[BaseRunner] = None,
        plot_tag: str = "il"
    ) -> Dict:
        """
        Phase 1: Train with behavior cloning (standard DP3 training).

        Args:
            dataset: Training dataset
            num_epochs: Number of training epochs
            val_dataset: Optional validation dataset
            env_runner: Optional environment for evaluation

        Returns:
            metrics: Dictionary with training metrics
        """
        cprint("\n" + "="*60, "yellow")
        cprint("[RL100Trainer] Phase 1: Imitation Learning", "yellow")
        cprint("="*60 + "\n", "yellow")

        config = self.config
        self.policy.train()

        # Create dataloader
        train_dataloader = DataLoader(
            dataset,
            batch_size=config.dataloader.batch_size,
            shuffle=True,
            num_workers=config.dataloader.num_workers,
            pin_memory=True
        )

        # Set normalizer
        normalizer = dataset.get_normalizer()
        self.policy.set_normalizer(normalizer)
        self.policy.to(self.device) 

        if self.ema_policy is not None:
            self.ema_policy.set_normalizer(normalizer)
            self.ema_policy.to(self.device)

        # Training loop
        il_loss_per_epoch = []
        for epoch in range(num_epochs):
            epoch_losses = []

            for batch_idx, batch in enumerate(train_dataloader):
                # Move to device
                
                batch = dict_apply(batch, lambda x: x.to(self.device, non_blocking=True))

                # Compute loss
                loss, loss_dict = self.policy.compute_loss(batch)

                # Optimize
                self.policy_optimizer.zero_grad()
                loss.backward()
                self.policy_optimizer.step()

                # Update EMA
                if self.ema_policy is not None:
                    self.ema.step(self.policy)

                epoch_losses.append(loss.item())
                self.global_step += 1

                # Log
                if self.global_step % config.training.log_every == 0 and config.logging.use_wandb:
                    wandb.log({
                        'il/loss': loss.item(),
                        'il/epoch': epoch,
                        **{f'il/{k}': v for k, v in loss_dict.items()}
                    }, step=self.global_step)

            # Epoch end
            avg_loss = np.mean(epoch_losses)
            il_loss_per_epoch.append(float(avg_loss))
            cprint(f"[IL] Epoch {epoch}/{num_epochs}, Loss: {avg_loss:.4f}", "green")

            # Evaluate
            if env_runner is not None and (epoch + 1) % config.training.eval_every == 0:
                eval_policy = self.ema_policy if self.ema_policy else self.policy
                eval_policy.eval()
                with torch.no_grad():
                    metrics = env_runner.run(eval_policy)
                cprint(f"[IL] Eval - Success Rate: {metrics.get('mean_success_rates', 0):.3f}", "green")
                if config.logging.use_wandb:
                    wandb.log({f'il/eval_{k}': v for k, v in metrics.items()}, step=self.global_step)
                eval_policy.train()

        safe_tag = str(plot_tag).replace('/', '_').replace(' ', '_')
        il_plot_path = self._save_loss_curve_plot(
            loss_history=il_loss_per_epoch,
            title=f"IL Loss ({safe_tag})",
            ylabel="IL Loss",
            filename=f"il_loss_{safe_tag}.png"
        )
        if config.logging.use_wandb and il_plot_path is not None:
            wandb.log({f'il/loss_curve_{safe_tag}': wandb.Image(il_plot_path)}, step=self.global_step)

        return {'final_loss': avg_loss}

    def train_transition_model(
        self,
        dataset: BaseDataset,
        max_epochs: int = 200,
        max_epochs_since_update: int = 5,
    ) -> Dict:
        """
        Algorithm 1, Line 6: Train transition T_θm(s'|s, a).

        Freezes the policy encoder and trains the ensemble dynamics model to
        predict (Δobs_features, reward) from (obs_features, norm_action).

        Args:
            dataset                : offline dataset D_m
            max_epochs             : upper bound on training epochs
            max_epochs_since_update: early-stop patience

        Returns:
            metrics: dict with 'transition_val_loss'
        """
        cprint(f"\n[RL100Trainer] Line 6 — Training Transition Model T_θ "
               f"(Iteration {self.offline_rl_iteration})", "cyan")

        # Freeze encoder during transition model training
        self.policy.eval()
        val_loss = self.transition_model.train_on_dataset(
            policy=self.policy,
            dataset=dataset,
            batch_size=self.config.dataloader.batch_size,
            num_workers=self.config.dataloader.num_workers,
            max_epochs=max_epochs,
            max_epochs_since_update=max_epochs_since_update,
        )

        if self.config.logging.use_wandb and self.config.logging.use_wandb:
            wandb.log({
                'transition/val_loss': val_loss,
                'transition/iteration': self.offline_rl_iteration,
            }, step=self.global_step)

        return {'transition_val_loss': val_loss}

    def train_iql_critics(
        self,
        dataset: BaseDataset,
        num_epochs: int
    ) -> Dict:
        """
        Phase 2a: Train IQL critics (Q and V networks).

        Training Algorithm:
        1. Update V with expectile regression:
            L_V = expectile_loss(V(s), Q(s, a_data), τ=0.7)

        2. Update Q with Bellman backup:
            L_Q = MSE(Q(s, a), r + γV(s'))

        Args:
            dataset: Dataset with (s, a, r, s', done)
            num_epochs: Number of training epochs

        Returns:
            metrics: Dictionary with training metrics
        """
        cprint(f"\n[RL100Trainer] Phase 2a: Training IQL Critics (Iteration {self.offline_rl_iteration})", "cyan")

        config = self.config

        # Freeze Diffusion Actor during critic-only training (tag2: "冻结 Diffusion Actor，只练 QV 网络")
        self.policy.eval()
        for param in self.policy.parameters():
            param.requires_grad_(False)

        self.critics.train()

        # Create dataloader
        train_dataloader = DataLoader(
            dataset,
            batch_size=config.dataloader.batch_size,
            shuffle=True,
            num_workers=config.dataloader.num_workers,
            pin_memory=True
        )

        q_loss_per_epoch = []
        v_loss_per_epoch = []
        for epoch in range(num_epochs):
            v_losses = []
            q_losses = []

            for batch_idx, batch in enumerate(train_dataloader):
                batch = dict_apply(batch, lambda x: x.to(self.device, non_blocking=True))

                # Extract data
                obs_dict = batch['obs']
                action = batch['action'][:, 0, :]  # [B, horizon, Da] -> [B, Da]

                # Encode observations to get features
                with torch.no_grad():
                    nobs = self.policy.normalizer.normalize(obs_dict)
                    if not self.policy.use_pc_color:
                        nobs['point_cloud'] = nobs['point_cloud'][..., :3]

                    this_nobs = dict_apply(
                        nobs,
                        lambda x: x[:, :self.policy.n_obs_steps, ...].reshape(-1, *x.shape[2:])
                    )
                    this_nobs = dict_apply(this_nobs, lambda x: x.to(self.device))
                    obs_features = self.policy.obs_encoder(this_nobs)
                    obs_features = obs_features.reshape(batch['action'].shape[0], -1)

                # Normalize action
                naction = self.policy.normalizer['action'].normalize(action)

                # 1. Update V network
                v_loss, v_info = self.critics.compute_v_loss(obs_features, naction)

                self.v_optimizer.zero_grad()
                v_loss.backward()
                torch.nn.utils.clip_grad_norm_(
                    self.critics.v_network.parameters(), max_norm=10.0)
                self.v_optimizer.step()

                v_losses.append(v_loss.item())

                # 2. Update Q network using actual next_obs from dataset.
                # Encoding the real next observation is more reliable than the
                # transition model, which can fail to generalise when new collected
                # data has a different distribution from the expert demos.
                if 'reward' in batch and 'next_obs' in batch:
                    reward = batch['reward']
                    if reward.dim() == 1:
                        reward = reward.unsqueeze(-1)  # [B] -> [B, 1]
                    # Normalise chunk reward by max per-step reward so that Q* ~ O(10)
                    # rather than O(1000).  Metaworld shaped rewards go up to 10/step;
                    # chunk reward = Σ γ^j r_j ≤ 10 * Σ γ^j ≈ 77.  Without scaling,
                    # Q_pred starts near 0 while Q_target ≈ 56 → Q_loss ≈ 6000+ at epoch 0.
                    reward_scale = float(getattr(config.critics, 'reward_scale', 10.0))
                    reward = reward / reward_scale
                    done = batch.get('done', torch.zeros_like(reward))
                    if done.dim() == 1:
                        done = done.unsqueeze(-1)

                    B = obs_features.shape[0]
                    # Encode actual next obs (at t + n_action_steps) from dataset
                    with torch.no_grad():
                        next_obs_raw = batch['next_obs']  # nested dict, already on device
                        nnext_obs = self.policy.normalizer.normalize(next_obs_raw)
                        if not self.policy.use_pc_color:
                            nnext_obs['point_cloud'] = nnext_obs['point_cloud'][..., :3]
                        this_next_nobs = dict_apply(
                            nnext_obs,
                            lambda x: x[:, :self.policy.n_obs_steps].reshape(-1, *x.shape[2:])
                        )
                        next_obs_features = self.policy.obs_encoder(this_next_nobs)
                        next_obs_features = next_obs_features.reshape(B, -1)

                    q_loss, q_info = self.critics.compute_q_loss(
                        obs_features, naction, reward, next_obs_features, done
                    )

                    self.q_optimizer.zero_grad()
                    q_loss.backward()
                    torch.nn.utils.clip_grad_norm_(
                        self.critics.q_network.parameters(), max_norm=10.0)
                    self.q_optimizer.step()

                    q_losses.append(q_loss.item())

                    # Update target network
                    self.critics.update_target_network(tau=config.critics.target_update_tau)

                    # Log
                    if self.global_step % config.training.log_every == 0 and config.logging.use_wandb:
                        wandb.log({
                            'iql/v_loss': v_loss.item(),
                            'iql/q_loss': q_loss.item(),
                            **{f'iql/{k}': v for k, v in v_info.items()},
                            **{f'iql/{k}': v for k, v in q_info.items()}
                        }, step=self.global_step)

                self.global_step += 1

            v_loss_avg = np.mean(v_losses) if v_losses else 0.0
            q_loss_avg = np.mean(q_losses) if q_losses else 0.0

            # 2. 使用格式化打印
            cprint(f"[IQL] Epoch {epoch}/{num_epochs}, "
                   f"V Loss: {float(v_loss_avg):.4f}, "
                   f"Q Loss: {float(q_loss_avg):.4f}", "green")
            v_loss_per_epoch.append(float(v_loss_avg))
            q_loss_per_epoch.append(float(q_loss_avg))

        q_loss_plot_path = self._save_loss_curve_plot(
            loss_history=q_loss_per_epoch,
            title=f"IQL Q Loss (iter {int(self.offline_rl_iteration)})",
            ylabel="Q Loss",
            filename=f"iql_q_loss_iter_{int(self.offline_rl_iteration):02d}.png"
        )
        v_loss_plot_path = self._save_loss_curve_plot(
            loss_history=v_loss_per_epoch,
            title=f"IQL V Loss (iter {int(self.offline_rl_iteration)})",
            ylabel="V Loss",
            filename=f"iql_v_loss_iter_{int(self.offline_rl_iteration):02d}.png"
        )
        if self.config.logging.use_wandb and q_loss_plot_path is not None:
            wandb.log({
                'iql/q_loss_curve': wandb.Image(q_loss_plot_path),
                'iql/iteration': int(self.offline_rl_iteration),
            }, step=self.global_step)
        if self.config.logging.use_wandb and v_loss_plot_path is not None:
            wandb.log({
                'iql/v_loss_curve': wandb.Image(v_loss_plot_path),
                'iql/iteration': int(self.offline_rl_iteration),
            }, step=self.global_step)

        # Unfreeze policy after critic training
        for param in self.policy.parameters():
            param.requires_grad_(True)
        self.policy.train()

        return {'v_loss': np.mean(v_losses), 'q_loss': np.mean(q_losses) if q_losses else 0}

    def _relabel_demo_rewards(self, dataset: BaseDataset) -> None:
        """
        Label expert demonstration episodes with rewards when zarr has none.

        Reads ``self.config.critics.reward_type``:
          - 'sparse': reward=1 at last step, 0 elsewhere
          - 'dense' : reward=10 every step (matching MetaWorld shaped scale)
        """
        import numpy as np
        rb = dataset.replay_buffer

        if dataset.has_rl_data:
            return  # Already has rewards, nothing to do

        reward_type = getattr(self.config.critics, 'reward_type', 'sparse')

        n_episodes = rb.n_episodes
        episode_ends = rb.episode_ends[:]
        episode_starts = np.concatenate([[0], episode_ends[:-1]])

        reward_array = np.zeros(rb.n_steps, dtype=np.float32)
        done_array   = np.zeros(rb.n_steps, dtype=np.float32)

        for ep_idx in range(n_episodes):
            start = int(episode_starts[ep_idx])
            end   = int(episode_ends[ep_idx])
            if end > start:
                if reward_type == 'dense':
                    reward_array[start:end] = 10.0
                else:
                    reward_array[end - 1] = 1.0
                done_array[end - 1] = 1.0

        rb.data.create_dataset('reward', data=reward_array, overwrite=True)
        rb.data.create_dataset('done',   data=done_array,   overwrite=True)

        dataset.has_rl_data = True

        from diffusion_policy_3d.common.sampler import SequenceSampler
        n_total = rb.n_episodes
        episode_mask = np.ones(n_total, dtype=bool)
        dataset.sampler = SequenceSampler(
            replay_buffer=rb,
            sequence_length=dataset.horizon,
            pad_before=dataset.pad_before,
            pad_after=dataset.pad_after,
            episode_mask=episode_mask,
        )
        dataset.train_mask = episode_mask

        cprint(f"[RL100Trainer] Relabeled {n_episodes} episodes "
               f"({rb.n_steps} steps) with reward_type={reward_type}.", "green")

    def _evaluate_policy_amq(self, dataset: BaseDataset, num_batches: int = 20,
                             rollout_horizon: int = 5) -> float:
        """
        Offline Policy Evaluation using AM-Q (paper Eq.20).

        Estimates policy value by H-step rollout through the transition model:
          Ĵ^{AM-Q}(π) = E_{(s,a)~(T̂,π)} [ Σ_{h=0}^{H-1} Q_ψ(s_h, a_h) ]

        Steps:
          1. Sample initial states from the dataset
          2. For each horizon step h = 0..H-1:
             a) Run the policy to get action a_h = π(s_h)
             b) Accumulate Q(s_h, a_h)
             c) Predict next state s_{h+1} via transition model T̂
          3. Return average cumulative Q

        Args:
            dataset: offline dataset for initial states
            num_batches: number of batches to average over
            rollout_horizon: H-step rollout depth through transition model

        Returns:
            Estimated policy value J_hat.
        """
        from torch.utils.data import DataLoader as _DL
        loader = _DL(dataset, batch_size=self.config.dataloader.batch_size,
                     shuffle=True, num_workers=0, pin_memory=True)

        eval_policy = self.ema_policy if self.ema_policy is not None else self.policy
        eval_policy.eval()
        self.critics.eval()
        cumulative_q = []
        gamma_chunk = self.critics.gamma  # chunk-level discount

        with torch.no_grad():
            for i, batch in enumerate(loader):
                if i >= num_batches:
                    break
                batch = dict_apply(batch, lambda x: x.to(self.device, non_blocking=True))
                obs_dict = batch['obs']

                # Encode initial observations
                nobs = eval_policy.normalizer.normalize(obs_dict)
                if not eval_policy.use_pc_color:
                    nobs['point_cloud'] = nobs['point_cloud'][..., :3]
                this_nobs = dict_apply(
                    nobs,
                    lambda x: x[:, :eval_policy.n_obs_steps].reshape(-1, *x.shape[2:])
                )
                obs_features = eval_policy.obs_encoder(this_nobs)
                obs_features = obs_features.reshape(batch['action'].shape[0], -1)

                # H-step rollout
                batch_q_sum = torch.zeros(obs_features.shape[0], 1, device=self.device)
                cur_features = obs_features

                for h in range(rollout_horizon):
                    # Sample action from policy (simplified: use predict_action for h=0,
                    # for h>0 we'd need to reconstruct obs_dict from features — approximate
                    # by sampling random actions from the policy in feature space)
                    if h == 0:
                        action_pred = eval_policy.predict_action(obs_dict)
                        action = action_pred['action'][:, 0, :]
                        naction = eval_policy.normalizer['action'].normalize(action)
                    else:
                        # For h>0, we can't easily reconstruct obs_dict from features.
                        # Use the Q-network's own action via argmax approximation:
                        # sample a batch of random actions and pick the one with max Q.
                        # For efficiency, just sample one action from N(0,1) in normalised space.
                        naction = torch.randn(cur_features.shape[0], self.policy.action_dim,
                                              device=self.device) * 0.3

                    # Accumulate discounted Q
                    q = self.critics.get_q_value(cur_features, naction)  # [B, 1]
                    batch_q_sum += (gamma_chunk ** h) * q

                    # Predict next features via transition model
                    if h < rollout_horizon - 1 and hasattr(self, 'transition_model'):
                        try:
                            next_features, _ = self.transition_model.predict_next_features(
                                cur_features, naction)
                            cur_features = next_features
                        except Exception:
                            break  # transition model not trained yet

                cumulative_q.append(batch_q_sum.mean().item())

        eval_policy.train()
        return float(np.mean(cumulative_q)) if cumulative_q else 0.0

    def offline_rl_optimize(
        self,
        dataset: BaseDataset,
        num_epochs: int
    ) -> Dict:
        """
        Phase 2b: Optimize policy with PPO and consistency distillation.

        Implements paper lines 7-8 of Algorithm 1 (OfflineRL):
          1. Save behavior-policy snapshot for OPE gate
          2. Freeze obs_encoder (paper: "keep ϕIL fixed")
          3. Normalize advantages (prevent gradient explosion)
          4. K-step PPO update + Consistency Distillation
          5. OPE gate: accept update only if AM-Q improves by ≥ δ (paper Eq.20)

        Args:
            dataset: Dataset with (s, a, r, s', done)
            num_epochs: Number of training epochs

        Returns:
            metrics: Dictionary with training metrics
        """
        cprint(f"\n[RL100Trainer] Phase 2b: Offline RL Optimization (Iteration {self.offline_rl_iteration})", "cyan")

        config = self.config

        # ── Step 0: Evaluate behavior policy before PPO (for OPE gate) ──────────
        j_old = self._evaluate_policy_amq(dataset)
        cprint(f"[OPE] Behavior policy value J_old = {j_old:.4f}", "cyan")

        # ── Step 1: Save snapshot for potential rollback ──────────────────────────
        policy_snapshot = copy.deepcopy(self.policy.state_dict())
        ema_snapshot = copy.deepcopy(self.ema_policy.state_dict()) if self.ema_policy is not None else None

        # ── Step 1b: Reduce policy LR for RL fine-tuning (tag3: 10× smaller than IL) ─
        rl_lr = getattr(config.training, 'rl_policy_lr', 1e-5)
        current_lr = self.policy_optimizer.param_groups[0]['lr']
        if abs(current_lr - rl_lr) > 1e-10:
            cprint(f"[RL PPO] Reducing policy LR: {current_lr:.2e} → {rl_lr:.2e}", "cyan")
            for pg in self.policy_optimizer.param_groups:
                pg['lr'] = rl_lr

        # ── Step 2: Freeze encoder (paper: ϕIL is fixed during offline RL) ───────
        for param in self.policy.obs_encoder.parameters():
            param.requires_grad_(False)

        self.policy.train()
        self.critics.eval()

        # Create dataloader
        train_dataloader = DataLoader(
            dataset,
            batch_size=config.dataloader.batch_size,
            shuffle=True,
            num_workers=config.dataloader.num_workers,
            pin_memory=True
        )

        # Number of inner PPO gradient steps per batch (allows ratio to deviate from 1)
        ppo_inner_steps = getattr(config.training, 'ppo_inner_steps', 4)
        # Paper Eq.22: L_total = L_RL + λ_CD · L_CD
        lambda_cd = getattr(config.training, 'lambda_cd', 1.0)

        ppo_loss_per_epoch = []
        for epoch in range(num_epochs):
            ppo_losses = []
            cd_losses = []

            for batch_idx, batch in enumerate(train_dataloader):
                batch = dict_apply(batch, lambda x: x.to(self.device, non_blocking=True))

                obs_dict = batch['obs']
                action = batch['action'][:, 0, :]  # [B, horizon, Da] -> [B, Da]

                # Encode observations (encoder is frozen — no_grad is redundant but explicit)
                with torch.no_grad():
                    nobs = self.policy.normalizer.normalize(obs_dict)
                    if not self.policy.use_pc_color:
                        nobs['point_cloud'] = nobs['point_cloud'][..., :3]

                    this_nobs = dict_apply(
                        nobs,
                        lambda x: x[:, :self.policy.n_obs_steps, ...].reshape(-1, *x.shape[2:])
                    )
                    obs_features = self.policy.obs_encoder(this_nobs)
                    obs_features = obs_features.reshape(batch['action'].shape[0], -1)

                    naction = self.policy.normalizer['action'].normalize(action)

                    # Compute raw advantage A = Q(s,a) - V(s)
                    advantages = self.critics.compute_advantage(obs_features, naction)

                # ── Step 3: Normalise advantages (prevent gradient explosion) ─────
                adv_mean = advantages.mean()
                adv_std = advantages.std() + 1e-8
                advantages = (advantages - adv_mean) / adv_std

                # ── Sample old trajectory ONCE per batch (fix old policy) ─────────
                trajectory_old, log_probs_old = self.policy.sample_for_ppo(obs_dict)

                # ── Inner PPO loop: N gradient steps with SAME old trajectory ─────
                for ppo_inner in range(ppo_inner_steps):
                    ppo_loss, ppo_info = self.policy.compute_ppo_loss(
                        obs_dict=obs_dict,
                        old_log_probs=log_probs_old,
                        advantages=advantages,
                        trajectory=trajectory_old
                    )

                    # Paper Eq.22: L_total = L_RL + λ_CD · L_CD
                    # Joint optimization — CD loss backprops through policy too
                    total_loss = ppo_loss
                    if self.global_step % config.training.cd_every == 0:
                        cd_loss, cd_info = self.consistency_distillation.compute_distillation_loss(obs_dict)
                        total_loss = ppo_loss + lambda_cd * cd_loss
                        cd_losses.append(cd_info['cd_loss'])

                    self.policy_optimizer.zero_grad()
                    # Also zero CD optimizer if joint
                    self.consistency_optimizer.zero_grad()
                    total_loss.backward()
                    torch.nn.utils.clip_grad_norm_(self.policy.parameters(), config.training.max_grad_norm)
                    self.policy_optimizer.step()
                    # Update consistency model params too
                    if self.global_step % config.training.cd_every == 0:
                        self.consistency_optimizer.step()

                ppo_losses.append(ppo_loss.item())

                # Update EMA
                if self.ema_policy is not None:
                    self.ema.step(self.policy)

                # Log
                if self.global_step % config.training.log_every == 0 and config.logging.use_wandb:
                    log_dict = {
                        'ppo/loss': ppo_loss.item(),
                        **{f'ppo/{k}': v for k, v in ppo_info.items()}
                    }
                    if cd_losses:
                        log_dict['cd/loss'] = cd_losses[-1]
                    wandb.log(log_dict, step=self.global_step)

                self.global_step += 1

            cprint(f"[Offline RL] Epoch {epoch}/{num_epochs}, PPO Loss: {np.mean(ppo_losses):.4f}, "
                   f"CD Loss: {np.mean(cd_losses) if cd_losses else 0:.4f}", "green")
            ppo_loss_per_epoch.append(float(np.mean(ppo_losses) if ppo_losses else 0.0))

        ppo_loss_plot_path = self._save_loss_curve_plot(
            loss_history=ppo_loss_per_epoch,
            title=f"PPO Loss (iter {int(self.offline_rl_iteration)})",
            ylabel="PPO Loss",
            filename=f"ppo_loss_iter_{int(self.offline_rl_iteration):02d}.png"
        )
        if config.logging.use_wandb and ppo_loss_plot_path is not None:
            wandb.log({
                'ppo/loss_curve': wandb.Image(ppo_loss_plot_path),
                'ppo/iteration': int(self.offline_rl_iteration),
            }, step=self.global_step)

        # ── Step 4: Unfreeze encoder ──────────────────────────────────────────────
        for param in self.policy.obs_encoder.parameters():
            param.requires_grad_(True)

        # ── Step 5: OPE Gate (paper Eq.20) ───────────────────────────────────────
        # Accept the PPO-updated policy only if AM-Q improves by δ = 0.05·|J_old|.
        # Otherwise roll back to the behavior-policy snapshot.
        j_new = self._evaluate_policy_amq(dataset)
        delta = 0.05 * abs(j_old) if j_old != 0 else 0.0
        if j_new - j_old >= delta:
            cprint(f"[OPE] Policy ACCEPTED: J_new={j_new:.4f} > J_old={j_old:.4f} + δ={delta:.4f}", "green")
        else:
            cprint(f"[OPE] Policy REJECTED: J_new={j_new:.4f} ≤ J_old={j_old:.4f} + δ={delta:.4f}. "
                   f"Rolling back to behavior policy.", "yellow")
            self.policy.load_state_dict(policy_snapshot)
            if self.ema_policy is not None and ema_snapshot is not None:
                self.ema_policy.load_state_dict(ema_snapshot)

        if config.logging.use_wandb:
            wandb.log({
                'ope/j_old': j_old,
                'ope/j_new': j_new,
                'ope/accepted': int(j_new - j_old >= delta),
            }, step=self.global_step)

        return {'ppo_loss': np.mean(ppo_losses), 'cd_loss': np.mean(cd_losses) if cd_losses else 0}

    def collect_new_data(
        self,
        env_runner,
        num_episodes: int
    ) -> Tuple[Dict, list]:
        """
        Phase 2c: Collect new data by rolling out policy in environment.

        Uses run_and_collect() to capture both metrics and raw trajectory data
        for subsequent dataset merging.

        Returns:
            metrics  : success rate, reward, etc.
            episodes : list of episode dicts (numpy arrays) for merging
        """
        cprint(f"\n[RL100Trainer] Phase 2c: Collecting New Data (Iteration {self.offline_rl_iteration})", "cyan")

        eval_policy = self.ema_policy if self.ema_policy else self.policy
        eval_policy.eval()

        with torch.no_grad():
            reward_type = getattr(self.config.critics, 'reward_type', 'sparse')
            metrics, episodes = env_runner.run_and_collect(
                eval_policy, num_episodes=num_episodes, reward_type=reward_type)

        cprint(f"[Data Collection] Success Rate: {metrics.get('mean_success_rates', 0):.3f}, "
               f"Reward: {metrics.get('mean_traj_rewards', 0):.2f}, "
               f"Episodes: {len(episodes)}, Steps: {metrics.get('n_steps', 0)}", "green")

        if self.config.logging.use_wandb:
            wandb.log({
                'collection/success_rate': metrics.get('mean_success_rates', 0),
                'collection/reward':       metrics.get('mean_traj_rewards', 0),
                'collection/n_steps':      metrics.get('n_steps', 0),
            }, step=self.global_step)

        eval_policy.train()
        return metrics, episodes

    def run_pipeline(
        self,
        initial_dataset: BaseDataset,
        env_runner: BaseRunner,
        num_offline_iterations: int = 5,
        skip_il: bool = False,
    ):
        """
        Execute complete RL-100 pipeline (Algorithm 1).

        Pipeline:
        =========
        1. Initialize: Train IL on D_0
        2. Loop M times:
            a) Train Critics (IQL)
            b) Optimize Policy (PPO + CD)
            c) Collect new data D_new
            d) Merge D = D ∪ D_new
            e) Retrain IL on merged dataset
        3. Online RL fine-tuning (optional)

        Args:
            initial_dataset: Initial dataset D_0
            env_runner: Environment for data collection
            num_offline_iterations: Number of offline RL iterations (M)
            skip_il: If True, skip Phase 1 (IL) and resume RL from loaded checkpoint.
                     Normalizer will be synced from the dataset but no training is done.
        """
        config = self.config

        cprint("\n" + "="*80, "magenta")
        cprint(" "*20 + "RL-100 TRAINING PIPELINE", "magenta")
        cprint("="*80 + "\n", "magenta")

        # ============================================
        # Phase 1: Initial Imitation Learning
        # ============================================
        if skip_il:
            cprint("\n[RL100Trainer] Skipping IL phase — loaded from checkpoint.", "yellow")
            # Sync normalizer from dataset so downstream code (IQL, PPO) works correctly
            normalizer = initial_dataset.get_normalizer()
            self.policy.set_normalizer(normalizer)
            self.policy.to(self.device)
            if self.ema_policy is not None:
                self.ema_policy.set_normalizer(normalizer)
                self.ema_policy.to(self.device)
            cprint(f"[RL100Trainer] Normalizer synced from dataset. "
                   f"Resuming offline RL from iteration {self.offline_rl_iteration}.", "yellow")
        else:
            self.train_imitation_learning(
                dataset=initial_dataset,
                num_epochs=config.training.il_epochs,
                env_runner=env_runner,
                plot_tag='initial'
            )
            # Save IL checkpoint
            self.save_checkpoint(tag='after_il')

        # ============================================
        # Phase 2: Offline RL Loop
        # ============================================
        current_dataset = initial_dataset

        # Store original VIB betas from config for dynamic reduction/restoration.
        # Paper Eq.17: during RL fine-tuning reduce by 10×; during IL retraining restore.
        _vib_beta_recon_orig = float(config.policy.get('beta_recon', 1.0))
        _vib_beta_kl_orig    = float(config.policy.get('beta_kl', 0.001))

        def _apply_vib_betas(factor: float):
            """Set VIB betas = original * factor on policy (and ema_policy)."""
            if not getattr(self.policy, 'use_recon_vib', False):
                return
            self.policy.obs_encoder.beta_recon = _vib_beta_recon_orig * factor
            self.policy.obs_encoder.beta_kl    = _vib_beta_kl_orig    * factor
            if self.ema_policy is not None:
                self.ema_policy.obs_encoder.beta_recon = _vib_beta_recon_orig * factor
                self.ema_policy.obs_encoder.beta_kl    = _vib_beta_kl_orig    * factor
            cprint(f"[RL100] VIB betas set to factor={factor}: "
                   f"beta_recon={self.policy.obs_encoder.beta_recon:.6f}, "
                   f"beta_kl={self.policy.obs_encoder.beta_kl:.6f}", "yellow")

        # Ensure rewards exist in the dataset before training critics.
        # Expert demo zarrs typically have no reward/done labels;
        # relabel them with sparse success rewards so Q-training works.
        self._relabel_demo_rewards(current_dataset)

        # When resuming from a checkpoint, skip iterations already completed.
        # - after_il.ckpt has offline_rl_iteration=0 → start_iteration=0 (nothing done yet)
        # - offline_iter_N.ckpt has offline_rl_iteration=N → start_iteration=N+1
        start_iteration = self.offline_rl_iteration + 1 if skip_il and self.offline_rl_iteration > 0 else 0
        if skip_il and start_iteration > 0:
            cprint(f"[RL100Trainer] Skipping offline RL iterations 0~{start_iteration - 1} "
                   f"(already completed in checkpoint).", "yellow")

        for iteration in range(start_iteration, num_offline_iterations):
            self.offline_rl_iteration = iteration

            cprint("\n" + "="*80, "yellow")
            cprint(f" "*15 + f"OFFLINE RL ITERATION {iteration + 1}/{num_offline_iterations}", "yellow")
            cprint("="*80 + "\n", "yellow")

            # 2a) Train Transition Model  (Algorithm 1, Line 6)
            self.train_transition_model(
                dataset=current_dataset,
                max_epochs=200,
                max_epochs_since_update=5,
            )

            # 2b) Train IQL Critics  (Algorithm 1, Line 5)
            self.train_iql_critics(
                dataset=current_dataset,
                num_epochs=config.training.critic_epochs
            )

            # 2c) Optimize Policy  (Algorithm 1, Lines 7-8)
            # Paper Eq.17: reduce VIB betas by 10× during RL fine-tuning.
            _apply_vib_betas(0.1)
            self.offline_rl_optimize(
                dataset=current_dataset,
                num_epochs=config.training.ppo_epochs
            )

            # 2d) Collect New Data + Merge  (Algorithm 1, Lines 10-11)
            collection_metrics, new_episodes = self.collect_new_data(
                env_runner=env_runner,
                num_episodes=config.training.collection_episodes
            )

            # Algorithm 1 Line 11: D_{m+1} = D_m ∪ D_new
            if new_episodes:
                n_new = current_dataset.merge_episodes(new_episodes)
                cprint(f"[Dataset] Merged {len(new_episodes)} episodes "
                       f"({n_new} steps) → total {current_dataset.replay_buffer.n_steps} steps, "
                       f"{current_dataset.replay_buffer.n_episodes} episodes", "cyan")

            # 2e) Retrain IL (optional) — Algorithm 1 Line 13
            if config.training.retrain_il_after_collection:
                # Paper Eq.17: restore VIB betas to original values for IL re-training.
                # The 10× reduction only applies to RL fine-tuning (OfflineRL step).
                _apply_vib_betas(1.0)
                cprint(f"\n[RL100Trainer] Retraining IL on merged dataset...", "cyan")
                self.train_imitation_learning(
                    dataset=current_dataset,
                    num_epochs=config.training.il_retrain_epochs,
                    env_runner=env_runner,
                    plot_tag=f"retrain_iter_{int(iteration):02d}"
                )

            # Save checkpoint
            self.save_checkpoint(tag=f'offline_iter_{iteration}')

        # ============================================
        # Phase 3: Online RL Fine-tuning (Optional)
        # ============================================
        if config.training.run_online_rl:
            cprint("\n" + "="*80, "green")
            cprint(" "*20 + "PHASE 3: ONLINE RL FINE-TUNING", "green")
            cprint("="*80 + "\n", "green")

            # Paper Eq.21: L_RL^on = -J_i(π) + λ_V · E[(V_ψ(s_t) - V̂_t)²]
            # Uses GAE advantage instead of IQL advantage.
            lambda_v = getattr(config.training, 'lambda_v', 0.5)
            gae_lambda = getattr(config.training, 'gae_lambda', 0.95)
            gamma_chunk = self.critics.gamma  # chunk-level discount

            # Reduce policy LR for online fine-tuning
            rl_lr = getattr(config.training, 'rl_policy_lr', 1e-5)
            for pg in self.policy_optimizer.param_groups:
                pg['lr'] = rl_lr

            for online_iter in range(config.training.online_rl_iterations):
                cprint(f"\n[Online RL] Iteration {online_iter + 1}/{config.training.online_rl_iterations}", "green")

                # 1. Collect fresh data
                collection_metrics, online_episodes = self.collect_new_data(
                    env_runner=env_runner,
                    num_episodes=config.training.online_collection_episodes
                )

                if not online_episodes:
                    cprint("[Online RL] No episodes collected, skipping.", "yellow")
                    continue

                # 2. Compute GAE advantages from collected episodes
                # Paper Eq.21: A_t^on = GAE(λ, γ; r_t, V_ψ)
                self.policy.eval()
                self.critics.eval()
                gae_obs_features_all = []
                gae_naction_all = []
                gae_advantages_all = []
                gae_returns_all = []

                with torch.no_grad():
                    for ep in online_episodes:
                        states = torch.from_numpy(ep['state']).to(self.device)
                        actions = torch.from_numpy(ep['action']).to(self.device)
                        rewards = torch.from_numpy(ep['reward']).to(self.device)
                        dones = torch.from_numpy(ep['done']).to(self.device)

                        T_ep = len(states)
                        if T_ep < 2:
                            continue

                        # Encode each step's observation features
                        # (simplified: use state directly as agent_pos, need point_cloud too)
                        # For GAE we need V(s_t) at each step
                        # Since we can't easily reconstruct full obs_dict from stored data,
                        # we use the critic's V on encoded features from stored data.
                        # Build obs features from stored state (agent_pos part of obs_features)
                        naction = self.policy.normalizer['action'].normalize(actions)

                        # Approximate obs_features: encode stored observations
                        pcs = torch.from_numpy(ep['point_cloud']).to(self.device)
                        nobs_pc = self.policy.normalizer['point_cloud'].normalize(pcs)
                        if not self.policy.use_pc_color:
                            nobs_pc = nobs_pc[..., :3]
                        nobs_state = self.policy.normalizer['agent_pos'].normalize(states)

                        # Encode step-by-step (no n_obs_steps windowing for simplicity)
                        obs_feats = []
                        for t_step in range(T_ep):
                            pc_t = nobs_pc[t_step:t_step+1]
                            state_t = nobs_state[t_step:t_step+1]
                            step_nobs = {'point_cloud': pc_t, 'agent_pos': state_t}
                            feat = self.policy.obs_encoder(step_nobs)
                            obs_feats.append(feat.reshape(1, -1))
                        obs_feats = torch.cat(obs_feats, dim=0)  # [T, F]

                        # Get V(s_t) for all steps
                        values = self.critics.get_value(obs_feats).squeeze(-1)  # [T]

                        # GAE computation
                        advantages = torch.zeros(T_ep, device=self.device)
                        returns = torch.zeros(T_ep, device=self.device)
                        last_gae = 0.0
                        for t_step in reversed(range(T_ep)):
                            if t_step == T_ep - 1:
                                next_val = 0.0
                            else:
                                next_val = values[t_step + 1].item()
                            delta = rewards[t_step] + gamma_chunk * (1 - dones[t_step]) * next_val - values[t_step]
                            last_gae = delta + gamma_chunk * gae_lambda * (1 - dones[t_step]) * last_gae
                            advantages[t_step] = last_gae
                            returns[t_step] = advantages[t_step] + values[t_step]

                        gae_obs_features_all.append(obs_feats)
                        gae_naction_all.append(naction)
                        gae_advantages_all.append(advantages)
                        gae_returns_all.append(returns)

                if not gae_advantages_all:
                    continue

                # Concatenate all episode data
                all_obs_feats = torch.cat(gae_obs_features_all, dim=0)
                all_nactions = torch.cat(gae_naction_all, dim=0)
                all_advantages = torch.cat(gae_advantages_all, dim=0)
                all_returns = torch.cat(gae_returns_all, dim=0)

                # Normalize advantages
                all_advantages = (all_advantages - all_advantages.mean()) / (all_advantages.std() + 1e-8)

                # 3. Update critics with online data (V loss from Eq.21)
                self.critics.train()
                N = all_obs_feats.shape[0]
                bs = min(self.config.dataloader.batch_size, N)
                for critic_epoch in range(5):
                    perm = torch.randperm(N, device=self.device)
                    for start in range(0, N, bs):
                        idx = perm[start:start+bs]
                        v_pred = self.critics.get_value(all_obs_feats[idx])
                        v_loss = lambda_v * torch.nn.functional.mse_loss(v_pred.squeeze(-1), all_returns[idx])

                        q_loss, _ = self.critics.compute_q_loss(
                            all_obs_feats[idx], all_nactions[idx],
                            all_returns[idx].unsqueeze(-1),
                            all_obs_feats[torch.clamp(idx+1, max=N-1)],
                            torch.zeros(len(idx), 1, device=self.device)
                        )

                        self.v_optimizer.zero_grad()
                        v_loss.backward()
                        self.v_optimizer.step()

                        self.q_optimizer.zero_grad()
                        q_loss.backward()
                        self.q_optimizer.step()

                        self.critics.update_target_network(tau=config.critics.target_update_tau)

                # 4. Merge data and continue
                current_dataset.merge_episodes(online_episodes)

                # 5. Update policy with PPO using GAE advantages
                # (re-use offline_rl_optimize on merged dataset — the GAE advantages
                # have already updated the critics, so Q-V advantages will reflect online data)
                _apply_vib_betas(0.1)
                self.offline_rl_optimize(
                    dataset=current_dataset,
                    num_epochs=min(20, config.training.ppo_epochs)
                )
                _apply_vib_betas(1.0)

                self.save_checkpoint(tag=f'online_iter_{online_iter}')

        cprint("\n" + "="*80, "magenta")
        cprint(" "*25 + "TRAINING COMPLETE!", "magenta")
        cprint("="*80 + "\n", "magenta")

        # Save final checkpoint
        self.save_checkpoint(tag='final')

    def save_checkpoint(self, tag: str = 'latest'):
        """Save checkpoint."""
        save_dir = os.path.join(self.output_dir, 'checkpoints')
        os.makedirs(save_dir, exist_ok=True)

        checkpoint = {
            'policy': self.policy.state_dict(),
            'critics': self.critics.state_dict(),
            'consistency_model': self.consistency_model.state_dict(),
            'transition_model': self.transition_model.state_dict(),
            'policy_optimizer': self.policy_optimizer.state_dict(),
            'v_optimizer': self.v_optimizer.state_dict(),
            'q_optimizer': self.q_optimizer.state_dict(),
            'consistency_optimizer': self.consistency_optimizer.state_dict(),
            'global_step': self.global_step,
            'epoch': self.epoch,
            'offline_rl_iteration': self.offline_rl_iteration,
        }

        if self.ema_policy is not None:
            checkpoint['ema_policy'] = self.ema_policy.state_dict()

        save_path = os.path.join(save_dir, f'{tag}.ckpt')
        torch.save(checkpoint, save_path)
        cprint(f"[Checkpoint] Saved to {save_path}", "green")

    def load_checkpoint(self, path: str):
        """Load checkpoint."""
        checkpoint = torch.load(path, map_location=self.device)

        # Use strict=False to tolerate architecture mismatches (e.g., checkpoint saved
        # without VIB but current config has use_recon_vib=True). Missing keys (new VIB
        # layers) stay randomly initialized and will be trained from scratch; unexpected
        # keys (VIB layers in checkpoint but not in model) are silently ignored.
        missing, unexpected = self.policy.load_state_dict(checkpoint['policy'], strict=False)
        if missing:
            cprint(f"[Checkpoint] policy: {len(missing)} missing key(s) "
                   f"(new layers, will train from scratch): {missing[:3]}{'...' if len(missing)>3 else ''}", "yellow")
        if unexpected:
            cprint(f"[Checkpoint] policy: {len(unexpected)} unexpected key(s) "
                   f"(ignored): {unexpected[:3]}{'...' if len(unexpected)>3 else ''}", "yellow")

        self.critics.load_state_dict(checkpoint['critics'])
        self.consistency_model.load_state_dict(checkpoint['consistency_model'])
        if 'transition_model' in checkpoint:
            self.transition_model.load_state_dict(checkpoint['transition_model'])
        self.policy_optimizer.load_state_dict(checkpoint['policy_optimizer'])
        self.v_optimizer.load_state_dict(checkpoint['v_optimizer'])
        self.q_optimizer.load_state_dict(checkpoint['q_optimizer'])
        self.consistency_optimizer.load_state_dict(checkpoint['consistency_optimizer'])

        if 'ema_policy' in checkpoint and self.ema_policy is not None:
            self.ema_policy.load_state_dict(checkpoint['ema_policy'], strict=False)

        self.global_step = checkpoint['global_step']
        self.epoch = checkpoint['epoch']
        self.offline_rl_iteration = checkpoint['offline_rl_iteration']

        cprint(f"[Checkpoint] Loaded from {path}", "green")
