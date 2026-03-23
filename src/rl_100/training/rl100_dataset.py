from __future__ import annotations

import os
from collections import OrderedDict
from dataclasses import dataclass
from pathlib import Path

import numpy as np
import torch
from torch.utils.data import Dataset

from lerobot.datasets.lerobot_dataset import LeRobotDataset
from lerobot.utils.constants import DONE, REWARD
from rl_100.lerobot_dataset_utils import EPISODE_SUCCESS, NEXT_SUCCESS, load_episode_summaries


def configure_hf_cache(cache_root: str | Path = "/tmp/rl100_hf_cache") -> Path:
    cache_root = Path(cache_root)
    cache_root.mkdir(parents=True, exist_ok=True)
    for subdir in ("hub", "datasets", "matplotlib", "xdg", "taichi", "quadrants"):
        (cache_root / subdir).mkdir(parents=True, exist_ok=True)
    os.environ["HF_HOME"] = str(cache_root)
    os.environ["HF_HUB_CACHE"] = str(cache_root / "hub")
    os.environ["HF_DATASETS_CACHE"] = str(cache_root / "datasets")
    os.environ.setdefault("MPLCONFIGDIR", str(cache_root / "matplotlib"))
    os.environ.setdefault("XDG_CACHE_HOME", str(cache_root / "xdg"))
    os.environ.setdefault("TAICHI_CACHE_DIR", str(cache_root / "taichi"))
    os.environ.setdefault("QUADRANTS_CACHE_DIR", str(cache_root / "quadrants"))
    try:
        from datasets import config as datasets_config

        datasets_config.HF_HOME = str(cache_root)
        datasets_config.HF_HUB_CACHE = str(cache_root / "hub")
        datasets_config.HF_DATASETS_CACHE = str(cache_root / "datasets")
    except Exception:
        pass
    return cache_root


@dataclass
class RolloutDatasetSpec:
    root: Path
    success_episodes: list[int]


class RL100TransitionDataset(Dataset):
    def __init__(
        self,
        root: str | Path,
        horizon: int,
        n_obs_steps: int,
        n_action_steps: int,
        gamma: float,
        relabel_sparse_reward: bool = True,
        assume_demo_success: bool = True,
    ):
        configure_hf_cache()
        self.root = Path(root).resolve()
        self.dataset = LeRobotDataset(repo_id=self.root.name, root=self.root)
        self.horizon = horizon
        self.n_obs_steps = n_obs_steps
        self.n_action_steps = n_action_steps
        self.gamma = gamma
        self.relabel_sparse_reward = relabel_sparse_reward
        self.assume_demo_success = assume_demo_success
        self.obs_keys = [key for key in self.dataset.features if key.startswith("observation.")]
        self.has_reward = REWARD in self.dataset.features
        self.has_done = DONE in self.dataset.features
        self.has_success = NEXT_SUCCESS in self.dataset.features
        self.has_episode_success = EPISODE_SUCCESS in self.dataset.features
        self.episode_summaries = load_episode_summaries(self.root)
        self.samples: list[tuple[int, int, int, int]] = []
        self._cache: OrderedDict[int, dict] = OrderedDict()
        self._cache_limit = 256
        self._episode_success: dict[int, bool] = {}
        self._build_index()

    def _build_index(self) -> None:
        for ep_idx in range(self.dataset.num_episodes):
            episode = self.dataset.meta.episodes[ep_idx]
            ep_start = int(episode["dataset_from_index"])
            ep_end = int(episode["dataset_to_index"])
            self._episode_success[ep_idx] = self._infer_episode_success(ep_idx, ep_start, ep_end)
            for abs_idx in range(ep_start, ep_end):
                self.samples.append((ep_idx, ep_start, ep_end, abs_idx))

    def _infer_episode_success(self, ep_idx: int, ep_start: int, ep_end: int) -> bool:
        if ep_idx in self.episode_summaries:
            return bool(self.episode_summaries[ep_idx].get("success", False))
        if not self.has_reward and not self.has_success:
            return bool(self.assume_demo_success)
        for abs_idx in range(ep_start, ep_end):
            frame = self._get_frame(abs_idx)
            if self.has_reward and float(np.asarray(frame[REWARD]).reshape(-1)[0]) > 0.0:
                return True
            if self.has_success and bool(np.asarray(frame[NEXT_SUCCESS]).reshape(-1)[0]):
                return True
            if self.has_episode_success and bool(np.asarray(frame[EPISODE_SUCCESS]).reshape(-1)[0]):
                return True
        return False

    def _get_frame(self, abs_idx: int) -> dict:
        if abs_idx in self._cache:
            value = self._cache.pop(abs_idx)
            self._cache[abs_idx] = value
            return value
        value = self.dataset[abs_idx]
        self._cache[abs_idx] = value
        if len(self._cache) > self._cache_limit:
            self._cache.popitem(last=False)
        return value

    def __len__(self) -> int:
        return len(self.samples)

    @staticmethod
    def _to_tensor(value) -> torch.Tensor:
        if isinstance(value, torch.Tensor):
            return value
        return torch.as_tensor(np.asarray(value))

    @staticmethod
    def _clip(ep_start: int, ep_end: int, idx: int) -> int:
        return max(ep_start, min(ep_end - 1, idx))

    def __getitem__(self, index: int) -> dict[str, torch.Tensor]:
        ep_idx, ep_start, ep_end, abs_idx = self.samples[index]
        obs_deltas = range(1 - self.n_obs_steps, 1)
        action_deltas = range(1 - self.n_obs_steps, 1 - self.n_obs_steps + self.horizon)
        next_anchor = abs_idx + self.n_action_steps

        obs_frames = [self._get_frame(self._clip(ep_start, ep_end, abs_idx + delta)) for delta in obs_deltas]
        next_obs_frames = [
            self._get_frame(self._clip(ep_start, ep_end, next_anchor + delta)) for delta in obs_deltas
        ]

        batch: dict[str, torch.Tensor] = {}
        for key in self.obs_keys:
            batch[key] = torch.stack([self._to_tensor(frame[key]) for frame in obs_frames], dim=0)
            batch[f"next.{key}"] = torch.stack([self._to_tensor(frame[key]) for frame in next_obs_frames], dim=0)

        action_frames = []
        action_is_pad = []
        for delta in action_deltas:
            query_idx = abs_idx + delta
            clipped_idx = self._clip(ep_start, ep_end, query_idx)
            action_frames.append(self._to_tensor(self._get_frame(clipped_idx)["action"]).float())
            action_is_pad.append(query_idx < ep_start or query_idx >= ep_end)
        batch["action"] = torch.stack(action_frames, dim=0)
        batch["action_is_pad"] = torch.as_tensor(action_is_pad, dtype=torch.bool)

        discounted_reward = 0.0
        done = False
        success = False
        for step_idx in range(self.n_action_steps):
            query_idx = self._clip(ep_start, ep_end, abs_idx + step_idx)
            frame = self._get_frame(query_idx)
            reward = 0.0
            if self.has_reward:
                reward = float(np.asarray(frame[REWARD]).reshape(-1)[0])
            elif self.relabel_sparse_reward and self._episode_success[ep_idx] and query_idx == ep_end - 1:
                reward = 1.0
            discounted_reward += (self.gamma**step_idx) * reward

            frame_done = False
            if self.has_done:
                frame_done = bool(np.asarray(frame[DONE]).reshape(-1)[0])
            elif self.relabel_sparse_reward and query_idx == ep_end - 1:
                frame_done = True
            done = done or frame_done

            if self.has_success:
                success = success or bool(np.asarray(frame[NEXT_SUCCESS]).reshape(-1)[0])
            elif self.has_episode_success:
                success = success or bool(np.asarray(frame[EPISODE_SUCCESS]).reshape(-1)[0])
            else:
                success = success or reward > 0.0

            if frame_done:
                break

        batch["chunk_reward"] = torch.tensor([discounted_reward], dtype=torch.float32)
        batch["chunk_done"] = torch.tensor([float(done)], dtype=torch.float32)
        batch["chunk_success"] = torch.tensor([float(success)], dtype=torch.float32)
        batch["episode_success"] = torch.tensor([float(self._episode_success[ep_idx])], dtype=torch.float32)
        batch["episode_index"] = torch.tensor(ep_idx, dtype=torch.long)
        return batch
