from __future__ import annotations
import json
import copy
from contextlib import nullcontext
from dataclasses import asdict, dataclass
import logging
from pathlib import Path
from typing import Any
import numpy as np
import torch
from torch.utils.data import ConcatDataset, DataLoader
from lerobot.datasets.factory import resolve_delta_timestamps
from lerobot.datasets.lerobot_dataset import LeRobotDataset, LeRobotDatasetMetadata
from lerobot.datasets.utils import dataset_to_policy_features
from lerobot.policies.factory import make_pre_post_processors
from lerobot.policies.utils import populate_queues, prepare_observation_for_inference
from lerobot.utils.constants import ACTION
from lerobot.utils.utils import get_safe_torch_device
from rl_100.env.genesis_env import GenesisEnv
from rl_100.lerobot_dataset_utils import append_episode_summary, build_frame, create_lerobot_dataset
from rl_100.training.rl100_consistency import ConsistencyDistillation, ConsistencyModel
from rl_100.training.rl100_critics import IQLCritics
from rl_100.training.rl100_dataset import RL100TransitionDataset, RolloutDatasetSpec, configure_hf_cache
from rl_100.training.rl100_policy import RL100DiffusionConfig, RL100DiffusionPolicy
from rl_100.training.rl100_transition import TransitionModel

@dataclass
class SimRL100Config:
    dataset_root: str
    output_dir: str
    task: str = "normal-fix"
    device: str = "cuda"
    seed: int = 42
    batch_size: int = 16
    num_workers: int = 2
    learning_rate: float = 1e-4
    critic_learning_rate: float = 3e-4
    weight_decay: float = 1e-6
    il_steps: int = 5_000
    il_retrain_steps: int = 1_000
    offline_iterations: int = 5
    critic_steps: int = 1_000
    offline_collection_episodes: int = 20
    offline_finetune_steps: int = 1_000
    ppo_inner_steps: int = 1
    online_iterations: int = 0
    online_collection_episodes: int = 20
    online_finetune_steps: int = 1_000
    online_value_steps: int = 200
    eval_episodes: int = 20
    save_every: int = 1
    observation_height: int = 224
    observation_width: int = 224
    max_episode_steps: int = 700
    show_viewer: bool = False
    merge_success_only: bool = True
    horizon: int = 16
    n_obs_steps: int = 2
    n_action_steps: int = 8
    num_inference_steps: int = 10
    ppo_clip_eps: float = 0.2
    sigma_min: float = 0.01
    sigma_max: float = 0.1
    gamma: float = 0.92274469442792
    expectile: float = 0.7
    target_update_tau: float = 0.005
    reward_scale: float = 1.0
    gae_lambda: float = 0.95
    max_grad_norm: float = 1.0
    amp: bool = False
    hf_cache_root: str = "/tmp/rl100_hf_cache"
    relabel_sparse_reward: bool = True
    assume_expert_success: bool = True
    lambda_cd: float = 1.0
    cd_every: int = 1
    rollout_policy_mode: str = "ddim"
    eval_policy_mode: str = "ddim"
    online_record_policy_mode: str = "ddim"
    transition_train_epochs: int = 50
    transition_train_patience: int = 5
    transition_holdout_ratio: float = 0.2
    transition_logvar_loss_coef: float = 0.01
    transition_learning_rate: float = 1e-3
    transition_max_batches: int = 0
    transition_deterministic_eval: bool = True
    ope_enabled: bool = True
    ope_num_batches: int = 8
    ope_rollout_horizon: int = 5
    ope_delta_coef: float = 0.05
    ope_delta_abs_min: float = 0.0
    ope_seed: int = 42
    ope_shuffle_batches: bool = True
    ope_use_common_random_numbers: bool = True
    use_wandb: bool = False
    wandb_project: str = "rl100-lerobot"
    wandb_entity: str | None = None
    wandb_run_name: str | None = None
    wandb_tags: tuple[str, ...] = ()


class SimRL100Trainer:
    def __init__(self, cfg: SimRL100Config):
        self.cfg = cfg
        self.output_dir = Path(cfg.output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)
        self.rollout_root = self.output_dir / "rollouts"
        self.rollout_root.mkdir(parents=True, exist_ok=True)
        self.device = get_safe_torch_device(cfg.device)
        self._restore_default_torch_device()
        configure_hf_cache(cfg.hf_cache_root)

        self.base_dataset_root = Path(cfg.dataset_root).resolve()
        self.base_dataset = self._load_il_dataset(self.base_dataset_root)
        self.policy, self.preprocessor, self.postprocessor = self._make_policy_stack()
        self.optimizer = torch.optim.AdamW(
            self.policy.parameters(),
            lr=cfg.learning_rate,
            weight_decay=cfg.weight_decay,
        )

        obs_dim = self.policy.encode_global_conditioning(self._peek_policy_batch(self.base_dataset)).shape[-1]
        self.critics = IQLCritics(
            obs_dim=obs_dim,
            action_dim=self.policy.chunk_action_dim,
            gamma=cfg.gamma,
            expectile=cfg.expectile,
        ).to(self.device)
        self.v_optimizer = torch.optim.AdamW(
            self.critics.value.parameters(),
            lr=cfg.critic_learning_rate,
            weight_decay=cfg.weight_decay,
        )
        self.q_optimizer = torch.optim.AdamW(
            self.critics.q.parameters(),
            lr=cfg.critic_learning_rate,
            weight_decay=cfg.weight_decay,
        )
        self.consistency_model = ConsistencyModel(self.policy.config, global_cond_dim=obs_dim).to(self.device)
        self.consistency_optimizer = torch.optim.AdamW(
            self.consistency_model.parameters(),
            lr=cfg.learning_rate,
            weight_decay=cfg.weight_decay,
        )
        self.consistency_distillation = ConsistencyDistillation(self.policy, self.consistency_model)
        self.transition_model = TransitionModel(
            obs_feature_dim=obs_dim,
            action_dim=self.policy.chunk_action_dim,
            lr=cfg.transition_learning_rate,
            device=str(self.device),
        )

        self.rl_roots: list[Path] = [self.base_dataset_root]
        self.il_specs: list[RolloutDatasetSpec] = [RolloutDatasetSpec(root=self.base_dataset_root, success_episodes=[])]
        self.step = 0
        self.log_step = 0
        self.history: list[dict[str, Any]] = []
        self.wandb_run = None

    def _init_wandb(self) -> None:
        if not self.cfg.use_wandb:
            return
        try:
            import wandb
        except ImportError:
            logging.warning("wandb is not installed; disabling wandb logging.")
            self.cfg.use_wandb = False
            return
        self.wandb_run = wandb.init(
            project=self.cfg.wandb_project,
            entity=self.cfg.wandb_entity,
            name=self.cfg.wandb_run_name,
            tags=list(self.cfg.wandb_tags),
            config=asdict(self.cfg),
            dir=str(self.output_dir),
        )

    @staticmethod
    def _sanitize_metrics(metrics: dict[str, Any]) -> dict[str, float | int | str]:
        sanitized: dict[str, float | int | str] = {}
        for key, value in metrics.items():
            if isinstance(value, (float, int, str)):
                sanitized[key] = value
            elif isinstance(value, np.generic):
                sanitized[key] = value.item()
        return sanitized

    @staticmethod
    def _metric_namespace(metrics: dict[str, Any]) -> str:
        phase = str(metrics.get("phase", "train"))
        if "eval_episodes" in metrics:
            return f"eval/{phase}"
        if "saved_episodes" in metrics:
            return f"collect/{phase}"
        return phase

    def _log_metrics(self, metrics: dict[str, Any], *, commit: bool = True) -> None:
        metrics = self._sanitize_metrics(metrics)
        if not metrics:
            return
        if self.cfg.use_wandb and self.wandb_run is not None:
            namespace = self._metric_namespace(metrics)
            payload: dict[str, float | int | str] = {}
            for key, value in metrics.items():
                if key in {"phase", "iteration"}:
                    payload[key] = value
                else:
                    payload[f"{namespace}/{key}"] = value
            payload[f"{namespace}/trainer_step"] = float(self.step)
            self.wandb_run.log(payload, step=self.log_step, commit=commit)
            self.log_step += 1

    def _record_metrics(self, metrics: dict[str, Any], *, commit: bool = True) -> dict[str, Any]:
        self._log_metrics(metrics, commit=commit)
        return metrics

    def _restore_default_torch_device(self) -> None:
        if hasattr(torch, "set_default_device"):
            torch.set_default_device("cpu")

    def _make_policy_config(
        self,
        dataset_root: Path | None = None,
        metadata: LeRobotDatasetMetadata | None = None,
    ) -> RL100DiffusionConfig:
        ds_meta = metadata
        if ds_meta is None:
            if dataset_root is None:
                dataset_root = self.base_dataset_root
            ds_meta = LeRobotDatasetMetadata(repo_id=dataset_root.name, root=dataset_root)
        features = dataset_to_policy_features(ds_meta.features)
        input_features = {key: feature for key, feature in features.items() if key != ACTION}
        output_features = {key: feature for key, feature in features.items() if key == ACTION}
        return RL100DiffusionConfig(
            input_features=input_features,
            output_features=output_features,
            device=str(self.device),
            horizon=self.cfg.horizon,
            n_obs_steps=self.cfg.n_obs_steps,
            n_action_steps=self.cfg.n_action_steps,
            num_inference_steps=self.cfg.num_inference_steps,
            crop_shape=None,
            resize_shape=None,
            noise_scheduler_type="DDIM",
            prediction_type="epsilon",
            ppo_clip_eps=self.cfg.ppo_clip_eps,
            sigma_min=self.cfg.sigma_min,
            sigma_max=self.cfg.sigma_max,
            use_variance_clip=True,
        )

    def _load_il_dataset(self, dataset_root: Path, episodes: list[int] | None = None) -> LeRobotDataset:
        ds_meta = LeRobotDatasetMetadata(repo_id=dataset_root.name, root=dataset_root)
        delta_timestamps = resolve_delta_timestamps(
            self._make_policy_config(dataset_root=dataset_root, metadata=ds_meta),
            ds_meta,
        )
        return LeRobotDataset(
            repo_id=dataset_root.name,
            root=dataset_root,
            episodes=episodes,
            delta_timestamps=delta_timestamps,
        )

    def _make_policy_stack(self):
        ds_meta = LeRobotDatasetMetadata(repo_id=self.base_dataset_root.name, root=self.base_dataset_root)
        policy_cfg = self._make_policy_config(metadata=ds_meta)
        policy = RL100DiffusionPolicy(policy_cfg)
        policy.to(self.device)
        policy.train()
        preprocessor, postprocessor = make_pre_post_processors(policy_cfg=policy_cfg, dataset_stats=ds_meta.stats)
        return policy, preprocessor, postprocessor

    def _peek_policy_batch(self, dataset: LeRobotDataset) -> dict[str, torch.Tensor]:
        item = dataset[0]
        batch = {key: value.unsqueeze(0) if isinstance(value, torch.Tensor) else torch.as_tensor(value).unsqueeze(0) for key, value in item.items() if key in dataset.features or key.endswith("_is_pad")}
        processed = self._filter_policy_batch(self.preprocessor(batch))
        processed = {key: value for key, value in processed.items() if key != ACTION and key != "action_is_pad"}
        return self._to_device(processed)

    def _make_il_dataloader(self) -> DataLoader:
        datasets: list[LeRobotDataset] = []
        for spec in self.il_specs:
            if spec.root == self.base_dataset_root:
                datasets.append(self.base_dataset)
                continue
            episodes = spec.success_episodes if self.cfg.merge_success_only else None
            if self.cfg.merge_success_only and not episodes:
                continue
            datasets.append(self._load_il_dataset(spec.root, episodes=episodes))
        train_dataset = datasets[0] if len(datasets) == 1 else ConcatDataset(datasets)
        drop_last = len(train_dataset) >= self.cfg.batch_size
        return DataLoader(
            train_dataset,
            batch_size=self.cfg.batch_size,
            shuffle=True,
            num_workers=self.cfg.num_workers,
            pin_memory=self.device.type != "cpu",
            drop_last=drop_last,
        )

    def _make_transition_dataloader(self) -> DataLoader:
        datasets = [
            RL100TransitionDataset(
                root=root,
                horizon=self.cfg.horizon,
                n_obs_steps=self.cfg.n_obs_steps,
                n_action_steps=self.cfg.n_action_steps,
                gamma=self.cfg.gamma,
                relabel_sparse_reward=self.cfg.relabel_sparse_reward,
                assume_demo_success=self.cfg.assume_expert_success,
            )
            for root in self.rl_roots
        ]
        train_dataset = datasets[0] if len(datasets) == 1 else ConcatDataset(datasets)
        return DataLoader(
            train_dataset,
            batch_size=self.cfg.batch_size,
            shuffle=True,
            num_workers=self.cfg.num_workers,
            pin_memory=self.device.type != "cpu",
            drop_last=len(train_dataset) >= self.cfg.batch_size,
        )

    @staticmethod
    def _split_transition_batch(batch: dict[str, torch.Tensor]) -> tuple[dict[str, torch.Tensor], dict[str, torch.Tensor], dict[str, torch.Tensor]]:
        current: dict[str, torch.Tensor] = {}
        nxt: dict[str, torch.Tensor] = {}
        extras: dict[str, torch.Tensor] = {}
        for key, value in batch.items():
            if key.startswith("next.observation."):
                nxt[key.replace("next.", "", 1)] = value
            elif key.startswith("observation.") or key in {ACTION, "action_is_pad"}:
                current[key] = value
            else:
                extras[key] = value
        return current, nxt, extras

    @staticmethod
    def _filter_policy_batch(batch: dict[str, Any], include_action: bool = True) -> dict[str, torch.Tensor]:
        result: dict[str, torch.Tensor] = {}
        for key, value in batch.items():
            if key.startswith("observation.") or key == "action_is_pad" or (include_action and key == ACTION):
                result[key] = value
        return result

    def _to_device(self, batch: dict[str, torch.Tensor]) -> dict[str, torch.Tensor]:
        result: dict[str, torch.Tensor] = {}
        for key, value in batch.items():
            if not isinstance(value, torch.Tensor):
                value = torch.as_tensor(value)
            result[key] = value.to(self.device, non_blocking=True)
        return result

    def _sample_initial_noise(self, batch_size: int, seed: int, dtype: torch.dtype | None = None) -> torch.Tensor:
        generator = torch.Generator(device=self.device.type if self.device.type != "mps" else "cpu")
        generator.manual_seed(int(seed))
        return torch.randn(
            batch_size,
            self.cfg.horizon,
            self.policy.action_dim,
            device=self.device,
            dtype=dtype or self.policy.dtype,
            generator=generator,
        )

    def _iter_obs_encoder_parameters(self):
        rgb_encoder = getattr(self.policy.diffusion, "rgb_encoder", None)
        if rgb_encoder is None:
            return []
        return list(rgb_encoder.parameters())

    def _set_obs_encoder_requires_grad(self, requires_grad: bool) -> None:
        for param in self._iter_obs_encoder_parameters():
            param.requires_grad_(requires_grad)

    def _generate_policy_rollout(
        self,
        global_cond: torch.Tensor,
        mode: str = "ddim",
        noise: torch.Tensor | None = None,
    ) -> tuple[torch.Tensor, dict[str, torch.Tensor | list[torch.Tensor]]]:
        mode = mode.lower()
        if mode == "ddim":
            horizon_actions, trajectory, log_probs = self.policy.sample_trajectory(global_cond, noise=noise)
            return self.policy.get_chunk_from_horizon(horizon_actions), {
                "trajectory": trajectory,
                "log_probs_old": log_probs,
                "global_cond": global_cond,
                "normalized_horizon_actions": horizon_actions,
                "mode": mode,
            }
        if mode == "cm":
            horizon_actions = self.consistency_model.predict_horizon_actions(global_cond=global_cond, noise=noise)
            return self.policy.get_chunk_from_horizon(horizon_actions), {
                "global_cond": global_cond,
                "normalized_horizon_actions": horizon_actions,
                "mode": mode,
            }
        raise ValueError(f"Unsupported policy mode: {mode}")

    def _prepare_amq_eval_feature_batches(self, num_batches: int, eval_seed: int | None = None) -> list[torch.Tensor]:
        dataloader = self._make_transition_dataloader()
        feature_batches: list[torch.Tensor] = []
        with torch.no_grad():
            for batch_idx, batch in enumerate(dataloader):
                if batch_idx >= num_batches:
                    break
                current_raw, _, _ = self._split_transition_batch(batch)
                current = self._filter_policy_batch(self.preprocessor(current_raw))
                current = self._to_device(current)
                feature_batches.append(self._encode_obs(current).detach().cpu())
        if self.cfg.ope_shuffle_batches and eval_seed is not None:
            rng = np.random.default_rng(eval_seed)
            rng.shuffle(feature_batches)
        return feature_batches

    def _evaluate_policy_amq(
        self,
        mode: str = "ddim",
        num_batches: int | None = None,
        rollout_horizon: int | None = None,
        eval_features: list[torch.Tensor] | None = None,
        eval_seed: int | None = None,
    ) -> float:
        num_batches = self.cfg.ope_num_batches if num_batches is None else num_batches
        rollout_horizon = self.cfg.ope_rollout_horizon if rollout_horizon is None else rollout_horizon
        feature_batches = eval_features or self._prepare_amq_eval_feature_batches(num_batches=num_batches, eval_seed=eval_seed)
        cumulative_q: list[float] = []
        self.critics.eval()
        self.policy.eval()
        self.consistency_model.eval()
        with torch.no_grad():
            for batch_idx, init_features in enumerate(feature_batches):
                cur_features = init_features.to(self.device, non_blocking=True)
                batch_q_sum = torch.zeros(cur_features.shape[0], 1, device=self.device)
                for h in range(rollout_horizon):
                    initial_noise = None
                    if self.cfg.ope_use_common_random_numbers and eval_seed is not None:
                        initial_noise = self._sample_initial_noise(
                            batch_size=cur_features.shape[0],
                            seed=eval_seed + batch_idx * 1009 + h * 104729,
                            dtype=cur_features.dtype,
                        )
                    chunk_action, _ = self._generate_policy_rollout(
                        global_cond=cur_features,
                        mode=mode,
                        noise=initial_noise,
                    )
                    q_value = self.critics.get_q_value(cur_features, chunk_action.reshape(cur_features.shape[0], -1))
                    batch_q_sum += (self.cfg.gamma**h) * q_value
                    if h < rollout_horizon - 1:
                        cur_features, _ = self.transition_model.predict_next_features(
                            obs_features=cur_features,
                            normalized_action=chunk_action.reshape(cur_features.shape[0], -1),
                            deterministic=self.cfg.transition_deterministic_eval,
                        )
                cumulative_q.append(float(batch_q_sum.mean().item()))
        return float(np.mean(cumulative_q)) if cumulative_q else 0.0

    def _build_transition_feature_dataset(self) -> tuple[np.ndarray, np.ndarray]:
        dataloader = self._make_transition_dataloader()
        all_inputs: list[np.ndarray] = []
        all_targets: list[np.ndarray] = []
        self.policy.eval()
        with torch.no_grad():
            for batch_idx, batch in enumerate(dataloader):
                if self.cfg.transition_max_batches > 0 and batch_idx >= self.cfg.transition_max_batches:
                    break
                current_raw, next_raw, extras = self._split_transition_batch(batch)
                current = self._filter_policy_batch(self.preprocessor(current_raw))
                next_obs = self._filter_policy_batch(self.preprocessor(next_raw), include_action=False)
                current = self._to_device(current)
                next_obs = self._to_device(next_obs)
                extras = self._to_device(extras)
                obs_features = self._encode_obs(current)
                next_obs_features = self._encode_obs(next_obs)
                normalized_chunk_action = self._normalized_chunk_action(current)
                delta_features = next_obs_features - obs_features
                reward = extras["chunk_reward"] / self.cfg.reward_scale
                model_input = torch.cat([obs_features, normalized_chunk_action], dim=-1)
                model_target = torch.cat([delta_features, reward], dim=-1)
                all_inputs.append(model_input.detach().cpu().numpy().astype(np.float32))
                all_targets.append(model_target.detach().cpu().numpy().astype(np.float32))
        return np.concatenate(all_inputs, axis=0), np.concatenate(all_targets, axis=0)

    def _train_transition_model(self) -> list[dict[str, float]]:
        inputs, targets = self._build_transition_feature_dataset()
        if inputs.shape[0] == 0:
            logs = [{"phase": "transition", "step": float(self.step), "transition_skipped": 1.0}]
            for item in logs:
                self._log_metrics(item)
            return logs
        metrics = self.transition_model.train_on_feature_arrays(
            inputs=inputs,
            targets=targets,
            batch_size=max(self.cfg.batch_size, 8),
            max_epochs=self.cfg.transition_train_epochs,
            max_epochs_since_update=self.cfg.transition_train_patience,
            holdout_ratio=self.cfg.transition_holdout_ratio,
            logvar_loss_coef=self.cfg.transition_logvar_loss_coef,
        )
        logs = [
            {
                "phase": "transition",
                "step": float(self.step),
                "transition_val_loss": float(metrics["final_val_loss"]),
                "transition_num_samples": float(inputs.shape[0]),
                "transition_num_elites": float(len(metrics.get("elites", []))),
            }
        ]
        for item in logs:
            self._log_metrics(item)
        return logs

    def _train_bc_steps(self, steps: int, phase: str) -> list[dict[str, float]]:
        if steps <= 0:
            return []
        self.policy.train()
        dataloader = self._make_il_dataloader()
        iterator = iter(dataloader)
        logs: list[dict[str, float]] = []
        amp_context = torch.autocast(device_type=self.device.type) if self.device.type == "cuda" and self.cfg.amp else nullcontext()
        for local_step in range(steps):
            try:
                batch = next(iterator)
            except StopIteration:
                iterator = iter(dataloader)
                batch = next(iterator)

            batch = self._to_device(self._filter_policy_batch(self.preprocessor(batch)))
            self.optimizer.zero_grad(set_to_none=True)
            with amp_context:
                loss, _ = self.policy.forward(batch)
            loss.backward()
            grad_norm = torch.nn.utils.clip_grad_norm_(self.policy.parameters(), self.cfg.max_grad_norm)
            self.optimizer.step()

            self.step += 1
            if local_step % 50 == 0 or local_step == steps - 1:
                metrics = {
                    "phase": phase,
                    "step": float(self.step),
                    "loss": float(loss.item()),
                    "grad_norm": float(grad_norm),
                }
                logs.append(metrics)
                self._log_metrics(metrics)
                print(
                    f"[{phase}] step={self.step} local_step={local_step + 1}/{steps} "
                    f"loss={loss.item():.4f} grad_norm={float(grad_norm):.4f}"
                )
        return logs

    def _encode_obs(self, batch: dict[str, torch.Tensor]) -> torch.Tensor:
        obs_only = {key: value for key, value in batch.items() if key != ACTION and key != "action_is_pad"}
        return self.policy.encode_global_conditioning(obs_only)

    def _normalized_chunk_action(self, batch: dict[str, torch.Tensor]) -> torch.Tensor:
        return self.policy.flatten_chunk_action(batch[ACTION])

    def _train_iql_critics(self, steps: int) -> list[dict[str, float]]:
        if steps <= 0:
            return []
        self.policy.eval()
        dataloader = self._make_transition_dataloader()
        iterator = iter(dataloader)
        logs: list[dict[str, float]] = []
        for local_step in range(steps):
            try:
                batch = next(iterator)
            except StopIteration:
                iterator = iter(dataloader)
                batch = next(iterator)

            current_raw, next_raw, extras = self._split_transition_batch(batch)
            current = self._filter_policy_batch(self.preprocessor(current_raw))
            next_obs = self._filter_policy_batch(self.preprocessor(next_raw), include_action=False)
            current = self._to_device(current)
            next_obs = self._to_device(next_obs)
            extras = self._to_device(extras)

            with torch.no_grad():
                obs_features = self._encode_obs(current)
                next_obs_features = self._encode_obs(next_obs)
                chunk_action = self._normalized_chunk_action(current)

            self.v_optimizer.zero_grad(set_to_none=True)
            v_loss, v_info = self.critics.compute_v_loss(obs_features, chunk_action)
            v_loss.backward()
            torch.nn.utils.clip_grad_norm_(self.critics.value.parameters(), self.cfg.max_grad_norm)
            self.v_optimizer.step()

            self.q_optimizer.zero_grad(set_to_none=True)
            reward = extras["chunk_reward"] / self.cfg.reward_scale
            done = extras["chunk_done"]
            q_loss, q_info = self.critics.compute_q_loss(obs_features, chunk_action, reward, next_obs_features, done)
            q_loss.backward()
            torch.nn.utils.clip_grad_norm_(self.critics.q.parameters(), self.cfg.max_grad_norm)
            self.q_optimizer.step()
            self.critics.soft_update_target(self.cfg.target_update_tau)

            if local_step % 50 == 0 or local_step == steps - 1:
                metrics = {
                    "phase": "offline_critic",
                    "step": float(self.step),
                    "v_loss": float(v_loss.item()),
                    "q_loss": float(q_loss.item()),
                    "adv_mean": float((self.critics.compute_advantage(obs_features, chunk_action)).mean().item()),
                }
                metrics.update(v_info)
                metrics.update(q_info)
                logs.append(metrics)
                self._log_metrics(metrics)
                print(
                    f"[offline_critic] step={self.step} local_step={local_step + 1}/{steps} "
                    f"v_loss={v_loss.item():.4f} q_loss={q_loss.item():.4f}"
                )
            self.step += 1
        return logs

    def _offline_policy_optimization(self, steps: int, phase: str) -> list[dict[str, float]]:
        if steps <= 0:
            return []
        dataloader = self._make_transition_dataloader()
        iterator = iter(dataloader)
        logs: list[dict[str, float]] = []
        self.policy.train()
        self.consistency_model.train()
        self.critics.eval()
        eval_seed = self.cfg.ope_seed + 10007 * max(1, len(self.history))
        eval_features = None
        j_old = 0.0
        policy_snapshot = None
        consistency_snapshot = None
        optimizer_snapshot = None
        consistency_optimizer_snapshot = None
        if self.cfg.ope_enabled:
            eval_features = self._prepare_amq_eval_feature_batches(
                num_batches=self.cfg.ope_num_batches,
                eval_seed=eval_seed,
            )
            j_old = self._evaluate_policy_amq(
                mode="ddim",
                num_batches=self.cfg.ope_num_batches,
                rollout_horizon=self.cfg.ope_rollout_horizon,
                eval_features=eval_features,
                eval_seed=eval_seed,
            )
            policy_snapshot = copy.deepcopy(self.policy.state_dict())
            consistency_snapshot = copy.deepcopy(self.consistency_model.state_dict())
            optimizer_snapshot = copy.deepcopy(self.optimizer.state_dict())
            consistency_optimizer_snapshot = copy.deepcopy(self.consistency_optimizer.state_dict())
        self._set_obs_encoder_requires_grad(False)
        for local_step in range(steps):
            try:
                batch = next(iterator)
            except StopIteration:
                iterator = iter(dataloader)
                batch = next(iterator)

            current_raw, _, _ = self._split_transition_batch(batch)
            current = self._filter_policy_batch(self.preprocessor(current_raw))
            current = self._to_device(current)

            with torch.no_grad():
                obs_features = self._encode_obs(current)
                chunk_action = self._normalized_chunk_action(current)
                advantages = self.critics.compute_advantage(obs_features, chunk_action)
                advantages = (advantages - advantages.mean()) / (advantages.std() + 1e-8)
                global_cond = obs_features
                initial_noise = torch.randn(
                    global_cond.shape[0],
                    self.cfg.horizon,
                    self.policy.action_dim,
                    device=self.device,
                    dtype=global_cond.dtype,
                )
                _, trajectory, old_log_probs = self.policy.sample_trajectory(global_cond, noise=initial_noise)

            last_info: dict[str, float] = {}
            ppo_loss_value = 0.0
            for _ in range(self.cfg.ppo_inner_steps):
                self.optimizer.zero_grad(set_to_none=True)
                self.consistency_optimizer.zero_grad(set_to_none=True)
                ppo_loss, ppo_info = self.policy.compute_ppo_loss(old_log_probs, advantages, trajectory, global_cond)
                total_loss = ppo_loss
                cd_loss_value = 0.0
                if self.cfg.lambda_cd > 0.0 and self.step % max(1, self.cfg.cd_every) == 0:
                    cd_loss, cd_info = self.consistency_distillation.compute_distillation_loss(
                        global_cond=global_cond,
                        noise=initial_noise,
                    )
                    total_loss = total_loss + self.cfg.lambda_cd * cd_loss
                    cd_loss_value = float(cd_info["cd_loss"])
                total_loss.backward()
                grad_norm = torch.nn.utils.clip_grad_norm_(self.policy.parameters(), self.cfg.max_grad_norm)
                self.optimizer.step()
                if cd_loss_value > 0.0:
                    torch.nn.utils.clip_grad_norm_(self.consistency_model.parameters(), self.cfg.max_grad_norm)
                    self.consistency_optimizer.step()
                ppo_loss_value = float(ppo_loss.item())
                last_info = dict(ppo_info)
                last_info["grad_norm"] = float(grad_norm)
                last_info["cd_loss"] = cd_loss_value

            if local_step % 50 == 0 or local_step == steps - 1:
                metrics = {
                    "phase": phase,
                    "step": float(self.step),
                    "ppo_loss": float(ppo_loss_value),
                    "mean_advantage": float(advantages.mean().item()),
                    "std_advantage": float(advantages.std().item()),
                }
                metrics.update(last_info)
                logs.append(metrics)
                self._log_metrics(metrics)
                print(
                    f"[{phase}] step={self.step} local_step={local_step + 1}/{steps} "
                    f"ppo_loss={ppo_loss_value:.4f} kl={last_info.get('approx_kl', 0.0):.4f} "
                    f"clip_frac={last_info.get('clip_frac', 0.0):.4f} "
                    f"cd_loss={last_info.get('cd_loss', 0.0):.4f}"
                )
            self.step += 1
        self._set_obs_encoder_requires_grad(True)
        if self.cfg.ope_enabled:
            j_new = self._evaluate_policy_amq(
                mode="ddim",
                num_batches=self.cfg.ope_num_batches,
                rollout_horizon=self.cfg.ope_rollout_horizon,
                eval_features=eval_features,
                eval_seed=eval_seed,
            )
            delta = max(self.cfg.ope_delta_abs_min, self.cfg.ope_delta_coef * abs(j_old)) if j_old != 0 else self.cfg.ope_delta_abs_min
            accepted = j_new - j_old >= delta
            logs.append(
                {
                    "phase": f"{phase}_ope",
                    "step": float(self.step),
                    "ope_j_old": float(j_old),
                    "ope_j_new": float(j_new),
                    "ope_delta": float(delta),
                    "ope_accepted": float(int(accepted)),
                }
            )
            self._log_metrics(logs[-1])
            if not accepted:
                if policy_snapshot is not None:
                    self.policy.load_state_dict(policy_snapshot)
                if consistency_snapshot is not None:
                    self.consistency_model.load_state_dict(consistency_snapshot)
                if optimizer_snapshot is not None:
                    self.optimizer.load_state_dict(optimizer_snapshot)
                if consistency_optimizer_snapshot is not None:
                    self.consistency_optimizer.load_state_dict(consistency_optimizer_snapshot)
                print(
                    f"[{phase}:ope] rejected update, rollback applied "
                    f"(j_old={j_old:.4f}, j_new={j_new:.4f}, delta={delta:.4f})"
                )
            else:
                print(
                    f"[{phase}:ope] accepted update "
                    f"(j_old={j_old:.4f}, j_new={j_new:.4f}, delta={delta:.4f})"
                )
        return logs

    def _policy_action_from_numpy_obs(
        self,
        numpy_observation: dict[str, Any],
        mode: str,
    ) -> tuple[torch.Tensor, dict[str, Tensor | list[Tensor]] | None]:
        safe_observation: dict[str, Any] = {}
        for key, value in numpy_observation.items():
            if isinstance(value, np.ndarray):
                safe_observation[key] = np.ascontiguousarray(value)
            else:
                safe_observation[key] = value
        observation = prepare_observation_for_inference(
            safe_observation,
            self.device,
            task=self.cfg.task,
            robot_type=None,
        )
        processed = self._to_device(self._filter_policy_batch(self.preprocessor(observation), include_action=False))
        with torch.inference_mode():
            mode = mode.lower()
            if mode == "ddim":
                action, info = self.policy.select_action_with_info(processed)
            elif mode == "cm":
                stacked = self.policy._stack_visual_inputs(processed)
                self.policy._queues = populate_queues(self.policy._queues, stacked)
                info = None
                if len(self.policy._queues[ACTION]) == 0:
                    chunk_batch = {
                        key: torch.stack(list(self.policy._queues[key]), dim=1)
                        for key in self.policy._queues
                        if key != ACTION
                    }
                    global_cond = self.policy.encode_global_conditioning(chunk_batch)
                    actions, info = self._generate_policy_rollout(global_cond=global_cond, mode="cm")
                    self.policy._queues[ACTION].extend(actions.transpose(0, 1))
                action = self.policy._queues[ACTION].popleft()
            else:
                raise ValueError(f"Unsupported policy mode: {mode}")
            action = self.postprocessor(action)
        if isinstance(action, dict):
            return action[ACTION], info
        return action, info

    @staticmethod
    def _to_numpy_trajectory(info: dict[str, Tensor | list[Tensor]]) -> dict[str, Any]:
        trajectory = [step.detach().cpu().numpy() for step in info["trajectory"]]  # type: ignore[index]
        log_probs = [step.detach().cpu().numpy() for step in info["log_probs_old"]]  # type: ignore[index]
        return {
            "trajectory": trajectory,
            "log_probs_old": log_probs,
        }

    def _collect_rollouts(
        self,
        episodes: int,
        phase: str,
        iteration: int,
        record_decisions: bool,
        mode: str,
    ) -> tuple[RolloutDatasetSpec, dict[str, Any], list[dict[str, Any]]]:
        rollout_dir = self.rollout_root / f"{phase}_{iteration:03d}"
        env = GenesisEnv(
            task=self.cfg.task,
            observation_height=self.cfg.observation_height,
            observation_width=self.cfg.observation_width,
            show_viewer=self.cfg.show_viewer,
            max_episode_steps=self.cfg.max_episode_steps,
        )
        dataset = create_lerobot_dataset(rollout_dir, env, include_rl_labels=True)
        success_count = 0
        saved_episode_indices: list[int] = []
        episode_infos: list[dict[str, Any]] = []

        for episode_idx in range(episodes):
            self.policy.eval()
            self.consistency_model.eval()
            self.policy.reset()
            self.preprocessor.reset()
            self.postprocessor.reset()
            numpy_observation, _ = env.reset(seed=self.cfg.seed + iteration * 1000 + episode_idx)
            frames: list[dict[str, Any]] = []
            done = False
            reward_sum = 0.0
            episode_success = False
            decision_steps: list[dict[str, Any]] = []
            current_decision: dict[str, Any] | None = None
            decision_env_step = 0
            active_mode = mode

            while not done:
                if current_decision is not None and len(self.policy._queues[ACTION]) == 0:
                    current_decision["next_obs"] = dict(numpy_observation)
                    decision_steps.append(current_decision)
                    current_decision = None
                    decision_env_step = 0

                active_mode = mode
                if record_decisions and mode == "cm":
                    active_mode = "ddim"
                action_tensor, info = self._policy_action_from_numpy_obs(numpy_observation, mode=active_mode)
                if info is not None and record_decisions and active_mode == "ddim":
                    current_decision = {
                        "obs": dict(numpy_observation),
                        **self._to_numpy_trajectory(info),
                        "reward": 0.0,
                        "done": False,
                    }
                    decision_env_step = 0

                action = action_tensor.squeeze(0).detach().cpu().numpy()
                next_observation, reward, terminated, truncated, info = env.step(action)
                done = bool(terminated or truncated)
                success = bool(info.get("is_success", reward > 0))
                reward_sum += float(reward)
                episode_success = episode_success or success
                if current_decision is not None:
                    current_decision["reward"] += (self.cfg.gamma**decision_env_step) * float(reward)
                    current_decision["done"] = current_decision["done"] or done
                    decision_env_step += 1

                frames.append(
                    build_frame(
                        numpy_observation=numpy_observation,
                        action=action,
                        task=env.get_task_description(),
                        reward=float(reward),
                        done=done,
                        success=success,
                        episode_success=episode_success,
                    )
                )
                numpy_observation = next_observation

            if current_decision is not None and record_decisions:
                current_decision["next_obs"] = dict(numpy_observation)
                decision_steps.append(current_decision)

            for frame in frames:
                frame["episode.success"] = np.asarray([episode_success], dtype=bool)
            for frame in frames:
                dataset.add_frame(frame)
            dataset.save_episode()
            episode_index = dataset.meta.total_episodes - 1
            saved_episode_indices.append(episode_index)
            append_episode_summary(
                dataset_root=dataset.root,
                episode_index=episode_index,
                success=episode_success,
                episode_return=reward_sum,
                episode_length=len(frames),
                task=env.get_task_description(),
                metadata=env.get_episode_metadata(),
            )
            success_count += int(episode_success)
            episode_infos.append({"success": episode_success, "decision_steps": decision_steps})

            print(
                f"[collect:{phase}] episode={episode_idx + 1}/{episodes} reward={reward_sum:.1f} "
                f"success={int(episode_success)} decisions={len(decision_steps)} mode={active_mode}"
            )

        env.close()
        self._restore_default_torch_device()
        dataset.finalize()
        success_episodes = [idx for idx, info in zip(saved_episode_indices, episode_infos, strict=True) if info["success"]]
        summary = {
            "phase": phase,
            "iteration": iteration,
            "episodes": episodes,
            "saved_episodes": len(saved_episode_indices),
            "success_count": success_count,
            "success_rate": success_count / max(1, episodes),
        }
        self._log_metrics(summary)
        return RolloutDatasetSpec(root=Path(dataset.root), success_episodes=success_episodes), summary, episode_infos

    def _evaluate(self, episodes: int, phase: str, iteration: int) -> dict[str, Any]:
        env = GenesisEnv(
            task=self.cfg.task,
            observation_height=self.cfg.observation_height,
            observation_width=self.cfg.observation_width,
            show_viewer=False,
            max_episode_steps=self.cfg.max_episode_steps,
        )
        rewards: list[float] = []
        success_count = 0
        for episode_idx in range(episodes):
            self.policy.eval()
            self.consistency_model.eval()
            self.policy.reset()
            self.preprocessor.reset()
            self.postprocessor.reset()
            numpy_observation, _ = env.reset(seed=self.cfg.seed + 100_000 + iteration * 1000 + episode_idx)
            done = False
            reward_sum = 0.0
            success = False
            while not done:
                action_tensor, _ = self._policy_action_from_numpy_obs(numpy_observation, mode=self.cfg.eval_policy_mode)
                action = action_tensor.squeeze(0).detach().cpu().numpy()
                numpy_observation, reward, terminated, truncated, info = env.step(action)
                done = bool(terminated or truncated)
                reward_sum += float(reward)
                success = success or bool(info.get("is_success", reward > 0))
            rewards.append(reward_sum)
            success_count += int(success)
        env.close()
        self._restore_default_torch_device()
        metrics = {
            "phase": phase,
            "iteration": iteration,
            "eval_episodes": episodes,
            "avg_reward": float(sum(rewards) / max(1, len(rewards))),
            "success_rate": success_count / max(1, episodes),
            "policy_mode": self.cfg.eval_policy_mode,
        }
        print(
            f"[eval:{phase}] iteration={iteration} avg_reward={metrics['avg_reward']:.3f} "
            f"success_rate={metrics['success_rate']:.3f}"
        )
        self._log_metrics(metrics)
        return metrics

    def _online_value_regression(self, decision_buffer: list[dict[str, Any]], steps: int) -> list[dict[str, float]]:
        if steps <= 0 or not decision_buffer:
            return []
        logs: list[dict[str, float]] = []
        indices = np.arange(len(decision_buffer))
        for local_step in range(steps):
            batch_indices = np.random.choice(indices, size=min(self.cfg.batch_size, len(indices)), replace=False)
            obs_batch = self._filter_policy_batch(self.preprocessor(
                {
                    key: torch.stack(
                        [torch.as_tensor(decision_buffer[idx]["obs"][key]) for idx in batch_indices], dim=0
                    )
                    for key in self.base_dataset.features
                    if key.startswith("observation.")
                }
            ), include_action=False)
            obs_batch = self._to_device(obs_batch)
            obs_features = self._encode_obs(obs_batch)
            returns = torch.as_tensor(
                [decision_buffer[idx]["return"] for idx in batch_indices],
                dtype=torch.float32,
                device=self.device,
            ).unsqueeze(-1)
            self.v_optimizer.zero_grad(set_to_none=True)
            value_loss = torch.nn.functional.mse_loss(self.critics.value(obs_features), returns)
            value_loss.backward()
            torch.nn.utils.clip_grad_norm_(self.critics.value.parameters(), self.cfg.max_grad_norm)
            self.v_optimizer.step()
            self.critics.soft_update_target(self.cfg.target_update_tau)
            if local_step % 50 == 0 or local_step == steps - 1:
                logs.append({"phase": "online_value", "step": float(self.step), "value_loss": float(value_loss.item())})
                self._log_metrics(logs[-1])
                print(f"[online_value] step={self.step} local_step={local_step + 1}/{steps} value_loss={value_loss.item():.4f}")
            self.step += 1
        return logs

    def _prepare_online_buffer(self, episode_infos: list[dict[str, Any]]) -> list[dict[str, Any]]:
        gamma = self.cfg.gamma
        lam = self.cfg.gae_lambda
        decision_buffer: list[dict[str, Any]] = []
        for episode_info in episode_infos:
            decisions = episode_info["decision_steps"]
            if not decisions:
                continue
            obs_batch = self._filter_policy_batch(self.preprocessor(
                {
                    key: torch.stack([torch.as_tensor(step["obs"][key]) for step in decisions], dim=0)
                    for key in self.base_dataset.features
                    if key.startswith("observation.")
                }
            ), include_action=False)
            next_obs_batch = self._filter_policy_batch(self.preprocessor(
                {
                    key: torch.stack([torch.as_tensor(step["next_obs"][key]) for step in decisions], dim=0)
                    for key in self.base_dataset.features
                    if key.startswith("observation.")
                }
            ), include_action=False)
            obs_batch = self._to_device(obs_batch)
            next_obs_batch = self._to_device(next_obs_batch)
            with torch.no_grad():
                values = self.critics.value(self._encode_obs(obs_batch)).squeeze(-1)
                next_values = self.critics.value(self._encode_obs(next_obs_batch)).squeeze(-1)
            rewards = torch.as_tensor([step["reward"] for step in decisions], dtype=torch.float32, device=self.device)
            dones = torch.as_tensor([float(step["done"]) for step in decisions], dtype=torch.float32, device=self.device)

            advantages = torch.zeros_like(rewards)
            last_gae = torch.zeros((), device=self.device)
            for t in reversed(range(len(decisions))):
                delta = rewards[t] + gamma * (1.0 - dones[t]) * next_values[t] - values[t]
                last_gae = delta + gamma * lam * (1.0 - dones[t]) * last_gae
                advantages[t] = last_gae
            returns = advantages + values

            for idx, decision in enumerate(decisions):
                decision_buffer.append(
                    {
                        **decision,
                        "advantage": float(advantages[idx].item()),
                        "return": float(returns[idx].item()),
                    }
                )

        if not decision_buffer:
            return decision_buffer
        adv = torch.as_tensor([item["advantage"] for item in decision_buffer], dtype=torch.float32)
        adv = (adv - adv.mean()) / (adv.std() + 1e-8)
        for item, norm_adv in zip(decision_buffer, adv.tolist(), strict=True):
            item["advantage"] = float(norm_adv)
        return decision_buffer

    def _online_policy_optimization(self, decision_buffer: list[dict[str, Any]], steps: int) -> list[dict[str, float]]:
        if steps <= 0 or not decision_buffer:
            return []
        logs: list[dict[str, float]] = []
        indices = np.arange(len(decision_buffer))
        self.consistency_model.train()
        for local_step in range(steps):
            batch_indices = np.random.choice(indices, size=min(self.cfg.batch_size, len(indices)), replace=False)
            obs_raw = {
                key: torch.stack([torch.as_tensor(decision_buffer[idx]["obs"][key]) for idx in batch_indices], dim=0)
                for key in self.base_dataset.features
                if key.startswith("observation.")
            }
            obs_batch = self._filter_policy_batch(self.preprocessor(obs_raw), include_action=False)
            obs_batch = self._to_device(obs_batch)
            global_cond = self._encode_obs(obs_batch)
            advantages = torch.as_tensor(
                [decision_buffer[idx]["advantage"] for idx in batch_indices],
                dtype=torch.float32,
                device=self.device,
            ).unsqueeze(-1)
            trajectories = [
                torch.as_tensor(
                    np.concatenate([decision_buffer[idx]["trajectory"][step_idx] for idx in batch_indices], axis=0),
                    device=self.device,
                    dtype=torch.float32,
                )
                for step_idx in range(len(decision_buffer[batch_indices[0]]["trajectory"]))
            ]
            old_log_probs = [
                torch.as_tensor(
                    np.concatenate([decision_buffer[idx]["log_probs_old"][step_idx] for idx in batch_indices], axis=0),
                    device=self.device,
                    dtype=torch.float32,
                )
                for step_idx in range(len(decision_buffer[batch_indices[0]]["log_probs_old"]))
            ]
            self.optimizer.zero_grad(set_to_none=True)
            self.consistency_optimizer.zero_grad(set_to_none=True)
            ppo_loss, ppo_info = self.policy.compute_ppo_loss(old_log_probs, advantages, trajectories, global_cond)
            total_loss = ppo_loss
            cd_loss_value = 0.0
            if self.cfg.lambda_cd > 0.0 and self.step % max(1, self.cfg.cd_every) == 0:
                cd_loss, cd_info = self.consistency_distillation.compute_distillation_loss(
                    global_cond=global_cond,
                    noise=trajectories[0],
                )
                total_loss = total_loss + self.cfg.lambda_cd * cd_loss
                cd_loss_value = float(cd_info["cd_loss"])
            total_loss.backward()
            grad_norm = torch.nn.utils.clip_grad_norm_(self.policy.parameters(), self.cfg.max_grad_norm)
            self.optimizer.step()
            if cd_loss_value > 0.0:
                torch.nn.utils.clip_grad_norm_(self.consistency_model.parameters(), self.cfg.max_grad_norm)
                self.consistency_optimizer.step()
            if local_step % 50 == 0 or local_step == steps - 1:
                metrics = {
                    "phase": "online_ppo",
                    "step": float(self.step),
                    "ppo_loss": float(ppo_loss.item()),
                    "grad_norm": float(grad_norm),
                    "cd_loss": float(cd_loss_value),
                }
                metrics.update(ppo_info)
                logs.append(metrics)
                self._log_metrics(metrics)
                print(
                    f"[online_ppo] step={self.step} local_step={local_step + 1}/{steps} "
                    f"ppo_loss={ppo_loss.item():.4f} kl={ppo_info.get('approx_kl', 0.0):.4f}"
                )
            self.step += 1
        return logs

    def _save_checkpoint(self, name: str) -> None:
        checkpoint_dir = self.output_dir / "checkpoints" / name
        checkpoint_dir.mkdir(parents=True, exist_ok=True)
        pretrained_dir = checkpoint_dir / "pretrained_model"
        self.policy.save_pretrained(pretrained_dir)
        self.preprocessor.save_pretrained(pretrained_dir)
        self.postprocessor.save_pretrained(pretrained_dir)
        torch.save(
            {
                "optimizer": self.optimizer.state_dict(),
                "critics": self.critics.state_dict(),
                "v_optimizer": self.v_optimizer.state_dict(),
                "q_optimizer": self.q_optimizer.state_dict(),
                "consistency_model": self.consistency_model.state_dict(),
                "consistency_optimizer": self.consistency_optimizer.state_dict(),
                "transition_model": self.transition_model.state_dict(),
                "step": self.step,
                "rl_roots": [str(root) for root in self.rl_roots],
                "il_specs": [{"root": str(spec.root), "success_episodes": spec.success_episodes} for spec in self.il_specs],
            },
            checkpoint_dir / "trainer_state.pt",
        )
        with open(checkpoint_dir / "sim_rl100_config.json", "w") as f:
            json.dump(asdict(self.cfg), f, indent=2)

    def run(self) -> None:
        torch.manual_seed(self.cfg.seed)
        np.random.seed(self.cfg.seed)
        if torch.cuda.is_available():
            torch.cuda.manual_seed_all(self.cfg.seed)
        self._init_wandb()

        try:
            self.history.extend(self._train_bc_steps(self.cfg.il_steps, phase="il"))
            self.history.append(self._evaluate(self.cfg.eval_episodes, phase="il", iteration=0))
            self._save_checkpoint("il")

            for iteration in range(1, self.cfg.offline_iterations + 1):
                self.history.extend(self._train_transition_model())
                self.history.extend(self._train_iql_critics(self.cfg.critic_steps))
                self.history.extend(self._offline_policy_optimization(self.cfg.offline_finetune_steps, phase=f"offline_ppo_{iteration}"))
                rollout_spec, collect_summary, _ = self._collect_rollouts(
                    episodes=self.cfg.offline_collection_episodes,
                    phase="offline",
                    iteration=iteration,
                    record_decisions=False,
                    mode=self.cfg.rollout_policy_mode,
                )
                self.history.append(collect_summary)
                self.rl_roots.append(rollout_spec.root)
                self.il_specs.append(rollout_spec)
                self.history.extend(self._train_bc_steps(self.cfg.il_retrain_steps, phase=f"offline_retrain_{iteration}"))
                self.history.append(self._evaluate(self.cfg.eval_episodes, phase="offline", iteration=iteration))
                if iteration % self.cfg.save_every == 0:
                    self._save_checkpoint(f"offline_{iteration:03d}")

            for iteration in range(1, self.cfg.online_iterations + 1):
                rollout_spec, collect_summary, episode_infos = self._collect_rollouts(
                    episodes=self.cfg.online_collection_episodes,
                    phase="online",
                    iteration=iteration,
                    record_decisions=True,
                    mode=self.cfg.online_record_policy_mode,
                )
                self.history.append(collect_summary)
                self.rl_roots.append(rollout_spec.root)
                self.il_specs.append(rollout_spec)
                decision_buffer = self._prepare_online_buffer(episode_infos)
                self.history.extend(self._online_value_regression(decision_buffer, self.cfg.online_value_steps))
                self.history.extend(self._online_policy_optimization(decision_buffer, self.cfg.online_finetune_steps))
                self.history.append(self._evaluate(self.cfg.eval_episodes, phase="online", iteration=iteration))
                if iteration % self.cfg.save_every == 0:
                    self._save_checkpoint(f"online_{iteration:03d}")
        finally:
            self._save_checkpoint("last")
            history_path = self.output_dir / "history.json"
            with open(history_path, "w") as f:
                json.dump(self.history, f, indent=2)
            if self.cfg.use_wandb and self.wandb_run is not None:
                if self.history:
                    final_metrics = self._sanitize_metrics(self.history[-1])
                    for key, value in final_metrics.items():
                        if key not in {"phase", "step", "iteration"}:
                            self.wandb_run.summary[f"final/{key}"] = value
                self.wandb_run.finish()


def default_output_dir(dataset_root: str | Path) -> Path:
    dataset_root = Path(dataset_root)
    return Path("outputs") / "rl100_sim" / dataset_root.name


def make_default_config(dataset_root: str | Path, task: str) -> SimRL100Config:
    return SimRL100Config(
        dataset_root=str(Path(dataset_root).resolve()),
        output_dir=str(default_output_dir(dataset_root)),
        task=task,
    )
