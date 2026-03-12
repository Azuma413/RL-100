from typing import Dict
import torch
import numpy as np
import copy
import zarr
from termcolor import cprint
from diffusion_policy_3d.common.pytorch_util import dict_apply
from diffusion_policy_3d.common.replay_buffer import ReplayBuffer
from diffusion_policy_3d.common.sampler import (
    SequenceSampler, get_val_mask, downsample_mask)
from diffusion_policy_3d.model.common.normalizer import LinearNormalizer, SingleFieldLinearNormalizer
from diffusion_policy_3d.dataset.base_dataset import BaseDataset

class MetaworldDataset(BaseDataset):
    def __init__(self,
            zarr_path,
            horizon=1,
            pad_before=0,
            pad_after=0,
            seed=42,
            val_ratio=0.0,
            max_train_episodes=None,
            n_action_steps=8,
            gamma=0.99,
            ):
        super().__init__()

        # Check which keys are available (support both old and new zarr formats)
        _zarr_store = zarr.open(zarr_path, 'r')
        _available_keys = list(_zarr_store['data'].keys())
        self.has_rl_data = 'reward' in _available_keys and 'done' in _available_keys
        keys_to_load = ['state', 'action', 'point_cloud']
        if self.has_rl_data:
            keys_to_load.extend(['reward', 'done'])

        self.replay_buffer = ReplayBuffer.copy_from_path(
            zarr_path, keys=keys_to_load)
        val_mask = get_val_mask(
            n_episodes=self.replay_buffer.n_episodes, 
            val_ratio=val_ratio,
            seed=seed)
        train_mask = ~val_mask
        train_mask = downsample_mask(
            mask=train_mask, 
            max_n=max_train_episodes, 
            seed=seed)

        self.sampler = SequenceSampler(
            replay_buffer=self.replay_buffer, 
            sequence_length=horizon,
            pad_before=pad_before, 
            pad_after=pad_after,
            episode_mask=train_mask)
        self.train_mask = train_mask
        self.horizon = horizon
        self.pad_before = pad_before
        self.pad_after = pad_after
        self.n_action_steps = n_action_steps
        self.gamma = gamma
        self._shape_mismatch_warned = False

    @staticmethod
    def _align_point_cloud_shape(point_cloud: np.ndarray, target_shape: tuple) -> np.ndarray:
        """
        Align point cloud array to replay buffer shape [T, N_target, C_target].

        - Channel mismatch: crop or zero-pad last dim.
        - Point-count mismatch: deterministic resample (linspace index) or repeat.
        """
        if point_cloud.ndim != 3:
            raise ValueError(f"point_cloud must be rank-3 [T, N, C], got shape={point_cloud.shape}")

        target_n, target_c = target_shape
        pc = point_cloud

        # Align channels first.
        cur_c = pc.shape[-1]
        if cur_c > target_c:
            pc = pc[..., :target_c]
        elif cur_c < target_c:
            pad_width = ((0, 0), (0, 0), (0, target_c - cur_c))
            pc = np.pad(pc, pad_width=pad_width, mode='constant')

        # Align number of points.
        cur_n = pc.shape[1]
        if cur_n > target_n:
            # Deterministic uniform index selection to keep behavior reproducible.
            indices = np.linspace(0, cur_n - 1, target_n, dtype=np.int64)
            pc = pc[:, indices, :]
        elif cur_n < target_n:
            repeat_factor = (target_n + cur_n - 1) // cur_n
            pc = np.tile(pc, (1, repeat_factor, 1))[:, :target_n, :]

        return pc.astype(np.float32, copy=False)

    def get_validation_dataset(self):
        val_set = copy.copy(self)
        val_set.sampler = SequenceSampler(
            replay_buffer=self.replay_buffer, 
            sequence_length=self.horizon,
            pad_before=self.pad_before, 
            pad_after=self.pad_after,
            episode_mask=~self.train_mask
            )
        val_set.train_mask = ~self.train_mask
        return val_set

    def get_normalizer(self, mode='limits', **kwargs):
        data = {
            'action': self.replay_buffer['action'],
            'agent_pos': self.replay_buffer['state'][...,:],
            'point_cloud': self.replay_buffer['point_cloud'],
        }
        normalizer = LinearNormalizer()
        normalizer.fit(data=data, last_n_dims=1, mode=mode, **kwargs)
        return normalizer

    def __len__(self) -> int:
        return len(self.sampler)

    def _sample_to_data(self, sample):
        agent_pos = sample['state'][:,].astype(np.float32)
        point_cloud = sample['point_cloud'][:,].astype(np.float32)

        data = {
            'obs': {
                'point_cloud': point_cloud, 
                'agent_pos': agent_pos, 
            },
            'action': sample['action'].astype(np.float32)
        }
        return data
    
    def __getitem__(self, idx: int) -> Dict[str, torch.Tensor]:
        sample = self.sampler.sample_sequence(idx)
        data = self._sample_to_data(sample)

        if self.has_rl_data:
            nc = self.n_action_steps
            # Paper: R_chunk = Σ_{j=0}^{n_c-1} γ^j · R_{t+j}
            # Accumulate discounted reward over the action-chunk window.
            raw_rewards = sample['reward'][:nc].astype(np.float32)  # (nc,)
            discount = np.array([self.gamma ** j for j in range(nc)], dtype=np.float32)
            chunk_reward = float(np.dot(discount, raw_rewards))
            data['reward'] = np.array(chunk_reward, dtype=np.float32)

            # done = True if any step within the chunk is terminal
            data['done'] = np.array(sample['done'][:nc].any(), dtype=np.float32)

            # next_obs: the obs window starting n_action_steps ahead (chunk-level MDP)
            buffer_start_idx, _, _, _ = self.sampler.indices[idx]
            total_len = len(self.replay_buffer['state'])
            next_idx = min(buffer_start_idx + nc, total_len - 1)
            next_end_idx = min(next_idx + self.horizon, total_len)

            next_state = self.replay_buffer['state'][next_idx:next_end_idx].astype(np.float32)
            next_pc = self.replay_buffer['point_cloud'][next_idx:next_end_idx].astype(np.float32)

            # Pad if we're near the end of the buffer
            actual_len = len(next_state)
            if actual_len < self.horizon:
                pad_len = self.horizon - actual_len
                next_state = np.concatenate(
                    [next_state, np.tile(next_state[-1:], (pad_len,) + (1,) * (next_state.ndim - 1))], axis=0)
                next_pc = np.concatenate(
                    [next_pc, np.tile(next_pc[-1:], (pad_len,) + (1,) * (next_pc.ndim - 1))], axis=0)

            data['next_obs'] = {
                'agent_pos': next_state,
                'point_cloud': next_pc,
            }

        torch_data = dict_apply(data, torch.from_numpy)
        return torch_data

    def merge_episodes(self, episodes: list) -> int:
        """
        Merge newly collected episodes into the replay buffer in-place.

        Each episode is a dict with numpy arrays of shape [T, ...]:
            state, action, point_cloud, reward, done

        The SequenceSampler is rebuilt after merging so that the new data
        is immediately available for training.

        Args:
            episodes: list of episode dicts from MetaworldRunner.run_and_collect()

        Returns:
            n_new_steps: total number of new timesteps added
        """
        if not episodes:
            return 0

        n_new_steps = 0
        target_state_shape = tuple(self.replay_buffer['state'].shape[1:])
        target_action_shape = tuple(self.replay_buffer['action'].shape[1:])
        target_pc_shape = tuple(self.replay_buffer['point_cloud'].shape[1:])

        for ep in episodes:
            state = np.asarray(ep['state'], dtype=np.float32)
            action = np.asarray(ep['action'], dtype=np.float32)
            point_cloud = np.asarray(ep['point_cloud'], dtype=np.float32)
            reward = np.asarray(
                ep.get('reward', np.zeros(len(state), dtype=np.float32)),
                dtype=np.float32
            ).reshape(-1)
            done = np.asarray(
                ep.get('done', np.zeros(len(state), dtype=np.float32)),
                dtype=np.float32
            ).reshape(-1)

            if state.shape[1:] != target_state_shape:
                raise ValueError(
                    f"State shape mismatch: episode {state.shape[1:]} vs replay_buffer {target_state_shape}"
                )
            if action.shape[1:] != target_action_shape:
                raise ValueError(
                    f"Action shape mismatch: episode {action.shape[1:]} vs replay_buffer {target_action_shape}"
                )
            if point_cloud.shape[1:] != target_pc_shape:
                original_shape = point_cloud.shape
                point_cloud = self._align_point_cloud_shape(point_cloud, target_pc_shape)
                if not self._shape_mismatch_warned:
                    cprint(
                        f"[MetaworldDataset] point_cloud shape mismatch detected. "
                        f"Auto-aligned from {original_shape[1:]} to {point_cloud.shape[1:]} "
                        f"to match replay buffer.",
                        "yellow"
                    )
                    self._shape_mismatch_warned = True

            T = len(state)
            if not (len(action) == len(point_cloud) == len(reward) == len(done) == T):
                raise ValueError(
                    "Episode length mismatch among fields: "
                    f"state={len(state)}, action={len(action)}, point_cloud={len(point_cloud)}, "
                    f"reward={len(reward)}, done={len(done)}"
                )

            # Ensure reward/done exist (add zeros if this is demo data without RL labels)
            ep_data = {
                'state': state,
                'action': action,
                'point_cloud': point_cloud,
                'reward': reward,
                'done': done,
            }

            self.replay_buffer.add_episode(ep_data)
            n_new_steps += len(ep['state'])

        # Flag that RL data is now present
        self.has_rl_data = True

        # Rebuild sampler to include all episodes (no episode cap after merging)
        n_total = self.replay_buffer.n_episodes
        episode_mask = np.ones(n_total, dtype=bool)
        self.sampler = SequenceSampler(
            replay_buffer=self.replay_buffer,
            sequence_length=self.horizon,
            pad_before=self.pad_before,
            pad_after=self.pad_after,
            episode_mask=episode_mask,
        )
        self.train_mask = episode_mask

        return n_new_steps
