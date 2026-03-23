from __future__ import annotations

from dataclasses import dataclass

import torch
import torch.nn.functional as F
from torch import Tensor, nn


class MLP(nn.Module):
    def __init__(self, input_dim: int, hidden_dims: tuple[int, ...], output_dim: int = 1):
        super().__init__()
        layers: list[nn.Module] = []
        prev_dim = input_dim
        for hidden_dim in hidden_dims:
            layers.extend(
                [
                    nn.Linear(prev_dim, hidden_dim),
                    nn.LayerNorm(hidden_dim),
                    nn.Mish(),
                ]
            )
            prev_dim = hidden_dim
        layers.append(nn.Linear(prev_dim, output_dim))
        self.network = nn.Sequential(*layers)

    def forward(self, x: Tensor) -> Tensor:
        return self.network(x)


class ValueNetwork(nn.Module):
    def __init__(self, obs_dim: int, hidden_dims: tuple[int, ...]):
        super().__init__()
        self.network = MLP(obs_dim, hidden_dims, output_dim=1)

    def forward(self, obs: Tensor) -> Tensor:
        return self.network(obs)


class TwinQNetwork(nn.Module):
    def __init__(self, obs_dim: int, action_dim: int, hidden_dims: tuple[int, ...]):
        super().__init__()
        input_dim = obs_dim + action_dim
        self.q1 = MLP(input_dim, hidden_dims, output_dim=1)
        self.q2 = MLP(input_dim, hidden_dims, output_dim=1)

    def forward(self, obs: Tensor, action: Tensor, return_both: bool = False) -> Tensor | tuple[Tensor, Tensor]:
        x = torch.cat([obs, action], dim=-1)
        q1 = self.q1(x)
        q2 = self.q2(x)
        if return_both:
            return q1, q2
        return torch.minimum(q1, q2)


@dataclass
class CriticLosses:
    q_loss: float
    v_loss: float
    q_mean: float
    v_mean: float
    target_mean: float


class IQLCritics(nn.Module):
    def __init__(
        self,
        obs_dim: int,
        action_dim: int,
        hidden_dims: tuple[int, ...] = (256, 256, 256),
        gamma: float = 0.99,
        expectile: float = 0.7,
    ):
        super().__init__()
        self.gamma = gamma
        self.expectile = expectile
        self.value = ValueNetwork(obs_dim, hidden_dims)
        self.target_value = ValueNetwork(obs_dim, hidden_dims)
        self.target_value.load_state_dict(self.value.state_dict())
        self.q = TwinQNetwork(obs_dim, action_dim, hidden_dims)
        for param in self.target_value.parameters():
            param.requires_grad_(False)

    @staticmethod
    def expectile_loss(pred: Tensor, target: Tensor, expectile: float) -> Tensor:
        diff = target - pred
        weight = torch.where(diff > 0, expectile, 1.0 - expectile)
        return (weight * diff.square()).mean()

    def compute_v_loss(self, obs: Tensor, action: Tensor) -> tuple[Tensor, dict[str, float]]:
        with torch.no_grad():
            q_target = self.q(obs, action)
        v_pred = self.value(obs)
        loss = self.expectile_loss(v_pred, q_target, self.expectile)
        return loss, {
            "v_loss": float(loss.item()),
            "v_mean": float(v_pred.mean().item()),
            "q_target_mean": float(q_target.mean().item()),
        }

    def compute_q_loss(
        self,
        obs: Tensor,
        action: Tensor,
        reward: Tensor,
        next_obs: Tensor,
        done: Tensor,
    ) -> tuple[Tensor, dict[str, float]]:
        with torch.no_grad():
            next_v = self.target_value(next_obs)
            q_target = reward + self.gamma * (1.0 - done) * next_v
        q1, q2 = self.q(obs, action, return_both=True)
        q_loss = F.mse_loss(q1, q_target) + F.mse_loss(q2, q_target)
        return q_loss, {
            "q_loss": float(q_loss.item()),
            "q1_mean": float(q1.mean().item()),
            "q2_mean": float(q2.mean().item()),
            "q_target_mean": float(q_target.mean().item()),
            "reward_mean": float(reward.mean().item()),
        }

    def compute_advantage(self, obs: Tensor, action: Tensor) -> Tensor:
        return self.q(obs, action) - self.value(obs)

    def soft_update_target(self, tau: float) -> None:
        for param, target_param in zip(self.value.parameters(), self.target_value.parameters(), strict=True):
            target_param.data.lerp_(param.data, tau)
