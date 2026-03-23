from __future__ import annotations
from typing import Any
import numpy as np
import torch
import torch.nn.functional as F
from torch import Tensor, nn

class EnsembleLinear(nn.Module):
    def __init__(self, input_dim: int, output_dim: int, num_ensemble: int, weight_decay: float = 0.0):
        super().__init__()
        self.weight_decay = weight_decay
        self.weight = nn.Parameter(torch.zeros(num_ensemble, input_dim, output_dim))
        self.bias = nn.Parameter(torch.zeros(num_ensemble, 1, output_dim))
        nn.init.trunc_normal_(self.weight, std=1.0 / (2 * input_dim**0.5))
        self.saved_weight = nn.Parameter(self.weight.detach().clone())
        self.saved_bias = nn.Parameter(self.bias.detach().clone())

    def forward(self, x: Tensor) -> Tensor:
        if x.dim() == 2:
            x = torch.einsum("bi,eio->ebo", x, self.weight)
        else:
            x = torch.einsum("ebi,eio->ebo", x, self.weight)
        return x + self.bias

    def update_save(self, indexes: list[int]) -> None:
        self.saved_weight.data[indexes] = self.weight.data[indexes]
        self.saved_bias.data[indexes] = self.bias.data[indexes]

    def load_save(self) -> None:
        self.weight.data.copy_(self.saved_weight.data)
        self.bias.data.copy_(self.saved_bias.data)

    def get_decay_loss(self) -> Tensor:
        return self.weight_decay * 0.5 * (self.weight**2).sum()


class Swish(nn.Module):
    def forward(self, x: Tensor) -> Tensor:
        return x * torch.sigmoid(x)


def soft_clamp(x: Tensor, _min: Tensor | None = None, _max: Tensor | None = None) -> Tensor:
    if _max is not None:
        x = _max - F.softplus(_max - x)
    if _min is not None:
        x = _min + F.softplus(x - _min)
    return x


class StandardScaler:
    def __init__(self) -> None:
        self.mu: np.ndarray | None = None
        self.std: np.ndarray | None = None

    def fit(self, data: np.ndarray) -> None:
        self.mu = np.mean(data, axis=0, keepdims=True)
        self.std = np.std(data, axis=0, keepdims=True)
        self.std[self.std < 1e-12] = 1.0

    def transform(self, data: np.ndarray) -> np.ndarray:
        return (data - self.mu) / self.std

    def transform_tensor(self, x: Tensor) -> Tensor:
        if self.mu is None or self.std is None:
            raise RuntimeError("StandardScaler must be fit before use.")
        mu = torch.as_tensor(self.mu, dtype=x.dtype, device=x.device)
        std = torch.as_tensor(self.std, dtype=x.dtype, device=x.device)
        return (x - mu) / std


class EnsembleDynamicsModel(nn.Module):
    def __init__(
        self,
        obs_dim: int,
        action_dim: int,
        hidden_dims: tuple[int, ...] = (200, 200, 200, 200),
        num_ensemble: int = 7,
        num_elites: int = 5,
        weight_decays: tuple[float, ...] | None = None,
    ) -> None:
        super().__init__()
        if weight_decays is None:
            weight_decays = (2.5e-5,) * len(hidden_dims) + (1e-4,)
        dims = [obs_dim + action_dim] + list(hidden_dims)
        self.backbones = nn.ModuleList(
            [
                EnsembleLinear(in_dim, out_dim, num_ensemble, wd)
                for in_dim, out_dim, wd in zip(dims[:-1], dims[1:], weight_decays[:-1], strict=True)
            ]
        )
        self.output_layer = EnsembleLinear(
            dims[-1],
            2 * (obs_dim + 1),
            num_ensemble,
            weight_decays[-1],
        )
        self.activation = Swish()
        self.max_logvar = nn.Parameter(torch.ones(obs_dim + 1) * 0.5, requires_grad=True)
        self.min_logvar = nn.Parameter(torch.ones(obs_dim + 1) * -10.0, requires_grad=True)
        self.elites = nn.Parameter(torch.arange(num_elites), requires_grad=False)
        self.num_ensemble = num_ensemble
        self.num_elites = num_elites

    def forward(self, x: Tensor) -> tuple[Tensor, Tensor]:
        for layer in self.backbones:
            x = self.activation(layer(x))
        mean, logvar = torch.chunk(self.output_layer(x), 2, dim=-1)
        logvar = soft_clamp(logvar, self.min_logvar, self.max_logvar)
        return mean, logvar

    def update_save(self, indexes: list[int]) -> None:
        for layer in self.backbones:
            layer.update_save(indexes)
        self.output_layer.update_save(indexes)

    def load_save(self) -> None:
        for layer in self.backbones:
            layer.load_save()
        self.output_layer.load_save()

    def set_elites(self, indexes: list[int]) -> None:
        self.elites = nn.Parameter(torch.tensor(indexes), requires_grad=False)

    def random_elite_idxs(self, batch_size: int) -> np.ndarray:
        elite_array = self.elites.detach().cpu().numpy()
        return np.random.choice(elite_array, size=batch_size)

    def get_decay_loss(self) -> Tensor:
        loss = sum(layer.get_decay_loss() for layer in self.backbones)
        return loss + self.output_layer.get_decay_loss()


class TransitionModel:
    def __init__(
        self,
        obs_feature_dim: int,
        action_dim: int,
        hidden_dims: tuple[int, ...] = (200, 200, 200, 200),
        num_ensemble: int = 7,
        num_elites: int = 5,
        lr: float = 1e-3,
        device: str = "cuda",
    ) -> None:
        self.obs_feature_dim = obs_feature_dim
        self.action_dim = action_dim
        self.device = torch.device(device)
        self.model = EnsembleDynamicsModel(
            obs_dim=obs_feature_dim,
            action_dim=action_dim,
            hidden_dims=hidden_dims,
            num_ensemble=num_ensemble,
            num_elites=num_elites,
        ).to(self.device)
        self.optimizer = torch.optim.Adam(self.model.parameters(), lr=lr)
        self.scaler = StandardScaler()
        self.is_trained = False

    def train_on_feature_arrays(
        self,
        inputs: np.ndarray,
        targets: np.ndarray,
        batch_size: int = 256,
        max_epochs: int = 200,
        max_epochs_since_update: int = 5,
        holdout_ratio: float = 0.2,
        logvar_loss_coef: float = 0.01,
    ) -> dict[str, Any]:
        if inputs.shape[0] == 0:
            raise ValueError("Transition model received an empty feature dataset.")
        num_samples = inputs.shape[0]
        holdout_size = min(int(num_samples * holdout_ratio), 1000)
        train_size = max(1, num_samples - holdout_size)
        if holdout_size <= 0:
            holdout_size = min(1, num_samples)
            train_size = max(1, num_samples - holdout_size)
        perm = np.random.permutation(num_samples)
        train_in = inputs[perm[:train_size]]
        train_tgt = targets[perm[:train_size]]
        hold_in = inputs[perm[train_size:]]
        hold_tgt = targets[perm[train_size:]]
        if hold_in.shape[0] == 0:
            hold_in = train_in[:1]
            hold_tgt = train_tgt[:1]

        self.scaler.fit(train_in)
        train_in_scaled = self.scaler.transform(train_in)
        hold_in_scaled = self.scaler.transform(hold_in)

        data_idxes = np.stack([np.random.permutation(train_size) for _ in range(self.model.num_ensemble)], axis=0)
        holdout_losses = [1e10] * self.model.num_ensemble
        train_loss_history: list[float] = []
        val_loss_history: list[float] = []
        epochs_since_update = 0

        for epoch in range(max_epochs):
            train_loss = self._learn_epoch(
                train_in_scaled[data_idxes],
                train_tgt[data_idxes],
                batch_size=batch_size,
                logvar_loss_coef=logvar_loss_coef,
            )
            new_holdout_losses = self._validate(hold_in_scaled, hold_tgt)
            val_loss = float(np.sort(new_holdout_losses)[: self.model.num_elites].mean())
            train_loss_history.append(train_loss)
            val_loss_history.append(val_loss)
            data_idxes = np.stack([np.random.permutation(train_size) for _ in range(self.model.num_ensemble)], axis=0)

            improved = [
                idx
                for idx, (new_loss, old_loss) in enumerate(zip(new_holdout_losses, holdout_losses, strict=True))
                if old_loss > 0 and (old_loss - new_loss) / old_loss > 0.01
            ]
            if improved:
                self.model.update_save(improved)
                holdout_losses = [
                    new_holdout_losses[idx] if idx in improved else holdout_losses[idx]
                    for idx in range(self.model.num_ensemble)
                ]
                epochs_since_update = 0
            else:
                epochs_since_update += 1

            if epochs_since_update >= max_epochs_since_update:
                break

        elites = sorted(range(len(holdout_losses)), key=lambda idx: holdout_losses[idx])[: self.model.num_elites]
        self.model.set_elites(elites)
        self.model.load_save()
        self.model.eval()
        self.is_trained = True
        return {
            "final_val_loss": float(np.sort(holdout_losses)[: self.model.num_elites].mean()),
            "train_loss_history": train_loss_history,
            "val_loss_history": val_loss_history,
            "elites": elites,
            "holdout_losses": [float(loss) for loss in holdout_losses],
        }

    def _learn_epoch(
        self,
        inputs: np.ndarray,
        targets: np.ndarray,
        batch_size: int,
        logvar_loss_coef: float,
    ) -> float:
        self.model.train()
        train_size = inputs.shape[1]
        losses: list[float] = []
        for start in range(0, train_size, batch_size):
            x = torch.as_tensor(inputs[:, start : start + batch_size], dtype=torch.float32, device=self.device)
            y = torch.as_tensor(targets[:, start : start + batch_size], dtype=torch.float32, device=self.device)
            mean, logvar = self.model(x)
            inv_var = torch.exp(-logvar)
            mse_loss = ((mean - y) ** 2 * inv_var).mean(dim=(1, 2)).sum()
            var_loss = logvar.mean(dim=(1, 2)).sum()
            loss = (
                mse_loss
                + var_loss
                + self.model.get_decay_loss()
                + logvar_loss_coef * self.model.max_logvar.sum()
                - logvar_loss_coef * self.model.min_logvar.sum()
            )
            self.optimizer.zero_grad(set_to_none=True)
            loss.backward()
            self.optimizer.step()
            losses.append(float(loss.item()))
        return float(np.mean(losses))

    @torch.no_grad()
    def _validate(self, inputs: np.ndarray, targets: np.ndarray) -> list[float]:
        self.model.eval()
        x = torch.as_tensor(inputs, dtype=torch.float32, device=self.device)
        y = torch.as_tensor(targets, dtype=torch.float32, device=self.device)
        mean, _ = self.model(x)
        losses = ((mean - y) ** 2).mean(dim=(1, 2))
        return losses.detach().cpu().numpy().tolist()

    @torch.no_grad()
    def predict_next_features(
        self,
        obs_features: Tensor,
        normalized_action: Tensor,
        deterministic: bool = False,
    ) -> tuple[Tensor, Tensor]:
        if self.scaler.mu is None or self.scaler.std is None:
            raise RuntimeError("Transition model has not been fit yet.")
        x = torch.cat([obs_features, normalized_action], dim=-1)
        x = self.scaler.transform_tensor(x)
        mean, logvar = self.model(x)
        elite_indices = self.model.elites.long()
        elite_mean = mean[elite_indices]
        if deterministic:
            selected = elite_mean.mean(dim=0)
        else:
            std = torch.exp(0.5 * logvar)
            samples = mean + torch.randn_like(std) * std
            elite_sample_idx = torch.as_tensor(self.model.random_elite_idxs(obs_features.shape[0]), device=self.device)
            selected = samples[elite_sample_idx, torch.arange(obs_features.shape[0], device=self.device)]
        delta_obs = selected[:, :-1]
        pred_reward = selected[:, -1:]
        return obs_features + delta_obs, pred_reward

    def state_dict(self) -> dict[str, Any]:
        return {
            "model": self.model.state_dict(),
            "optimizer": self.optimizer.state_dict(),
            "scaler_mu": self.scaler.mu,
            "scaler_std": self.scaler.std,
        }

    def load_state_dict(self, state: dict[str, Any]) -> None:
        self.model.load_state_dict(state["model"])
        optimizer_state = state.get("optimizer")
        if optimizer_state is not None:
            self.optimizer.load_state_dict(optimizer_state)
        self.scaler.mu = state.get("scaler_mu")
        self.scaler.std = state.get("scaler_std")
        self.is_trained = self.scaler.mu is not None and self.scaler.std is not None
        self.model.eval()
