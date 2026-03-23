from __future__ import annotations
from collections import deque
from dataclasses import dataclass
import torch
from torch import Tensor
from lerobot.configs.policies import PreTrainedConfig
from lerobot.policies.diffusion.configuration_diffusion import DiffusionConfig
from lerobot.policies.diffusion.modeling_diffusion import DiffusionPolicy
from lerobot.policies.utils import populate_queues
from lerobot.utils.constants import ACTION, OBS_ENV_STATE, OBS_IMAGES, OBS_STATE

@PreTrainedConfig.register_subclass("rl100_diffusion")
@dataclass
class RL100DiffusionConfig(DiffusionConfig):
    ppo_clip_eps: float = 0.2
    sigma_min: float = 0.01
    sigma_max: float = 0.1
    use_variance_clip: bool = True


class RL100DiffusionPolicy(DiffusionPolicy):
    config_class = RL100DiffusionConfig
    name = "rl100_diffusion"

    def __init__(self, config: RL100DiffusionConfig, **kwargs):
        super().__init__(config, **kwargs)
        self.config = config

    @property
    def action_dim(self) -> int:
        action_feature = self.config.action_feature
        if action_feature is None:
            raise ValueError("Action feature is required for RL-100 diffusion policy.")
        return action_feature.shape[0]

    @property
    def chunk_action_dim(self) -> int:
        return self.action_dim * self.config.n_action_steps

    def _stack_visual_inputs(self, batch: dict[str, Tensor]) -> dict[str, Tensor]:
        if not self.config.image_features:
            return batch
        if OBS_IMAGES in batch:
            return batch
        batch = dict(batch)
        batch[OBS_IMAGES] = torch.stack([batch[key] for key in self.config.image_features], dim=-4)
        return batch

    def encode_global_conditioning(self, batch: dict[str, Tensor]) -> Tensor:
        batch = self._stack_visual_inputs(batch)
        return self.diffusion._prepare_global_conditioning(batch)

    def get_chunk_from_horizon(self, horizon_actions: Tensor) -> Tensor:
        start = self.config.n_obs_steps - 1
        end = start + self.config.n_action_steps
        return horizon_actions[:, start:end]

    def flatten_chunk_action(self, horizon_actions: Tensor) -> Tensor:
        return self.get_chunk_from_horizon(horizon_actions).reshape(horizon_actions.shape[0], -1)

    @property
    def dtype(self) -> torch.dtype:
        return next(self.parameters()).dtype

    def get_variance_at_timestep(self, timestep: Tensor, prev_timestep: Tensor) -> Tensor:
        scheduler = self.diffusion.noise_scheduler
        alphas_cumprod = scheduler.alphas_cumprod.to(timestep.device)
        alpha_t = alphas_cumprod[timestep]
        alpha_t_prev = torch.where(
            prev_timestep >= 0,
            alphas_cumprod[prev_timestep.clamp(min=0)],
            torch.ones_like(alpha_t),
        )
        variance = (1.0 - alpha_t_prev) / (1.0 - alpha_t) * (1.0 - alpha_t / alpha_t_prev)
        final_step_mask = prev_timestep < 0
        if self.config.use_variance_clip:
            variance = torch.clamp(variance, self.config.sigma_min**2, self.config.sigma_max**2)
        variance = torch.where(final_step_mask, torch.zeros_like(variance), variance)
        return variance

    def compute_gaussian_log_prob(self, x: Tensor, mean: Tensor, variance: Tensor) -> Tensor:
        variance = variance.clamp_min(1e-8).view(-1)
        dims = x.shape[1] * x.shape[2]
        return -0.5 * (
            dims * torch.log(2 * torch.pi * variance) + torch.sum((x - mean).square(), dim=(1, 2)) / variance
        )

    def _compute_step_statistics(
        self,
        x_t: Tensor,
        timestep: Tensor,
        prev_timestep: Tensor,
        global_cond: Tensor,
    ) -> tuple[Tensor, Tensor]:
        noise_pred = self.diffusion.unet(x_t, timestep, global_cond=global_cond)
        alphas_cumprod = self.diffusion.noise_scheduler.alphas_cumprod.to(x_t.device)
        alpha_t = alphas_cumprod[timestep].view(-1, 1, 1)
        alpha_t_prev = torch.where(
            (prev_timestep >= 0).view(-1, 1, 1),
            alphas_cumprod[prev_timestep.clamp(min=0)].view(-1, 1, 1),
            torch.ones_like(alpha_t),
        )
        pred_x0 = (x_t - torch.sqrt(1.0 - alpha_t) * noise_pred) / torch.sqrt(alpha_t)
        variance = self.get_variance_at_timestep(timestep, prev_timestep)
        noise_coeff = torch.sqrt(torch.clamp(1.0 - alpha_t_prev - variance.view(-1, 1, 1), min=0.0))
        mean = torch.sqrt(alpha_t_prev) * pred_x0 + noise_coeff * noise_pred
        return mean, variance

    @torch.no_grad()
    def sample_trajectory(
        self,
        global_cond: Tensor,
        noise: Tensor | None = None,
    ) -> tuple[Tensor, list[Tensor], list[Tensor]]:
        batch_size = global_cond.shape[0]
        device = global_cond.device
        dtype = global_cond.dtype
        sample = (
            noise
            if noise is not None
            else torch.randn(
                batch_size,
                self.config.horizon,
                self.action_dim,
                device=device,
                dtype=dtype,
            )
        )
        scheduler = self.diffusion.noise_scheduler
        scheduler.set_timesteps(self.diffusion.num_inference_steps)
        trajectory = [sample.clone()]
        log_probs: list[Tensor] = []
        for i, timestep in enumerate(scheduler.timesteps):
            t = torch.full((batch_size,), int(timestep), device=device, dtype=torch.long)
            if i + 1 < len(scheduler.timesteps):
                t_prev = torch.full((batch_size,), int(scheduler.timesteps[i + 1]), device=device, dtype=torch.long)
            else:
                t_prev = torch.full((batch_size,), -1, device=device, dtype=torch.long)
            mean, variance = self._compute_step_statistics(sample, t, t_prev, global_cond)
            if torch.all(t_prev < 0):
                sample = mean
                log_prob = torch.zeros(batch_size, device=device, dtype=dtype)
            else:
                sample = mean + torch.sqrt(variance).view(-1, 1, 1) * torch.randn_like(sample)
                log_prob = self.compute_gaussian_log_prob(sample, mean, variance)
            trajectory.append(sample.clone())
            log_probs.append(log_prob)
        return sample, trajectory, log_probs

    @torch.no_grad()
    def predict_horizon_actions_from_global_cond(
        self,
        global_cond: Tensor,
        noise: Tensor | None = None,
    ) -> Tensor:
        horizon_actions, _, _ = self.sample_trajectory(global_cond, noise=noise)
        return horizon_actions

    @torch.no_grad()
    def predict_action_chunk_from_global_cond(
        self,
        global_cond: Tensor,
        noise: Tensor | None = None,
    ) -> Tensor:
        horizon_actions = self.predict_horizon_actions_from_global_cond(global_cond, noise=noise)
        return self.get_chunk_from_horizon(horizon_actions)

    def compute_ppo_loss(
        self,
        old_log_probs: list[Tensor],
        advantages: Tensor,
        trajectory: list[Tensor],
        global_cond: Tensor,
    ) -> tuple[Tensor, dict[str, float]]:
        scheduler = self.diffusion.noise_scheduler
        scheduler.set_timesteps(self.diffusion.num_inference_steps)
        batch_size = global_cond.shape[0]
        device = global_cond.device
        advantages = advantages.view(batch_size)

        ppo_losses: list[Tensor] = []
        ratios: list[float] = []
        approx_kls: list[float] = []
        clip_fracs: list[float] = []
        ratio_devs: list[float] = []
        min_ratios: list[float] = []
        max_ratios: list[float] = []

        for i, timestep in enumerate(scheduler.timesteps):
            if i + 1 >= len(trajectory):
                break
            if i + 1 < len(scheduler.timesteps):
                prev_timestep = int(scheduler.timesteps[i + 1])
            else:
                prev_timestep = -1
            if prev_timestep < 0:
                continue
            t = torch.full((batch_size,), int(timestep), device=device, dtype=torch.long)
            t_prev = torch.full((batch_size,), prev_timestep, device=device, dtype=torch.long)
            mean, variance = self._compute_step_statistics(trajectory[i], t, t_prev, global_cond)
            log_prob = self.compute_gaussian_log_prob(trajectory[i + 1], mean, variance)
            log_ratio = log_prob - old_log_probs[i].view(batch_size)
            ratio = torch.exp(log_ratio)
            clipped_ratio = torch.clamp(
                ratio,
                1.0 - self.config.ppo_clip_eps,
                1.0 + self.config.ppo_clip_eps,
            )
            surrogate = torch.minimum(ratio * advantages, clipped_ratio * advantages)
            ppo_losses.append(-surrogate.mean())

            approx_kl = ((ratio - 1.0) - log_ratio).mean()
            clip_frac = ((ratio - 1.0).abs() > self.config.ppo_clip_eps).float().mean()
            ratios.append(float(ratio.mean().item()))
            approx_kls.append(float(approx_kl.item()))
            clip_fracs.append(float(clip_frac.item()))
            ratio_devs.append(float((ratio - 1.0).abs().mean().item()))
            min_ratios.append(float(ratio.min().item()))
            max_ratios.append(float(ratio.max().item()))

        if not ppo_losses:
            zero = global_cond.new_zeros(())
            return zero, {
                "ppo_loss": 0.0,
                "approx_kl": 0.0,
                "clip_frac": 0.0,
                "mean_ratio": 1.0,
                "mean_abs_ratio_dev": 0.0,
                "min_ratio": 1.0,
                "max_ratio": 1.0,
            }
        total_loss = torch.stack(ppo_losses).mean()
        return total_loss, {
            "ppo_loss": float(total_loss.item()),
            "approx_kl": float(sum(approx_kls) / len(approx_kls)),
            "clip_frac": float(sum(clip_fracs) / len(clip_fracs)),
            "mean_ratio": float(sum(ratios) / len(ratios)),
            "mean_abs_ratio_dev": float(sum(ratio_devs) / len(ratio_devs)),
            "min_ratio": float(sum(min_ratios) / len(min_ratios)),
            "max_ratio": float(sum(max_ratios) / len(max_ratios)),
        }

    @torch.no_grad()
    def predict_action_chunk_with_metadata(
        self,
        batch: dict[str, Tensor],
        noise: Tensor | None = None,
    ) -> tuple[Tensor, dict[str, Tensor | list[Tensor]]]:
        global_cond = self.encode_global_conditioning(batch)
        horizon_actions, trajectory, log_probs = self.sample_trajectory(global_cond, noise=noise)
        return self.get_chunk_from_horizon(horizon_actions), {
            "trajectory": trajectory,
            "log_probs_old": log_probs,
            "global_cond": global_cond,
            "normalized_horizon_actions": horizon_actions,
        }

    @torch.no_grad()
    def select_action_with_info(
        self,
        batch: dict[str, Tensor],
        noise: Tensor | None = None,
    ) -> tuple[Tensor, dict[str, Tensor | list[Tensor]] | None]:
        if ACTION in batch:
            batch = dict(batch)
            batch.pop(ACTION)
        batch = self._stack_visual_inputs(batch)
        self._queues = populate_queues(self._queues, batch)

        info: dict[str, Tensor | list[Tensor]] | None = None
        if len(self._queues[ACTION]) == 0:
            chunk_batch = {key: torch.stack(list(self._queues[key]), dim=1) for key in self._queues if key != ACTION}
            actions, info = self.predict_action_chunk_with_metadata(chunk_batch, noise=noise)
            self._queues[ACTION].extend(actions.transpose(0, 1))

        action = self._queues[ACTION].popleft()
        return action, info

    def reset(self):
        self._queues = {
            OBS_STATE: deque(maxlen=self.config.n_obs_steps),
            ACTION: deque(maxlen=self.config.n_action_steps),
        }
        if self.config.image_features:
            self._queues[OBS_IMAGES] = deque(maxlen=self.config.n_obs_steps)
        if self.config.env_state_feature:
            self._queues[OBS_ENV_STATE] = deque(maxlen=self.config.n_obs_steps)
