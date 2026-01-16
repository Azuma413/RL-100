import torch
import torch.nn as nn
import torch.nn.functional as F
import torchvision
import copy

from typing import Optional, Dict, Tuple, Union, List, Type
from termcolor import cprint


def create_mlp(
        input_dim: int,
        output_dim: int,
        net_arch: List[int],
        activation_fn: Type[nn.Module] = nn.ReLU,
        squash_output: bool = False,
) -> List[nn.Module]:
    """
    Create a multi layer perceptron (MLP), which is
    a collection of fully-connected layers each followed by an activation function.

    :param input_dim: Dimension of the input vector
    :param output_dim:
    :param net_arch: Architecture of the neural net
        It represents the number of units per layer.
        The length of this list is the number of layers.
    :param activation_fn: The activation function
        to use after each layer.
    :param squash_output: Whether to squash the output using a Tanh
        activation function
    :return:
    """

    if len(net_arch) > 0:
        modules = [nn.Linear(input_dim, net_arch[0]), activation_fn()]
    else:
        modules = []

    for idx in range(len(net_arch) - 1):
        modules.append(nn.Linear(net_arch[idx], net_arch[idx + 1]))
        modules.append(activation_fn())

    if output_dim > 0:
        last_layer_dim = net_arch[-1] if len(net_arch) > 0 else input_dim
        modules.append(nn.Linear(last_layer_dim, output_dim))
    if squash_output:
        modules.append(nn.Tanh())
    return modules




class PointNetEncoderXYZRGB(nn.Module):
    """Encoder for Pointcloud
    """

    def __init__(self,
                 in_channels: int,
                 out_channels: int=1024,
                 use_layernorm: bool=False,
                 final_norm: str='none',
                 use_projection: bool=True,
                 use_vib: bool=False,
                 **kwargs
                 ):
        """_summary_

        Args:
            in_channels (int): feature size of input (3 or 6)
            input_transform (bool, optional): whether to use transformation for coordinates. Defaults to True.
            feature_transform (bool, optional): whether to use transformation for features. Defaults to True.
            is_seg (bool, optional): for segmentation or classification. Defaults to False.
        """
        super().__init__()
        block_channel = [64, 128, 256, 512]
        self.use_vib = use_vib
        cprint("pointnet use_layernorm: {}".format(use_layernorm), 'cyan')
        cprint("pointnet use_final_norm: {}".format(final_norm), 'cyan')
        cprint("pointnet use_vib: {}".format(use_vib), 'cyan')
        
        self.mlp = nn.Sequential(
            nn.Linear(in_channels, block_channel[0]),
            nn.LayerNorm(block_channel[0]) if use_layernorm else nn.Identity(),
            nn.ReLU(),
            nn.Linear(block_channel[0], block_channel[1]),
            nn.LayerNorm(block_channel[1]) if use_layernorm else nn.Identity(),
            nn.ReLU(),
            nn.Linear(block_channel[1], block_channel[2]),
            nn.LayerNorm(block_channel[2]) if use_layernorm else nn.Identity(),
            nn.ReLU(),
            nn.Linear(block_channel[2], block_channel[3]),
        )
        
       
        if final_norm == 'layernorm':
            self.final_projection = nn.Sequential(
                nn.Linear(block_channel[-1], out_channels),
                nn.LayerNorm(out_channels)
            )
        elif final_norm == 'none':
            self.final_projection = nn.Linear(block_channel[-1], out_channels)
        else:
            raise NotImplementedError(f"final_norm: {final_norm}")

        # VIB: Variational Information Bottleneck
        if self.use_vib:
            # VAE branches for mu and logvar
            self.mu_layer = nn.Linear(block_channel[-1], out_channels)
            self.logvar_layer = nn.Linear(block_channel[-1], out_channels)
            # Reconstruction decoder for point cloud
            self.recon_decoder = nn.Sequential(
                nn.Linear(out_channels, 256),
                nn.ReLU(),
                nn.Linear(256, 512 * in_channels)  # Reconstruct 512 points with in_channels features
            )
            self.in_channels = in_channels
            cprint("[PointNetEncoderXYZRGB] VIB enabled with reconstruction decoder", "cyan")

    def forward(self, x, return_recon=False):
        """
        Args:
            x: (B, N, C) point cloud with C channels (3 or 6)
            return_recon: whether to return reconstruction for VIB loss
        Returns:
            if use_vib and return_recon:
                feat, mu, logvar, recon_pc
            else:
                feat
        """
        x = self.mlp(x)  # (B, N, 512)
        x = torch.max(x, 1)[0]  # (B, 512) - max pooling

        if self.use_vib:
            # VAE: compute mu and logvar
            mu = self.mu_layer(x)  # (B, out_channels)
            logvar = self.logvar_layer(x)  # (B, out_channels)

            # Reparameterization trick: z = mu + eps * std
            std = torch.exp(0.5 * logvar)
            eps = torch.randn_like(std)
            z = mu + eps * std  # (B, out_channels)

            # z is already the final feature representation, no need for final_projection
            feat = z

            if return_recon:
                # Reconstruct point cloud
                recon = self.recon_decoder(z)  # (B, 512*C)
                recon_pc = recon.reshape(-1, 512, self.in_channels)  # (B, 512, C)
                return feat, mu, logvar, recon_pc
            else:
                return feat
        else:
            # Original forward without VIB
            x = self.final_projection(x)
            return x
    

class PointNetEncoderXYZ(nn.Module):
    """Encoder for Pointcloud
    """

    def __init__(self,
                 in_channels: int=3,
                 out_channels: int=1024,
                 use_layernorm: bool=False,
                 final_norm: str='none',
                 use_projection: bool=True,
                 use_vib: bool=False,
                 **kwargs
                 ):
        """_summary_

        Args:
            in_channels (int): feature size of input (3 or 6)
            input_transform (bool, optional): whether to use transformation for coordinates. Defaults to True.
            feature_transform (bool, optional): whether to use transformation for features. Defaults to True.
            is_seg (bool, optional): for segmentation or classification. Defaults to False.
        """
        super().__init__()
        block_channel = [64, 128, 256]
        self.use_vib = use_vib
        cprint("[PointNetEncoderXYZ] use_layernorm: {}".format(use_layernorm), 'cyan')
        cprint("[PointNetEncoderXYZ] use_final_norm: {}".format(final_norm), 'cyan')
        cprint("[PointNetEncoderXYZ] use_vib: {}".format(use_vib), 'cyan')
        
        assert in_channels == 3, cprint(f"PointNetEncoderXYZ only supports 3 channels, but got {in_channels}", "red")
       
        self.mlp = nn.Sequential(
            nn.Linear(in_channels, block_channel[0]),
            nn.LayerNorm(block_channel[0]) if use_layernorm else nn.Identity(),
            nn.ReLU(),
            nn.Linear(block_channel[0], block_channel[1]),
            nn.LayerNorm(block_channel[1]) if use_layernorm else nn.Identity(),
            nn.ReLU(),
            nn.Linear(block_channel[1], block_channel[2]),
            nn.LayerNorm(block_channel[2]) if use_layernorm else nn.Identity(),
            nn.ReLU(),
        )
        
        
        if final_norm == 'layernorm':
            self.final_projection = nn.Sequential(
                nn.Linear(block_channel[-1], out_channels),
                nn.LayerNorm(out_channels)
            )
        elif final_norm == 'none':
            self.final_projection = nn.Linear(block_channel[-1], out_channels)
        else:
            raise NotImplementedError(f"final_norm: {final_norm}")

        self.use_projection = use_projection
        if not use_projection:
            self.final_projection = nn.Identity()
            cprint("[PointNetEncoderXYZ] not use projection", "yellow")

        # VIB: Variational Information Bottleneck
        if self.use_vib:
            # VAE branches for mu and logvar
            self.mu_layer = nn.Linear(block_channel[-1], out_channels)
            self.logvar_layer = nn.Linear(block_channel[-1], out_channels)
            # Reconstruction decoder for point cloud
            self.recon_decoder = nn.Sequential(
                nn.Linear(out_channels, 256),
                nn.ReLU(),
                nn.Linear(256, 512 * 3)  # Reconstruct 512 points with 3D coordinates
            )
            cprint("[PointNetEncoderXYZ] VIB enabled with reconstruction decoder", "cyan")
            
        VIS_WITH_GRAD_CAM = False
        if VIS_WITH_GRAD_CAM:
            self.gradient = None
            self.feature = None
            self.input_pointcloud = None
            self.mlp[0].register_forward_hook(self.save_input)
            self.mlp[6].register_forward_hook(self.save_feature)
            self.mlp[6].register_backward_hook(self.save_gradient)


    def forward(self, x, return_recon=False):
        """
        Args:
            x: (B, N, 3) point cloud
            return_recon: whether to return reconstruction for VIB loss
        Returns:
            if use_vib and return_recon:
                feat, mu, logvar, recon_pc
            else:
                feat
        """
        x = self.mlp(x)  # (B, N, 256)
        x = torch.max(x, 1)[0]  # (B, 256) - max pooling

        if self.use_vib:
            # VAE: compute mu and logvar
            mu = self.mu_layer(x)  # (B, out_channels)
            logvar = self.logvar_layer(x)  # (B, out_channels)

            # Reparameterization trick: z = mu + eps * std
            std = torch.exp(0.5 * logvar)
            eps = torch.randn_like(std)
            z = mu + eps * std  # (B, out_channels)

            # z is already the final feature representation, no need for final_projection
            feat = z

            if return_recon:
                # Reconstruct point cloud
                recon = self.recon_decoder(z)  # (B, 512*3)
                recon_pc = recon.reshape(-1, 512, 3)  # (B, 512, 3)
                return feat, mu, logvar, recon_pc
            else:
                return feat
        else:
            # Original forward without VIB
            x = self.final_projection(x)
            return x
    
    def save_gradient(self, module, grad_input, grad_output):
        """
        for grad-cam
        """
        self.gradient = grad_output[0]

    def save_feature(self, module, input, output):
        """
        for grad-cam
        """
        if isinstance(output, tuple):
            self.feature = output[0].detach()
        else:
            self.feature = output.detach()
    
    def save_input(self, module, input, output):
        """
        for grad-cam
        """
        self.input_pointcloud = input[0].detach()

    


class DP3Encoder(nn.Module):
    def __init__(self,
                 observation_space: Dict,
                 img_crop_shape=None,
                 out_channel=256,
                 state_mlp_size=(64, 64), state_mlp_activation_fn=nn.ReLU,
                 pointcloud_encoder_cfg=None,
                 use_pc_color=False,
                 pointnet_type='pointnet',
                 use_recon_vib=False,
                 beta_recon=1.0,
                 beta_kl=0.001,
                 ):
        super().__init__()
        self.imagination_key = 'imagin_robot'
        self.state_key = 'agent_pos'
        self.point_cloud_key = 'point_cloud'
        self.rgb_image_key = 'image'
        self.n_output_channels = out_channel
        
        self.use_imagined_robot = self.imagination_key in observation_space.keys()
        self.point_cloud_shape = observation_space[self.point_cloud_key]
        self.state_shape = observation_space[self.state_key]
        if self.use_imagined_robot:
            self.imagination_shape = observation_space[self.imagination_key]
        else:
            self.imagination_shape = None
            
        
        
        cprint(f"[DP3Encoder] point cloud shape: {self.point_cloud_shape}", "yellow")
        cprint(f"[DP3Encoder] state shape: {self.state_shape}", "yellow")
        cprint(f"[DP3Encoder] imagination point shape: {self.imagination_shape}", "yellow")
        

        self.use_pc_color = use_pc_color
        self.pointnet_type = pointnet_type
        self.use_recon_vib = use_recon_vib
        self.beta_recon = beta_recon
        self.beta_kl = beta_kl

        cprint(f"[DP3Encoder] use_recon_vib: {use_recon_vib}", "cyan")
        cprint(f"[DP3Encoder] beta_recon: {beta_recon}, beta_kl: {beta_kl}", "cyan")

        if pointnet_type == "pointnet":
            if use_pc_color:
                pointcloud_encoder_cfg.in_channels = 6
                pointcloud_encoder_cfg.use_vib = use_recon_vib
                self.extractor = PointNetEncoderXYZRGB(**pointcloud_encoder_cfg)
            else:
                pointcloud_encoder_cfg.in_channels = 3
                pointcloud_encoder_cfg.use_vib = use_recon_vib
                self.extractor = PointNetEncoderXYZ(**pointcloud_encoder_cfg)
        else:
            raise NotImplementedError(f"pointnet_type: {pointnet_type}")


        if len(state_mlp_size) == 0:
            raise RuntimeError(f"State mlp size is empty")
        elif len(state_mlp_size) == 1:
            net_arch = []
        else:
            net_arch = state_mlp_size[:-1]
        output_dim = state_mlp_size[-1]

        self.n_output_channels  += output_dim
        self.state_mlp = nn.Sequential(*create_mlp(self.state_shape[0], output_dim, net_arch, state_mlp_activation_fn))

        # State reconstruction decoder for VIB
        if self.use_recon_vib:
            self.state_recon_decoder = nn.Sequential(
                nn.Linear(output_dim, 64),
                nn.ReLU(),
                nn.Linear(64, self.state_shape[0])
            )
            cprint(f"[DP3Encoder] State reconstruction decoder initialized", "cyan")

        cprint(f"[DP3Encoder] output dim: {self.n_output_channels}", "red")


    def forward(self, observations: Dict, return_reg_loss: bool = False) -> Union[torch.Tensor, Tuple[torch.Tensor, Dict]]:
        """
        Args:
            observations: Dictionary containing point_cloud, agent_pos, etc.
            return_reg_loss: If True, return (features, reg_loss_dict) for VIB training

        Returns:
            If return_reg_loss=False: features tensor
            If return_reg_loss=True: (features, reg_loss_dict) where reg_loss_dict contains:
                - kl_loss: KL divergence loss
                - recon_loss: reconstruction loss (point cloud + state)
                - total_reg_loss: weighted sum of losses
        """
        points = observations[self.point_cloud_key]
        assert len(points.shape) == 3, cprint(f"point cloud shape: {points.shape}, length should be 3", "red")

        # Store original point cloud for reconstruction loss (before concatenation with imagined robot)
        original_points = points

        if self.use_imagined_robot:
            img_points = observations[self.imagination_key][..., :points.shape[-1]] # align the last dim
            points = torch.concat([points, img_points], dim=1)

        # Extract point cloud features (with VIB if enabled)
        if self.use_recon_vib and return_reg_loss:
            pn_feat, mu, logvar, recon_pc = self.extractor(points, return_recon=True)

            # Compute KL divergence loss: -0.5 * sum(1 + logvar - mu^2 - exp(logvar))
            kl_loss = -0.5 * torch.sum(1 + logvar - mu.pow(2) - logvar.exp(), dim=-1)
            kl_loss = kl_loss.mean()

            # Compute point cloud reconstruction loss using Chamfer Distance
            # Use original_points (before imagined robot concatenation) for reconstruction target
            original_points_xyz = original_points[..., :3]  # Extract XYZ coordinates

            # Sample points from original_points_xyz to match recon_pc's size (512 points)
            # recon_pc shape: (B, 512, 3)
            B, N_recon, _ = recon_pc.shape
            _, N_orig, _ = original_points_xyz.shape

            if N_orig > N_recon:
                # Randomly sample N_recon points from original point cloud
                indices = torch.randperm(N_orig, device=original_points_xyz.device)[:N_recon]
                original_points_xyz_sampled = original_points_xyz[:, indices, :]
            elif N_orig < N_recon:
                # If original has fewer points, repeat points to match recon size
                repeat_factor = (N_recon + N_orig - 1) // N_orig
                original_points_xyz_sampled = original_points_xyz.repeat(1, repeat_factor, 1)[:, :N_recon, :]
            else:
                original_points_xyz_sampled = original_points_xyz

            try:
                from pytorch3d.loss import chamfer_distance
                # chamfer_distance expects (B, N, 3) for both inputs
                recon_loss_pc, _ = chamfer_distance(original_points_xyz_sampled, recon_pc)
            except ImportError:
                # Fallback to MSE on XYZ coordinates
                recon_loss_pc = F.mse_loss(recon_pc, original_points_xyz_sampled)

        else:
            pn_feat = self.extractor(points)
            kl_loss = torch.tensor(0.0, device=pn_feat.device)
            recon_loss_pc = torch.tensor(0.0, device=pn_feat.device)

        state = observations[self.state_key]
        state_feat = self.state_mlp(state)  # B * 64

        # Compute state reconstruction loss if VIB is enabled
        if self.use_recon_vib and return_reg_loss:
            recon_state = self.state_recon_decoder(state_feat)
            recon_loss_state = F.mse_loss(recon_state, state)

            # Total reconstruction loss
            recon_loss = recon_loss_pc + recon_loss_state

            # Weighted total regularization loss
            total_reg_loss = self.beta_recon * recon_loss + self.beta_kl * kl_loss

            reg_loss_dict = {
                'kl_loss': kl_loss.item() if isinstance(kl_loss, torch.Tensor) else kl_loss,
                'recon_loss': recon_loss.item() if isinstance(recon_loss, torch.Tensor) else recon_loss,
                'recon_loss_pc': recon_loss_pc.item() if isinstance(recon_loss_pc, torch.Tensor) else recon_loss_pc,
                'recon_loss_state': recon_loss_state.item() if isinstance(recon_loss_state, torch.Tensor) else recon_loss_state,
                'total_reg_loss': total_reg_loss
            }
        else:
            reg_loss_dict = {
                'kl_loss': 0.0,
                'recon_loss': 0.0,
                'recon_loss_pc': 0.0,
                'recon_loss_state': 0.0,
                'total_reg_loss': torch.tensor(0.0, device=pn_feat.device)
            }

        final_feat = torch.cat([pn_feat, state_feat], dim=-1)

        if return_reg_loss:
            return final_feat, reg_loss_dict
        else:
            return final_feat


    def output_shape(self):
        return self.n_output_channels