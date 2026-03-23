from __future__ import annotations
from dataclasses import replace
import torch
import torch.nn.functional as F
from torch import Tensor, nn
from lerobot.policies.diffusion.modeling_diffusion import DiffusionConditionalUnet1d
from rl_100.training.rl100_policy import RL100DiffusionConfig, RL100DiffusionPolicy

class ConsistencyModel(nn.Module):
    def __init__(self, config: RL100DiffusionConfig, global_cond_dim: int):
        super().__init__()
        student_config = replace(config)
        self.model = DiffusionConditionalUnet1d(student_config, global_cond_dim=global_cond_dim)
        self.action_dim = config.action_feature.shape[0]
        self.horizon = config.horizon
        self.num_train_timesteps = config.num_train_timesteps

    def forward(
        self,
        noisy_action: Tensor,
        global_cond: Tensor,
        timestep: Tensor | None = None,
    ) -> Tensor:
        if timestep is None:
            timestep = torch.full(
                (noisy_action.shape[0],),
                self.num_train_timesteps - 1,
                device=noisy_action.device,
                dtype=torch.long,
            )
        return self.model(noisy_action, timestep, global_cond=global_cond)

    @torch.no_grad()
    def predict_horizon_actions(
        self,
        global_cond: Tensor,
        noise: Tensor | None = None,
    ) -> Tensor:
        batch_size = global_cond.shape[0]
        device = global_cond.device
        dtype = global_cond.dtype
        noisy_action = noise
        if noisy_action is None:
            noisy_action = torch.randn(
                batch_size,
                self.horizon,
                self.action_dim,
                device=device,
                dtype=dtype,
            )
        return self.forward(noisy_action=noisy_action, global_cond=global_cond)


class ConsistencyDistillation:
    def __init__(self, teacher_policy: RL100DiffusionPolicy, student_model: ConsistencyModel):
        self.teacher_policy = teacher_policy
        self.student_model = student_model

    def compute_distillation_loss(
        self,
        global_cond: Tensor,
        noise: Tensor | None = None,
    ) -> tuple[Tensor, dict[str, float]]:
        batch_size = global_cond.shape[0]
        device = global_cond.device
        dtype = global_cond.dtype

        initial_noise = noise
        if initial_noise is None:
            initial_noise = torch.randn(
                batch_size,
                self.teacher_policy.config.horizon,
                self.teacher_policy.action_dim,
                device=device,
                dtype=dtype,
            )

        teacher_was_training = self.teacher_policy.training
        self.teacher_policy.eval()
        try:
            with torch.no_grad():
                teacher_horizon = self.teacher_policy.predict_horizon_actions_from_global_cond(
                    global_cond=global_cond,
                    noise=initial_noise,
                )
        finally:
            if teacher_was_training:
                self.teacher_policy.train()

        student_horizon = self.student_model.predict_horizon_actions(
            global_cond=global_cond,
            noise=initial_noise,
        )
        loss = F.mse_loss(student_horizon, teacher_horizon)
        return loss, {"cd_loss": float(loss.item())}
