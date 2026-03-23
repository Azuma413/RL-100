from __future__ import annotations

import json
from contextlib import nullcontext
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any

import numpy as np
import torch
from torch.utils.data import ConcatDataset, DataLoader

from lerobot.datasets.factory import resolve_delta_timestamps
from lerobot.datasets.lerobot_dataset import LeRobotDataset, LeRobotDatasetMetadata
from lerobot.datasets.utils import dataset_to_policy_features
from lerobot.policies.factory import make_pre_post_processors
from lerobot.policies.utils import prepare_observation_for_inference
from lerobot.utils.constants import ACTION
from lerobot.utils.utils import get_safe_torch_device
from rl_100.env.genesis_env import GenesisEnv
from rl_100.lerobot_dataset_utils import build_frame, create_lerobot_dataset
from rl_100.training.rl100_critics import IQLCritics
from rl_100.training.rl100_dataset import RL100TransitionDataset, RolloutDatasetSpec, configure_hf_cache
from rl_100.training.rl100_policy import RL100DiffusionConfig, RL100DiffusionPolicy


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


class SimRL100Trainer:
    def __init__(self, cfg: SimRL100Config):
        self.cfg = cfg
        self.output_dir = Path(cfg.output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)
        self.rollout_root = self.output_dir / "rollouts"
        self.rollout_root.mkdir(parents=True, exist_ok=True)
        self.device = get_safe_torch_device(cfg.device)
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

        self.rl_roots: list[Path] = [self.base_dataset_root]
        self.il_specs: list[RolloutDatasetSpec] = [RolloutDatasetSpec(root=self.base_dataset_root, success_episodes=[])]
        self.step = 0
        self.history: list[dict[str, Any]] = []

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
        return {key: value for key, value in processed.items() if key != ACTION and key != "action_is_pad"}

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

            batch = self._filter_policy_batch(self.preprocessor(batch))
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
        self.critics.eval()
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
                global_cond = self._encode_obs(current)
                _, trajectory, old_log_probs = self.policy.sample_trajectory(global_cond)

            last_info: dict[str, float] = {}
            ppo_loss_value = 0.0
            for _ in range(self.cfg.ppo_inner_steps):
                self.optimizer.zero_grad(set_to_none=True)
                ppo_loss, ppo_info = self.policy.compute_ppo_loss(old_log_probs, advantages, trajectory, global_cond)
                ppo_loss.backward()
                grad_norm = torch.nn.utils.clip_grad_norm_(self.policy.parameters(), self.cfg.max_grad_norm)
                self.optimizer.step()
                ppo_loss_value = float(ppo_loss.item())
                last_info = dict(ppo_info)
                last_info["grad_norm"] = float(grad_norm)

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
                print(
                    f"[{phase}] step={self.step} local_step={local_step + 1}/{steps} "
                    f"ppo_loss={ppo_loss_value:.4f} kl={last_info.get('approx_kl', 0.0):.4f} "
                    f"clip_frac={last_info.get('clip_frac', 0.0):.4f}"
                )
            self.step += 1
        return logs

    def _policy_action_from_numpy_obs(
        self,
        numpy_observation: dict[str, Any],
    ) -> tuple[torch.Tensor, dict[str, Tensor | list[Tensor]] | None]:
        observation = prepare_observation_for_inference(
            dict(numpy_observation),
            self.device,
            task=self.cfg.task,
            robot_type=None,
        )
        processed = self._filter_policy_batch(self.preprocessor(observation), include_action=False)
        with torch.inference_mode():
            action, info = self.policy.select_action_with_info(processed)
            action = self.postprocessor(action)
        return action[ACTION], info

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
    ) -> tuple[RolloutDatasetSpec, dict[str, Any], list[dict[str, Any]]]:
        rollout_dir = self.rollout_root / f"{phase}_{iteration:03d}"
        env = GenesisEnv(
            task=self.cfg.task,
            observation_height=self.cfg.observation_height,
            observation_width=self.cfg.observation_width,
            show_viewer=self.cfg.show_viewer,
        )
        dataset = create_lerobot_dataset(rollout_dir, env, include_rl_labels=True)
        success_count = 0
        saved_episode_indices: list[int] = []
        episode_infos: list[dict[str, Any]] = []

        for episode_idx in range(episodes):
            self.policy.eval()
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

            while not done:
                if current_decision is not None and len(self.policy._queues[ACTION]) == 0:
                    current_decision["next_obs"] = dict(numpy_observation)
                    decision_steps.append(current_decision)
                    current_decision = None
                    decision_env_step = 0

                action_tensor, info = self._policy_action_from_numpy_obs(numpy_observation)
                if info is not None and record_decisions:
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
                    )
                )
                numpy_observation = next_observation

            if current_decision is not None and record_decisions:
                current_decision["next_obs"] = dict(numpy_observation)
                decision_steps.append(current_decision)

            for frame in frames:
                dataset.add_frame(frame)
            dataset.save_episode()
            saved_episode_indices.append(dataset.meta.total_episodes - 1)
            success_count += int(episode_success)
            episode_infos.append({"success": episode_success, "decision_steps": decision_steps})

            print(
                f"[collect:{phase}] episode={episode_idx + 1}/{episodes} reward={reward_sum:.1f} "
                f"success={int(episode_success)} decisions={len(decision_steps)}"
            )

        env.close()
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
        return RolloutDatasetSpec(root=Path(dataset.root), success_episodes=success_episodes), summary, episode_infos

    def _evaluate(self, episodes: int, phase: str, iteration: int) -> dict[str, Any]:
        env = GenesisEnv(
            task=self.cfg.task,
            observation_height=self.cfg.observation_height,
            observation_width=self.cfg.observation_width,
            show_viewer=False,
        )
        rewards: list[float] = []
        success_count = 0
        for episode_idx in range(episodes):
            self.policy.eval()
            self.policy.reset()
            self.preprocessor.reset()
            self.postprocessor.reset()
            numpy_observation, _ = env.reset(seed=self.cfg.seed + 100_000 + iteration * 1000 + episode_idx)
            done = False
            reward_sum = 0.0
            success = False
            while not done:
                action_tensor, _ = self._policy_action_from_numpy_obs(numpy_observation)
                action = action_tensor.squeeze(0).detach().cpu().numpy()
                numpy_observation, reward, terminated, truncated, info = env.step(action)
                done = bool(terminated or truncated)
                reward_sum += float(reward)
                success = success or bool(info.get("is_success", reward > 0))
            rewards.append(reward_sum)
            success_count += int(success)
        env.close()
        metrics = {
            "phase": phase,
            "iteration": iteration,
            "eval_episodes": episodes,
            "avg_reward": float(sum(rewards) / max(1, len(rewards))),
            "success_rate": success_count / max(1, episodes),
        }
        print(
            f"[eval:{phase}] iteration={iteration} avg_reward={metrics['avg_reward']:.3f} "
            f"success_rate={metrics['success_rate']:.3f}"
        )
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
            ppo_loss, ppo_info = self.policy.compute_ppo_loss(old_log_probs, advantages, trajectories, global_cond)
            ppo_loss.backward()
            grad_norm = torch.nn.utils.clip_grad_norm_(self.policy.parameters(), self.cfg.max_grad_norm)
            self.optimizer.step()
            if local_step % 50 == 0 or local_step == steps - 1:
                metrics = {
                    "phase": "online_ppo",
                    "step": float(self.step),
                    "ppo_loss": float(ppo_loss.item()),
                    "grad_norm": float(grad_norm),
                }
                metrics.update(ppo_info)
                logs.append(metrics)
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

        self.history.extend(self._train_bc_steps(self.cfg.il_steps, phase="il"))
        self.history.append(self._evaluate(self.cfg.eval_episodes, phase="il", iteration=0))
        self._save_checkpoint("il")

        for iteration in range(1, self.cfg.offline_iterations + 1):
            self.history.extend(self._train_iql_critics(self.cfg.critic_steps))
            self.history.extend(self._offline_policy_optimization(self.cfg.offline_finetune_steps, phase=f"offline_ppo_{iteration}"))
            rollout_spec, collect_summary, _ = self._collect_rollouts(
                episodes=self.cfg.offline_collection_episodes,
                phase="offline",
                iteration=iteration,
                record_decisions=False,
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

        self._save_checkpoint("last")
        history_path = self.output_dir / "history.json"
        with open(history_path, "w") as f:
            json.dump(self.history, f, indent=2)


def default_output_dir(dataset_root: str | Path) -> Path:
    dataset_root = Path(dataset_root)
    return Path("outputs") / "rl100_sim" / dataset_root.name


def make_default_config(dataset_root: str | Path, task: str) -> SimRL100Config:
    return SimRL100Config(
        dataset_root=str(Path(dataset_root).resolve()),
        output_dir=str(default_output_dir(dataset_root)),
        task=task,
    )
