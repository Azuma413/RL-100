Job start at 2026-03-16 18:00:45
Job run at:
   Static hostname: localhost.localdomain
Transient hostname: r8a100-a05
         Icon name: computer-server
           Chassis: server
        Machine ID: a5c347209fb04991b4efdd1a4af6d42d
           Boot ID: 746e45d88d2945eeb8383abb275c0ce3
  Operating System: Rocky Linux 8.7 (Green Obsidian)
       CPE OS Name: cpe:/o:rocky:rocky:8:GA
            Kernel: Linux 4.18.0-425.10.1.el8_7.x86_64
      Architecture: x86-64
Filesystem                                        Size  Used Avail Use% Mounted on
/dev/mapper/rl-root                               120G   19G  102G  16% /
/dev/sdb1                                         1.1T  8.4G  1.1T   1% /tmp
/dev/sda2                                         2.0G  306M  1.7G  15% /boot
/dev/sdb2                                         4.2T  177G  4.1T   5% /local
/dev/mapper/rl-var                                768G   22G  747G   3% /var
/dev/sda1                                         599M  5.8M  594M   1% /boot/efi
ssd.nas00.future.cn:/rocky8_home                   16G   15G  1.9G  89% /home
ssd.nas00.future.cn:/rocky8_workspace             400G     0  400G   0% /workspace
ssd.nas00.future.cn:/rocky8_tools                 5.0T   99G  5.0T   2% /tools
ssd.nas00.future.cn:/centos7_home                  16G  4.2G   12G  26% /centos7/home
ssd.nas00.future.cn:/centos7_workspace            400G     0  400G   0% /centos7/workspace
ssd.nas00.future.cn:/centos7_tools                5.0T  235G  4.8T   5% /centos7/tools
ssd.nas00.future.cn:/eda-tools                    8.0T  6.3T  1.8T  79% /centos7/eda-tools
hdd.nas00.future.cn:/share_personal               500G     0  500G   0% /share/personal
zone05.nas01.future.cn:/NAS_HPC_collab_codemodel   40T   37T  3.7T  91% /share/collab/codemodel
ext-zone00.nas02.future.cn:/nfs_global            407T  385T   23T  95% /nfs_global
ssd.nas00.future.cn:/common_datasets               75T   64T   12T  85% /datasets
192.168.12.10@o2ib:192.168.12.11@o2ib:/lustre     1.9P   12T  1.8P   1% /lustre
beegfs_nodev                                       70T   15T   56T  21% /fast
Currently Loaded Modulefiles: 1) cluster-tools/v1.0 3) cuda-cudnn/12.1-8.9.3 5) git/2.31.1 2) cmake/3.21.7 4) gcc/9.3.0 6) slurm-tools/v1.0
/tools/cluster-software/gcc/gcc-9.3.0/bin/gcc
/home/S/yangrongzheng/miniconda3/bin/python
/home/S/yangrongzheng/miniconda3/bin/python3
############### /home : /home/S/yangrongzheng
Disk quotas for user yangrongzheng (uid 6215): 
     Filesystem   space   quota   limit   grace   files   quota   limit   grace
          /home  14455M  16384M  20480M            169k       0       0        

############### /workspace
Disk quotas for user yangrongzheng (uid 6215): 
     Filesystem   space   quota   limit   grace   files   quota   limit   grace
     /workspace      0K    400G    500G               1       0       0        

############### /nfs_global
Disk quotas for user yangrongzheng (uid 6215): 
     Filesystem   space   quota   limit   grace   files   quota   limit   grace
    /nfs_global    363G   5120G   7168G            350k   5000k  10000k        

############### /lustre
Disk quotas for usr yangrongzheng (uid 6215):
     Filesystem    used   quota   limit   grace   files   quota   limit   grace
        /lustre      0k      8T     10T       -       0  3000000 36000000       -
uid 6215 is using default block quota setting
uid 6215 is using default file quota setting
name, driver_version, power.limit [W]
NVIDIA A100-PCIE-40GB, 550.54.15, 225.00 W
NVIDIA A100-PCIE-40GB, 550.54.15, 225.00 W
NVIDIA A100-PCIE-40GB, 550.54.15, 225.00 W
NVIDIA A100-PCIE-40GB, 550.54.15, 225.00 W
NVIDIA A100-PCIE-40GB, 550.54.15, 225.00 W
NVIDIA A100-PCIE-40GB, 550.54.15, 225.00 W
NVIDIA A100-PCIE-40GB, 550.54.15, 225.00 W
NVIDIA A100-PCIE-40GB, 550.54.15, 225.00 W
Using GPU(s) 0,1,2,3,4,5,6,7
This job is assigned the following resources by SLURM:
CPU_IDs=0-111 GRES=gpu:8(IDX:0-7)
Main program continues to run. Monitoring information will be exported after three hours.
Have already added /tools/cluster-modulefiles into $MODULEPATH
no change     /home/S/yangrongzheng/miniconda3/condabin/conda
no change     /home/S/yangrongzheng/miniconda3/bin/conda
no change     /home/S/yangrongzheng/miniconda3/bin/conda-env
no change     /home/S/yangrongzheng/miniconda3/bin/activate
no change     /home/S/yangrongzheng/miniconda3/bin/deactivate
no change     /home/S/yangrongzheng/miniconda3/etc/profile.d/conda.sh
no change     /home/S/yangrongzheng/miniconda3/etc/fish/conf.d/conda.fish
no change     /home/S/yangrongzheng/miniconda3/shell/condabin/Conda.psm1
no change     /home/S/yangrongzheng/miniconda3/shell/condabin/conda-hook.ps1
no change     /home/S/yangrongzheng/miniconda3/lib/python3.13/site-packages/xontrib/conda.xsh
no change     /home/S/yangrongzheng/miniconda3/etc/profile.d/conda.csh
no change     /home/S/yangrongzheng/.bashrc
No action taken.

================================================================================
                              RL-100 TRAINING
================================================================================

Configuration:
task:
  name: dial-turn
  task_name: ${.name}
  shape_meta:
    obs:
      point_cloud:
        shape:
        - 512
        - 3
        type: point_cloud
      agent_pos:
        shape:
        - 9
        type: low_dim
    action:
      shape:
      - 4
  env_runner:
    _target_: diffusion_policy_3d.env_runner.metaworld_runner.MetaworldRunner
    eval_episodes: 100
    n_obs_steps: ${n_obs_steps}
    n_action_steps: ${n_action_steps}
    fps: 10
    n_envs: null
    n_train: null
    n_test: null
    task_name: ${task_name}
    device: ${training.device}
    use_point_crop: ${policy.use_point_crop}
    num_points: 512
  dataset:
    _target_: diffusion_policy_3d.dataset.metaworld_dataset.MetaworldDataset
    zarr_path: data/metaworld_dial-turn_expert.zarr
    horizon: ${horizon}
    pad_before: ${eval:'${n_obs_steps}-1'}
    pad_after: ${eval:'${n_action_steps}-1'}
    seed: 42
    val_ratio: 0.02
    max_train_episodes: 90
    n_action_steps: ${n_action_steps}
    gamma: 0.99
name: train_rl100
task_name: ${task.name}
shape_meta: ${task.shape_meta}
exp_name: debug
horizon: 16
n_obs_steps: 2
n_action_steps: 8
obs_as_global_cond: true
policy:
  _target_: diffusion_policy_3d.policy.rl100_policy.RL100Policy
  shape_meta: ${shape_meta}
  horizon: ${horizon}
  n_obs_steps: ${n_obs_steps}
  n_action_steps: ${n_action_steps}
  num_inference_steps: 10
  use_point_crop: true
  encoder_output_dim: 64
  diffusion_step_embed_dim: 128
  down_dims:
  - 512
  - 1024
  - 2048
  kernel_size: 5
  n_groups: 8
  condition_type: film
  use_pc_color: false
  pointnet_type: pointnet
  obs_as_global_cond: ${obs_as_global_cond}
  noise_scheduler:
    _target_: diffusers.schedulers.scheduling_ddim.DDIMScheduler
    num_train_timesteps: 100
    beta_schedule: squaredcos_cap_v2
    clip_sample: true
    prediction_type: epsilon
  pointcloud_encoder_cfg:
    in_channels: 3
    out_channels: 64
    use_layernorm: true
    final_norm: layernorm
    normal_channel: false
  use_recon_vib: false
  beta_recon: 0.0001
  beta_kl: 0.0001
  ppo_clip_eps: 0.2
  sigma_min: 0.01
  sigma_max: 0.1
  use_variance_clip: true
critics:
  hidden_dims:
  - 256
  - 256
  - 256
  gamma: 0.9227
  tau: 0.7
  target_update_tau: 0.005
  reward_scale: 1.0
  reward_type: sparse
optimizer:
  policy:
    _target_: torch.optim.AdamW
    lr: 0.0001
    weight_decay: 1.0e-06
    betas:
    - 0.9
    - 0.999
  v_network:
    _target_: torch.optim.AdamW
    lr: 0.0003
    weight_decay: 1.0e-06
  q_network:
    _target_: torch.optim.AdamW
    lr: 0.0003
    weight_decay: 1.0e-06
  consistency:
    _target_: torch.optim.AdamW
    lr: 0.0001
    weight_decay: 1.0e-06
ema:
  _target_: diffusion_policy_3d.model.diffusion.ema_model.EMAModel
  power: 0.75
  max_value: 0.9999
  min_value: 0.0
dataloader:
  batch_size: 256
  num_workers: 8
  shuffle: true
  pin_memory: true
  drop_last: false
  persistent_workers: true
training:
  device: cuda:0
  seed: 42
  use_ema: true
  il_epochs: 1000
  il_retrain_epochs: 100
  retrain_il_after_collection: true
  num_offline_iterations: 10
  critic_epochs: 20
  ppo_epochs: 20
  ppo_inner_steps: 2
  collection_episodes: 20
  cd_every: 5
  lambda_cd: 1.0
  rl_policy_lr: 1.0e-05
  run_online_rl: true
  online_rl_iterations: 10
  online_collection_episodes: 20
  lambda_v: 0.5
  gae_lambda: 0.95
  gradient_accumulate_every: 1
  max_grad_norm: 1.0
  log_every: 10
  eval_every: 100
  checkpoint_every: 200
  resume: true
  resume_path: /nfs_global/S/yangrongzheng/RL100/3D-Diffusion-Policy/3D-Diffusion-Policy/checkpoints/after_il.ckpt
runtime:
  collection_policy: ddim
  collection_use_ema: false
  merge_success_only: true
  final_eval_policies:
  - ddim
  - cm
  final_eval_use_ema: true
  eval_policy_mode: ddim
  eval_use_ema: true
checkpoint:
  save_ckpt: true
  save_last_ckpt: true
  save_last_snapshot: false
  topk:
    monitor_key: test_mean_score
    mode: max
    k: 1
logging:
  use_wandb: false
  project: rl100-dp3
  group: ${task.name}
  name: rl100_${task.name}_seed${training.seed}
  mode: online


[Setup] Random seed: 42
[Setup] Output directory: /nfs_global/S/yangrongzheng/RL100/3D-Diffusion-Policy/3D-Diffusion-Policy

[Setup] Loading dataset...
Replay Buffer: state, shape (20000, 9), dtype float32, range -0.16~0.88
Replay Buffer: action, shape (20000, 4), dtype float32, range -1.51~1.69
Replay Buffer: point_cloud, shape (20000, 1024, 6), dtype float32, range -0.95~255.00
Replay Buffer: reward, shape (20000,), dtype float32, range 0.00~1.00
Replay Buffer: done, shape (20000,), dtype float32, range 0.00~1.00
--------------------------
[Setup] Dataset loaded: 17370 episodes
[Setup] Dataset has reward/done labels: True
[Setup] Dataset point_cloud points: 1024
[Setup] Initializing environment runner...
[Setup] env_runner.num_points=512 differs from dataset=1024. Override to dataset value to avoid merge shape mismatch.
[MetaWorldEnv] use_point_crop: True
[Setup] Environment runner initialized

[Setup] Initializing RL100Trainer...
[RL100Trainer] Initializing RL100Policy...
[DP3Encoder] point cloud shape: [512, 3]
[DP3Encoder] state shape: [9]
[DP3Encoder] imagination point shape: None
[DP3Encoder] use_recon_vib: False
[DP3Encoder] beta_recon: 0.0001, beta_kl: 0.0001
[PointNetEncoderXYZ] use_layernorm: True
[PointNetEncoderXYZ] use_final_norm: layernorm
[PointNetEncoderXYZ] use_vib: False
[DP3Encoder] output dim: 128
[DiffusionUnetHybridPointcloudPolicy] use_pc_color: False
[DiffusionUnetHybridPointcloudPolicy] pointnet_type: pointnet
[2026-03-16 18:00:59,255][diffusion_policy_3d.model.diffusion.conditional_unet1d][INFO] - number of parameters: 2.550744e+08
----------------------------------
Class name: RL100Policy
  Number of parameters: 255.1383M
   _dummy_variable: 0.0000M (0.00%)
   obs_encoder: 0.0639M (0.03%)
   model: 255.0744M (99.97%)
   mask_generator: 0.0000M (0.00%)
----------------------------------
[RL100Trainer] Initializing IQL Critics...
[RL100Trainer] Initializing Consistency Model...
[2026-03-16 18:01:01,102][diffusion_policy_3d.model.diffusion.conditional_unet1d][INFO] - number of parameters: 2.550744e+08
[RL100Trainer] Initializing Transition Model T_θ(s'|s,a)...
[Setup] RL100Trainer initialized

[Setup] Resuming from checkpoint: /nfs_global/S/yangrongzheng/RL100/3D-Diffusion-Policy/3D-Diffusion-Policy/checkpoints/after_il.ckpt
[Checkpoint] critics: skipped 2 incompatible key(s): ['q_network.q1.network.0.weight', 'q_network.q2.network.0.weight']
[Checkpoint] critics: 2 missing key(s): ['q_network.q1.network.0.weight', 'q_network.q2.network.0.weight']
[Checkpoint] transition_model full restore failed (RuntimeError: Error(s) in loading state_dict for EnsembleDynamicsModel:
	size mismatch for backbones.0.weight: copying a param with shape torch.Size([7, 260, 200]) from checkpoint, the shape in current model is torch.Size([7, 288, 200]).
	size mismatch for backbones.0.saved_weight: copying a param with shape torch.Size([7, 260, 200]) from checkpoint, the shape in current model is torch.Size([7, 288, 200]).); trying partial model restore.
[Checkpoint] transition_model.model: skipped 2 incompatible key(s): ['backbones.0.weight', 'backbones.0.saved_weight']
[Checkpoint] transition_model.model: 2 missing key(s): ['backbones.0.weight', 'backbones.0.saved_weight']
[Checkpoint] Loaded from /nfs_global/S/yangrongzheng/RL100/3D-Diffusion-Policy/3D-Diffusion-Policy/checkpoints/after_il.ckpt
[Setup] IL phase will be skipped — starting directly from offline RL.

[Training] Starting RL-100 pipeline...

================================================================================
                    RL-100 TRAINING PIPELINE
================================================================================


[RL100Trainer] Skipping IL phase — loaded from checkpoint.
[RL100Trainer] Normalizer synced from dataset. Resuming offline RL from iteration 0.
[RL100Trainer] Dataset already contains reward/done labels; keep existing rewards.

================================================================================
               OFFLINE RL ITERATION 1/10
================================================================================


[RL100Trainer] Line 6 — Training Transition Model T_θ (Iteration 0)

[TransitionModel] Encoding dataset for transition model training...
[TransitionModel] Dataset: 17370 samples, input_dim=288, target_dim=257
[TransitionModel] Epoch    0 | train=5.39305 | val=0.00466 | no-improve=0/5
[TransitionModel] Epoch   20 | train=-31.27108 | val=0.00050 | no-improve=0/5
[TransitionModel] Epoch   40 | train=-37.27283 | val=0.00038 | no-improve=0/5
[TransitionModel] Epoch   60 | train=-41.47412 | val=0.00032 | no-improve=0/5
[TransitionModel] Epoch   80 | train=-45.42663 | val=0.00027 | no-improve=0/5
[TransitionModel] Epoch  100 | train=-49.15089 | val=0.00021 | no-improve=0/5
[TransitionModel] Epoch  120 | train=-52.82454 | val=0.00017 | no-improve=0/5
[TransitionModel] Epoch  140 | train=-56.30543 | val=0.00015 | no-improve=0/5
[TransitionModel] Epoch  160 | train=-59.88554 | val=0.00014 | no-improve=3/5
[TransitionModel] Epoch  180 | train=-63.24838 | val=0.00013 | no-improve=1/5
[TransitionModel] Training complete. Elites=[5, 1, 3, 4, 0], val_loss=0.00012

[RL100Trainer] Phase 2a: Training IQL Critics (Iteration 0)
[IQL] Epoch 0/20, V Loss: 0.0089, Q Loss: 0.0591
[IQL] Epoch 1/20, V Loss: 0.0002, Q Loss: 0.0089
[IQL] Epoch 2/20, V Loss: 0.0001, Q Loss: 0.0088
[IQL] Epoch 3/20, V Loss: 0.0001, Q Loss: 0.0087
[IQL] Epoch 4/20, V Loss: 0.0002, Q Loss: 0.0085
[IQL] Epoch 5/20, V Loss: 0.0002, Q Loss: 0.0084
[IQL] Epoch 6/20, V Loss: 0.0002, Q Loss: 0.0085
[IQL] Epoch 7/20, V Loss: 0.0002, Q Loss: 0.0084
[IQL] Epoch 8/20, V Loss: 0.0001, Q Loss: 0.0082
[IQL] Epoch 9/20, V Loss: 0.0002, Q Loss: 0.0082
[IQL] Epoch 10/20, V Loss: 0.0003, Q Loss: 0.0081
[IQL] Epoch 11/20, V Loss: 0.0001, Q Loss: 0.0080
[IQL] Epoch 12/20, V Loss: 0.0002, Q Loss: 0.0080
[IQL] Epoch 13/20, V Loss: 0.0003, Q Loss: 0.0081
[IQL] Epoch 14/20, V Loss: 0.0002, Q Loss: 0.0078
[IQL] Epoch 15/20, V Loss: 0.0002, Q Loss: 0.0077
[IQL] Epoch 16/20, V Loss: 0.0003, Q Loss: 0.0078
[IQL] Epoch 17/20, V Loss: 0.0002, Q Loss: 0.0078
[IQL] Epoch 18/20, V Loss: 0.0002, Q Loss: 0.0075
[IQL] Epoch 19/20, V Loss: 0.0004, Q Loss: 0.0077
[Plot] Saved: /nfs_global/S/yangrongzheng/RL100/3D-Diffusion-Policy/3D-Diffusion-Policy/plots/iql_q_loss_iter_00.png
[Plot] Saved: /nfs_global/S/yangrongzheng/RL100/3D-Diffusion-Policy/3D-Diffusion-Policy/plots/iql_v_loss_iter_00.png

[RL100Trainer] Phase 2b: Offline RL Optimization (Iteration 0)
[OPE] Behavior policy value J_old = 0.2774
[RL PPO] Reducing policy LR: 1.00e-04 → 1.00e-05
[Offline RL] Epoch 0/20, PPO Loss: -0.0179, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 15.2362, Reg Loss: 0.0000, CD Loss: 0.3100
[Offline RL] Epoch 1/20, PPO Loss: -0.0194, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 13.8626, Reg Loss: 0.0000, CD Loss: 0.0734
[Offline RL] Epoch 2/20, PPO Loss: -0.0184, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 13.4143, Reg Loss: 0.0000, CD Loss: 0.0590
[Offline RL] Epoch 3/20, PPO Loss: -0.0176, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 13.3945, Reg Loss: 0.0000, CD Loss: 0.0492
[Offline RL] Epoch 4/20, PPO Loss: -0.0170, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 12.9855, Reg Loss: 0.0000, CD Loss: 0.0414
[Offline RL] Epoch 5/20, PPO Loss: -0.0161, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 13.5930, Reg Loss: 0.0000, CD Loss: 0.0330
[Offline RL] Epoch 6/20, PPO Loss: -0.0157, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 13.8850, Reg Loss: 0.0000, CD Loss: 0.0254
[Offline RL] Epoch 7/20, PPO Loss: -0.0154, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 13.4396, Reg Loss: 0.0000, CD Loss: 0.0200
[Offline RL] Epoch 8/20, PPO Loss: -0.0148, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 13.3885, Reg Loss: 0.0000, CD Loss: 0.0182
[Offline RL] Epoch 9/20, PPO Loss: -0.0150, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 13.5899, Reg Loss: 0.0000, CD Loss: 0.0168
[Offline RL] Epoch 10/20, PPO Loss: -0.0151, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 13.3305, Reg Loss: 0.0000, CD Loss: 0.0156
[Offline RL] Epoch 11/20, PPO Loss: -0.0151, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 13.7594, Reg Loss: 0.0000, CD Loss: 0.0145
[Offline RL] Epoch 12/20, PPO Loss: -0.0153, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 13.7548, Reg Loss: 0.0000, CD Loss: 0.0138
[Offline RL] Epoch 13/20, PPO Loss: -0.0150, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 13.4812, Reg Loss: 0.0000, CD Loss: 0.0130
[Offline RL] Epoch 14/20, PPO Loss: -0.0150, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 13.7617, Reg Loss: 0.0000, CD Loss: 0.0129
[Offline RL] Epoch 15/20, PPO Loss: -0.0153, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 12.9553, Reg Loss: 0.0000, CD Loss: 0.0122
[Offline RL] Epoch 16/20, PPO Loss: -0.0152, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 13.7546, Reg Loss: 0.0000, CD Loss: 0.0114
[Offline RL] Epoch 17/20, PPO Loss: -0.0150, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 14.0521, Reg Loss: 0.0000, CD Loss: 0.0113
[Offline RL] Epoch 18/20, PPO Loss: -0.0152, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 13.7002, Reg Loss: 0.0000, CD Loss: 0.0114
[Offline RL] Epoch 19/20, PPO Loss: -0.0150, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 13.3874, Reg Loss: 0.0000, CD Loss: 0.0116
[Plot] Saved: /nfs_global/S/yangrongzheng/RL100/3D-Diffusion-Policy/3D-Diffusion-Policy/plots/ppo_loss_iter_00.png
[OPE] Policy REJECTED: J_new=0.2779 ≤ J_old=0.2774 + δ=0.0139. Rolling back to behavior policy.

[RL100Trainer] Phase 2c: Collecting New Data (Iteration 0)
[Collect] 20 episodes, success=0.600, env_return=1022.39, rl_reward=0.60, steps=4000
[Data Collection] Success Rate: 0.600, EnvReturn: 1022.39, RLReward: 0.60, Episodes: 20, Steps: 4000
[Dataset] offline collection: keeping 12/20 successful episodes (dropped 8 failures) before merge.
[Dataset] Merged 12 episodes (2400 steps) → total 22400 steps, 112 episodes

[RL100Trainer] Retraining IL on merged dataset...

============================================================
[RL100Trainer] Phase 1: Imitation Learning
============================================================

[IL] Epoch 0/100, Loss: 0.0161, Val Loss: 0.0109
[IL] Epoch 1/100, Loss: 0.0114, Val Loss: 0.0085
[IL] Epoch 2/100, Loss: 0.0102, Val Loss: 0.0080
[IL] Epoch 3/100, Loss: 0.0103, Val Loss: 0.0062
[IL] Epoch 4/100, Loss: 0.0091, Val Loss: 0.0078
[IL] Epoch 5/100, Loss: 0.0084, Val Loss: 0.0068
[IL] Epoch 6/100, Loss: 0.0082, Val Loss: 0.0064
[IL] Epoch 7/100, Loss: 0.0076, Val Loss: 0.0072
[IL] Epoch 8/100, Loss: 0.0078, Val Loss: 0.0076
[IL] Epoch 9/100, Loss: 0.0074, Val Loss: 0.0109
[IL] Epoch 10/100, Loss: 0.0079, Val Loss: 0.0087
[IL] Epoch 11/100, Loss: 0.0076, Val Loss: 0.0068
[IL] Epoch 12/100, Loss: 0.0076, Val Loss: 0.0110
[IL] Epoch 13/100, Loss: 0.0074, Val Loss: 0.0070
[IL] Epoch 14/100, Loss: 0.0065, Val Loss: 0.0057
[IL] Epoch 15/100, Loss: 0.0068, Val Loss: 0.0086
[IL] Epoch 16/100, Loss: 0.0077, Val Loss: 0.0070
[IL] Epoch 17/100, Loss: 0.0070, Val Loss: 0.0080
[IL] Epoch 18/100, Loss: 0.0070, Val Loss: 0.0078
[IL] Epoch 19/100, Loss: 0.0066, Val Loss: 0.0063
[IL] Epoch 20/100, Loss: 0.0064, Val Loss: 0.0084
[IL] Epoch 21/100, Loss: 0.0065, Val Loss: 0.0079
[IL] Epoch 22/100, Loss: 0.0066, Val Loss: 0.0076
[IL] Epoch 23/100, Loss: 0.0070, Val Loss: 0.0073
[IL] Epoch 24/100, Loss: 0.0066, Val Loss: 0.0101
[IL] Epoch 25/100, Loss: 0.0061, Val Loss: 0.0073
[IL] Epoch 26/100, Loss: 0.0070, Val Loss: 0.0071
[IL] Epoch 27/100, Loss: 0.0067, Val Loss: 0.0117
[IL] Epoch 28/100, Loss: 0.0061, Val Loss: 0.0085
[IL] Epoch 29/100, Loss: 0.0062, Val Loss: 0.0101
[IL] Epoch 30/100, Loss: 0.0061, Val Loss: 0.0078
[IL] Epoch 31/100, Loss: 0.0064, Val Loss: 0.0091
[IL] Epoch 32/100, Loss: 0.0065, Val Loss: 0.0076
[IL] Epoch 33/100, Loss: 0.0063, Val Loss: 0.0102
[IL] Epoch 34/100, Loss: 0.0061, Val Loss: 0.0051
[IL] Epoch 35/100, Loss: 0.0065, Val Loss: 0.0063
[IL] Epoch 36/100, Loss: 0.0063, Val Loss: 0.0069
[IL] Epoch 37/100, Loss: 0.0057, Val Loss: 0.0096
[IL] Epoch 38/100, Loss: 0.0058, Val Loss: 0.0100
[IL] Epoch 39/100, Loss: 0.0061, Val Loss: 0.0099
[IL] Epoch 40/100, Loss: 0.0059, Val Loss: 0.0067
[IL] Epoch 41/100, Loss: 0.0059, Val Loss: 0.0105
[IL] Epoch 42/100, Loss: 0.0061, Val Loss: 0.0081
[IL] Epoch 43/100, Loss: 0.0061, Val Loss: 0.0066
[IL] Epoch 44/100, Loss: 0.0058, Val Loss: 0.0075
[IL] Epoch 45/100, Loss: 0.0061, Val Loss: 0.0075
[IL] Epoch 46/100, Loss: 0.0053, Val Loss: 0.0082
[IL] Epoch 47/100, Loss: 0.0054, Val Loss: 0.0103
[IL] Epoch 48/100, Loss: 0.0061, Val Loss: 0.0082
[IL] Epoch 49/100, Loss: 0.0054, Val Loss: 0.0083
[IL] Epoch 50/100, Loss: 0.0061, Val Loss: 0.0083
[IL] Epoch 51/100, Loss: 0.0055, Val Loss: 0.0115
[IL] Epoch 52/100, Loss: 0.0058, Val Loss: 0.0081
[IL] Epoch 53/100, Loss: 0.0057, Val Loss: 0.0077
[IL] Epoch 54/100, Loss: 0.0061, Val Loss: 0.0089
[IL] Epoch 55/100, Loss: 0.0055, Val Loss: 0.0093
[IL] Epoch 56/100, Loss: 0.0059, Val Loss: 0.0087
[IL] Epoch 57/100, Loss: 0.0055, Val Loss: 0.0097
[IL] Epoch 58/100, Loss: 0.0057, Val Loss: 0.0080
[IL] Epoch 59/100, Loss: 0.0055, Val Loss: 0.0076
[IL] Epoch 60/100, Loss: 0.0054, Val Loss: 0.0078
[IL] Epoch 61/100, Loss: 0.0051, Val Loss: 0.0107
[IL] Epoch 62/100, Loss: 0.0053, Val Loss: 0.0127
[IL] Epoch 63/100, Loss: 0.0054, Val Loss: 0.0069
[IL] Epoch 64/100, Loss: 0.0051, Val Loss: 0.0074
[IL] Epoch 65/100, Loss: 0.0055, Val Loss: 0.0090
[IL] Epoch 66/100, Loss: 0.0057, Val Loss: 0.0111
[IL] Epoch 67/100, Loss: 0.0055, Val Loss: 0.0082
[IL] Epoch 68/100, Loss: 0.0052, Val Loss: 0.0116
[IL] Epoch 69/100, Loss: 0.0051, Val Loss: 0.0089
[IL] Epoch 70/100, Loss: 0.0057, Val Loss: 0.0101
[IL] Epoch 71/100, Loss: 0.0049, Val Loss: 0.0089
[IL] Epoch 72/100, Loss: 0.0054, Val Loss: 0.0151
[IL] Epoch 73/100, Loss: 0.0058, Val Loss: 0.0096
[IL] Epoch 74/100, Loss: 0.0049, Val Loss: 0.0080
[IL] Epoch 75/100, Loss: 0.0053, Val Loss: 0.0086
[IL] Epoch 76/100, Loss: 0.0056, Val Loss: 0.0115
[IL] Epoch 77/100, Loss: 0.0047, Val Loss: 0.0112
[IL] Epoch 78/100, Loss: 0.0050, Val Loss: 0.0111
[IL] Epoch 79/100, Loss: 0.0051, Val Loss: 0.0094
[IL] Epoch 80/100, Loss: 0.0055, Val Loss: 0.0092
[IL] Epoch 81/100, Loss: 0.0052, Val Loss: 0.0090
[IL] Epoch 82/100, Loss: 0.0048, Val Loss: 0.0080
[IL] Epoch 83/100, Loss: 0.0054, Val Loss: 0.0094
[IL] Epoch 84/100, Loss: 0.0048, Val Loss: 0.0113
[IL] Epoch 85/100, Loss: 0.0047, Val Loss: 0.0087
[IL] Epoch 86/100, Loss: 0.0050, Val Loss: 0.0084
[IL] Epoch 87/100, Loss: 0.0050, Val Loss: 0.0132
[IL] Epoch 88/100, Loss: 0.0052, Val Loss: 0.0092
[IL] Epoch 89/100, Loss: 0.0045, Val Loss: 0.0074
[IL] Epoch 90/100, Loss: 0.0048, Val Loss: 0.0136
[IL] Epoch 91/100, Loss: 0.0053, Val Loss: 0.0074
[IL] Epoch 92/100, Loss: 0.0048, Val Loss: 0.0120
[IL] Epoch 93/100, Loss: 0.0053, Val Loss: 0.0109
[IL] Epoch 94/100, Loss: 0.0051, Val Loss: 0.0081
[IL] Epoch 95/100, Loss: 0.0048, Val Loss: 0.0100
[IL] Epoch 96/100, Loss: 0.0048, Val Loss: 0.0100
[IL] Epoch 97/100, Loss: 0.0047, Val Loss: 0.0091
[IL] Epoch 98/100, Loss: 0.0047, Val Loss: 0.0109
[IL] Epoch 99/100, Loss: 0.0044, Val Loss: 0.0090
test_mean_score: 0.77
[IL] Eval - Success Rate: 0.770
[Plot] Saved: /nfs_global/S/yangrongzheng/RL100/3D-Diffusion-Policy/3D-Diffusion-Policy/plots/il_loss_retrain_iter_00.png
[Checkpoint] Saved to /nfs_global/S/yangrongzheng/RL100/3D-Diffusion-Policy/3D-Diffusion-Policy/checkpoints/offline_iter_0.ckpt

================================================================================
               OFFLINE RL ITERATION 2/10
================================================================================


[RL100Trainer] Line 6 — Training Transition Model T_θ (Iteration 1)

[TransitionModel] Encoding dataset for transition model training...
[TransitionModel] Dataset: 19686 samples, input_dim=288, target_dim=257
[TransitionModel] Epoch    0 | train=-54.40700 | val=0.00034 | no-improve=0/5
[TransitionModel] Epoch   20 | train=-69.50238 | val=0.00020 | no-improve=0/5
[TransitionModel] Epoch   40 | train=-73.56060 | val=0.00019 | no-improve=4/5
[TransitionModel] Epoch   60 | train=-77.81695 | val=0.00020 | no-improve=3/5
[TransitionModel] Epoch   62 | train=-78.16358 | val=0.00020 | no-improve=5/5
[TransitionModel] Training complete. Elites=[4, 5, 2, 3, 0], val_loss=0.00018

[RL100Trainer] Phase 2a: Training IQL Critics (Iteration 1)
[IQL] Epoch 0/20, V Loss: 0.0002, Q Loss: 0.0074
[IQL] Epoch 1/20, V Loss: 0.0001, Q Loss: 0.0073
[IQL] Epoch 2/20, V Loss: 0.0002, Q Loss: 0.0074
[IQL] Epoch 3/20, V Loss: 0.0001, Q Loss: 0.0072
[IQL] Epoch 4/20, V Loss: 0.0001, Q Loss: 0.0071
[IQL] Epoch 5/20, V Loss: 0.0002, Q Loss: 0.0072
[IQL] Epoch 6/20, V Loss: 0.0003, Q Loss: 0.0071
[IQL] Epoch 7/20, V Loss: 0.0002, Q Loss: 0.0070
[IQL] Epoch 8/20, V Loss: 0.0002, Q Loss: 0.0070
[IQL] Epoch 9/20, V Loss: 0.0002, Q Loss: 0.0068
[IQL] Epoch 10/20, V Loss: 0.0002, Q Loss: 0.0069
[IQL] Epoch 11/20, V Loss: 0.0002, Q Loss: 0.0068
[IQL] Epoch 12/20, V Loss: 0.0002, Q Loss: 0.0068
[IQL] Epoch 13/20, V Loss: 0.0002, Q Loss: 0.0067
[IQL] Epoch 14/20, V Loss: 0.0002, Q Loss: 0.0066
[IQL] Epoch 15/20, V Loss: 0.0002, Q Loss: 0.0065
[IQL] Epoch 16/20, V Loss: 0.0003, Q Loss: 0.0065
[IQL] Epoch 17/20, V Loss: 0.0002, Q Loss: 0.0066
[IQL] Epoch 18/20, V Loss: 0.0002, Q Loss: 0.0065
[IQL] Epoch 19/20, V Loss: 0.0002, Q Loss: 0.0063
[Plot] Saved: /nfs_global/S/yangrongzheng/RL100/3D-Diffusion-Policy/3D-Diffusion-Policy/plots/iql_q_loss_iter_01.png
[Plot] Saved: /nfs_global/S/yangrongzheng/RL100/3D-Diffusion-Policy/3D-Diffusion-Policy/plots/iql_v_loss_iter_01.png

[RL100Trainer] Phase 2b: Offline RL Optimization (Iteration 1)
[OPE] Behavior policy value J_old = 0.4618
[RL PPO] Reducing policy LR: 1.00e-04 → 1.00e-05
[Offline RL] Epoch 0/20, PPO Loss: -0.0201, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 14.5387, Reg Loss: 0.0000, CD Loss: 0.2909
[Offline RL] Epoch 1/20, PPO Loss: -0.0196, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 13.2631, Reg Loss: 0.0000, CD Loss: 0.0697
[Offline RL] Epoch 2/20, PPO Loss: -0.0176, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 13.3326, Reg Loss: 0.0000, CD Loss: 0.0552
[Offline RL] Epoch 3/20, PPO Loss: -0.0175, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 12.9740, Reg Loss: 0.0000, CD Loss: 0.0450
[Offline RL] Epoch 4/20, PPO Loss: -0.0176, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 12.9712, Reg Loss: 0.0000, CD Loss: 0.0356
[Offline RL] Epoch 5/20, PPO Loss: -0.0180, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 12.8625, Reg Loss: 0.0000, CD Loss: 0.0271
[Offline RL] Epoch 6/20, PPO Loss: -0.0174, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 13.3354, Reg Loss: 0.0000, CD Loss: 0.0216
[Offline RL] Epoch 7/20, PPO Loss: -0.0175, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 12.6877, Reg Loss: 0.0000, CD Loss: 0.0187
[Offline RL] Epoch 8/20, PPO Loss: -0.0173, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 13.1295, Reg Loss: 0.0000, CD Loss: 0.0170
[Offline RL] Epoch 9/20, PPO Loss: -0.0172, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 12.5665, Reg Loss: 0.0000, CD Loss: 0.0161
[Offline RL] Epoch 10/20, PPO Loss: -0.0167, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 13.4889, Reg Loss: 0.0000, CD Loss: 0.0153
[Offline RL] Epoch 11/20, PPO Loss: -0.0171, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 12.6991, Reg Loss: 0.0000, CD Loss: 0.0140
[Offline RL] Epoch 12/20, PPO Loss: -0.0168, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 12.8700, Reg Loss: 0.0000, CD Loss: 0.0145
[Offline RL] Epoch 13/20, PPO Loss: -0.0163, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 13.0511, Reg Loss: 0.0000, CD Loss: 0.0137
[Offline RL] Epoch 14/20, PPO Loss: -0.0164, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 13.1771, Reg Loss: 0.0000, CD Loss: 0.0131
[Offline RL] Epoch 15/20, PPO Loss: -0.0163, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 13.4048, Reg Loss: 0.0000, CD Loss: 0.0128
[Offline RL] Epoch 16/20, PPO Loss: -0.0164, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 13.3416, Reg Loss: 0.0000, CD Loss: 0.0124
[Offline RL] Epoch 17/20, PPO Loss: -0.0167, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 13.0588, Reg Loss: 0.0000, CD Loss: 0.0123
[Offline RL] Epoch 18/20, PPO Loss: -0.0163, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 13.5493, Reg Loss: 0.0000, CD Loss: 0.0122
[Offline RL] Epoch 19/20, PPO Loss: -0.0166, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 13.4542, Reg Loss: 0.0000, CD Loss: 0.0125
[Plot] Saved: /nfs_global/S/yangrongzheng/RL100/3D-Diffusion-Policy/3D-Diffusion-Policy/plots/ppo_loss_iter_01.png
[OPE] Policy REJECTED: J_new=0.4559 ≤ J_old=0.4618 + δ=0.0231. Rolling back to behavior policy.

[RL100Trainer] Phase 2c: Collecting New Data (Iteration 1)
[Collect] 20 episodes, success=0.600, env_return=1053.61, rl_reward=0.60, steps=4000
[Data Collection] Success Rate: 0.600, EnvReturn: 1053.61, RLReward: 0.60, Episodes: 20, Steps: 4000
[Dataset] offline collection: keeping 12/20 successful episodes (dropped 8 failures) before merge.
[Dataset] Merged 12 episodes (2400 steps) → total 24800 steps, 124 episodes

[RL100Trainer] Retraining IL on merged dataset...

============================================================
[RL100Trainer] Phase 1: Imitation Learning
============================================================

[IL] Epoch 0/100, Loss: 0.0129, Val Loss: 0.0065
[IL] Epoch 1/100, Loss: 0.0073, Val Loss: 0.0083
[IL] Epoch 2/100, Loss: 0.0074, Val Loss: 0.0088
[IL] Epoch 3/100, Loss: 0.0068, Val Loss: 0.0087
[IL] Epoch 4/100, Loss: 0.0071, Val Loss: 0.0066
[IL] Epoch 5/100, Loss: 0.0067, Val Loss: 0.0112
[IL] Epoch 6/100, Loss: 0.0067, Val Loss: 0.0064
[IL] Epoch 7/100, Loss: 0.0068, Val Loss: 0.0067
[IL] Epoch 8/100, Loss: 0.0064, Val Loss: 0.0082
[IL] Epoch 9/100, Loss: 0.0064, Val Loss: 0.0104
[IL] Epoch 10/100, Loss: 0.0062, Val Loss: 0.0098
[IL] Epoch 11/100, Loss: 0.0065, Val Loss: 0.0057
[IL] Epoch 12/100, Loss: 0.0062, Val Loss: 0.0082
[IL] Epoch 13/100, Loss: 0.0060, Val Loss: 0.0082
[IL] Epoch 14/100, Loss: 0.0063, Val Loss: 0.0142
[IL] Epoch 15/100, Loss: 0.0067, Val Loss: 0.0061
[IL] Epoch 16/100, Loss: 0.0061, Val Loss: 0.0102
[IL] Epoch 17/100, Loss: 0.0061, Val Loss: 0.0096
[IL] Epoch 18/100, Loss: 0.0054, Val Loss: 0.0071
[IL] Epoch 19/100, Loss: 0.0062, Val Loss: 0.0087
[IL] Epoch 20/100, Loss: 0.0063, Val Loss: 0.0133
[IL] Epoch 21/100, Loss: 0.0064, Val Loss: 0.0097
[IL] Epoch 22/100, Loss: 0.0058, Val Loss: 0.0090
[IL] Epoch 23/100, Loss: 0.0059, Val Loss: 0.0065
[IL] Epoch 24/100, Loss: 0.0053, Val Loss: 0.0090
[IL] Epoch 25/100, Loss: 0.0061, Val Loss: 0.0085
[IL] Epoch 26/100, Loss: 0.0055, Val Loss: 0.0081
[IL] Epoch 27/100, Loss: 0.0055, Val Loss: 0.0087
[IL] Epoch 28/100, Loss: 0.0060, Val Loss: 0.0109
[IL] Epoch 29/100, Loss: 0.0056, Val Loss: 0.0094
[IL] Epoch 30/100, Loss: 0.0055, Val Loss: 0.0096
[IL] Epoch 31/100, Loss: 0.0053, Val Loss: 0.0099
[IL] Epoch 32/100, Loss: 0.0051, Val Loss: 0.0067
[IL] Epoch 33/100, Loss: 0.0057, Val Loss: 0.0094
[IL] Epoch 34/100, Loss: 0.0054, Val Loss: 0.0100
[IL] Epoch 35/100, Loss: 0.0055, Val Loss: 0.0063
[IL] Epoch 36/100, Loss: 0.0055, Val Loss: 0.0074
[IL] Epoch 37/100, Loss: 0.0052, Val Loss: 0.0114
[IL] Epoch 38/100, Loss: 0.0054, Val Loss: 0.0096
[IL] Epoch 39/100, Loss: 0.0055, Val Loss: 0.0091
[IL] Epoch 40/100, Loss: 0.0051, Val Loss: 0.0132
[IL] Epoch 41/100, Loss: 0.0054, Val Loss: 0.0104
[IL] Epoch 42/100, Loss: 0.0055, Val Loss: 0.0075
[IL] Epoch 43/100, Loss: 0.0048, Val Loss: 0.0112
[IL] Epoch 44/100, Loss: 0.0053, Val Loss: 0.0093
[IL] Epoch 45/100, Loss: 0.0060, Val Loss: 0.0124
[IL] Epoch 46/100, Loss: 0.0059, Val Loss: 0.0124
[IL] Epoch 47/100, Loss: 0.0052, Val Loss: 0.0102
[IL] Epoch 48/100, Loss: 0.0052, Val Loss: 0.0096
[IL] Epoch 49/100, Loss: 0.0055, Val Loss: 0.0088
[IL] Epoch 50/100, Loss: 0.0054, Val Loss: 0.0082
[IL] Epoch 51/100, Loss: 0.0051, Val Loss: 0.0075
[IL] Epoch 52/100, Loss: 0.0052, Val Loss: 0.0087
[IL] Epoch 53/100, Loss: 0.0051, Val Loss: 0.0111
[IL] Epoch 54/100, Loss: 0.0056, Val Loss: 0.0071
[IL] Epoch 55/100, Loss: 0.0050, Val Loss: 0.0114
[IL] Epoch 56/100, Loss: 0.0052, Val Loss: 0.0113
[IL] Epoch 57/100, Loss: 0.0048, Val Loss: 0.0117
[IL] Epoch 58/100, Loss: 0.0051, Val Loss: 0.0086
[IL] Epoch 59/100, Loss: 0.0050, Val Loss: 0.0102
[IL] Epoch 60/100, Loss: 0.0050, Val Loss: 0.0130
[IL] Epoch 61/100, Loss: 0.0047, Val Loss: 0.0115
[IL] Epoch 62/100, Loss: 0.0050, Val Loss: 0.0088
[IL] Epoch 63/100, Loss: 0.0050, Val Loss: 0.0088
[IL] Epoch 64/100, Loss: 0.0050, Val Loss: 0.0071
[IL] Epoch 65/100, Loss: 0.0049, Val Loss: 0.0127
[IL] Epoch 66/100, Loss: 0.0054, Val Loss: 0.0070
[IL] Epoch 67/100, Loss: 0.0051, Val Loss: 0.0077
[IL] Epoch 68/100, Loss: 0.0051, Val Loss: 0.0120
[IL] Epoch 69/100, Loss: 0.0050, Val Loss: 0.0113
[IL] Epoch 70/100, Loss: 0.0051, Val Loss: 0.0094
[IL] Epoch 71/100, Loss: 0.0050, Val Loss: 0.0071
[IL] Epoch 72/100, Loss: 0.0046, Val Loss: 0.0082
[IL] Epoch 73/100, Loss: 0.0047, Val Loss: 0.0128
[IL] Epoch 74/100, Loss: 0.0049, Val Loss: 0.0185
[IL] Epoch 75/100, Loss: 0.0049, Val Loss: 0.0144
[IL] Epoch 76/100, Loss: 0.0048, Val Loss: 0.0125
[IL] Epoch 77/100, Loss: 0.0049, Val Loss: 0.0108
[IL] Epoch 78/100, Loss: 0.0047, Val Loss: 0.0073
[IL] Epoch 79/100, Loss: 0.0046, Val Loss: 0.0120
[IL] Epoch 80/100, Loss: 0.0043, Val Loss: 0.0088
[IL] Epoch 81/100, Loss: 0.0045, Val Loss: 0.0113
[IL] Epoch 82/100, Loss: 0.0043, Val Loss: 0.0091
[IL] Epoch 83/100, Loss: 0.0046, Val Loss: 0.0089
[IL] Epoch 84/100, Loss: 0.0052, Val Loss: 0.0077
[IL] Epoch 85/100, Loss: 0.0045, Val Loss: 0.0113
[IL] Epoch 86/100, Loss: 0.0046, Val Loss: 0.0086
[IL] Epoch 87/100, Loss: 0.0045, Val Loss: 0.0123
[IL] Epoch 88/100, Loss: 0.0044, Val Loss: 0.0101
[IL] Epoch 89/100, Loss: 0.0047, Val Loss: 0.0056
[IL] Epoch 90/100, Loss: 0.0051, Val Loss: 0.0111
[IL] Epoch 91/100, Loss: 0.0047, Val Loss: 0.0134
[IL] Epoch 92/100, Loss: 0.0055, Val Loss: 0.0092
[IL] Epoch 93/100, Loss: 0.0047, Val Loss: 0.0128
[IL] Epoch 94/100, Loss: 0.0049, Val Loss: 0.0089
[IL] Epoch 95/100, Loss: 0.0044, Val Loss: 0.0081
[IL] Epoch 96/100, Loss: 0.0047, Val Loss: 0.0139
[IL] Epoch 97/100, Loss: 0.0046, Val Loss: 0.0144
[IL] Epoch 98/100, Loss: 0.0044, Val Loss: 0.0137
[IL] Epoch 99/100, Loss: 0.0045, Val Loss: 0.0127
test_mean_score: 0.72
[IL] Eval - Success Rate: 0.720
[Plot] Saved: /nfs_global/S/yangrongzheng/RL100/3D-Diffusion-Policy/3D-Diffusion-Policy/plots/il_loss_retrain_iter_01.png
[Checkpoint] Saved to /nfs_global/S/yangrongzheng/RL100/3D-Diffusion-Policy/3D-Diffusion-Policy/checkpoints/offline_iter_1.ckpt

================================================================================
               OFFLINE RL ITERATION 3/10
================================================================================


[RL100Trainer] Line 6 — Training Transition Model T_θ (Iteration 2)

[TransitionModel] Encoding dataset for transition model training...
[TransitionModel] Dataset: 22002 samples, input_dim=288, target_dim=257
[TransitionModel] Epoch    0 | train=-64.94358 | val=0.00038 | no-improve=0/5
[TransitionModel] Epoch   20 | train=-80.26637 | val=0.00025 | no-improve=0/5
[TransitionModel] Epoch   27 | train=-82.02944 | val=0.00027 | no-improve=5/5
[TransitionModel] Training complete. Elites=[4, 0, 5, 1, 6], val_loss=0.00023

[RL100Trainer] Phase 2a: Training IQL Critics (Iteration 2)
[IQL] Epoch 0/20, V Loss: 0.0002, Q Loss: 0.0063
[IQL] Epoch 1/20, V Loss: 0.0002, Q Loss: 0.0064
[IQL] Epoch 2/20, V Loss: 0.0002, Q Loss: 0.0063
[IQL] Epoch 3/20, V Loss: 0.0003, Q Loss: 0.0064
[IQL] Epoch 4/20, V Loss: 0.0003, Q Loss: 0.0063
[IQL] Epoch 5/20, V Loss: 0.0003, Q Loss: 0.0064
[IQL] Epoch 6/20, V Loss: 0.0002, Q Loss: 0.0061
[IQL] Epoch 7/20, V Loss: 0.0002, Q Loss: 0.0061
[IQL] Epoch 8/20, V Loss: 0.0003, Q Loss: 0.0061
[IQL] Epoch 9/20, V Loss: 0.0003, Q Loss: 0.0061
[IQL] Epoch 10/20, V Loss: 0.0002, Q Loss: 0.0060
[IQL] Epoch 11/20, V Loss: 0.0003, Q Loss: 0.0061
[IQL] Epoch 12/20, V Loss: 0.0002, Q Loss: 0.0058
[IQL] Epoch 13/20, V Loss: 0.0002, Q Loss: 0.0058
[IQL] Epoch 14/20, V Loss: 0.0002, Q Loss: 0.0059
[IQL] Epoch 15/20, V Loss: 0.0002, Q Loss: 0.0059
[IQL] Epoch 16/20, V Loss: 0.0002, Q Loss: 0.0058
[IQL] Epoch 17/20, V Loss: 0.0003, Q Loss: 0.0058
[IQL] Epoch 18/20, V Loss: 0.0002, Q Loss: 0.0057
[IQL] Epoch 19/20, V Loss: 0.0003, Q Loss: 0.0059
[Plot] Saved: /nfs_global/S/yangrongzheng/RL100/3D-Diffusion-Policy/3D-Diffusion-Policy/plots/iql_q_loss_iter_02.png
[Plot] Saved: /nfs_global/S/yangrongzheng/RL100/3D-Diffusion-Policy/3D-Diffusion-Policy/plots/iql_v_loss_iter_02.png

[RL100Trainer] Phase 2b: Offline RL Optimization (Iteration 2)
[OPE] Behavior policy value J_old = 0.6123
[RL PPO] Reducing policy LR: 1.00e-04 → 1.00e-05
[Offline RL] Epoch 0/20, PPO Loss: -0.0214, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 13.5506, Reg Loss: 0.0000, CD Loss: 0.2649
[Offline RL] Epoch 1/20, PPO Loss: -0.0197, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 12.4479, Reg Loss: 0.0000, CD Loss: 0.0662
[Offline RL] Epoch 2/20, PPO Loss: -0.0178, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 12.7225, Reg Loss: 0.0000, CD Loss: 0.0528
[Offline RL] Epoch 3/20, PPO Loss: -0.0176, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 12.9780, Reg Loss: 0.0000, CD Loss: 0.0421
[Offline RL] Epoch 4/20, PPO Loss: -0.0167, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 13.4841, Reg Loss: 0.0000, CD Loss: 0.0331
[Offline RL] Epoch 5/20, PPO Loss: -0.0171, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 13.1773, Reg Loss: 0.0000, CD Loss: 0.0262
[Offline RL] Epoch 6/20, PPO Loss: -0.0166, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 13.4430, Reg Loss: 0.0000, CD Loss: 0.0219
[Offline RL] Epoch 7/20, PPO Loss: -0.0167, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 13.5920, Reg Loss: 0.0000, CD Loss: 0.0197
[Offline RL] Epoch 8/20, PPO Loss: -0.0166, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 13.4130, Reg Loss: 0.0000, CD Loss: 0.0181
[Offline RL] Epoch 9/20, PPO Loss: -0.0163, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 13.2946, Reg Loss: 0.0000, CD Loss: 0.0168
[Offline RL] Epoch 10/20, PPO Loss: -0.0163, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 13.5109, Reg Loss: 0.0000, CD Loss: 0.0164
[Offline RL] Epoch 11/20, PPO Loss: -0.0165, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 13.7882, Reg Loss: 0.0000, CD Loss: 0.0160
[Offline RL] Epoch 12/20, PPO Loss: -0.0164, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 13.4893, Reg Loss: 0.0000, CD Loss: 0.0149
[Offline RL] Epoch 13/20, PPO Loss: -0.0164, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 13.8995, Reg Loss: 0.0000, CD Loss: 0.0144
[Offline RL] Epoch 14/20, PPO Loss: -0.0161, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 14.2111, Reg Loss: 0.0000, CD Loss: 0.0147
[Offline RL] Epoch 15/20, PPO Loss: -0.0162, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 13.4149, Reg Loss: 0.0000, CD Loss: 0.0150
[Offline RL] Epoch 16/20, PPO Loss: -0.0158, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 13.5482, Reg Loss: 0.0000, CD Loss: 0.0150
[Offline RL] Epoch 17/20, PPO Loss: -0.0157, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 14.0854, Reg Loss: 0.0000, CD Loss: 0.0152
[Offline RL] Epoch 18/20, PPO Loss: -0.0155, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 13.9343, Reg Loss: 0.0000, CD Loss: 0.0157
[Offline RL] Epoch 19/20, PPO Loss: -0.0160, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 13.8176, Reg Loss: 0.0000, CD Loss: 0.0165
[Plot] Saved: /nfs_global/S/yangrongzheng/RL100/3D-Diffusion-Policy/3D-Diffusion-Policy/plots/ppo_loss_iter_02.png
[OPE] Policy REJECTED: J_new=0.6134 ≤ J_old=0.6123 + δ=0.0306. Rolling back to behavior policy.

[RL100Trainer] Phase 2c: Collecting New Data (Iteration 2)
[Collect] 20 episodes, success=0.850, env_return=1048.69, rl_reward=0.85, steps=4000
[Data Collection] Success Rate: 0.850, EnvReturn: 1048.69, RLReward: 0.85, Episodes: 20, Steps: 4000
[Dataset] offline collection: keeping 17/20 successful episodes (dropped 3 failures) before merge.
[Dataset] Merged 17 episodes (3400 steps) → total 28200 steps, 141 episodes

[RL100Trainer] Retraining IL on merged dataset...

============================================================
[RL100Trainer] Phase 1: Imitation Learning
============================================================

[IL] Epoch 0/100, Loss: 0.0084, Val Loss: 0.0066
[IL] Epoch 1/100, Loss: 0.0068, Val Loss: 0.0139
[IL] Epoch 2/100, Loss: 0.0071, Val Loss: 0.0123
[IL] Epoch 3/100, Loss: 0.0066, Val Loss: 0.0125
[IL] Epoch 4/100, Loss: 0.0064, Val Loss: 0.0132
[IL] Epoch 5/100, Loss: 0.0062, Val Loss: 0.0085
[IL] Epoch 6/100, Loss: 0.0062, Val Loss: 0.0170
[IL] Epoch 7/100, Loss: 0.0056, Val Loss: 0.0088
[IL] Epoch 8/100, Loss: 0.0057, Val Loss: 0.0098
[IL] Epoch 9/100, Loss: 0.0056, Val Loss: 0.0100
[IL] Epoch 10/100, Loss: 0.0057, Val Loss: 0.0110
[IL] Epoch 11/100, Loss: 0.0058, Val Loss: 0.0102
[IL] Epoch 12/100, Loss: 0.0061, Val Loss: 0.0109
[IL] Epoch 13/100, Loss: 0.0059, Val Loss: 0.0124
[IL] Epoch 14/100, Loss: 0.0056, Val Loss: 0.0107
[IL] Epoch 15/100, Loss: 0.0060, Val Loss: 0.0105
[IL] Epoch 16/100, Loss: 0.0058, Val Loss: 0.0139
[IL] Epoch 17/100, Loss: 0.0052, Val Loss: 0.0111
[IL] Epoch 18/100, Loss: 0.0060, Val Loss: 0.0078
[IL] Epoch 19/100, Loss: 0.0059, Val Loss: 0.0112
[IL] Epoch 20/100, Loss: 0.0059, Val Loss: 0.0104
[IL] Epoch 21/100, Loss: 0.0055, Val Loss: 0.0092
[IL] Epoch 22/100, Loss: 0.0055, Val Loss: 0.0117
[IL] Epoch 23/100, Loss: 0.0059, Val Loss: 0.0086
[IL] Epoch 24/100, Loss: 0.0055, Val Loss: 0.0105
[IL] Epoch 25/100, Loss: 0.0059, Val Loss: 0.0101
[IL] Epoch 26/100, Loss: 0.0055, Val Loss: 0.0081
[IL] Epoch 27/100, Loss: 0.0057, Val Loss: 0.0089
[IL] Epoch 28/100, Loss: 0.0058, Val Loss: 0.0098
[IL] Epoch 29/100, Loss: 0.0056, Val Loss: 0.0088
[IL] Epoch 30/100, Loss: 0.0056, Val Loss: 0.0099
[IL] Epoch 31/100, Loss: 0.0052, Val Loss: 0.0097
[IL] Epoch 32/100, Loss: 0.0055, Val Loss: 0.0105
[IL] Epoch 33/100, Loss: 0.0051, Val Loss: 0.0125
[IL] Epoch 34/100, Loss: 0.0049, Val Loss: 0.0093
[IL] Epoch 35/100, Loss: 0.0049, Val Loss: 0.0108
[IL] Epoch 36/100, Loss: 0.0055, Val Loss: 0.0075
[IL] Epoch 37/100, Loss: 0.0048, Val Loss: 0.0094
[IL] Epoch 38/100, Loss: 0.0050, Val Loss: 0.0086
[IL] Epoch 39/100, Loss: 0.0051, Val Loss: 0.0168
[IL] Epoch 40/100, Loss: 0.0053, Val Loss: 0.0110
[IL] Epoch 41/100, Loss: 0.0050, Val Loss: 0.0091
[IL] Epoch 42/100, Loss: 0.0050, Val Loss: 0.0099
[IL] Epoch 43/100, Loss: 0.0051, Val Loss: 0.0111
[IL] Epoch 44/100, Loss: 0.0052, Val Loss: 0.0116
[IL] Epoch 45/100, Loss: 0.0050, Val Loss: 0.0143
[IL] Epoch 46/100, Loss: 0.0052, Val Loss: 0.0132
[IL] Epoch 47/100, Loss: 0.0054, Val Loss: 0.0126
[IL] Epoch 48/100, Loss: 0.0054, Val Loss: 0.0083
[IL] Epoch 49/100, Loss: 0.0050, Val Loss: 0.0101
[IL] Epoch 50/100, Loss: 0.0053, Val Loss: 0.0099
[IL] Epoch 51/100, Loss: 0.0052, Val Loss: 0.0067
[IL] Epoch 52/100, Loss: 0.0052, Val Loss: 0.0119
[IL] Epoch 53/100, Loss: 0.0054, Val Loss: 0.0077
[IL] Epoch 54/100, Loss: 0.0051, Val Loss: 0.0083
[IL] Epoch 55/100, Loss: 0.0052, Val Loss: 0.0088
[IL] Epoch 56/100, Loss: 0.0047, Val Loss: 0.0144
[IL] Epoch 57/100, Loss: 0.0053, Val Loss: 0.0170
[IL] Epoch 58/100, Loss: 0.0048, Val Loss: 0.0107
[IL] Epoch 59/100, Loss: 0.0049, Val Loss: 0.0175
[IL] Epoch 60/100, Loss: 0.0051, Val Loss: 0.0137
[IL] Epoch 61/100, Loss: 0.0047, Val Loss: 0.0073
[IL] Epoch 62/100, Loss: 0.0052, Val Loss: 0.0118
[IL] Epoch 63/100, Loss: 0.0044, Val Loss: 0.0084
[IL] Epoch 64/100, Loss: 0.0049, Val Loss: 0.0126
[IL] Epoch 65/100, Loss: 0.0052, Val Loss: 0.0152
[IL] Epoch 66/100, Loss: 0.0049, Val Loss: 0.0101
[IL] Epoch 67/100, Loss: 0.0049, Val Loss: 0.0116
[IL] Epoch 68/100, Loss: 0.0046, Val Loss: 0.0109
[IL] Epoch 69/100, Loss: 0.0053, Val Loss: 0.0109
[IL] Epoch 70/100, Loss: 0.0046, Val Loss: 0.0122
[IL] Epoch 71/100, Loss: 0.0046, Val Loss: 0.0122
[IL] Epoch 72/100, Loss: 0.0045, Val Loss: 0.0125
[IL] Epoch 73/100, Loss: 0.0046, Val Loss: 0.0157
[IL] Epoch 74/100, Loss: 0.0044, Val Loss: 0.0154
[IL] Epoch 75/100, Loss: 0.0047, Val Loss: 0.0150
[IL] Epoch 76/100, Loss: 0.0046, Val Loss: 0.0127
[IL] Epoch 77/100, Loss: 0.0047, Val Loss: 0.0125
[IL] Epoch 78/100, Loss: 0.0044, Val Loss: 0.0113
[IL] Epoch 79/100, Loss: 0.0044, Val Loss: 0.0124
[IL] Epoch 80/100, Loss: 0.0044, Val Loss: 0.0124
[IL] Epoch 81/100, Loss: 0.0051, Val Loss: 0.0093
[IL] Epoch 82/100, Loss: 0.0045, Val Loss: 0.0140
[IL] Epoch 83/100, Loss: 0.0051, Val Loss: 0.0133
[IL] Epoch 84/100, Loss: 0.0048, Val Loss: 0.0183
[IL] Epoch 85/100, Loss: 0.0045, Val Loss: 0.0120
[IL] Epoch 86/100, Loss: 0.0048, Val Loss: 0.0087
[IL] Epoch 87/100, Loss: 0.0045, Val Loss: 0.0117
[IL] Epoch 88/100, Loss: 0.0044, Val Loss: 0.0172
[IL] Epoch 89/100, Loss: 0.0046, Val Loss: 0.0148
[IL] Epoch 90/100, Loss: 0.0045, Val Loss: 0.0071
[IL] Epoch 91/100, Loss: 0.0049, Val Loss: 0.0091
[IL] Epoch 92/100, Loss: 0.0044, Val Loss: 0.0111
[IL] Epoch 93/100, Loss: 0.0040, Val Loss: 0.0087
[IL] Epoch 94/100, Loss: 0.0044, Val Loss: 0.0097
[IL] Epoch 95/100, Loss: 0.0050, Val Loss: 0.0108
[IL] Epoch 96/100, Loss: 0.0046, Val Loss: 0.0120
[IL] Epoch 97/100, Loss: 0.0046, Val Loss: 0.0140
[IL] Epoch 98/100, Loss: 0.0045, Val Loss: 0.0116
[IL] Epoch 99/100, Loss: 0.0045, Val Loss: 0.0118
test_mean_score: 0.74
[IL] Eval - Success Rate: 0.740
[Plot] Saved: /nfs_global/S/yangrongzheng/RL100/3D-Diffusion-Policy/3D-Diffusion-Policy/plots/il_loss_retrain_iter_02.png
[Checkpoint] Saved to /nfs_global/S/yangrongzheng/RL100/3D-Diffusion-Policy/3D-Diffusion-Policy/checkpoints/offline_iter_2.ckpt

================================================================================
               OFFLINE RL ITERATION 4/10
================================================================================


[RL100Trainer] Line 6 — Training Transition Model T_θ (Iteration 3)

[TransitionModel] Encoding dataset for transition model training...
[TransitionModel] Dataset: 25283 samples, input_dim=288, target_dim=257
[TransitionModel] Epoch    0 | train=-76.21794 | val=0.00027 | no-improve=0/5
[TransitionModel] Epoch   20 | train=-86.38890 | val=0.00021 | no-improve=0/5
[TransitionModel] Epoch   26 | train=-88.15170 | val=0.00021 | no-improve=5/5
[TransitionModel] Training complete. Elites=[6, 5, 3, 0, 1], val_loss=0.00020

[RL100Trainer] Phase 2a: Training IQL Critics (Iteration 3)
[IQL] Epoch 0/20, V Loss: 0.0002, Q Loss: 0.0057
[IQL] Epoch 1/20, V Loss: 0.0003, Q Loss: 0.0058
[IQL] Epoch 2/20, V Loss: 0.0003, Q Loss: 0.0057
[IQL] Epoch 3/20, V Loss: 0.0002, Q Loss: 0.0056
[IQL] Epoch 4/20, V Loss: 0.0002, Q Loss: 0.0057
[IQL] Epoch 5/20, V Loss: 0.0003, Q Loss: 0.0056
[IQL] Epoch 6/20, V Loss: 0.0002, Q Loss: 0.0056
[IQL] Epoch 7/20, V Loss: 0.0003, Q Loss: 0.0056
[IQL] Epoch 8/20, V Loss: 0.0002, Q Loss: 0.0055
[IQL] Epoch 9/20, V Loss: 0.0002, Q Loss: 0.0055
[IQL] Epoch 10/20, V Loss: 0.0003, Q Loss: 0.0054
[IQL] Epoch 11/20, V Loss: 0.0002, Q Loss: 0.0054
[IQL] Epoch 12/20, V Loss: 0.0002, Q Loss: 0.0055
[IQL] Epoch 13/20, V Loss: 0.0002, Q Loss: 0.0055
[IQL] Epoch 14/20, V Loss: 0.0002, Q Loss: 0.0054
[IQL] Epoch 15/20, V Loss: 0.0002, Q Loss: 0.0054
[IQL] Epoch 16/20, V Loss: 0.0003, Q Loss: 0.0054
[IQL] Epoch 17/20, V Loss: 0.0003, Q Loss: 0.0054
[IQL] Epoch 18/20, V Loss: 0.0002, Q Loss: 0.0055
[IQL] Epoch 19/20, V Loss: 0.0002, Q Loss: 0.0055
[Plot] Saved: /nfs_global/S/yangrongzheng/RL100/3D-Diffusion-Policy/3D-Diffusion-Policy/plots/iql_q_loss_iter_03.png
[Plot] Saved: /nfs_global/S/yangrongzheng/RL100/3D-Diffusion-Policy/3D-Diffusion-Policy/plots/iql_v_loss_iter_03.png

[RL100Trainer] Phase 2b: Offline RL Optimization (Iteration 3)
[OPE] Behavior policy value J_old = 0.7043
[RL PPO] Reducing policy LR: 1.00e-04 → 1.00e-05
[Offline RL] Epoch 0/20, PPO Loss: -0.0203, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 12.9970, Reg Loss: 0.0000, CD Loss: 0.2466
[Offline RL] Epoch 1/20, PPO Loss: -0.0184, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 12.4915, Reg Loss: 0.0000, CD Loss: 0.0614
[Offline RL] Epoch 2/20, PPO Loss: -0.0174, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 12.5043, Reg Loss: 0.0000, CD Loss: 0.0473
[Offline RL] Epoch 3/20, PPO Loss: -0.0163, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 12.5953, Reg Loss: 0.0000, CD Loss: 0.0370
[Offline RL] Epoch 4/20, PPO Loss: -0.0159, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 13.1497, Reg Loss: 0.0000, CD Loss: 0.0276
[Offline RL] Epoch 5/20, PPO Loss: -0.0157, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 12.4219, Reg Loss: 0.0000, CD Loss: 0.0224
[Offline RL] Epoch 6/20, PPO Loss: -0.0146, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 12.4852, Reg Loss: 0.0000, CD Loss: 0.0197
[Offline RL] Epoch 7/20, PPO Loss: -0.0137, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 13.1810, Reg Loss: 0.0000, CD Loss: 0.0177
[Offline RL] Epoch 8/20, PPO Loss: -0.0141, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 12.9217, Reg Loss: 0.0000, CD Loss: 0.0158
[Offline RL] Epoch 9/20, PPO Loss: -0.0144, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 12.8012, Reg Loss: 0.0000, CD Loss: 0.0154
[Offline RL] Epoch 10/20, PPO Loss: -0.0139, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 13.3077, Reg Loss: 0.0000, CD Loss: 0.0145
[Offline RL] Epoch 11/20, PPO Loss: -0.0142, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 12.9326, Reg Loss: 0.0000, CD Loss: 0.0153
[Offline RL] Epoch 12/20, PPO Loss: -0.0140, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 13.3209, Reg Loss: 0.0000, CD Loss: 0.0137
[Offline RL] Epoch 13/20, PPO Loss: -0.0138, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 13.1695, Reg Loss: 0.0000, CD Loss: 0.0143
[Offline RL] Epoch 14/20, PPO Loss: -0.0135, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 13.8971, Reg Loss: 0.0000, CD Loss: 0.0150
[Offline RL] Epoch 15/20, PPO Loss: -0.0134, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 13.3504, Reg Loss: 0.0000, CD Loss: 0.0153
[Offline RL] Epoch 16/20, PPO Loss: -0.0134, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 13.3833, Reg Loss: 0.0000, CD Loss: 0.0155
[Offline RL] Epoch 17/20, PPO Loss: -0.0137, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 13.0929, Reg Loss: 0.0000, CD Loss: 0.0162
[Offline RL] Epoch 18/20, PPO Loss: -0.0136, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 13.1145, Reg Loss: 0.0000, CD Loss: 0.0181
[Offline RL] Epoch 19/20, PPO Loss: -0.0131, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 13.1266, Reg Loss: 0.0000, CD Loss: 0.0196
[Plot] Saved: /nfs_global/S/yangrongzheng/RL100/3D-Diffusion-Policy/3D-Diffusion-Policy/plots/ppo_loss_iter_03.png
[OPE] Policy REJECTED: J_new=0.7212 ≤ J_old=0.7043 + δ=0.0352. Rolling back to behavior policy.

[RL100Trainer] Phase 2c: Collecting New Data (Iteration 3)
[Collect] 20 episodes, success=0.850, env_return=813.28, rl_reward=0.85, steps=4000
[Data Collection] Success Rate: 0.850, EnvReturn: 813.28, RLReward: 0.85, Episodes: 20, Steps: 4000
[Dataset] offline collection: keeping 17/20 successful episodes (dropped 3 failures) before merge.
[Dataset] Merged 17 episodes (3400 steps) → total 31600 steps, 158 episodes

[RL100Trainer] Retraining IL on merged dataset...

============================================================
[RL100Trainer] Phase 1: Imitation Learning
============================================================

[IL] Epoch 0/100, Loss: 0.0285, Val Loss: 0.0121
[IL] Epoch 1/100, Loss: 0.0138, Val Loss: 0.0095
[IL] Epoch 2/100, Loss: 0.0120, Val Loss: 0.0101
[IL] Epoch 3/100, Loss: 0.0110, Val Loss: 0.0086
[IL] Epoch 4/100, Loss: 0.0099, Val Loss: 0.0081
[IL] Epoch 5/100, Loss: 0.0095, Val Loss: 0.0069
[IL] Epoch 6/100, Loss: 0.0086, Val Loss: 0.0148
[IL] Epoch 7/100, Loss: 0.0087, Val Loss: 0.0119
[IL] Epoch 8/100, Loss: 0.0086, Val Loss: 0.0082
[IL] Epoch 9/100, Loss: 0.0076, Val Loss: 0.0090
[IL] Epoch 10/100, Loss: 0.0079, Val Loss: 0.0098
[IL] Epoch 11/100, Loss: 0.0078, Val Loss: 0.0109
[IL] Epoch 12/100, Loss: 0.0072, Val Loss: 0.0092
[IL] Epoch 13/100, Loss: 0.0073, Val Loss: 0.0078
[IL] Epoch 14/100, Loss: 0.0075, Val Loss: 0.0111
[IL] Epoch 15/100, Loss: 0.0070, Val Loss: 0.0080
[IL] Epoch 16/100, Loss: 0.0068, Val Loss: 0.0098
[IL] Epoch 17/100, Loss: 0.0067, Val Loss: 0.0076
[IL] Epoch 18/100, Loss: 0.0062, Val Loss: 0.0084
[IL] Epoch 19/100, Loss: 0.0065, Val Loss: 0.0086
[IL] Epoch 20/100, Loss: 0.0068, Val Loss: 0.0105
[IL] Epoch 21/100, Loss: 0.0064, Val Loss: 0.0099
[IL] Epoch 22/100, Loss: 0.0066, Val Loss: 0.0084
[IL] Epoch 23/100, Loss: 0.0065, Val Loss: 0.0096
[IL] Epoch 24/100, Loss: 0.0065, Val Loss: 0.0105
[IL] Epoch 25/100, Loss: 0.0062, Val Loss: 0.0078
[IL] Epoch 26/100, Loss: 0.0063, Val Loss: 0.0093
[IL] Epoch 27/100, Loss: 0.0067, Val Loss: 0.0112
[IL] Epoch 28/100, Loss: 0.0066, Val Loss: 0.0127
[IL] Epoch 29/100, Loss: 0.0067, Val Loss: 0.0085
[IL] Epoch 30/100, Loss: 0.0063, Val Loss: 0.0104
[IL] Epoch 31/100, Loss: 0.0063, Val Loss: 0.0105
[IL] Epoch 32/100, Loss: 0.0061, Val Loss: 0.0117
[IL] Epoch 33/100, Loss: 0.0061, Val Loss: 0.0113
[IL] Epoch 34/100, Loss: 0.0065, Val Loss: 0.0104
[IL] Epoch 35/100, Loss: 0.0061, Val Loss: 0.0076
[IL] Epoch 36/100, Loss: 0.0056, Val Loss: 0.0076
[IL] Epoch 37/100, Loss: 0.0059, Val Loss: 0.0105
[IL] Epoch 38/100, Loss: 0.0062, Val Loss: 0.0091
[IL] Epoch 39/100, Loss: 0.0057, Val Loss: 0.0092
[IL] Epoch 40/100, Loss: 0.0062, Val Loss: 0.0078
[IL] Epoch 41/100, Loss: 0.0059, Val Loss: 0.0083
[IL] Epoch 42/100, Loss: 0.0057, Val Loss: 0.0101
[IL] Epoch 43/100, Loss: 0.0056, Val Loss: 0.0090
[IL] Epoch 44/100, Loss: 0.0059, Val Loss: 0.0107
[IL] Epoch 45/100, Loss: 0.0055, Val Loss: 0.0094
[IL] Epoch 46/100, Loss: 0.0058, Val Loss: 0.0083
[IL] Epoch 47/100, Loss: 0.0058, Val Loss: 0.0082
[IL] Epoch 48/100, Loss: 0.0055, Val Loss: 0.0114
[IL] Epoch 49/100, Loss: 0.0060, Val Loss: 0.0127
[IL] Epoch 50/100, Loss: 0.0054, Val Loss: 0.0082
[IL] Epoch 51/100, Loss: 0.0056, Val Loss: 0.0086
[IL] Epoch 52/100, Loss: 0.0058, Val Loss: 0.0122
[IL] Epoch 53/100, Loss: 0.0054, Val Loss: 0.0084
[IL] Epoch 54/100, Loss: 0.0052, Val Loss: 0.0092
[IL] Epoch 55/100, Loss: 0.0052, Val Loss: 0.0102
[IL] Epoch 56/100, Loss: 0.0054, Val Loss: 0.0087
[IL] Epoch 57/100, Loss: 0.0053, Val Loss: 0.0143
[IL] Epoch 58/100, Loss: 0.0053, Val Loss: 0.0129
[IL] Epoch 59/100, Loss: 0.0050, Val Loss: 0.0080
[IL] Epoch 60/100, Loss: 0.0058, Val Loss: 0.0092
[IL] Epoch 61/100, Loss: 0.0062, Val Loss: 0.0168
[IL] Epoch 62/100, Loss: 0.0057, Val Loss: 0.0088
[IL] Epoch 63/100, Loss: 0.0051, Val Loss: 0.0175
[IL] Epoch 64/100, Loss: 0.0053, Val Loss: 0.0091
[IL] Epoch 65/100, Loss: 0.0058, Val Loss: 0.0118
[IL] Epoch 66/100, Loss: 0.0051, Val Loss: 0.0109
[IL] Epoch 67/100, Loss: 0.0049, Val Loss: 0.0094
[IL] Epoch 68/100, Loss: 0.0048, Val Loss: 0.0117
[IL] Epoch 69/100, Loss: 0.0054, Val Loss: 0.0112
[IL] Epoch 70/100, Loss: 0.0052, Val Loss: 0.0091
[IL] Epoch 71/100, Loss: 0.0052, Val Loss: 0.0079
[IL] Epoch 72/100, Loss: 0.0052, Val Loss: 0.0068
[IL] Epoch 73/100, Loss: 0.0053, Val Loss: 0.0106
[IL] Epoch 74/100, Loss: 0.0051, Val Loss: 0.0100
[IL] Epoch 75/100, Loss: 0.0050, Val Loss: 0.0119
[IL] Epoch 76/100, Loss: 0.0057, Val Loss: 0.0100
[IL] Epoch 77/100, Loss: 0.0049, Val Loss: 0.0109
[IL] Epoch 78/100, Loss: 0.0050, Val Loss: 0.0190
[IL] Epoch 79/100, Loss: 0.0046, Val Loss: 0.0087
[IL] Epoch 80/100, Loss: 0.0056, Val Loss: 0.0079
[IL] Epoch 81/100, Loss: 0.0051, Val Loss: 0.0084
[IL] Epoch 82/100, Loss: 0.0051, Val Loss: 0.0140
[IL] Epoch 83/100, Loss: 0.0047, Val Loss: 0.0116
[IL] Epoch 84/100, Loss: 0.0048, Val Loss: 0.0191
[IL] Epoch 85/100, Loss: 0.0048, Val Loss: 0.0104
[IL] Epoch 86/100, Loss: 0.0048, Val Loss: 0.0073
[IL] Epoch 87/100, Loss: 0.0048, Val Loss: 0.0077
[IL] Epoch 88/100, Loss: 0.0056, Val Loss: 0.0120
[IL] Epoch 89/100, Loss: 0.0052, Val Loss: 0.0109
[IL] Epoch 90/100, Loss: 0.0051, Val Loss: 0.0120
[IL] Epoch 91/100, Loss: 0.0047, Val Loss: 0.0105
[IL] Epoch 92/100, Loss: 0.0048, Val Loss: 0.0105
[IL] Epoch 93/100, Loss: 0.0050, Val Loss: 0.0104
[IL] Epoch 94/100, Loss: 0.0049, Val Loss: 0.0158
[IL] Epoch 95/100, Loss: 0.0051, Val Loss: 0.0145
[IL] Epoch 96/100, Loss: 0.0049, Val Loss: 0.0090
[IL] Epoch 97/100, Loss: 0.0047, Val Loss: 0.0309
[IL] Epoch 98/100, Loss: 0.0048, Val Loss: 0.0086
[IL] Epoch 99/100, Loss: 0.0048, Val Loss: 0.0145
test_mean_score: 0.8
[IL] Eval - Success Rate: 0.800
[Plot] Saved: /nfs_global/S/yangrongzheng/RL100/3D-Diffusion-Policy/3D-Diffusion-Policy/plots/il_loss_retrain_iter_03.png
[Checkpoint] Saved to /nfs_global/S/yangrongzheng/RL100/3D-Diffusion-Policy/3D-Diffusion-Policy/checkpoints/offline_iter_3.ckpt

================================================================================
               OFFLINE RL ITERATION 5/10
================================================================================


[RL100Trainer] Line 6 — Training Transition Model T_θ (Iteration 4)

[TransitionModel] Encoding dataset for transition model training...
[TransitionModel] Dataset: 28564 samples, input_dim=288, target_dim=257
[TransitionModel] Epoch    0 | train=-76.67439 | val=0.00044 | no-improve=0/5
[TransitionModel] Epoch   20 | train=-92.87812 | val=0.00028 | no-improve=0/5
[TransitionModel] Epoch   40 | train=-99.13602 | val=0.00027 | no-improve=3/5
[TransitionModel] Epoch   42 | train=-99.76135 | val=0.00027 | no-improve=5/5
[TransitionModel] Training complete. Elites=[6, 1, 3, 5, 0], val_loss=0.00026

[RL100Trainer] Phase 2a: Training IQL Critics (Iteration 4)
[IQL] Epoch 0/20, V Loss: 0.0002, Q Loss: 0.0060
[IQL] Epoch 1/20, V Loss: 0.0002, Q Loss: 0.0058
[IQL] Epoch 2/20, V Loss: 0.0002, Q Loss: 0.0057
[IQL] Epoch 3/20, V Loss: 0.0002, Q Loss: 0.0057
[IQL] Epoch 4/20, V Loss: 0.0003, Q Loss: 0.0059
[IQL] Epoch 5/20, V Loss: 0.0002, Q Loss: 0.0056
[IQL] Epoch 6/20, V Loss: 0.0002, Q Loss: 0.0057
[IQL] Epoch 7/20, V Loss: 0.0002, Q Loss: 0.0056
[IQL] Epoch 8/20, V Loss: 0.0002, Q Loss: 0.0058
[IQL] Epoch 9/20, V Loss: 0.0002, Q Loss: 0.0057
[IQL] Epoch 10/20, V Loss: 0.0003, Q Loss: 0.0056
[IQL] Epoch 11/20, V Loss: 0.0002, Q Loss: 0.0055
[IQL] Epoch 12/20, V Loss: 0.0002, Q Loss: 0.0056
[IQL] Epoch 13/20, V Loss: 0.0002, Q Loss: 0.0056
[IQL] Epoch 14/20, V Loss: 0.0002, Q Loss: 0.0056
[IQL] Epoch 15/20, V Loss: 0.0003, Q Loss: 0.0056
[IQL] Epoch 16/20, V Loss: 0.0002, Q Loss: 0.0056
[IQL] Epoch 17/20, V Loss: 0.0002, Q Loss: 0.0057
[IQL] Epoch 18/20, V Loss: 0.0002, Q Loss: 0.0056
[IQL] Epoch 19/20, V Loss: 0.0002, Q Loss: 0.0057
[Plot] Saved: /nfs_global/S/yangrongzheng/RL100/3D-Diffusion-Policy/3D-Diffusion-Policy/plots/iql_q_loss_iter_04.png
[Plot] Saved: /nfs_global/S/yangrongzheng/RL100/3D-Diffusion-Policy/3D-Diffusion-Policy/plots/iql_v_loss_iter_04.png

[RL100Trainer] Phase 2b: Offline RL Optimization (Iteration 4)
[OPE] Behavior policy value J_old = 0.6160
[RL PPO] Reducing policy LR: 1.00e-04 → 1.00e-05
[Offline RL] Epoch 0/20, PPO Loss: -0.0238, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 13.3974, Reg Loss: 0.0000, CD Loss: 0.2202
[Offline RL] Epoch 1/20, PPO Loss: -0.0208, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 12.9849, Reg Loss: 0.0000, CD Loss: 0.0559
[Offline RL] Epoch 2/20, PPO Loss: -0.0206, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 12.6206, Reg Loss: 0.0000, CD Loss: 0.0425
[Offline RL] Epoch 3/20, PPO Loss: -0.0203, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 13.0439, Reg Loss: 0.0000, CD Loss: 0.0320
[Offline RL] Epoch 4/20, PPO Loss: -0.0203, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 13.1602, Reg Loss: 0.0000, CD Loss: 0.0246
[Offline RL] Epoch 5/20, PPO Loss: -0.0194, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 13.0158, Reg Loss: 0.0000, CD Loss: 0.0196
[Offline RL] Epoch 6/20, PPO Loss: -0.0191, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 13.0003, Reg Loss: 0.0000, CD Loss: 0.0171
[Offline RL] Epoch 7/20, PPO Loss: -0.0187, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 13.2060, Reg Loss: 0.0000, CD Loss: 0.0150
[Offline RL] Epoch 8/20, PPO Loss: -0.0184, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 13.0786, Reg Loss: 0.0000, CD Loss: 0.0139
[Offline RL] Epoch 9/20, PPO Loss: -0.0183, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 12.9471, Reg Loss: 0.0000, CD Loss: 0.0130
[Offline RL] Epoch 10/20, PPO Loss: -0.0180, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 13.0920, Reg Loss: 0.0000, CD Loss: 0.0127
[Offline RL] Epoch 11/20, PPO Loss: -0.0178, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 13.7068, Reg Loss: 0.0000, CD Loss: 0.0124
[Offline RL] Epoch 12/20, PPO Loss: -0.0181, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 13.3070, Reg Loss: 0.0000, CD Loss: 0.0116
[Offline RL] Epoch 13/20, PPO Loss: -0.0187, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 13.1940, Reg Loss: 0.0000, CD Loss: 0.0116
[Offline RL] Epoch 14/20, PPO Loss: -0.0189, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 13.3742, Reg Loss: 0.0000, CD Loss: 0.0108
[Offline RL] Epoch 15/20, PPO Loss: -0.0188, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 13.6125, Reg Loss: 0.0000, CD Loss: 0.0110
[Offline RL] Epoch 16/20, PPO Loss: -0.0190, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 13.4489, Reg Loss: 0.0000, CD Loss: 0.0107
[Offline RL] Epoch 17/20, PPO Loss: -0.0192, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 13.8445, Reg Loss: 0.0000, CD Loss: 0.0119
[Offline RL] Epoch 18/20, PPO Loss: -0.0193, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 13.8809, Reg Loss: 0.0000, CD Loss: 0.0110
[Offline RL] Epoch 19/20, PPO Loss: -0.0193, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 13.6521, Reg Loss: 0.0000, CD Loss: 0.0107
[Plot] Saved: /nfs_global/S/yangrongzheng/RL100/3D-Diffusion-Policy/3D-Diffusion-Policy/plots/ppo_loss_iter_04.png
[OPE] Policy REJECTED: J_new=0.6204 ≤ J_old=0.6160 + δ=0.0308. Rolling back to behavior policy.

[RL100Trainer] Phase 2c: Collecting New Data (Iteration 4)
[Collect] 20 episodes, success=0.600, env_return=1093.66, rl_reward=0.60, steps=4000
[Data Collection] Success Rate: 0.600, EnvReturn: 1093.66, RLReward: 0.60, Episodes: 20, Steps: 4000
[Dataset] offline collection: keeping 12/20 successful episodes (dropped 8 failures) before merge.
[Dataset] Merged 12 episodes (2400 steps) → total 34000 steps, 170 episodes

[RL100Trainer] Retraining IL on merged dataset...

============================================================
[RL100Trainer] Phase 1: Imitation Learning
============================================================

[IL] Epoch 0/100, Loss: 0.0067, Val Loss: 0.0195
[IL] Epoch 1/100, Loss: 0.0061, Val Loss: 0.0142
[IL] Epoch 2/100, Loss: 0.0063, Val Loss: 0.0194
[IL] Epoch 3/100, Loss: 0.0060, Val Loss: 0.0122
[IL] Epoch 4/100, Loss: 0.0059, Val Loss: 0.0120
[IL] Epoch 5/100, Loss: 0.0056, Val Loss: 0.0096
[IL] Epoch 6/100, Loss: 0.0054, Val Loss: 0.0150
[IL] Epoch 7/100, Loss: 0.0059, Val Loss: 0.0091
[IL] Epoch 8/100, Loss: 0.0056, Val Loss: 0.0081
[IL] Epoch 9/100, Loss: 0.0056, Val Loss: 0.0104
[IL] Epoch 10/100, Loss: 0.0054, Val Loss: 0.0098
[IL] Epoch 11/100, Loss: 0.0053, Val Loss: 0.0151
[IL] Epoch 12/100, Loss: 0.0049, Val Loss: 0.0075
[IL] Epoch 13/100, Loss: 0.0061, Val Loss: 0.0128
[IL] Epoch 14/100, Loss: 0.0055, Val Loss: 0.0078
[IL] Epoch 15/100, Loss: 0.0054, Val Loss: 0.0098
[IL] Epoch 16/100, Loss: 0.0055, Val Loss: 0.0113
[IL] Epoch 17/100, Loss: 0.0052, Val Loss: 0.0113
[IL] Epoch 18/100, Loss: 0.0053, Val Loss: 0.0133
[IL] Epoch 19/100, Loss: 0.0049, Val Loss: 0.0145
[IL] Epoch 20/100, Loss: 0.0051, Val Loss: 0.0132
[IL] Epoch 21/100, Loss: 0.0052, Val Loss: 0.0142
[IL] Epoch 22/100, Loss: 0.0055, Val Loss: 0.0139
[IL] Epoch 23/100, Loss: 0.0052, Val Loss: 0.0127
[IL] Epoch 24/100, Loss: 0.0051, Val Loss: 0.0139
[IL] Epoch 25/100, Loss: 0.0053, Val Loss: 0.0086
[IL] Epoch 26/100, Loss: 0.0053, Val Loss: 0.0133
[IL] Epoch 27/100, Loss: 0.0051, Val Loss: 0.0117
[IL] Epoch 28/100, Loss: 0.0049, Val Loss: 0.0147
[IL] Epoch 29/100, Loss: 0.0047, Val Loss: 0.0130
[IL] Epoch 30/100, Loss: 0.0048, Val Loss: 0.0135
[IL] Epoch 31/100, Loss: 0.0050, Val Loss: 0.0187
[IL] Epoch 32/100, Loss: 0.0049, Val Loss: 0.0292
[IL] Epoch 33/100, Loss: 0.0051, Val Loss: 0.0088
[IL] Epoch 34/100, Loss: 0.0050, Val Loss: 0.0095
[IL] Epoch 35/100, Loss: 0.0049, Val Loss: 0.0125
[IL] Epoch 36/100, Loss: 0.0048, Val Loss: 0.0167
[IL] Epoch 37/100, Loss: 0.0049, Val Loss: 0.0091
[IL] Epoch 38/100, Loss: 0.0049, Val Loss: 0.0189
[IL] Epoch 39/100, Loss: 0.0050, Val Loss: 0.0147
[IL] Epoch 40/100, Loss: 0.0050, Val Loss: 0.0093
[IL] Epoch 41/100, Loss: 0.0048, Val Loss: 0.0139
[IL] Epoch 42/100, Loss: 0.0051, Val Loss: 0.0158
[IL] Epoch 43/100, Loss: 0.0053, Val Loss: 0.0131
[IL] Epoch 44/100, Loss: 0.0046, Val Loss: 0.0120
[IL] Epoch 45/100, Loss: 0.0045, Val Loss: 0.0096
[IL] Epoch 46/100, Loss: 0.0044, Val Loss: 0.0097
[IL] Epoch 47/100, Loss: 0.0051, Val Loss: 0.0190
[IL] Epoch 48/100, Loss: 0.0046, Val Loss: 0.0117
[IL] Epoch 49/100, Loss: 0.0049, Val Loss: 0.0161
[IL] Epoch 50/100, Loss: 0.0050, Val Loss: 0.0229
[IL] Epoch 51/100, Loss: 0.0050, Val Loss: 0.0118
[IL] Epoch 52/100, Loss: 0.0046, Val Loss: 0.0242
[IL] Epoch 53/100, Loss: 0.0052, Val Loss: 0.0115
[IL] Epoch 54/100, Loss: 0.0047, Val Loss: 0.0169
[IL] Epoch 55/100, Loss: 0.0047, Val Loss: 0.0167
[IL] Epoch 56/100, Loss: 0.0044, Val Loss: 0.0133
[IL] Epoch 57/100, Loss: 0.0046, Val Loss: 0.0118
[IL] Epoch 58/100, Loss: 0.0043, Val Loss: 0.0091
[IL] Epoch 59/100, Loss: 0.0053, Val Loss: 0.0094
[IL] Epoch 60/100, Loss: 0.0050, Val Loss: 0.0146
[IL] Epoch 61/100, Loss: 0.0046, Val Loss: 0.0104
[IL] Epoch 62/100, Loss: 0.0046, Val Loss: 0.0103
[IL] Epoch 63/100, Loss: 0.0043, Val Loss: 0.0133
[IL] Epoch 64/100, Loss: 0.0045, Val Loss: 0.0151
[IL] Epoch 65/100, Loss: 0.0045, Val Loss: 0.0124
[IL] Epoch 66/100, Loss: 0.0048, Val Loss: 0.0113
[IL] Epoch 67/100, Loss: 0.0046, Val Loss: 0.0109
[IL] Epoch 68/100, Loss: 0.0044, Val Loss: 0.0130
[IL] Epoch 69/100, Loss: 0.0046, Val Loss: 0.0107
[IL] Epoch 70/100, Loss: 0.0047, Val Loss: 0.0090
[IL] Epoch 71/100, Loss: 0.0047, Val Loss: 0.0187
[IL] Epoch 72/100, Loss: 0.0044, Val Loss: 0.0099
[IL] Epoch 73/100, Loss: 0.0044, Val Loss: 0.0184
[IL] Epoch 74/100, Loss: 0.0042, Val Loss: 0.0196
[IL] Epoch 75/100, Loss: 0.0050, Val Loss: 0.0083
[IL] Epoch 76/100, Loss: 0.0043, Val Loss: 0.0109
[IL] Epoch 77/100, Loss: 0.0046, Val Loss: 0.0177
[IL] Epoch 78/100, Loss: 0.0049, Val Loss: 0.0157
[IL] Epoch 79/100, Loss: 0.0046, Val Loss: 0.0241
[IL] Epoch 80/100, Loss: 0.0043, Val Loss: 0.0111
[IL] Epoch 81/100, Loss: 0.0045, Val Loss: 0.0086
[IL] Epoch 82/100, Loss: 0.0042, Val Loss: 0.0136
[IL] Epoch 83/100, Loss: 0.0045, Val Loss: 0.0170
[IL] Epoch 84/100, Loss: 0.0044, Val Loss: 0.0124
[IL] Epoch 85/100, Loss: 0.0044, Val Loss: 0.0129
[IL] Epoch 86/100, Loss: 0.0046, Val Loss: 0.0167
[IL] Epoch 87/100, Loss: 0.0045, Val Loss: 0.0072
[IL] Epoch 88/100, Loss: 0.0043, Val Loss: 0.0195
[IL] Epoch 89/100, Loss: 0.0045, Val Loss: 0.0198
[IL] Epoch 90/100, Loss: 0.0047, Val Loss: 0.0331
[IL] Epoch 91/100, Loss: 0.0044, Val Loss: 0.0131
[IL] Epoch 92/100, Loss: 0.0042, Val Loss: 0.0187
[IL] Epoch 93/100, Loss: 0.0045, Val Loss: 0.0125
[IL] Epoch 94/100, Loss: 0.0041, Val Loss: 0.0087
[IL] Epoch 95/100, Loss: 0.0041, Val Loss: 0.0145
[IL] Epoch 96/100, Loss: 0.0046, Val Loss: 0.0125
[IL] Epoch 97/100, Loss: 0.0043, Val Loss: 0.0154
[IL] Epoch 98/100, Loss: 0.0041, Val Loss: 0.0115
[IL] Epoch 99/100, Loss: 0.0045, Val Loss: 0.0210
test_mean_score: 0.84
[IL] Eval - Success Rate: 0.840
[Plot] Saved: /nfs_global/S/yangrongzheng/RL100/3D-Diffusion-Policy/3D-Diffusion-Policy/plots/il_loss_retrain_iter_04.png
[Checkpoint] Saved to /nfs_global/S/yangrongzheng/RL100/3D-Diffusion-Policy/3D-Diffusion-Policy/checkpoints/offline_iter_4.ckpt

================================================================================
               OFFLINE RL ITERATION 6/10
================================================================================


[RL100Trainer] Line 6 — Training Transition Model T_θ (Iteration 5)

[TransitionModel] Encoding dataset for transition model training...
[TransitionModel] Dataset: 30880 samples, input_dim=288, target_dim=257
[TransitionModel] Epoch    0 | train=-95.89357 | val=0.00041 | no-improve=0/5
[TransitionModel] Epoch   20 | train=-105.76736 | val=0.00036 | no-improve=1/5
[TransitionModel] Epoch   24 | train=-106.92001 | val=0.00038 | no-improve=5/5
[TransitionModel] Training complete. Elites=[6, 5, 3, 1, 4], val_loss=0.00033

[RL100Trainer] Phase 2a: Training IQL Critics (Iteration 5)
[IQL] Epoch 0/20, V Loss: 0.0002, Q Loss: 0.0056
[IQL] Epoch 1/20, V Loss: 0.0002, Q Loss: 0.0055
[IQL] Epoch 2/20, V Loss: 0.0002, Q Loss: 0.0056
[IQL] Epoch 3/20, V Loss: 0.0002, Q Loss: 0.0055
[IQL] Epoch 4/20, V Loss: 0.0002, Q Loss: 0.0055
[IQL] Epoch 5/20, V Loss: 0.0002, Q Loss: 0.0056
[IQL] Epoch 6/20, V Loss: 0.0002, Q Loss: 0.0055
[IQL] Epoch 7/20, V Loss: 0.0002, Q Loss: 0.0054
[IQL] Epoch 8/20, V Loss: 0.0003, Q Loss: 0.0057
[IQL] Epoch 9/20, V Loss: 0.0001, Q Loss: 0.0056
[IQL] Epoch 10/20, V Loss: 0.0001, Q Loss: 0.0055
[IQL] Epoch 11/20, V Loss: 0.0002, Q Loss: 0.0054
[IQL] Epoch 12/20, V Loss: 0.0002, Q Loss: 0.0055
[IQL] Epoch 13/20, V Loss: 0.0002, Q Loss: 0.0056
[IQL] Epoch 14/20, V Loss: 0.0002, Q Loss: 0.0055
[IQL] Epoch 15/20, V Loss: 0.0002, Q Loss: 0.0056
[IQL] Epoch 16/20, V Loss: 0.0002, Q Loss: 0.0054
[IQL] Epoch 17/20, V Loss: 0.0002, Q Loss: 0.0055
[IQL] Epoch 18/20, V Loss: 0.0002, Q Loss: 0.0054
[IQL] Epoch 19/20, V Loss: 0.0002, Q Loss: 0.0054
[Plot] Saved: /nfs_global/S/yangrongzheng/RL100/3D-Diffusion-Policy/3D-Diffusion-Policy/plots/iql_q_loss_iter_05.png
[Plot] Saved: /nfs_global/S/yangrongzheng/RL100/3D-Diffusion-Policy/3D-Diffusion-Policy/plots/iql_v_loss_iter_05.png

[RL100Trainer] Phase 2b: Offline RL Optimization (Iteration 5)
[OPE] Behavior policy value J_old = 0.5877
[RL PPO] Reducing policy LR: 1.00e-04 → 1.00e-05
[Offline RL] Epoch 0/20, PPO Loss: -0.0187, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 12.2546, Reg Loss: 0.0000, CD Loss: 0.2024
[Offline RL] Epoch 1/20, PPO Loss: -0.0168, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 11.5086, Reg Loss: 0.0000, CD Loss: 0.0510
[Offline RL] Epoch 2/20, PPO Loss: -0.0161, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 11.8446, Reg Loss: 0.0000, CD Loss: 0.0392
[Offline RL] Epoch 3/20, PPO Loss: -0.0153, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 12.1653, Reg Loss: 0.0000, CD Loss: 0.0286
[Offline RL] Epoch 4/20, PPO Loss: -0.0148, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 11.8463, Reg Loss: 0.0000, CD Loss: 0.0219
[Offline RL] Epoch 5/20, PPO Loss: -0.0143, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 12.8542, Reg Loss: 0.0000, CD Loss: 0.0175
[Offline RL] Epoch 6/20, PPO Loss: -0.0144, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 12.3655, Reg Loss: 0.0000, CD Loss: 0.0154
[Offline RL] Epoch 7/20, PPO Loss: -0.0148, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 12.2633, Reg Loss: 0.0000, CD Loss: 0.0141
[Offline RL] Epoch 8/20, PPO Loss: -0.0149, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 12.8916, Reg Loss: 0.0000, CD Loss: 0.0130
[Offline RL] Epoch 9/20, PPO Loss: -0.0146, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 12.3118, Reg Loss: 0.0000, CD Loss: 0.0118
[Offline RL] Epoch 10/20, PPO Loss: -0.0145, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 12.5926, Reg Loss: 0.0000, CD Loss: 0.0115
[Offline RL] Epoch 11/20, PPO Loss: -0.0151, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 12.6539, Reg Loss: 0.0000, CD Loss: 0.0107
[Offline RL] Epoch 12/20, PPO Loss: -0.0149, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 12.7163, Reg Loss: 0.0000, CD Loss: 0.0104
[Offline RL] Epoch 13/20, PPO Loss: -0.0150, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 12.7915, Reg Loss: 0.0000, CD Loss: 0.0107
[Offline RL] Epoch 14/20, PPO Loss: -0.0151, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 12.7250, Reg Loss: 0.0000, CD Loss: 0.0111
[Offline RL] Epoch 15/20, PPO Loss: -0.0157, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 12.3860, Reg Loss: 0.0000, CD Loss: 0.0110
[Offline RL] Epoch 16/20, PPO Loss: -0.0153, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 13.0531, Reg Loss: 0.0000, CD Loss: 0.0097
[Offline RL] Epoch 17/20, PPO Loss: -0.0156, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 13.3744, Reg Loss: 0.0000, CD Loss: 0.0097
[Offline RL] Epoch 18/20, PPO Loss: -0.0159, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 12.5880, Reg Loss: 0.0000, CD Loss: 0.0097
[Offline RL] Epoch 19/20, PPO Loss: -0.0160, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 13.0198, Reg Loss: 0.0000, CD Loss: 0.0098
[Plot] Saved: /nfs_global/S/yangrongzheng/RL100/3D-Diffusion-Policy/3D-Diffusion-Policy/plots/ppo_loss_iter_05.png
[OPE] Policy REJECTED: J_new=0.5941 ≤ J_old=0.5877 + δ=0.0294. Rolling back to behavior policy.

[RL100Trainer] Phase 2c: Collecting New Data (Iteration 5)
[Collect] 20 episodes, success=1.000, env_return=1214.34, rl_reward=1.00, steps=4000
[Data Collection] Success Rate: 1.000, EnvReturn: 1214.34, RLReward: 1.00, Episodes: 20, Steps: 4000
[Dataset] offline collection: keeping 20/20 successful episodes (dropped 0 failures) before merge.
[Dataset] Merged 20 episodes (4000 steps) → total 38000 steps, 190 episodes

[RL100Trainer] Retraining IL on merged dataset...

============================================================
[RL100Trainer] Phase 1: Imitation Learning
============================================================

[IL] Epoch 0/100, Loss: 0.0063, Val Loss: 0.0160
[IL] Epoch 1/100, Loss: 0.0059, Val Loss: 0.0100
[IL] Epoch 2/100, Loss: 0.0058, Val Loss: 0.0104
[IL] Epoch 3/100, Loss: 0.0056, Val Loss: 0.0153
[IL] Epoch 4/100, Loss: 0.0052, Val Loss: 0.0108
[IL] Epoch 5/100, Loss: 0.0054, Val Loss: 0.0159
[IL] Epoch 6/100, Loss: 0.0056, Val Loss: 0.0266
[IL] Epoch 7/100, Loss: 0.0054, Val Loss: 0.0172
[IL] Epoch 8/100, Loss: 0.0053, Val Loss: 0.0100
[IL] Epoch 9/100, Loss: 0.0051, Val Loss: 0.0154
[IL] Epoch 10/100, Loss: 0.0049, Val Loss: 0.0118
[IL] Epoch 11/100, Loss: 0.0052, Val Loss: 0.0206
[IL] Epoch 12/100, Loss: 0.0051, Val Loss: 0.0143
[IL] Epoch 13/100, Loss: 0.0053, Val Loss: 0.0093
[IL] Epoch 14/100, Loss: 0.0052, Val Loss: 0.0124
[IL] Epoch 15/100, Loss: 0.0050, Val Loss: 0.0106
[IL] Epoch 16/100, Loss: 0.0051, Val Loss: 0.0124
[IL] Epoch 17/100, Loss: 0.0051, Val Loss: 0.0130
[IL] Epoch 18/100, Loss: 0.0049, Val Loss: 0.0186
[IL] Epoch 19/100, Loss: 0.0049, Val Loss: 0.0179
[IL] Epoch 20/100, Loss: 0.0049, Val Loss: 0.0122
[IL] Epoch 21/100, Loss: 0.0048, Val Loss: 0.0156
[IL] Epoch 22/100, Loss: 0.0046, Val Loss: 0.0109
[IL] Epoch 23/100, Loss: 0.0046, Val Loss: 0.0177
[IL] Epoch 24/100, Loss: 0.0054, Val Loss: 0.0168
[IL] Epoch 25/100, Loss: 0.0047, Val Loss: 0.0142
[IL] Epoch 26/100, Loss: 0.0048, Val Loss: 0.0146
[IL] Epoch 27/100, Loss: 0.0049, Val Loss: 0.0157
[IL] Epoch 28/100, Loss: 0.0046, Val Loss: 0.0123
[IL] Epoch 29/100, Loss: 0.0054, Val Loss: 0.0095
[IL] Epoch 30/100, Loss: 0.0047, Val Loss: 0.0135
[IL] Epoch 31/100, Loss: 0.0048, Val Loss: 0.0169
[IL] Epoch 32/100, Loss: 0.0048, Val Loss: 0.0097
[IL] Epoch 33/100, Loss: 0.0048, Val Loss: 0.0127
[IL] Epoch 34/100, Loss: 0.0046, Val Loss: 0.0192
[IL] Epoch 35/100, Loss: 0.0047, Val Loss: 0.0167
[IL] Epoch 36/100, Loss: 0.0045, Val Loss: 0.0150
[IL] Epoch 37/100, Loss: 0.0043, Val Loss: 0.0142
[IL] Epoch 38/100, Loss: 0.0046, Val Loss: 0.0123
[IL] Epoch 39/100, Loss: 0.0044, Val Loss: 0.0206
[IL] Epoch 40/100, Loss: 0.0046, Val Loss: 0.0137
[IL] Epoch 41/100, Loss: 0.0043, Val Loss: 0.0086
[IL] Epoch 42/100, Loss: 0.0045, Val Loss: 0.0194
[IL] Epoch 43/100, Loss: 0.0045, Val Loss: 0.0134
[IL] Epoch 44/100, Loss: 0.0045, Val Loss: 0.0152
[IL] Epoch 45/100, Loss: 0.0042, Val Loss: 0.0126
[IL] Epoch 46/100, Loss: 0.0046, Val Loss: 0.0155
[IL] Epoch 47/100, Loss: 0.0042, Val Loss: 0.0155
[IL] Epoch 48/100, Loss: 0.0046, Val Loss: 0.0132
[IL] Epoch 49/100, Loss: 0.0045, Val Loss: 0.0133
[IL] Epoch 50/100, Loss: 0.0044, Val Loss: 0.0120
[IL] Epoch 51/100, Loss: 0.0050, Val Loss: 0.0118
[IL] Epoch 52/100, Loss: 0.0040, Val Loss: 0.0169
[IL] Epoch 53/100, Loss: 0.0044, Val Loss: 0.0095
[IL] Epoch 54/100, Loss: 0.0045, Val Loss: 0.0176
[IL] Epoch 55/100, Loss: 0.0045, Val Loss: 0.0121
[IL] Epoch 56/100, Loss: 0.0045, Val Loss: 0.0207
[IL] Epoch 57/100, Loss: 0.0045, Val Loss: 0.0210
[IL] Epoch 58/100, Loss: 0.0044, Val Loss: 0.0131
[IL] Epoch 59/100, Loss: 0.0041, Val Loss: 0.0251
[IL] Epoch 60/100, Loss: 0.0047, Val Loss: 0.0128
[IL] Epoch 61/100, Loss: 0.0044, Val Loss: 0.0208
[IL] Epoch 62/100, Loss: 0.0041, Val Loss: 0.0156
[IL] Epoch 63/100, Loss: 0.0044, Val Loss: 0.0253
[IL] Epoch 64/100, Loss: 0.0041, Val Loss: 0.0201
[IL] Epoch 65/100, Loss: 0.0044, Val Loss: 0.0133
[IL] Epoch 66/100, Loss: 0.0042, Val Loss: 0.0130
[IL] Epoch 67/100, Loss: 0.0040, Val Loss: 0.0173
[IL] Epoch 68/100, Loss: 0.0041, Val Loss: 0.0160
[IL] Epoch 69/100, Loss: 0.0043, Val Loss: 0.0148
[IL] Epoch 70/100, Loss: 0.0046, Val Loss: 0.0120
[IL] Epoch 71/100, Loss: 0.0044, Val Loss: 0.0197
[IL] Epoch 72/100, Loss: 0.0045, Val Loss: 0.0104
[IL] Epoch 73/100, Loss: 0.0047, Val Loss: 0.0114
[IL] Epoch 74/100, Loss: 0.0044, Val Loss: 0.0199
[IL] Epoch 75/100, Loss: 0.0042, Val Loss: 0.0173
[IL] Epoch 76/100, Loss: 0.0045, Val Loss: 0.0186
[IL] Epoch 77/100, Loss: 0.0038, Val Loss: 0.0165
[IL] Epoch 78/100, Loss: 0.0042, Val Loss: 0.0125
[IL] Epoch 79/100, Loss: 0.0043, Val Loss: 0.0154
[IL] Epoch 80/100, Loss: 0.0041, Val Loss: 0.0176
[IL] Epoch 81/100, Loss: 0.0044, Val Loss: 0.0156
[IL] Epoch 82/100, Loss: 0.0044, Val Loss: 0.0141
[IL] Epoch 83/100, Loss: 0.0043, Val Loss: 0.0139
[IL] Epoch 84/100, Loss: 0.0038, Val Loss: 0.0152
[IL] Epoch 85/100, Loss: 0.0042, Val Loss: 0.0241
[IL] Epoch 86/100, Loss: 0.0038, Val Loss: 0.0104
[IL] Epoch 87/100, Loss: 0.0044, Val Loss: 0.0140
[IL] Epoch 88/100, Loss: 0.0042, Val Loss: 0.0175
[IL] Epoch 89/100, Loss: 0.0040, Val Loss: 0.0180
[IL] Epoch 90/100, Loss: 0.0038, Val Loss: 0.0183
[IL] Epoch 91/100, Loss: 0.0038, Val Loss: 0.0156
[IL] Epoch 92/100, Loss: 0.0044, Val Loss: 0.0143
[IL] Epoch 93/100, Loss: 0.0045, Val Loss: 0.0127
[IL] Epoch 94/100, Loss: 0.0041, Val Loss: 0.0128
[IL] Epoch 95/100, Loss: 0.0046, Val Loss: 0.0092
[IL] Epoch 96/100, Loss: 0.0042, Val Loss: 0.0156
[IL] Epoch 97/100, Loss: 0.0042, Val Loss: 0.0164
[IL] Epoch 98/100, Loss: 0.0044, Val Loss: 0.0115
[IL] Epoch 99/100, Loss: 0.0044, Val Loss: 0.0203
test_mean_score: 0.83
[IL] Eval - Success Rate: 0.830
[Plot] Saved: /nfs_global/S/yangrongzheng/RL100/3D-Diffusion-Policy/3D-Diffusion-Policy/plots/il_loss_retrain_iter_05.png
[Checkpoint] Saved to /nfs_global/S/yangrongzheng/RL100/3D-Diffusion-Policy/3D-Diffusion-Policy/checkpoints/offline_iter_5.ckpt

================================================================================
               OFFLINE RL ITERATION 7/10
================================================================================


[RL100Trainer] Line 6 — Training Transition Model T_θ (Iteration 6)

[TransitionModel] Encoding dataset for transition model training...
[TransitionModel] Dataset: 34740 samples, input_dim=288, target_dim=257
[TransitionModel] Epoch    0 | train=-103.97468 | val=0.00036 | no-improve=0/5
[TransitionModel] Epoch   20 | train=-113.69085 | val=0.00034 | no-improve=0/5
[TransitionModel] Epoch   25 | train=-115.36615 | val=0.00034 | no-improve=5/5
[TransitionModel] Training complete. Elites=[6, 4, 5, 1, 3], val_loss=0.00029

[RL100Trainer] Phase 2a: Training IQL Critics (Iteration 6)
[IQL] Epoch 0/20, V Loss: 0.0001, Q Loss: 0.0058
[IQL] Epoch 1/20, V Loss: 0.0002, Q Loss: 0.0058
[IQL] Epoch 2/20, V Loss: 0.0002, Q Loss: 0.0057
[IQL] Epoch 3/20, V Loss: 0.0001, Q Loss: 0.0056
[IQL] Epoch 4/20, V Loss: 0.0002, Q Loss: 0.0057
[IQL] Epoch 5/20, V Loss: 0.0002, Q Loss: 0.0057
[IQL] Epoch 6/20, V Loss: 0.0001, Q Loss: 0.0056
[IQL] Epoch 7/20, V Loss: 0.0002, Q Loss: 0.0056
[IQL] Epoch 8/20, V Loss: 0.0002, Q Loss: 0.0056
[IQL] Epoch 9/20, V Loss: 0.0002, Q Loss: 0.0057
[IQL] Epoch 10/20, V Loss: 0.0002, Q Loss: 0.0056
[IQL] Epoch 11/20, V Loss: 0.0002, Q Loss: 0.0055
[IQL] Epoch 12/20, V Loss: 0.0002, Q Loss: 0.0055
[IQL] Epoch 13/20, V Loss: 0.0002, Q Loss: 0.0055
[IQL] Epoch 14/20, V Loss: 0.0002, Q Loss: 0.0055
[IQL] Epoch 15/20, V Loss: 0.0002, Q Loss: 0.0055
[IQL] Epoch 16/20, V Loss: 0.0002, Q Loss: 0.0055
[IQL] Epoch 17/20, V Loss: 0.0002, Q Loss: 0.0056
[IQL] Epoch 18/20, V Loss: 0.0001, Q Loss: 0.0054
[IQL] Epoch 19/20, V Loss: 0.0002, Q Loss: 0.0055
[Plot] Saved: /nfs_global/S/yangrongzheng/RL100/3D-Diffusion-Policy/3D-Diffusion-Policy/plots/iql_q_loss_iter_06.png
[Plot] Saved: /nfs_global/S/yangrongzheng/RL100/3D-Diffusion-Policy/3D-Diffusion-Policy/plots/iql_v_loss_iter_06.png

[RL100Trainer] Phase 2b: Offline RL Optimization (Iteration 6)
[OPE] Behavior policy value J_old = 0.6241
[RL PPO] Reducing policy LR: 1.00e-04 → 1.00e-05
[Offline RL] Epoch 0/20, PPO Loss: -0.0183, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 11.8784, Reg Loss: 0.0000, CD Loss: 0.1888
[Offline RL] Epoch 1/20, PPO Loss: -0.0162, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 11.3747, Reg Loss: 0.0000, CD Loss: 0.0474
[Offline RL] Epoch 2/20, PPO Loss: -0.0147, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 12.0210, Reg Loss: 0.0000, CD Loss: 0.0358
[Offline RL] Epoch 3/20, PPO Loss: -0.0144, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 12.0401, Reg Loss: 0.0000, CD Loss: 0.0258
[Offline RL] Epoch 4/20, PPO Loss: -0.0139, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 11.9096, Reg Loss: 0.0000, CD Loss: 0.0193
[Offline RL] Epoch 5/20, PPO Loss: -0.0137, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 12.3053, Reg Loss: 0.0000, CD Loss: 0.0168
[Offline RL] Epoch 6/20, PPO Loss: -0.0137, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 11.9884, Reg Loss: 0.0000, CD Loss: 0.0154
[Offline RL] Epoch 7/20, PPO Loss: -0.0131, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 12.1456, Reg Loss: 0.0000, CD Loss: 0.0145
[Offline RL] Epoch 8/20, PPO Loss: -0.0131, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 12.3582, Reg Loss: 0.0000, CD Loss: 0.0142
[Offline RL] Epoch 9/20, PPO Loss: -0.0128, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 12.4907, Reg Loss: 0.0000, CD Loss: 0.0144
[Offline RL] Epoch 10/20, PPO Loss: -0.0130, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 12.8530, Reg Loss: 0.0000, CD Loss: 0.0138
[Offline RL] Epoch 11/20, PPO Loss: -0.0130, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 12.7832, Reg Loss: 0.0000, CD Loss: 0.0141
[Offline RL] Epoch 12/20, PPO Loss: -0.0130, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 12.5954, Reg Loss: 0.0000, CD Loss: 0.0142
[Offline RL] Epoch 13/20, PPO Loss: -0.0134, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 12.3915, Reg Loss: 0.0000, CD Loss: 0.0129
[Offline RL] Epoch 14/20, PPO Loss: -0.0137, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 12.1696, Reg Loss: 0.0000, CD Loss: 0.0125
[Offline RL] Epoch 15/20, PPO Loss: -0.0138, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 12.1504, Reg Loss: 0.0000, CD Loss: 0.0131
[Offline RL] Epoch 16/20, PPO Loss: -0.0137, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 12.2794, Reg Loss: 0.0000, CD Loss: 0.0116
[Offline RL] Epoch 17/20, PPO Loss: -0.0139, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 12.1658, Reg Loss: 0.0000, CD Loss: 0.0112
[Offline RL] Epoch 18/20, PPO Loss: -0.0133, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 12.5650, Reg Loss: 0.0000, CD Loss: 0.0113
[Offline RL] Epoch 19/20, PPO Loss: -0.0136, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 12.4845, Reg Loss: 0.0000, CD Loss: 0.0119
[Plot] Saved: /nfs_global/S/yangrongzheng/RL100/3D-Diffusion-Policy/3D-Diffusion-Policy/plots/ppo_loss_iter_06.png
[OPE] Policy REJECTED: J_new=0.6311 ≤ J_old=0.6241 + δ=0.0312. Rolling back to behavior policy.

[RL100Trainer] Phase 2c: Collecting New Data (Iteration 6)
[Collect] 20 episodes, success=0.750, env_return=1036.60, rl_reward=0.75, steps=4000
[Data Collection] Success Rate: 0.750, EnvReturn: 1036.60, RLReward: 0.75, Episodes: 20, Steps: 4000
[Dataset] offline collection: keeping 15/20 successful episodes (dropped 5 failures) before merge.
[Dataset] Merged 15 episodes (3000 steps) → total 41000 steps, 205 episodes

[RL100Trainer] Retraining IL on merged dataset...

============================================================
[RL100Trainer] Phase 1: Imitation Learning
============================================================

[IL] Epoch 0/100, Loss: 0.0051, Val Loss: 0.0110
[IL] Epoch 1/100, Loss: 0.0056, Val Loss: 0.0140
[IL] Epoch 2/100, Loss: 0.0047, Val Loss: 0.0165
[IL] Epoch 3/100, Loss: 0.0048, Val Loss: 0.0131
[IL] Epoch 4/100, Loss: 0.0051, Val Loss: 0.0195
[IL] Epoch 5/100, Loss: 0.0047, Val Loss: 0.0134
[IL] Epoch 6/100, Loss: 0.0047, Val Loss: 0.0130
[IL] Epoch 7/100, Loss: 0.0049, Val Loss: 0.0113
[IL] Epoch 8/100, Loss: 0.0046, Val Loss: 0.0134
[IL] Epoch 9/100, Loss: 0.0062, Val Loss: 0.0189
[IL] Epoch 10/100, Loss: 0.0077, Val Loss: 0.0121
[IL] Epoch 11/100, Loss: 0.0048, Val Loss: 0.0193
[IL] Epoch 12/100, Loss: 0.0047, Val Loss: 0.0117
[IL] Epoch 13/100, Loss: 0.0046, Val Loss: 0.0160
[IL] Epoch 14/100, Loss: 0.0051, Val Loss: 0.0165
[IL] Epoch 15/100, Loss: 0.0042, Val Loss: 0.0169
[IL] Epoch 16/100, Loss: 0.0046, Val Loss: 0.0095
[IL] Epoch 17/100, Loss: 0.0045, Val Loss: 0.0137
[IL] Epoch 18/100, Loss: 0.0042, Val Loss: 0.0140
[IL] Epoch 19/100, Loss: 0.0041, Val Loss: 0.0118
[IL] Epoch 20/100, Loss: 0.0043, Val Loss: 0.0099
[IL] Epoch 21/100, Loss: 0.0040, Val Loss: 0.0174
[IL] Epoch 22/100, Loss: 0.0040, Val Loss: 0.0149
[IL] Epoch 23/100, Loss: 0.0044, Val Loss: 0.0191
[IL] Epoch 24/100, Loss: 0.0042, Val Loss: 0.0180
[IL] Epoch 25/100, Loss: 0.0041, Val Loss: 0.0174
[IL] Epoch 26/100, Loss: 0.0048, Val Loss: 0.0168
[IL] Epoch 27/100, Loss: 0.0044, Val Loss: 0.0118
[IL] Epoch 28/100, Loss: 0.0048, Val Loss: 0.0200
[IL] Epoch 29/100, Loss: 0.0046, Val Loss: 0.0128
[IL] Epoch 30/100, Loss: 0.0042, Val Loss: 0.0190
[IL] Epoch 31/100, Loss: 0.0052, Val Loss: 0.0156
[IL] Epoch 32/100, Loss: 0.0039, Val Loss: 0.0192
[IL] Epoch 33/100, Loss: 0.0039, Val Loss: 0.0192
[IL] Epoch 34/100, Loss: 0.0041, Val Loss: 0.0104
[IL] Epoch 35/100, Loss: 0.0040, Val Loss: 0.0171
[IL] Epoch 36/100, Loss: 0.0041, Val Loss: 0.0104
[IL] Epoch 37/100, Loss: 0.0047, Val Loss: 0.0102
[IL] Epoch 38/100, Loss: 0.0042, Val Loss: 0.0255
[IL] Epoch 39/100, Loss: 0.0045, Val Loss: 0.0266
[IL] Epoch 40/100, Loss: 0.0042, Val Loss: 0.0137
[IL] Epoch 41/100, Loss: 0.0041, Val Loss: 0.0124
[IL] Epoch 42/100, Loss: 0.0042, Val Loss: 0.0102
[IL] Epoch 43/100, Loss: 0.0060, Val Loss: 0.0119
[IL] Epoch 44/100, Loss: 0.0043, Val Loss: 0.0148
[IL] Epoch 45/100, Loss: 0.0041, Val Loss: 0.0145
[IL] Epoch 46/100, Loss: 0.0036, Val Loss: 0.0126
[IL] Epoch 47/100, Loss: 0.0045, Val Loss: 0.0132
[IL] Epoch 48/100, Loss: 0.0086, Val Loss: 0.0119
[IL] Epoch 49/100, Loss: 0.0044, Val Loss: 0.0141
[IL] Epoch 50/100, Loss: 0.0042, Val Loss: 0.0128
[IL] Epoch 51/100, Loss: 0.0043, Val Loss: 0.0150
[IL] Epoch 52/100, Loss: 0.0040, Val Loss: 0.0127
[IL] Epoch 53/100, Loss: 0.0040, Val Loss: 0.0140
[IL] Epoch 54/100, Loss: 0.0039, Val Loss: 0.0149
[IL] Epoch 55/100, Loss: 0.0057, Val Loss: 0.0122
[IL] Epoch 56/100, Loss: 0.0049, Val Loss: 0.0094
[IL] Epoch 57/100, Loss: 0.0040, Val Loss: 0.0173
[IL] Epoch 58/100, Loss: 0.0044, Val Loss: 0.0346
[IL] Epoch 59/100, Loss: 0.0078, Val Loss: 0.0222
[IL] Epoch 60/100, Loss: 0.0042, Val Loss: 0.0168
[IL] Epoch 61/100, Loss: 0.0040, Val Loss: 0.0142
[IL] Epoch 62/100, Loss: 0.0037, Val Loss: 0.0165
[IL] Epoch 63/100, Loss: 0.0037, Val Loss: 0.0122
[IL] Epoch 64/100, Loss: 0.0042, Val Loss: 0.0310
[IL] Epoch 65/100, Loss: 0.0080, Val Loss: 0.0217
[IL] Epoch 66/100, Loss: 0.0041, Val Loss: 0.0095
[IL] Epoch 67/100, Loss: 0.0050, Val Loss: 0.0098
[IL] Epoch 68/100, Loss: 0.0038, Val Loss: 0.0087
[IL] Epoch 69/100, Loss: 0.0040, Val Loss: 0.0300
[IL] Epoch 70/100, Loss: 0.0047, Val Loss: 0.0162
[IL] Epoch 71/100, Loss: 0.0039, Val Loss: 0.0191
[IL] Epoch 72/100, Loss: 0.0035, Val Loss: 0.0144
[IL] Epoch 73/100, Loss: 0.0035, Val Loss: 0.0134
[IL] Epoch 74/100, Loss: 0.0036, Val Loss: 0.0163
[IL] Epoch 75/100, Loss: 0.0051, Val Loss: 0.0240
[IL] Epoch 76/100, Loss: 0.0073, Val Loss: 0.0192
[IL] Epoch 77/100, Loss: 0.0040, Val Loss: 0.0139
[IL] Epoch 78/100, Loss: 0.0036, Val Loss: 0.0133
[IL] Epoch 79/100, Loss: 0.0038, Val Loss: 0.0158
[IL] Epoch 80/100, Loss: 0.0035, Val Loss: 0.0132
[IL] Epoch 81/100, Loss: 0.0035, Val Loss: 0.0135
[IL] Epoch 82/100, Loss: 0.0037, Val Loss: 0.0133
[IL] Epoch 83/100, Loss: 0.0039, Val Loss: 0.0182
[IL] Epoch 84/100, Loss: 0.0040, Val Loss: 0.0157
[IL] Epoch 85/100, Loss: 0.0041, Val Loss: 0.0145
[IL] Epoch 86/100, Loss: 0.0039, Val Loss: 0.0158
[IL] Epoch 87/100, Loss: 0.0039, Val Loss: 0.0147
[IL] Epoch 88/100, Loss: 0.0037, Val Loss: 0.0122
[IL] Epoch 89/100, Loss: 0.0049, Val Loss: 0.0139
[IL] Epoch 90/100, Loss: 0.0039, Val Loss: 0.0108
[IL] Epoch 91/100, Loss: 0.0043, Val Loss: 0.0207
[IL] Epoch 92/100, Loss: 0.0042, Val Loss: 0.0245
[IL] Epoch 93/100, Loss: 0.0036, Val Loss: 0.0115
[IL] Epoch 94/100, Loss: 0.0037, Val Loss: 0.0303
[IL] Epoch 95/100, Loss: 0.0036, Val Loss: 0.0175
[IL] Epoch 96/100, Loss: 0.0039, Val Loss: 0.0172
[IL] Epoch 97/100, Loss: 0.0039, Val Loss: 0.0122
[IL] Epoch 98/100, Loss: 0.0042, Val Loss: 0.0191
[IL] Epoch 99/100, Loss: 0.0044, Val Loss: 0.0153
test_mean_score: 0.84
[IL] Eval - Success Rate: 0.840
[Plot] Saved: /nfs_global/S/yangrongzheng/RL100/3D-Diffusion-Policy/3D-Diffusion-Policy/plots/il_loss_retrain_iter_06.png
[Checkpoint] Saved to /nfs_global/S/yangrongzheng/RL100/3D-Diffusion-Policy/3D-Diffusion-Policy/checkpoints/offline_iter_6.ckpt

================================================================================
               OFFLINE RL ITERATION 8/10
================================================================================


[RL100Trainer] Line 6 — Training Transition Model T_θ (Iteration 7)

[TransitionModel] Encoding dataset for transition model training...
[TransitionModel] Dataset: 37635 samples, input_dim=288, target_dim=257
[TransitionModel] Epoch    0 | train=-112.72972 | val=0.00041 | no-improve=0/5
[TransitionModel] Epoch   20 | train=-122.58099 | val=0.00039 | no-improve=3/5
[TransitionModel] Epoch   28 | train=-125.73951 | val=0.00040 | no-improve=5/5
[TransitionModel] Training complete. Elites=[6, 2, 1, 0, 5], val_loss=0.00036

[RL100Trainer] Phase 2a: Training IQL Critics (Iteration 7)
[IQL] Epoch 0/20, V Loss: 0.0002, Q Loss: 0.0055
[IQL] Epoch 1/20, V Loss: 0.0002, Q Loss: 0.0055
[IQL] Epoch 2/20, V Loss: 0.0002, Q Loss: 0.0055
[IQL] Epoch 3/20, V Loss: 0.0002, Q Loss: 0.0053
[IQL] Epoch 4/20, V Loss: 0.0002, Q Loss: 0.0054
[IQL] Epoch 5/20, V Loss: 0.0002, Q Loss: 0.0053
[IQL] Epoch 6/20, V Loss: 0.0002, Q Loss: 0.0054
[IQL] Epoch 7/20, V Loss: 0.0002, Q Loss: 0.0053
[IQL] Epoch 8/20, V Loss: 0.0002, Q Loss: 0.0054
[IQL] Epoch 9/20, V Loss: 0.0002, Q Loss: 0.0054
[IQL] Epoch 10/20, V Loss: 0.0002, Q Loss: 0.0053
[IQL] Epoch 11/20, V Loss: 0.0002, Q Loss: 0.0053
[IQL] Epoch 12/20, V Loss: 0.0002, Q Loss: 0.0053
[IQL] Epoch 13/20, V Loss: 0.0002, Q Loss: 0.0053
[IQL] Epoch 14/20, V Loss: 0.0002, Q Loss: 0.0053
[IQL] Epoch 15/20, V Loss: 0.0002, Q Loss: 0.0053
[IQL] Epoch 16/20, V Loss: 0.0002, Q Loss: 0.0053
[IQL] Epoch 17/20, V Loss: 0.0002, Q Loss: 0.0053
[IQL] Epoch 18/20, V Loss: 0.0002, Q Loss: 0.0054
[IQL] Epoch 19/20, V Loss: 0.0002, Q Loss: 0.0052
[Plot] Saved: /nfs_global/S/yangrongzheng/RL100/3D-Diffusion-Policy/3D-Diffusion-Policy/plots/iql_q_loss_iter_07.png
[Plot] Saved: /nfs_global/S/yangrongzheng/RL100/3D-Diffusion-Policy/3D-Diffusion-Policy/plots/iql_v_loss_iter_07.png

[RL100Trainer] Phase 2b: Offline RL Optimization (Iteration 7)
[OPE] Behavior policy value J_old = 0.6570
[RL PPO] Reducing policy LR: 1.00e-04 → 1.00e-05
[Offline RL] Epoch 0/20, PPO Loss: -0.0207, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 12.3355, Reg Loss: 0.0000, CD Loss: 0.1798
[Offline RL] Epoch 1/20, PPO Loss: -0.0178, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 12.6297, Reg Loss: 0.0000, CD Loss: 0.0446
[Offline RL] Epoch 2/20, PPO Loss: -0.0172, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 12.4046, Reg Loss: 0.0000, CD Loss: 0.0332
[Offline RL] Epoch 3/20, PPO Loss: -0.0169, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 12.9495, Reg Loss: 0.0000, CD Loss: 0.0221
[Offline RL] Epoch 4/20, PPO Loss: -0.0164, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 12.5326, Reg Loss: 0.0000, CD Loss: 0.0172
[Offline RL] Epoch 5/20, PPO Loss: -0.0156, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 12.9491, Reg Loss: 0.0000, CD Loss: 0.0144
[Offline RL] Epoch 6/20, PPO Loss: -0.0165, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 12.6023, Reg Loss: 0.0000, CD Loss: 0.0133
[Offline RL] Epoch 7/20, PPO Loss: -0.0167, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 12.8250, Reg Loss: 0.0000, CD Loss: 0.0131
[Offline RL] Epoch 8/20, PPO Loss: -0.0166, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 12.8942, Reg Loss: 0.0000, CD Loss: 0.0126
[Offline RL] Epoch 9/20, PPO Loss: -0.0166, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 12.9734, Reg Loss: 0.0000, CD Loss: 0.0116
[Offline RL] Epoch 10/20, PPO Loss: -0.0164, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 12.9866, Reg Loss: 0.0000, CD Loss: 0.0110
[Offline RL] Epoch 11/20, PPO Loss: -0.0170, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 12.9185, Reg Loss: 0.0000, CD Loss: 0.0112
[Offline RL] Epoch 12/20, PPO Loss: -0.0184, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 12.6607, Reg Loss: 0.0000, CD Loss: 0.0152
[Offline RL] Epoch 13/20, PPO Loss: -0.0180, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 13.3160, Reg Loss: 0.0000, CD Loss: 0.0126
[Offline RL] Epoch 14/20, PPO Loss: -0.0182, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 13.2156, Reg Loss: 0.0000, CD Loss: 0.0126
[Offline RL] Epoch 15/20, PPO Loss: -0.0181, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 12.9207, Reg Loss: 0.0000, CD Loss: 0.0124
[Offline RL] Epoch 16/20, PPO Loss: -0.0177, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 13.1360, Reg Loss: 0.0000, CD Loss: 0.0120
[Offline RL] Epoch 17/20, PPO Loss: -0.0181, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 13.0867, Reg Loss: 0.0000, CD Loss: 0.0132
[Offline RL] Epoch 18/20, PPO Loss: -0.0176, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 13.3063, Reg Loss: 0.0000, CD Loss: 0.0118
[Offline RL] Epoch 19/20, PPO Loss: -0.0180, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 12.9497, Reg Loss: 0.0000, CD Loss: 0.0115
[Plot] Saved: /nfs_global/S/yangrongzheng/RL100/3D-Diffusion-Policy/3D-Diffusion-Policy/plots/ppo_loss_iter_07.png
[OPE] Policy REJECTED: J_new=0.6570 ≤ J_old=0.6570 + δ=0.0329. Rolling back to behavior policy.

[RL100Trainer] Phase 2c: Collecting New Data (Iteration 7)
[Collect] 20 episodes, success=0.650, env_return=1064.07, rl_reward=0.65, steps=4000
[Data Collection] Success Rate: 0.650, EnvReturn: 1064.07, RLReward: 0.65, Episodes: 20, Steps: 4000
[Dataset] offline collection: keeping 13/20 successful episodes (dropped 7 failures) before merge.
[Dataset] Merged 13 episodes (2600 steps) → total 43600 steps, 218 episodes

[RL100Trainer] Retraining IL on merged dataset...

============================================================
[RL100Trainer] Phase 1: Imitation Learning
============================================================

[IL] Epoch 0/100, Loss: 0.0047, Val Loss: 0.0192
[IL] Epoch 1/100, Loss: 0.0043, Val Loss: 0.0087
[IL] Epoch 2/100, Loss: 0.0041, Val Loss: 0.0192
[IL] Epoch 3/100, Loss: 0.0045, Val Loss: 0.0113
[IL] Epoch 4/100, Loss: 0.0041, Val Loss: 0.0111
[IL] Epoch 5/100, Loss: 0.0044, Val Loss: 0.0193
[IL] Epoch 6/100, Loss: 0.0044, Val Loss: 0.0194
[IL] Epoch 7/100, Loss: 0.0044, Val Loss: 0.0106
[IL] Epoch 8/100, Loss: 0.0047, Val Loss: 0.0098
[IL] Epoch 9/100, Loss: 0.0042, Val Loss: 0.0111
[IL] Epoch 10/100, Loss: 0.0041, Val Loss: 0.0219
[IL] Epoch 11/100, Loss: 0.0044, Val Loss: 0.0171
[IL] Epoch 12/100, Loss: 0.0039, Val Loss: 0.0140
[IL] Epoch 13/100, Loss: 0.0042, Val Loss: 0.0126
[IL] Epoch 14/100, Loss: 0.0039, Val Loss: 0.0149
[IL] Epoch 15/100, Loss: 0.0045, Val Loss: 0.0167
[IL] Epoch 16/100, Loss: 0.0040, Val Loss: 0.0106
[IL] Epoch 17/100, Loss: 0.0041, Val Loss: 0.0190
[IL] Epoch 18/100, Loss: 0.0044, Val Loss: 0.0134
[IL] Epoch 19/100, Loss: 0.0041, Val Loss: 0.0114
[IL] Epoch 20/100, Loss: 0.0042, Val Loss: 0.0208
[IL] Epoch 21/100, Loss: 0.0039, Val Loss: 0.0119
[IL] Epoch 22/100, Loss: 0.0041, Val Loss: 0.0224
[IL] Epoch 23/100, Loss: 0.0040, Val Loss: 0.0140
[IL] Epoch 24/100, Loss: 0.0039, Val Loss: 0.0183
[IL] Epoch 25/100, Loss: 0.0042, Val Loss: 0.0244
[IL] Epoch 26/100, Loss: 0.0039, Val Loss: 0.0140
[IL] Epoch 27/100, Loss: 0.0039, Val Loss: 0.0148
[IL] Epoch 28/100, Loss: 0.0041, Val Loss: 0.0132
[IL] Epoch 29/100, Loss: 0.0039, Val Loss: 0.0116
[IL] Epoch 30/100, Loss: 0.0040, Val Loss: 0.0192
[IL] Epoch 31/100, Loss: 0.0040, Val Loss: 0.0150
[IL] Epoch 32/100, Loss: 0.0035, Val Loss: 0.0177
[IL] Epoch 33/100, Loss: 0.0038, Val Loss: 0.0182
[IL] Epoch 34/100, Loss: 0.0039, Val Loss: 0.0204
[IL] Epoch 35/100, Loss: 0.0042, Val Loss: 0.0143
[IL] Epoch 36/100, Loss: 0.0039, Val Loss: 0.0146
[IL] Epoch 37/100, Loss: 0.0040, Val Loss: 0.0190
[IL] Epoch 38/100, Loss: 0.0036, Val Loss: 0.0137
[IL] Epoch 39/100, Loss: 0.0038, Val Loss: 0.0108
[IL] Epoch 40/100, Loss: 0.0043, Val Loss: 0.0152
[IL] Epoch 41/100, Loss: 0.0037, Val Loss: 0.0094
[IL] Epoch 42/100, Loss: 0.0037, Val Loss: 0.0169
[IL] Epoch 43/100, Loss: 0.0042, Val Loss: 0.0153
[IL] Epoch 44/100, Loss: 0.0037, Val Loss: 0.0127
[IL] Epoch 45/100, Loss: 0.0037, Val Loss: 0.0200
[IL] Epoch 46/100, Loss: 0.0037, Val Loss: 0.0211
[IL] Epoch 47/100, Loss: 0.0038, Val Loss: 0.0140
[IL] Epoch 48/100, Loss: 0.0037, Val Loss: 0.0151
[IL] Epoch 49/100, Loss: 0.0038, Val Loss: 0.0204
[IL] Epoch 50/100, Loss: 0.0039, Val Loss: 0.0136
[IL] Epoch 51/100, Loss: 0.0034, Val Loss: 0.0262
[IL] Epoch 52/100, Loss: 0.0037, Val Loss: 0.0152
[IL] Epoch 53/100, Loss: 0.0037, Val Loss: 0.0164
[IL] Epoch 54/100, Loss: 0.0038, Val Loss: 0.0172
[IL] Epoch 55/100, Loss: 0.0036, Val Loss: 0.0101
[IL] Epoch 56/100, Loss: 0.0037, Val Loss: 0.0105
[IL] Epoch 57/100, Loss: 0.0039, Val Loss: 0.0165
[IL] Epoch 58/100, Loss: 0.0035, Val Loss: 0.0131
[IL] Epoch 59/100, Loss: 0.0037, Val Loss: 0.0129
[IL] Epoch 60/100, Loss: 0.0037, Val Loss: 0.0155
[IL] Epoch 61/100, Loss: 0.0037, Val Loss: 0.0263
[IL] Epoch 62/100, Loss: 0.0041, Val Loss: 0.0127
[IL] Epoch 63/100, Loss: 0.0038, Val Loss: 0.0138
[IL] Epoch 64/100, Loss: 0.0040, Val Loss: 0.0135
[IL] Epoch 65/100, Loss: 0.0035, Val Loss: 0.0174
[IL] Epoch 66/100, Loss: 0.0035, Val Loss: 0.0127
[IL] Epoch 67/100, Loss: 0.0037, Val Loss: 0.0118
[IL] Epoch 68/100, Loss: 0.0034, Val Loss: 0.0101
[IL] Epoch 69/100, Loss: 0.0035, Val Loss: 0.0189
[IL] Epoch 70/100, Loss: 0.0039, Val Loss: 0.0134
[IL] Epoch 71/100, Loss: 0.0038, Val Loss: 0.0136
[IL] Epoch 72/100, Loss: 0.0036, Val Loss: 0.0138
[IL] Epoch 73/100, Loss: 0.0034, Val Loss: 0.0136
[IL] Epoch 74/100, Loss: 0.0034, Val Loss: 0.0127
[IL] Epoch 75/100, Loss: 0.0034, Val Loss: 0.0184
[IL] Epoch 76/100, Loss: 0.0035, Val Loss: 0.0173
[IL] Epoch 77/100, Loss: 0.0038, Val Loss: 0.0155
[IL] Epoch 78/100, Loss: 0.0035, Val Loss: 0.0158
[IL] Epoch 79/100, Loss: 0.0038, Val Loss: 0.0218
[IL] Epoch 80/100, Loss: 0.0037, Val Loss: 0.0107
[IL] Epoch 81/100, Loss: 0.0038, Val Loss: 0.0125
[IL] Epoch 82/100, Loss: 0.0038, Val Loss: 0.0160
[IL] Epoch 83/100, Loss: 0.0035, Val Loss: 0.0116
[IL] Epoch 84/100, Loss: 0.0038, Val Loss: 0.0130
[IL] Epoch 85/100, Loss: 0.0036, Val Loss: 0.0133
[IL] Epoch 86/100, Loss: 0.0034, Val Loss: 0.0135
[IL] Epoch 87/100, Loss: 0.0034, Val Loss: 0.0186
[IL] Epoch 88/100, Loss: 0.0036, Val Loss: 0.0128
[IL] Epoch 89/100, Loss: 0.0035, Val Loss: 0.0184
[IL] Epoch 90/100, Loss: 0.0033, Val Loss: 0.0197
[IL] Epoch 91/100, Loss: 0.0035, Val Loss: 0.0234
[IL] Epoch 92/100, Loss: 0.0035, Val Loss: 0.0159
[IL] Epoch 93/100, Loss: 0.0034, Val Loss: 0.0187
[IL] Epoch 94/100, Loss: 0.0036, Val Loss: 0.0122
[IL] Epoch 95/100, Loss: 0.0037, Val Loss: 0.0171
[IL] Epoch 96/100, Loss: 0.0035, Val Loss: 0.0130
[IL] Epoch 97/100, Loss: 0.0032, Val Loss: 0.0274
[IL] Epoch 98/100, Loss: 0.0035, Val Loss: 0.0101
[IL] Epoch 99/100, Loss: 0.0039, Val Loss: 0.0190
test_mean_score: 0.83
[IL] Eval - Success Rate: 0.830
[Plot] Saved: /nfs_global/S/yangrongzheng/RL100/3D-Diffusion-Policy/3D-Diffusion-Policy/plots/il_loss_retrain_iter_07.png
[Checkpoint] Saved to /nfs_global/S/yangrongzheng/RL100/3D-Diffusion-Policy/3D-Diffusion-Policy/checkpoints/offline_iter_7.ckpt

================================================================================
               OFFLINE RL ITERATION 9/10
================================================================================


[RL100Trainer] Line 6 — Training Transition Model T_θ (Iteration 8)

[TransitionModel] Encoding dataset for transition model training...
[TransitionModel] Dataset: 40144 samples, input_dim=288, target_dim=257
[TransitionModel] Epoch    0 | train=-123.29818 | val=0.00041 | no-improve=0/5
[TransitionModel] Epoch   16 | train=-132.07873 | val=0.00036 | no-improve=5/5
[TransitionModel] Training complete. Elites=[1, 2, 0, 4, 6], val_loss=0.00034

[RL100Trainer] Phase 2a: Training IQL Critics (Iteration 8)
[IQL] Epoch 0/20, V Loss: 0.0002, Q Loss: 0.0053
[IQL] Epoch 1/20, V Loss: 0.0002, Q Loss: 0.0053
[IQL] Epoch 2/20, V Loss: 0.0002, Q Loss: 0.0052
[IQL] Epoch 3/20, V Loss: 0.0002, Q Loss: 0.0052
[IQL] Epoch 4/20, V Loss: 0.0003, Q Loss: 0.0053
[IQL] Epoch 5/20, V Loss: 0.0002, Q Loss: 0.0052
[IQL] Epoch 6/20, V Loss: 0.0002, Q Loss: 0.0052
[IQL] Epoch 7/20, V Loss: 0.0002, Q Loss: 0.0051
[IQL] Epoch 8/20, V Loss: 0.0002, Q Loss: 0.0051
[IQL] Epoch 9/20, V Loss: 0.0002, Q Loss: 0.0051
[IQL] Epoch 10/20, V Loss: 0.0002, Q Loss: 0.0052
[IQL] Epoch 11/20, V Loss: 0.0002, Q Loss: 0.0051
[IQL] Epoch 12/20, V Loss: 0.0002, Q Loss: 0.0051
[IQL] Epoch 13/20, V Loss: 0.0002, Q Loss: 0.0050
[IQL] Epoch 14/20, V Loss: 0.0002, Q Loss: 0.0050
[IQL] Epoch 15/20, V Loss: 0.0002, Q Loss: 0.0050
[IQL] Epoch 16/20, V Loss: 0.0002, Q Loss: 0.0050
[IQL] Epoch 17/20, V Loss: 0.0002, Q Loss: 0.0050
[IQL] Epoch 18/20, V Loss: 0.0002, Q Loss: 0.0049
[IQL] Epoch 19/20, V Loss: 0.0002, Q Loss: 0.0050
[Plot] Saved: /nfs_global/S/yangrongzheng/RL100/3D-Diffusion-Policy/3D-Diffusion-Policy/plots/iql_q_loss_iter_08.png
[Plot] Saved: /nfs_global/S/yangrongzheng/RL100/3D-Diffusion-Policy/3D-Diffusion-Policy/plots/iql_v_loss_iter_08.png

[RL100Trainer] Phase 2b: Offline RL Optimization (Iteration 8)
[OPE] Behavior policy value J_old = 0.6955
[RL PPO] Reducing policy LR: 1.00e-04 → 1.00e-05
[Offline RL] Epoch 0/20, PPO Loss: -0.0194, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 12.0036, Reg Loss: 0.0000, CD Loss: 0.1690
[Offline RL] Epoch 1/20, PPO Loss: -0.0169, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 12.1671, Reg Loss: 0.0000, CD Loss: 0.0419
[Offline RL] Epoch 2/20, PPO Loss: -0.0163, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 12.1037, Reg Loss: 0.0000, CD Loss: 0.0293
[Offline RL] Epoch 3/20, PPO Loss: -0.0157, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 12.2543, Reg Loss: 0.0000, CD Loss: 0.0196
[Offline RL] Epoch 4/20, PPO Loss: -0.0151, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 12.2565, Reg Loss: 0.0000, CD Loss: 0.0163
[Offline RL] Epoch 5/20, PPO Loss: -0.0143, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 12.5673, Reg Loss: 0.0000, CD Loss: 0.0137
[Offline RL] Epoch 6/20, PPO Loss: -0.0142, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 12.5145, Reg Loss: 0.0000, CD Loss: 0.0131
[Offline RL] Epoch 7/20, PPO Loss: -0.0143, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 12.4719, Reg Loss: 0.0000, CD Loss: 0.0120
[Offline RL] Epoch 8/20, PPO Loss: -0.0144, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 12.1708, Reg Loss: 0.0000, CD Loss: 0.0114
[Offline RL] Epoch 9/20, PPO Loss: -0.0147, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 12.2713, Reg Loss: 0.0000, CD Loss: 0.0113
[Offline RL] Epoch 10/20, PPO Loss: -0.0151, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 12.4653, Reg Loss: 0.0000, CD Loss: 0.0106
[Offline RL] Epoch 11/20, PPO Loss: -0.0157, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 12.5304, Reg Loss: 0.0000, CD Loss: 0.0098
[Offline RL] Epoch 12/20, PPO Loss: -0.0159, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 12.5208, Reg Loss: 0.0000, CD Loss: 0.0096
[Offline RL] Epoch 13/20, PPO Loss: -0.0159, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 12.8254, Reg Loss: 0.0000, CD Loss: 0.0095
[Offline RL] Epoch 14/20, PPO Loss: -0.0168, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 12.5691, Reg Loss: 0.0000, CD Loss: 0.0094
[Offline RL] Epoch 15/20, PPO Loss: -0.0170, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 12.8016, Reg Loss: 0.0000, CD Loss: 0.0092
[Offline RL] Epoch 16/20, PPO Loss: -0.0171, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 12.7430, Reg Loss: 0.0000, CD Loss: 0.0094
[Offline RL] Epoch 17/20, PPO Loss: -0.0172, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 12.8239, Reg Loss: 0.0000, CD Loss: 0.0098
[Offline RL] Epoch 18/20, PPO Loss: -0.0173, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 13.2046, Reg Loss: 0.0000, CD Loss: 0.0113
[Offline RL] Epoch 19/20, PPO Loss: -0.0172, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 13.1984, Reg Loss: 0.0000, CD Loss: 0.0113
[Plot] Saved: /nfs_global/S/yangrongzheng/RL100/3D-Diffusion-Policy/3D-Diffusion-Policy/plots/ppo_loss_iter_08.png
[OPE] Policy REJECTED: J_new=0.7074 ≤ J_old=0.6955 + δ=0.0348. Rolling back to behavior policy.

[RL100Trainer] Phase 2c: Collecting New Data (Iteration 8)
[Collect] 20 episodes, success=1.000, env_return=1093.36, rl_reward=1.00, steps=4000
[Data Collection] Success Rate: 1.000, EnvReturn: 1093.36, RLReward: 1.00, Episodes: 20, Steps: 4000
[Dataset] offline collection: keeping 20/20 successful episodes (dropped 0 failures) before merge.
[Dataset] Merged 20 episodes (4000 steps) → total 47600 steps, 238 episodes

[RL100Trainer] Retraining IL on merged dataset...

============================================================
[RL100Trainer] Phase 1: Imitation Learning
============================================================

[IL] Epoch 0/100, Loss: 0.0053, Val Loss: 0.0109
[IL] Epoch 1/100, Loss: 0.0044, Val Loss: 0.0171
[IL] Epoch 2/100, Loss: 0.0048, Val Loss: 0.0123
[IL] Epoch 3/100, Loss: 0.0043, Val Loss: 0.0127
[IL] Epoch 4/100, Loss: 0.0042, Val Loss: 0.0163
[IL] Epoch 5/100, Loss: 0.0040, Val Loss: 0.0095
[IL] Epoch 6/100, Loss: 0.0040, Val Loss: 0.0143
[IL] Epoch 7/100, Loss: 0.0041, Val Loss: 0.0153
[IL] Epoch 8/100, Loss: 0.0041, Val Loss: 0.0154
[IL] Epoch 9/100, Loss: 0.0041, Val Loss: 0.0133
[IL] Epoch 10/100, Loss: 0.0037, Val Loss: 0.0132
[IL] Epoch 11/100, Loss: 0.0038, Val Loss: 0.0102
[IL] Epoch 12/100, Loss: 0.0040, Val Loss: 0.0213
[IL] Epoch 13/100, Loss: 0.0040, Val Loss: 0.0125
[IL] Epoch 14/100, Loss: 0.0040, Val Loss: 0.0172
[IL] Epoch 15/100, Loss: 0.0039, Val Loss: 0.0135
[IL] Epoch 16/100, Loss: 0.0036, Val Loss: 0.0132
[IL] Epoch 17/100, Loss: 0.0038, Val Loss: 0.0127
[IL] Epoch 18/100, Loss: 0.0037, Val Loss: 0.0137
[IL] Epoch 19/100, Loss: 0.0039, Val Loss: 0.0163
[IL] Epoch 20/100, Loss: 0.0038, Val Loss: 0.0109
[IL] Epoch 21/100, Loss: 0.0035, Val Loss: 0.0128
[IL] Epoch 22/100, Loss: 0.0034, Val Loss: 0.0213
[IL] Epoch 23/100, Loss: 0.0040, Val Loss: 0.0144
[IL] Epoch 24/100, Loss: 0.0040, Val Loss: 0.0124
[IL] Epoch 25/100, Loss: 0.0037, Val Loss: 0.0168
[IL] Epoch 26/100, Loss: 0.0038, Val Loss: 0.0210
[IL] Epoch 27/100, Loss: 0.0037, Val Loss: 0.0167
[IL] Epoch 28/100, Loss: 0.0041, Val Loss: 0.0148
[IL] Epoch 29/100, Loss: 0.0036, Val Loss: 0.0131
[IL] Epoch 30/100, Loss: 0.0040, Val Loss: 0.0129
[IL] Epoch 31/100, Loss: 0.0035, Val Loss: 0.0171
[IL] Epoch 32/100, Loss: 0.0039, Val Loss: 0.0186
[IL] Epoch 33/100, Loss: 0.0036, Val Loss: 0.0159
[IL] Epoch 34/100, Loss: 0.0037, Val Loss: 0.0129
[IL] Epoch 35/100, Loss: 0.0036, Val Loss: 0.0172
[IL] Epoch 36/100, Loss: 0.0033, Val Loss: 0.0172
[IL] Epoch 37/100, Loss: 0.0035, Val Loss: 0.0140
[IL] Epoch 38/100, Loss: 0.0039, Val Loss: 0.0122
[IL] Epoch 39/100, Loss: 0.0035, Val Loss: 0.0190
[IL] Epoch 40/100, Loss: 0.0035, Val Loss: 0.0159
[IL] Epoch 41/100, Loss: 0.0036, Val Loss: 0.0125
[IL] Epoch 42/100, Loss: 0.0034, Val Loss: 0.0180
[IL] Epoch 43/100, Loss: 0.0038, Val Loss: 0.0163
[IL] Epoch 44/100, Loss: 0.0034, Val Loss: 0.0123
[IL] Epoch 45/100, Loss: 0.0033, Val Loss: 0.0189
[IL] Epoch 46/100, Loss: 0.0034, Val Loss: 0.0147
[IL] Epoch 47/100, Loss: 0.0035, Val Loss: 0.0146
[IL] Epoch 48/100, Loss: 0.0038, Val Loss: 0.0107
[IL] Epoch 49/100, Loss: 0.0038, Val Loss: 0.0125
[IL] Epoch 50/100, Loss: 0.0034, Val Loss: 0.0154
[IL] Epoch 51/100, Loss: 0.0038, Val Loss: 0.0122
[IL] Epoch 52/100, Loss: 0.0034, Val Loss: 0.0148
[IL] Epoch 53/100, Loss: 0.0033, Val Loss: 0.0141
[IL] Epoch 54/100, Loss: 0.0036, Val Loss: 0.0160
[IL] Epoch 55/100, Loss: 0.0039, Val Loss: 0.0104
[IL] Epoch 56/100, Loss: 0.0041, Val Loss: 0.0168
[IL] Epoch 57/100, Loss: 0.0036, Val Loss: 0.0153
[IL] Epoch 58/100, Loss: 0.0033, Val Loss: 0.0175
[IL] Epoch 59/100, Loss: 0.0033, Val Loss: 0.0128
[IL] Epoch 60/100, Loss: 0.0035, Val Loss: 0.0164
[IL] Epoch 61/100, Loss: 0.0034, Val Loss: 0.0213
[IL] Epoch 62/100, Loss: 0.0034, Val Loss: 0.0162
[IL] Epoch 63/100, Loss: 0.0035, Val Loss: 0.0162
[IL] Epoch 64/100, Loss: 0.0035, Val Loss: 0.0137
[IL] Epoch 65/100, Loss: 0.0032, Val Loss: 0.0143
[IL] Epoch 66/100, Loss: 0.0032, Val Loss: 0.0134
[IL] Epoch 67/100, Loss: 0.0033, Val Loss: 0.0116
[IL] Epoch 68/100, Loss: 0.0032, Val Loss: 0.0123
[IL] Epoch 69/100, Loss: 0.0031, Val Loss: 0.0116
[IL] Epoch 70/100, Loss: 0.0037, Val Loss: 0.0118
[IL] Epoch 71/100, Loss: 0.0034, Val Loss: 0.0144
[IL] Epoch 72/100, Loss: 0.0034, Val Loss: 0.0151
[IL] Epoch 73/100, Loss: 0.0036, Val Loss: 0.0091
[IL] Epoch 74/100, Loss: 0.0033, Val Loss: 0.0099
[IL] Epoch 75/100, Loss: 0.0038, Val Loss: 0.0093
[IL] Epoch 76/100, Loss: 0.0034, Val Loss: 0.0127
[IL] Epoch 77/100, Loss: 0.0034, Val Loss: 0.0146
[IL] Epoch 78/100, Loss: 0.0033, Val Loss: 0.0128
[IL] Epoch 79/100, Loss: 0.0036, Val Loss: 0.0101
[IL] Epoch 80/100, Loss: 0.0034, Val Loss: 0.0200
[IL] Epoch 81/100, Loss: 0.0033, Val Loss: 0.0118
[IL] Epoch 82/100, Loss: 0.0035, Val Loss: 0.0138
[IL] Epoch 83/100, Loss: 0.0033, Val Loss: 0.0177
[IL] Epoch 84/100, Loss: 0.0036, Val Loss: 0.0217
[IL] Epoch 85/100, Loss: 0.0031, Val Loss: 0.0175
[IL] Epoch 86/100, Loss: 0.0033, Val Loss: 0.0142
[IL] Epoch 87/100, Loss: 0.0031, Val Loss: 0.0245
[IL] Epoch 88/100, Loss: 0.0034, Val Loss: 0.0155
[IL] Epoch 89/100, Loss: 0.0035, Val Loss: 0.0178
[IL] Epoch 90/100, Loss: 0.0032, Val Loss: 0.0154
[IL] Epoch 91/100, Loss: 0.0033, Val Loss: 0.0145
[IL] Epoch 92/100, Loss: 0.0034, Val Loss: 0.0172
[IL] Epoch 93/100, Loss: 0.0039, Val Loss: 0.0137
[IL] Epoch 94/100, Loss: 0.0033, Val Loss: 0.0153
[IL] Epoch 95/100, Loss: 0.0033, Val Loss: 0.0142
[IL] Epoch 96/100, Loss: 0.0032, Val Loss: 0.0133
[IL] Epoch 97/100, Loss: 0.0033, Val Loss: 0.0145
[IL] Epoch 98/100, Loss: 0.0030, Val Loss: 0.0178
[IL] Epoch 99/100, Loss: 0.0031, Val Loss: 0.0172
test_mean_score: 0.76
[IL] Eval - Success Rate: 0.760
[Plot] Saved: /nfs_global/S/yangrongzheng/RL100/3D-Diffusion-Policy/3D-Diffusion-Policy/plots/il_loss_retrain_iter_08.png
[Checkpoint] Saved to /nfs_global/S/yangrongzheng/RL100/3D-Diffusion-Policy/3D-Diffusion-Policy/checkpoints/offline_iter_8.ckpt

================================================================================
               OFFLINE RL ITERATION 10/10
================================================================================


[RL100Trainer] Line 6 — Training Transition Model T_θ (Iteration 9)

[TransitionModel] Encoding dataset for transition model training...
[TransitionModel] Dataset: 44004 samples, input_dim=288, target_dim=257
[TransitionModel] Epoch    0 | train=-129.37589 | val=0.00041 | no-improve=0/5
[TransitionModel] Epoch   20 | train=-140.95636 | val=0.00040 | no-improve=4/5
[TransitionModel] Epoch   21 | train=-141.36144 | val=0.00043 | no-improve=5/5
[TransitionModel] Training complete. Elites=[6, 4, 2, 1, 3], val_loss=0.00036

[RL100Trainer] Phase 2a: Training IQL Critics (Iteration 9)
[IQL] Epoch 0/20, V Loss: 0.0002, Q Loss: 0.0050
[IQL] Epoch 1/20, V Loss: 0.0002, Q Loss: 0.0051
[IQL] Epoch 2/20, V Loss: 0.0002, Q Loss: 0.0051
[IQL] Epoch 3/20, V Loss: 0.0002, Q Loss: 0.0050
[IQL] Epoch 4/20, V Loss: 0.0002, Q Loss: 0.0050
[IQL] Epoch 5/20, V Loss: 0.0002, Q Loss: 0.0050
[IQL] Epoch 6/20, V Loss: 0.0002, Q Loss: 0.0050
[IQL] Epoch 7/20, V Loss: 0.0002, Q Loss: 0.0050
[IQL] Epoch 8/20, V Loss: 0.0002, Q Loss: 0.0049
[IQL] Epoch 9/20, V Loss: 0.0002, Q Loss: 0.0050
[IQL] Epoch 10/20, V Loss: 0.0002, Q Loss: 0.0049
[IQL] Epoch 11/20, V Loss: 0.0002, Q Loss: 0.0050
[IQL] Epoch 12/20, V Loss: 0.0002, Q Loss: 0.0049
[IQL] Epoch 13/20, V Loss: 0.0002, Q Loss: 0.0049
[IQL] Epoch 14/20, V Loss: 0.0002, Q Loss: 0.0049
[IQL] Epoch 15/20, V Loss: 0.0002, Q Loss: 0.0049
[IQL] Epoch 16/20, V Loss: 0.0002, Q Loss: 0.0049
[IQL] Epoch 17/20, V Loss: 0.0002, Q Loss: 0.0048
[IQL] Epoch 18/20, V Loss: 0.0002, Q Loss: 0.0048
[IQL] Epoch 19/20, V Loss: 0.0002, Q Loss: 0.0047
[Plot] Saved: /nfs_global/S/yangrongzheng/RL100/3D-Diffusion-Policy/3D-Diffusion-Policy/plots/iql_q_loss_iter_09.png
[Plot] Saved: /nfs_global/S/yangrongzheng/RL100/3D-Diffusion-Policy/3D-Diffusion-Policy/plots/iql_v_loss_iter_09.png

[RL100Trainer] Phase 2b: Offline RL Optimization (Iteration 9)
[OPE] Behavior policy value J_old = 0.6925
[RL PPO] Reducing policy LR: 1.00e-04 → 1.00e-05
[Offline RL] Epoch 0/20, PPO Loss: -0.0169, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 11.3608, Reg Loss: 0.0000, CD Loss: 0.1600
[Offline RL] Epoch 1/20, PPO Loss: -0.0140, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 11.8784, Reg Loss: 0.0000, CD Loss: 0.0413
[Offline RL] Epoch 2/20, PPO Loss: -0.0136, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 12.1001, Reg Loss: 0.0000, CD Loss: 0.0279
[Offline RL] Epoch 3/20, PPO Loss: -0.0134, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 12.0992, Reg Loss: 0.0000, CD Loss: 0.0194
[Offline RL] Epoch 4/20, PPO Loss: -0.0134, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 12.0618, Reg Loss: 0.0000, CD Loss: 0.0176
[Offline RL] Epoch 5/20, PPO Loss: -0.0137, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 11.9528, Reg Loss: 0.0000, CD Loss: 0.0153
[Offline RL] Epoch 6/20, PPO Loss: -0.0131, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 12.2087, Reg Loss: 0.0000, CD Loss: 0.0139
[Offline RL] Epoch 7/20, PPO Loss: -0.0133, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 12.0402, Reg Loss: 0.0000, CD Loss: 0.0127
[Offline RL] Epoch 8/20, PPO Loss: -0.0130, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 12.0714, Reg Loss: 0.0000, CD Loss: 0.0130
[Offline RL] Epoch 9/20, PPO Loss: -0.0140, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 12.0427, Reg Loss: 0.0000, CD Loss: 0.0128
[Offline RL] Epoch 10/20, PPO Loss: -0.0142, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 12.2452, Reg Loss: 0.0000, CD Loss: 0.0126
[Offline RL] Epoch 11/20, PPO Loss: -0.0147, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 12.2497, Reg Loss: 0.0000, CD Loss: 0.0114
[Offline RL] Epoch 12/20, PPO Loss: -0.0142, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 12.5611, Reg Loss: 0.0000, CD Loss: 0.0104
[Offline RL] Epoch 13/20, PPO Loss: -0.0142, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 12.7843, Reg Loss: 0.0000, CD Loss: 0.0103
[Offline RL] Epoch 14/20, PPO Loss: -0.0145, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 12.4634, Reg Loss: 0.0000, CD Loss: 0.0098
[Offline RL] Epoch 15/20, PPO Loss: -0.0148, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 12.4772, Reg Loss: 0.0000, CD Loss: 0.0096
[Offline RL] Epoch 16/20, PPO Loss: -0.0149, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 12.4020, Reg Loss: 0.0000, CD Loss: 0.0095
[Offline RL] Epoch 17/20, PPO Loss: -0.0148, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 12.4835, Reg Loss: 0.0000, CD Loss: 0.0096
[Offline RL] Epoch 18/20, PPO Loss: -0.0148, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 12.7930, Reg Loss: 0.0000, CD Loss: 0.0097
[Offline RL] Epoch 19/20, PPO Loss: -0.0150, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 12.4565, Reg Loss: 0.0000, CD Loss: 0.0108
[Plot] Saved: /nfs_global/S/yangrongzheng/RL100/3D-Diffusion-Policy/3D-Diffusion-Policy/plots/ppo_loss_iter_09.png
[OPE] Policy REJECTED: J_new=0.7103 ≤ J_old=0.6925 + δ=0.0346. Rolling back to behavior policy.

[RL100Trainer] Phase 2c: Collecting New Data (Iteration 9)
[Collect] 20 episodes, success=0.850, env_return=1230.73, rl_reward=0.85, steps=4000
[Data Collection] Success Rate: 0.850, EnvReturn: 1230.73, RLReward: 0.85, Episodes: 20, Steps: 4000
[Dataset] offline collection: keeping 17/20 successful episodes (dropped 3 failures) before merge.
[Dataset] Merged 17 episodes (3400 steps) → total 51000 steps, 255 episodes

[RL100Trainer] Retraining IL on merged dataset...

============================================================
[RL100Trainer] Phase 1: Imitation Learning
============================================================

[IL] Epoch 0/100, Loss: 0.0059, Val Loss: 0.0126
[IL] Epoch 1/100, Loss: 0.0038, Val Loss: 0.0120
[IL] Epoch 2/100, Loss: 0.0037, Val Loss: 0.0173
[IL] Epoch 3/100, Loss: 0.0036, Val Loss: 0.0124
[IL] Epoch 4/100, Loss: 0.0036, Val Loss: 0.0122
[IL] Epoch 5/100, Loss: 0.0038, Val Loss: 0.0165
[IL] Epoch 6/100, Loss: 0.0036, Val Loss: 0.0127
[IL] Epoch 7/100, Loss: 0.0038, Val Loss: 0.0127
[IL] Epoch 8/100, Loss: 0.0037, Val Loss: 0.0179
[IL] Epoch 9/100, Loss: 0.0037, Val Loss: 0.0098
[IL] Epoch 10/100, Loss: 0.0037, Val Loss: 0.0137
[IL] Epoch 11/100, Loss: 0.0038, Val Loss: 0.0144
[IL] Epoch 12/100, Loss: 0.0035, Val Loss: 0.0143
[IL] Epoch 13/100, Loss: 0.0037, Val Loss: 0.0144
[IL] Epoch 14/100, Loss: 0.0034, Val Loss: 0.0098
[IL] Epoch 15/100, Loss: 0.0033, Val Loss: 0.0212
[IL] Epoch 16/100, Loss: 0.0035, Val Loss: 0.0133
[IL] Epoch 17/100, Loss: 0.0034, Val Loss: 0.0177
[IL] Epoch 18/100, Loss: 0.0034, Val Loss: 0.0131
[IL] Epoch 19/100, Loss: 0.0033, Val Loss: 0.0225
[IL] Epoch 20/100, Loss: 0.0036, Val Loss: 0.0119
[IL] Epoch 21/100, Loss: 0.0036, Val Loss: 0.0118
[IL] Epoch 22/100, Loss: 0.0033, Val Loss: 0.0111
[IL] Epoch 23/100, Loss: 0.0033, Val Loss: 0.0178
[IL] Epoch 24/100, Loss: 0.0034, Val Loss: 0.0141
[IL] Epoch 25/100, Loss: 0.0033, Val Loss: 0.0130
[IL] Epoch 26/100, Loss: 0.0034, Val Loss: 0.0126
[IL] Epoch 27/100, Loss: 0.0034, Val Loss: 0.0130
[IL] Epoch 28/100, Loss: 0.0036, Val Loss: 0.0169
[IL] Epoch 29/100, Loss: 0.0033, Val Loss: 0.0191
[IL] Epoch 30/100, Loss: 0.0035, Val Loss: 0.0166
[IL] Epoch 31/100, Loss: 0.0037, Val Loss: 0.0114
[IL] Epoch 32/100, Loss: 0.0037, Val Loss: 0.0141
[IL] Epoch 33/100, Loss: 0.0035, Val Loss: 0.0137
[IL] Epoch 34/100, Loss: 0.0032, Val Loss: 0.0118
[IL] Epoch 35/100, Loss: 0.0034, Val Loss: 0.0216
[IL] Epoch 36/100, Loss: 0.0034, Val Loss: 0.0149
[IL] Epoch 37/100, Loss: 0.0034, Val Loss: 0.0108
[IL] Epoch 38/100, Loss: 0.0031, Val Loss: 0.0153
[IL] Epoch 39/100, Loss: 0.0033, Val Loss: 0.0144
[IL] Epoch 40/100, Loss: 0.0034, Val Loss: 0.0158
[IL] Epoch 41/100, Loss: 0.0035, Val Loss: 0.0135
[IL] Epoch 42/100, Loss: 0.0031, Val Loss: 0.0160
[IL] Epoch 43/100, Loss: 0.0032, Val Loss: 0.0153
[IL] Epoch 44/100, Loss: 0.0034, Val Loss: 0.0144
[IL] Epoch 45/100, Loss: 0.0031, Val Loss: 0.0233
[IL] Epoch 46/100, Loss: 0.0032, Val Loss: 0.0173
[IL] Epoch 47/100, Loss: 0.0029, Val Loss: 0.0199
[IL] Epoch 48/100, Loss: 0.0032, Val Loss: 0.0187
[IL] Epoch 49/100, Loss: 0.0038, Val Loss: 0.0154
[IL] Epoch 50/100, Loss: 0.0031, Val Loss: 0.0124
[IL] Epoch 51/100, Loss: 0.0029, Val Loss: 0.0153
[IL] Epoch 52/100, Loss: 0.0032, Val Loss: 0.0162
[IL] Epoch 53/100, Loss: 0.0033, Val Loss: 0.0183
[IL] Epoch 54/100, Loss: 0.0030, Val Loss: 0.0096
[IL] Epoch 55/100, Loss: 0.0029, Val Loss: 0.0125
[IL] Epoch 56/100, Loss: 0.0035, Val Loss: 0.0183
[IL] Epoch 57/100, Loss: 0.0034, Val Loss: 0.0164
[IL] Epoch 58/100, Loss: 0.0033, Val Loss: 0.0181
[IL] Epoch 59/100, Loss: 0.0032, Val Loss: 0.0233
[IL] Epoch 60/100, Loss: 0.0034, Val Loss: 0.0177
[IL] Epoch 61/100, Loss: 0.0031, Val Loss: 0.0150
[IL] Epoch 62/100, Loss: 0.0031, Val Loss: 0.0190
[IL] Epoch 63/100, Loss: 0.0031, Val Loss: 0.0159
[IL] Epoch 64/100, Loss: 0.0032, Val Loss: 0.0142
[IL] Epoch 65/100, Loss: 0.0032, Val Loss: 0.0119
[IL] Epoch 66/100, Loss: 0.0031, Val Loss: 0.0172
[IL] Epoch 67/100, Loss: 0.0030, Val Loss: 0.0154
[IL] Epoch 68/100, Loss: 0.0033, Val Loss: 0.0123
[IL] Epoch 69/100, Loss: 0.0031, Val Loss: 0.0171
[IL] Epoch 70/100, Loss: 0.0030, Val Loss: 0.0151
[IL] Epoch 71/100, Loss: 0.0031, Val Loss: 0.0320
[IL] Epoch 72/100, Loss: 0.0031, Val Loss: 0.0189
[IL] Epoch 73/100, Loss: 0.0031, Val Loss: 0.0163
[IL] Epoch 74/100, Loss: 0.0031, Val Loss: 0.0174
[IL] Epoch 75/100, Loss: 0.0031, Val Loss: 0.0121
[IL] Epoch 76/100, Loss: 0.0031, Val Loss: 0.0174
[IL] Epoch 77/100, Loss: 0.0031, Val Loss: 0.0168
[IL] Epoch 78/100, Loss: 0.0034, Val Loss: 0.0173
[IL] Epoch 79/100, Loss: 0.0032, Val Loss: 0.0155
[IL] Epoch 80/100, Loss: 0.0030, Val Loss: 0.0174
[IL] Epoch 81/100, Loss: 0.0031, Val Loss: 0.0105
[IL] Epoch 82/100, Loss: 0.0029, Val Loss: 0.0181
[IL] Epoch 83/100, Loss: 0.0031, Val Loss: 0.0120
[IL] Epoch 84/100, Loss: 0.0029, Val Loss: 0.0175
[IL] Epoch 85/100, Loss: 0.0031, Val Loss: 0.0132
[IL] Epoch 86/100, Loss: 0.0030, Val Loss: 0.0194
[IL] Epoch 87/100, Loss: 0.0028, Val Loss: 0.0112
[IL] Epoch 88/100, Loss: 0.0031, Val Loss: 0.0212
[IL] Epoch 89/100, Loss: 0.0031, Val Loss: 0.0142
[IL] Epoch 90/100, Loss: 0.0032, Val Loss: 0.0203
[IL] Epoch 91/100, Loss: 0.0031, Val Loss: 0.0148
[IL] Epoch 92/100, Loss: 0.0030, Val Loss: 0.0119
[IL] Epoch 93/100, Loss: 0.0029, Val Loss: 0.0164
[IL] Epoch 94/100, Loss: 0.0027, Val Loss: 0.0145
[IL] Epoch 95/100, Loss: 0.0028, Val Loss: 0.0129
[IL] Epoch 96/100, Loss: 0.0030, Val Loss: 0.0230
[IL] Epoch 97/100, Loss: 0.0030, Val Loss: 0.0257
[IL] Epoch 98/100, Loss: 0.0030, Val Loss: 0.0128
[IL] Epoch 99/100, Loss: 0.0032, Val Loss: 0.0182
test_mean_score: 0.82
[IL] Eval - Success Rate: 0.820
[Plot] Saved: /nfs_global/S/yangrongzheng/RL100/3D-Diffusion-Policy/3D-Diffusion-Policy/plots/il_loss_retrain_iter_09.png
[Checkpoint] Saved to /nfs_global/S/yangrongzheng/RL100/3D-Diffusion-Policy/3D-Diffusion-Policy/checkpoints/offline_iter_9.ckpt

================================================================================
                    PHASE 3: ONLINE RL FINE-TUNING
================================================================================


[Online RL] Iteration 1/10

[RL100Trainer] Phase 2c: Collecting New Data (Iteration 9)
[Collect] 20 episodes, success=0.800, env_return=1122.63, rl_reward=0.80, steps=4000
[Data Collection] Success Rate: 0.800, EnvReturn: 1122.63, RLReward: 0.80, Episodes: 20, Steps: 4000
[Dataset] online collection: keeping 16/20 successful episodes (dropped 4 failures) before merge.
[Online RL] Epoch 1/20, PPO Loss: -0.0054, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 24.3994, Reg Loss: 0.0000, CD Loss: 0.3341
[Online RL] Epoch 2/20, PPO Loss: -0.0470, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 19.9433, Reg Loss: 0.0000, CD Loss: 0.0000
[Online RL] Epoch 3/20, PPO Loss: -0.0286, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 15.4258, Reg Loss: 0.0000, CD Loss: 2.2487
[Online RL] Epoch 4/20, PPO Loss: -0.0624, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 20.6396, Reg Loss: 0.0000, CD Loss: 0.0000
[Online RL] Epoch 5/20, PPO Loss: -0.0903, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 16.2485, Reg Loss: 0.0000, CD Loss: 0.0000
[Online RL] Epoch 6/20, PPO Loss: -0.1052, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 14.8388, Reg Loss: 0.0000, CD Loss: 0.1460
[Online RL] Epoch 7/20, PPO Loss: -0.0929, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 11.6702, Reg Loss: 0.0000, CD Loss: 0.0000
[Online RL] Epoch 8/20, PPO Loss: -0.1171, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 13.6046, Reg Loss: 0.0000, CD Loss: 0.3465
[Online RL] Epoch 9/20, PPO Loss: -0.1391, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 9.7705, Reg Loss: 0.0000, CD Loss: 0.0000
[Online RL] Epoch 10/20, PPO Loss: -0.1533, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 8.2575, Reg Loss: 0.0000, CD Loss: 0.0000
[Online RL] Epoch 11/20, PPO Loss: -0.1327, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 8.0089, Reg Loss: 0.0000, CD Loss: 0.2392
[Online RL] Epoch 12/20, PPO Loss: -0.1263, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 5.6695, Reg Loss: 0.0000, CD Loss: 0.0000
[Online RL] Epoch 13/20, PPO Loss: -0.1496, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 5.8897, Reg Loss: 0.0000, CD Loss: 0.0854
[Online RL] Epoch 14/20, PPO Loss: -0.1088, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 4.9039, Reg Loss: 0.0000, CD Loss: 0.0000
[Online RL] Epoch 15/20, PPO Loss: -0.1199, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 4.9174, Reg Loss: 0.0000, CD Loss: 0.0000
[Online RL] Epoch 16/20, PPO Loss: -0.1373, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 10.1212, Reg Loss: 0.0000, CD Loss: 0.1027
[Online RL] Epoch 17/20, PPO Loss: -0.1323, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 4.9331, Reg Loss: 0.0000, CD Loss: 0.0000
[Online RL] Epoch 18/20, PPO Loss: -0.1587, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 4.0410, Reg Loss: 0.0000, CD Loss: 0.1456
[Online RL] Epoch 19/20, PPO Loss: -0.1468, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 2.9765, Reg Loss: 0.0000, CD Loss: 0.0000
[Online RL] Epoch 20/20, PPO Loss: -0.1255, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 4.7069, Reg Loss: 0.0000, CD Loss: 0.0000
[Plot] Saved: /nfs_global/S/yangrongzheng/RL100/3D-Diffusion-Policy/3D-Diffusion-Policy/plots/online_v_loss_iter_00.png
[Plot] Saved: /nfs_global/S/yangrongzheng/RL100/3D-Diffusion-Policy/3D-Diffusion-Policy/plots/online_ppo_loss_iter_00.png
[Plot] Saved: /nfs_global/S/yangrongzheng/RL100/3D-Diffusion-Policy/3D-Diffusion-Policy/plots/online_ppo_kl_iter_00.png
[Plot] Saved: /nfs_global/S/yangrongzheng/RL100/3D-Diffusion-Policy/3D-Diffusion-Policy/plots/online_ppo_clipfrac_iter_00.png
[Plot] Saved: /nfs_global/S/yangrongzheng/RL100/3D-Diffusion-Policy/3D-Diffusion-Policy/plots/online_ppo_gradnorm_iter_00.png
[Plot] Saved: /nfs_global/S/yangrongzheng/RL100/3D-Diffusion-Policy/3D-Diffusion-Policy/plots/online_cd_loss_iter_00.png
[Checkpoint] Saved to /nfs_global/S/yangrongzheng/RL100/3D-Diffusion-Policy/3D-Diffusion-Policy/checkpoints/online_iter_0.ckpt

[Online RL] Iteration 2/10

[RL100Trainer] Phase 2c: Collecting New Data (Iteration 9)
[Collect] 20 episodes, success=0.800, env_return=1156.84, rl_reward=0.80, steps=4000
[Data Collection] Success Rate: 0.800, EnvReturn: 1156.84, RLReward: 0.80, Episodes: 20, Steps: 4000
[Dataset] online collection: keeping 16/20 successful episodes (dropped 4 failures) before merge.
[Online RL] Epoch 1/20, PPO Loss: 0.0079, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 21.9492, Reg Loss: 0.0000, CD Loss: 0.1420
[Online RL] Epoch 2/20, PPO Loss: -0.0031, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 16.1033, Reg Loss: 0.0000, CD Loss: 0.0000
[Online RL] Epoch 3/20, PPO Loss: -0.0284, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 11.4954, Reg Loss: 0.0000, CD Loss: 0.1006
[Online RL] Epoch 4/20, PPO Loss: -0.0634, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 13.2697, Reg Loss: 0.0000, CD Loss: 0.0000
[Online RL] Epoch 5/20, PPO Loss: -0.1077, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 10.7468, Reg Loss: 0.0000, CD Loss: 0.0000
[Online RL] Epoch 6/20, PPO Loss: -0.1007, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 8.5198, Reg Loss: 0.0000, CD Loss: 0.0654
[Online RL] Epoch 7/20, PPO Loss: -0.1182, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 7.1921, Reg Loss: 0.0000, CD Loss: 0.0000
[Online RL] Epoch 8/20, PPO Loss: -0.1107, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 5.7128, Reg Loss: 0.0000, CD Loss: 0.0753
[Online RL] Epoch 9/20, PPO Loss: -0.1165, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 7.2493, Reg Loss: 0.0000, CD Loss: 0.0000
[Online RL] Epoch 10/20, PPO Loss: -0.1001, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 5.6774, Reg Loss: 0.0000, CD Loss: 0.0000
[Online RL] Epoch 11/20, PPO Loss: -0.1318, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 6.7369, Reg Loss: 0.0000, CD Loss: 0.0944
[Online RL] Epoch 12/20, PPO Loss: -0.1332, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 3.6800, Reg Loss: 0.0000, CD Loss: 0.0000
[Online RL] Epoch 13/20, PPO Loss: -0.1180, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 3.8767, Reg Loss: 0.0000, CD Loss: 0.1031
[Online RL] Epoch 14/20, PPO Loss: -0.1302, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 2.9819, Reg Loss: 0.0000, CD Loss: 0.0000
[Online RL] Epoch 15/20, PPO Loss: -0.1360, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 4.6709, Reg Loss: 0.0000, CD Loss: 0.0000
[Online RL] Epoch 16/20, PPO Loss: -0.1517, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 3.4778, Reg Loss: 0.0000, CD Loss: 0.0974
[Online RL] Epoch 17/20, PPO Loss: -0.1198, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 2.4315, Reg Loss: 0.0000, CD Loss: 0.0000
[Online RL] Epoch 18/20, PPO Loss: -0.1354, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 3.3053, Reg Loss: 0.0000, CD Loss: 0.0807
[Online RL] Epoch 19/20, PPO Loss: -0.1327, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 2.5991, Reg Loss: 0.0000, CD Loss: 0.0000
[Online RL] Epoch 20/20, PPO Loss: -0.1140, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 5.4033, Reg Loss: 0.0000, CD Loss: 0.0000
[Plot] Saved: /nfs_global/S/yangrongzheng/RL100/3D-Diffusion-Policy/3D-Diffusion-Policy/plots/online_v_loss_iter_01.png
[Plot] Saved: /nfs_global/S/yangrongzheng/RL100/3D-Diffusion-Policy/3D-Diffusion-Policy/plots/online_ppo_loss_iter_01.png
[Plot] Saved: /nfs_global/S/yangrongzheng/RL100/3D-Diffusion-Policy/3D-Diffusion-Policy/plots/online_ppo_kl_iter_01.png
[Plot] Saved: /nfs_global/S/yangrongzheng/RL100/3D-Diffusion-Policy/3D-Diffusion-Policy/plots/online_ppo_clipfrac_iter_01.png
[Plot] Saved: /nfs_global/S/yangrongzheng/RL100/3D-Diffusion-Policy/3D-Diffusion-Policy/plots/online_ppo_gradnorm_iter_01.png
[Plot] Saved: /nfs_global/S/yangrongzheng/RL100/3D-Diffusion-Policy/3D-Diffusion-Policy/plots/online_cd_loss_iter_01.png
[Checkpoint] Saved to /nfs_global/S/yangrongzheng/RL100/3D-Diffusion-Policy/3D-Diffusion-Policy/checkpoints/online_iter_1.ckpt

[Online RL] Iteration 3/10

[RL100Trainer] Phase 2c: Collecting New Data (Iteration 9)
[Collect] 20 episodes, success=0.800, env_return=1055.57, rl_reward=0.80, steps=4000
[Data Collection] Success Rate: 0.800, EnvReturn: 1055.57, RLReward: 0.80, Episodes: 20, Steps: 4000
[Dataset] online collection: keeping 16/20 successful episodes (dropped 4 failures) before merge.
[Online RL] Epoch 1/20, PPO Loss: 0.0188, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 21.7148, Reg Loss: 0.0000, CD Loss: 0.0658
[Online RL] Epoch 2/20, PPO Loss: -0.0495, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 16.0597, Reg Loss: 0.0000, CD Loss: 0.0000
[Online RL] Epoch 3/20, PPO Loss: -0.0630, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 12.7861, Reg Loss: 0.0000, CD Loss: 0.0596
[Online RL] Epoch 4/20, PPO Loss: -0.0582, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 9.8654, Reg Loss: 0.0000, CD Loss: 0.0000
[Online RL] Epoch 5/20, PPO Loss: -0.0621, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 11.9432, Reg Loss: 0.0000, CD Loss: 0.0000
[Online RL] Epoch 6/20, PPO Loss: -0.0638, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 7.2149, Reg Loss: 0.0000, CD Loss: 0.0617
[Online RL] Epoch 7/20, PPO Loss: -0.0903, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 13.7154, Reg Loss: 0.0000, CD Loss: 0.0000
[Online RL] Epoch 8/20, PPO Loss: -0.1128, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 7.5679, Reg Loss: 0.0000, CD Loss: 0.0650
[Online RL] Epoch 9/20, PPO Loss: -0.1201, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 8.0723, Reg Loss: 0.0000, CD Loss: 0.0000
[Online RL] Epoch 10/20, PPO Loss: -0.1223, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 3.4229, Reg Loss: 0.0000, CD Loss: 0.0000
[Online RL] Epoch 11/20, PPO Loss: -0.1140, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 7.5156, Reg Loss: 0.0000, CD Loss: 0.0715
[Online RL] Epoch 12/20, PPO Loss: -0.1290, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 7.8443, Reg Loss: 0.0000, CD Loss: 0.0000
[Online RL] Epoch 13/20, PPO Loss: -0.1279, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 5.8310, Reg Loss: 0.0000, CD Loss: 0.0686
[Online RL] Epoch 14/20, PPO Loss: -0.1392, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 3.0545, Reg Loss: 0.0000, CD Loss: 0.0000
[Online RL] Epoch 15/20, PPO Loss: -0.1456, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 2.8256, Reg Loss: 0.0000, CD Loss: 0.0000
[Online RL] Epoch 16/20, PPO Loss: -0.1364, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 13.7233, Reg Loss: 0.0000, CD Loss: 0.0635
[Online RL] Epoch 17/20, PPO Loss: -0.1146, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 4.2107, Reg Loss: 0.0000, CD Loss: 0.0000
[Online RL] Epoch 18/20, PPO Loss: -0.1130, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 4.2402, Reg Loss: 0.0000, CD Loss: 0.0532
[Online RL] Epoch 19/20, PPO Loss: -0.1500, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 2.9686, Reg Loss: 0.0000, CD Loss: 0.0000
[Online RL] Epoch 20/20, PPO Loss: -0.1335, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 3.5271, Reg Loss: 0.0000, CD Loss: 0.0000
[Plot] Saved: /nfs_global/S/yangrongzheng/RL100/3D-Diffusion-Policy/3D-Diffusion-Policy/plots/online_v_loss_iter_02.png
[Plot] Saved: /nfs_global/S/yangrongzheng/RL100/3D-Diffusion-Policy/3D-Diffusion-Policy/plots/online_ppo_loss_iter_02.png
[Plot] Saved: /nfs_global/S/yangrongzheng/RL100/3D-Diffusion-Policy/3D-Diffusion-Policy/plots/online_ppo_kl_iter_02.png
[Plot] Saved: /nfs_global/S/yangrongzheng/RL100/3D-Diffusion-Policy/3D-Diffusion-Policy/plots/online_ppo_clipfrac_iter_02.png
[Plot] Saved: /nfs_global/S/yangrongzheng/RL100/3D-Diffusion-Policy/3D-Diffusion-Policy/plots/online_ppo_gradnorm_iter_02.png
[Plot] Saved: /nfs_global/S/yangrongzheng/RL100/3D-Diffusion-Policy/3D-Diffusion-Policy/plots/online_cd_loss_iter_02.png
[Checkpoint] Saved to /nfs_global/S/yangrongzheng/RL100/3D-Diffusion-Policy/3D-Diffusion-Policy/checkpoints/online_iter_2.ckpt

[Online RL] Iteration 4/10

[RL100Trainer] Phase 2c: Collecting New Data (Iteration 9)
[Collect] 20 episodes, success=0.750, env_return=1028.35, rl_reward=0.75, steps=4000
[Data Collection] Success Rate: 0.750, EnvReturn: 1028.35, RLReward: 0.75, Episodes: 20, Steps: 4000
[Dataset] online collection: keeping 15/20 successful episodes (dropped 5 failures) before merge.
[Online RL] Epoch 1/20, PPO Loss: -0.0197, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 22.4264, Reg Loss: 0.0000, CD Loss: 0.0514
[Online RL] Epoch 2/20, PPO Loss: 0.0091, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 20.1076, Reg Loss: 0.0000, CD Loss: 0.0000
[Online RL] Epoch 3/20, PPO Loss: -0.0559, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 10.7575, Reg Loss: 0.0000, CD Loss: 0.0500
[Online RL] Epoch 4/20, PPO Loss: -0.0460, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 12.1772, Reg Loss: 0.0000, CD Loss: 0.0000
[Online RL] Epoch 5/20, PPO Loss: -0.0889, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 9.4623, Reg Loss: 0.0000, CD Loss: 0.0000
[Online RL] Epoch 6/20, PPO Loss: -0.0767, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 9.8052, Reg Loss: 0.0000, CD Loss: 0.0528
[Online RL] Epoch 7/20, PPO Loss: -0.0965, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 5.8021, Reg Loss: 0.0000, CD Loss: 0.0000
[Online RL] Epoch 8/20, PPO Loss: -0.0938, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 5.6926, Reg Loss: 0.0000, CD Loss: 0.0563
[Online RL] Epoch 9/20, PPO Loss: -0.1145, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 5.6394, Reg Loss: 0.0000, CD Loss: 0.0000
[Online RL] Epoch 10/20, PPO Loss: -0.1177, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 4.7871, Reg Loss: 0.0000, CD Loss: 0.0000
[Online RL] Epoch 11/20, PPO Loss: -0.1150, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 6.9640, Reg Loss: 0.0000, CD Loss: 0.0548
[Online RL] Epoch 12/20, PPO Loss: -0.1236, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 5.7773, Reg Loss: 0.0000, CD Loss: 0.0000
[Online RL] Epoch 13/20, PPO Loss: -0.1137, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 6.2730, Reg Loss: 0.0000, CD Loss: 0.0551
[Online RL] Epoch 14/20, PPO Loss: -0.1203, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 6.8089, Reg Loss: 0.0000, CD Loss: 0.0000
[Online RL] Epoch 15/20, PPO Loss: -0.1104, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 5.7311, Reg Loss: 0.0000, CD Loss: 0.0000
[Online RL] Epoch 16/20, PPO Loss: -0.1727, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 6.4812, Reg Loss: 0.0000, CD Loss: 0.0500
[Online RL] Epoch 17/20, PPO Loss: -0.1395, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 4.1471, Reg Loss: 0.0000, CD Loss: 0.0000
[Online RL] Epoch 18/20, PPO Loss: -0.1511, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 3.7565, Reg Loss: 0.0000, CD Loss: 0.0475
[Online RL] Epoch 19/20, PPO Loss: -0.1150, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 4.9555, Reg Loss: 0.0000, CD Loss: 0.0000
[Online RL] Epoch 20/20, PPO Loss: -0.1215, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 4.3289, Reg Loss: 0.0000, CD Loss: 0.0000
[Plot] Saved: /nfs_global/S/yangrongzheng/RL100/3D-Diffusion-Policy/3D-Diffusion-Policy/plots/online_v_loss_iter_03.png
[Plot] Saved: /nfs_global/S/yangrongzheng/RL100/3D-Diffusion-Policy/3D-Diffusion-Policy/plots/online_ppo_loss_iter_03.png
[Plot] Saved: /nfs_global/S/yangrongzheng/RL100/3D-Diffusion-Policy/3D-Diffusion-Policy/plots/online_ppo_kl_iter_03.png
[Plot] Saved: /nfs_global/S/yangrongzheng/RL100/3D-Diffusion-Policy/3D-Diffusion-Policy/plots/online_ppo_clipfrac_iter_03.png
[Plot] Saved: /nfs_global/S/yangrongzheng/RL100/3D-Diffusion-Policy/3D-Diffusion-Policy/plots/online_ppo_gradnorm_iter_03.png
[Plot] Saved: /nfs_global/S/yangrongzheng/RL100/3D-Diffusion-Policy/3D-Diffusion-Policy/plots/online_cd_loss_iter_03.png
[Checkpoint] Saved to /nfs_global/S/yangrongzheng/RL100/3D-Diffusion-Policy/3D-Diffusion-Policy/checkpoints/online_iter_3.ckpt

[Online RL] Iteration 5/10

[RL100Trainer] Phase 2c: Collecting New Data (Iteration 9)
[Collect] 20 episodes, success=0.700, env_return=1025.60, rl_reward=0.70, steps=4000
[Data Collection] Success Rate: 0.700, EnvReturn: 1025.60, RLReward: 0.70, Episodes: 20, Steps: 4000
[Dataset] online collection: keeping 14/20 successful episodes (dropped 6 failures) before merge.
[Online RL] Epoch 1/20, PPO Loss: 0.0338, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 24.4949, Reg Loss: 0.0000, CD Loss: 0.0455
[Online RL] Epoch 2/20, PPO Loss: -0.0268, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 14.9420, Reg Loss: 0.0000, CD Loss: 0.0000
[Online RL] Epoch 3/20, PPO Loss: -0.0755, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 13.7273, Reg Loss: 0.0000, CD Loss: 0.0475
[Online RL] Epoch 4/20, PPO Loss: -0.1061, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 15.2877, Reg Loss: 0.0000, CD Loss: 0.0000
[Online RL] Epoch 5/20, PPO Loss: -0.0864, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 11.8379, Reg Loss: 0.0000, CD Loss: 0.0000
[Online RL] Epoch 6/20, PPO Loss: -0.1066, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 12.9236, Reg Loss: 0.0000, CD Loss: 0.0467
[Online RL] Epoch 7/20, PPO Loss: -0.1415, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 7.6470, Reg Loss: 0.0000, CD Loss: 0.0000
[Online RL] Epoch 8/20, PPO Loss: -0.1289, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 7.0309, Reg Loss: 0.0000, CD Loss: 0.0432
[Online RL] Epoch 9/20, PPO Loss: -0.0874, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 9.8202, Reg Loss: 0.0000, CD Loss: 0.0000
[Online RL] Epoch 10/20, PPO Loss: -0.1568, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 11.7958, Reg Loss: 0.0000, CD Loss: 0.0000
[Online RL] Epoch 11/20, PPO Loss: -0.1732, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 7.1158, Reg Loss: 0.0000, CD Loss: 0.0454
[Online RL] Epoch 12/20, PPO Loss: -0.1249, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 6.1202, Reg Loss: 0.0000, CD Loss: 0.0000
[Online RL] Epoch 13/20, PPO Loss: -0.1605, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 3.7897, Reg Loss: 0.0000, CD Loss: 0.0452
[Online RL] Epoch 14/20, PPO Loss: -0.1268, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 8.2348, Reg Loss: 0.0000, CD Loss: 0.0000
[Online RL] Epoch 15/20, PPO Loss: -0.1960, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 8.9835, Reg Loss: 0.0000, CD Loss: 0.0000
[Online RL] Epoch 16/20, PPO Loss: -0.1735, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 5.7071, Reg Loss: 0.0000, CD Loss: 0.0438
[Online RL] Epoch 17/20, PPO Loss: -0.1558, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 5.3015, Reg Loss: 0.0000, CD Loss: 0.0000
[Online RL] Epoch 18/20, PPO Loss: -0.1478, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 5.3687, Reg Loss: 0.0000, CD Loss: 0.0433
[Online RL] Epoch 19/20, PPO Loss: -0.1406, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 6.2033, Reg Loss: 0.0000, CD Loss: 0.0000
[Online RL] Epoch 20/20, PPO Loss: -0.1472, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 5.3458, Reg Loss: 0.0000, CD Loss: 0.0000
[Plot] Saved: /nfs_global/S/yangrongzheng/RL100/3D-Diffusion-Policy/3D-Diffusion-Policy/plots/online_v_loss_iter_04.png
[Plot] Saved: /nfs_global/S/yangrongzheng/RL100/3D-Diffusion-Policy/3D-Diffusion-Policy/plots/online_ppo_loss_iter_04.png
[Plot] Saved: /nfs_global/S/yangrongzheng/RL100/3D-Diffusion-Policy/3D-Diffusion-Policy/plots/online_ppo_kl_iter_04.png
[Plot] Saved: /nfs_global/S/yangrongzheng/RL100/3D-Diffusion-Policy/3D-Diffusion-Policy/plots/online_ppo_clipfrac_iter_04.png
[Plot] Saved: /nfs_global/S/yangrongzheng/RL100/3D-Diffusion-Policy/3D-Diffusion-Policy/plots/online_ppo_gradnorm_iter_04.png
[Plot] Saved: /nfs_global/S/yangrongzheng/RL100/3D-Diffusion-Policy/3D-Diffusion-Policy/plots/online_cd_loss_iter_04.png
[Checkpoint] Saved to /nfs_global/S/yangrongzheng/RL100/3D-Diffusion-Policy/3D-Diffusion-Policy/checkpoints/online_iter_4.ckpt

[Online RL] Iteration 6/10

[RL100Trainer] Phase 2c: Collecting New Data (Iteration 9)
[Collect] 20 episodes, success=0.750, env_return=1191.89, rl_reward=0.75, steps=4000
[Data Collection] Success Rate: 0.750, EnvReturn: 1191.89, RLReward: 0.75, Episodes: 20, Steps: 4000
[Dataset] online collection: keeping 15/20 successful episodes (dropped 5 failures) before merge.
[Online RL] Epoch 1/20, PPO Loss: 0.0177, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 26.1060, Reg Loss: 0.0000, CD Loss: 0.0445
[Online RL] Epoch 2/20, PPO Loss: -0.0322, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 14.0856, Reg Loss: 0.0000, CD Loss: 0.0000
[Online RL] Epoch 3/20, PPO Loss: -0.0804, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 29.8007, Reg Loss: 0.0000, CD Loss: 0.0463
[Online RL] Epoch 4/20, PPO Loss: -0.0354, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 11.8841, Reg Loss: 0.0000, CD Loss: 0.0000
[Online RL] Epoch 5/20, PPO Loss: -0.0873, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 9.2541, Reg Loss: 0.0000, CD Loss: 0.0000
[Online RL] Epoch 6/20, PPO Loss: -0.1400, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 8.8230, Reg Loss: 0.0000, CD Loss: 0.0452
[Online RL] Epoch 7/20, PPO Loss: -0.1230, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 7.8356, Reg Loss: 0.0000, CD Loss: 0.0000
[Online RL] Epoch 8/20, PPO Loss: -0.1092, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 6.0542, Reg Loss: 0.0000, CD Loss: 0.0426
[Online RL] Epoch 9/20, PPO Loss: -0.1371, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 5.0741, Reg Loss: 0.0000, CD Loss: 0.0000
[Online RL] Epoch 10/20, PPO Loss: -0.1171, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 8.5788, Reg Loss: 0.0000, CD Loss: 0.0000
[Online RL] Epoch 11/20, PPO Loss: -0.0984, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 3.5494, Reg Loss: 0.0000, CD Loss: 0.0438
[Online RL] Epoch 12/20, PPO Loss: -0.1174, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 4.3342, Reg Loss: 0.0000, CD Loss: 0.0000
[Online RL] Epoch 13/20, PPO Loss: -0.0933, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 4.1481, Reg Loss: 0.0000, CD Loss: 0.0404
[Online RL] Epoch 14/20, PPO Loss: -0.1095, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 3.7310, Reg Loss: 0.0000, CD Loss: 0.0000
[Online RL] Epoch 15/20, PPO Loss: -0.1381, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 5.3365, Reg Loss: 0.0000, CD Loss: 0.0000
[Online RL] Epoch 16/20, PPO Loss: -0.1374, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 3.1095, Reg Loss: 0.0000, CD Loss: 0.0416
[Online RL] Epoch 17/20, PPO Loss: -0.1247, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 2.7103, Reg Loss: 0.0000, CD Loss: 0.0000
[Online RL] Epoch 18/20, PPO Loss: -0.1309, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 2.7263, Reg Loss: 0.0000, CD Loss: 0.0461
[Online RL] Epoch 19/20, PPO Loss: -0.1109, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 3.0848, Reg Loss: 0.0000, CD Loss: 0.0000
[Online RL] Epoch 20/20, PPO Loss: -0.0980, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 4.3752, Reg Loss: 0.0000, CD Loss: 0.0000
[Plot] Saved: /nfs_global/S/yangrongzheng/RL100/3D-Diffusion-Policy/3D-Diffusion-Policy/plots/online_v_loss_iter_05.png
[Plot] Saved: /nfs_global/S/yangrongzheng/RL100/3D-Diffusion-Policy/3D-Diffusion-Policy/plots/online_ppo_loss_iter_05.png
[Plot] Saved: /nfs_global/S/yangrongzheng/RL100/3D-Diffusion-Policy/3D-Diffusion-Policy/plots/online_ppo_kl_iter_05.png
[Plot] Saved: /nfs_global/S/yangrongzheng/RL100/3D-Diffusion-Policy/3D-Diffusion-Policy/plots/online_ppo_clipfrac_iter_05.png
[Plot] Saved: /nfs_global/S/yangrongzheng/RL100/3D-Diffusion-Policy/3D-Diffusion-Policy/plots/online_ppo_gradnorm_iter_05.png
[Plot] Saved: /nfs_global/S/yangrongzheng/RL100/3D-Diffusion-Policy/3D-Diffusion-Policy/plots/online_cd_loss_iter_05.png
[Checkpoint] Saved to /nfs_global/S/yangrongzheng/RL100/3D-Diffusion-Policy/3D-Diffusion-Policy/checkpoints/online_iter_5.ckpt

[Online RL] Iteration 7/10

[RL100Trainer] Phase 2c: Collecting New Data (Iteration 9)
[Collect] 20 episodes, success=0.800, env_return=1127.32, rl_reward=0.80, steps=4000
[Data Collection] Success Rate: 0.800, EnvReturn: 1127.32, RLReward: 0.80, Episodes: 20, Steps: 4000
[Dataset] online collection: keeping 16/20 successful episodes (dropped 4 failures) before merge.
[Online RL] Epoch 1/20, PPO Loss: -0.0042, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 18.5416, Reg Loss: 0.0000, CD Loss: 0.0428
[Online RL] Epoch 2/20, PPO Loss: -0.0301, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 20.9378, Reg Loss: 0.0000, CD Loss: 0.0000
[Online RL] Epoch 3/20, PPO Loss: -0.0577, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 9.2734, Reg Loss: 0.0000, CD Loss: 0.0434
[Online RL] Epoch 4/20, PPO Loss: -0.0537, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 8.8574, Reg Loss: 0.0000, CD Loss: 0.0000
[Online RL] Epoch 5/20, PPO Loss: -0.0827, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 7.9045, Reg Loss: 0.0000, CD Loss: 0.0000
[Online RL] Epoch 6/20, PPO Loss: -0.0962, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 11.0185, Reg Loss: 0.0000, CD Loss: 0.0410
[Online RL] Epoch 7/20, PPO Loss: -0.0989, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 6.3205, Reg Loss: 0.0000, CD Loss: 0.0000
[Online RL] Epoch 8/20, PPO Loss: -0.0736, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 4.8735, Reg Loss: 0.0000, CD Loss: 0.0444
[Online RL] Epoch 9/20, PPO Loss: -0.1347, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 6.1624, Reg Loss: 0.0000, CD Loss: 0.0000
[Online RL] Epoch 10/20, PPO Loss: -0.1116, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 4.8145, Reg Loss: 0.0000, CD Loss: 0.0000
[Online RL] Epoch 11/20, PPO Loss: -0.0972, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 3.4790, Reg Loss: 0.0000, CD Loss: 0.0410
[Online RL] Epoch 12/20, PPO Loss: -0.1154, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 3.2921, Reg Loss: 0.0000, CD Loss: 0.0000
[Online RL] Epoch 13/20, PPO Loss: -0.1246, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 2.0165, Reg Loss: 0.0000, CD Loss: 0.0377
[Online RL] Epoch 14/20, PPO Loss: -0.1480, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 3.4387, Reg Loss: 0.0000, CD Loss: 0.0000
[Online RL] Epoch 15/20, PPO Loss: -0.1009, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 3.5674, Reg Loss: 0.0000, CD Loss: 0.0000
[Online RL] Epoch 16/20, PPO Loss: -0.1104, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 2.4726, Reg Loss: 0.0000, CD Loss: 0.0384
[Online RL] Epoch 17/20, PPO Loss: -0.0942, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 2.8529, Reg Loss: 0.0000, CD Loss: 0.0000
[Online RL] Epoch 18/20, PPO Loss: -0.1479, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 3.4233, Reg Loss: 0.0000, CD Loss: 0.0406
[Online RL] Epoch 19/20, PPO Loss: -0.1413, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 4.5990, Reg Loss: 0.0000, CD Loss: 0.0000
[Online RL] Epoch 20/20, PPO Loss: -0.1124, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 5.6821, Reg Loss: 0.0000, CD Loss: 0.0000
[Plot] Saved: /nfs_global/S/yangrongzheng/RL100/3D-Diffusion-Policy/3D-Diffusion-Policy/plots/online_v_loss_iter_06.png
[Plot] Saved: /nfs_global/S/yangrongzheng/RL100/3D-Diffusion-Policy/3D-Diffusion-Policy/plots/online_ppo_loss_iter_06.png
[Plot] Saved: /nfs_global/S/yangrongzheng/RL100/3D-Diffusion-Policy/3D-Diffusion-Policy/plots/online_ppo_kl_iter_06.png
[Plot] Saved: /nfs_global/S/yangrongzheng/RL100/3D-Diffusion-Policy/3D-Diffusion-Policy/plots/online_ppo_clipfrac_iter_06.png
[Plot] Saved: /nfs_global/S/yangrongzheng/RL100/3D-Diffusion-Policy/3D-Diffusion-Policy/plots/online_ppo_gradnorm_iter_06.png
[Plot] Saved: /nfs_global/S/yangrongzheng/RL100/3D-Diffusion-Policy/3D-Diffusion-Policy/plots/online_cd_loss_iter_06.png
[Checkpoint] Saved to /nfs_global/S/yangrongzheng/RL100/3D-Diffusion-Policy/3D-Diffusion-Policy/checkpoints/online_iter_6.ckpt

[Online RL] Iteration 8/10

[RL100Trainer] Phase 2c: Collecting New Data (Iteration 9)
[Collect] 20 episodes, success=0.950, env_return=1187.45, rl_reward=0.95, steps=4000
[Data Collection] Success Rate: 0.950, EnvReturn: 1187.45, RLReward: 0.95, Episodes: 20, Steps: 4000
[Dataset] online collection: keeping 19/20 successful episodes (dropped 1 failures) before merge.
[Online RL] Epoch 1/20, PPO Loss: 0.0082, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 23.0597, Reg Loss: 0.0000, CD Loss: 0.0377
[Online RL] Epoch 2/20, PPO Loss: -0.0326, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 13.1446, Reg Loss: 0.0000, CD Loss: 0.0000
[Online RL] Epoch 3/20, PPO Loss: -0.0511, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 9.3533, Reg Loss: 0.0000, CD Loss: 0.0385
[Online RL] Epoch 4/20, PPO Loss: -0.0682, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 10.9993, Reg Loss: 0.0000, CD Loss: 0.0000
[Online RL] Epoch 5/20, PPO Loss: -0.0873, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 8.5774, Reg Loss: 0.0000, CD Loss: 0.0000
[Online RL] Epoch 6/20, PPO Loss: -0.0852, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 8.3825, Reg Loss: 0.0000, CD Loss: 0.0372
[Online RL] Epoch 7/20, PPO Loss: -0.0966, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 5.6719, Reg Loss: 0.0000, CD Loss: 0.0000
[Online RL] Epoch 8/20, PPO Loss: -0.1109, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 8.1851, Reg Loss: 0.0000, CD Loss: 0.0372
[Online RL] Epoch 9/20, PPO Loss: -0.1153, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 7.5257, Reg Loss: 0.0000, CD Loss: 0.0000
[Online RL] Epoch 10/20, PPO Loss: -0.1046, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 6.9853, Reg Loss: 0.0000, CD Loss: 0.0000
[Online RL] Epoch 11/20, PPO Loss: -0.1161, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 5.3050, Reg Loss: 0.0000, CD Loss: 0.0359
[Online RL] Epoch 12/20, PPO Loss: -0.1151, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 4.6255, Reg Loss: 0.0000, CD Loss: 0.0000
[Online RL] Epoch 13/20, PPO Loss: -0.1250, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 5.9309, Reg Loss: 0.0000, CD Loss: 0.0339
[Online RL] Epoch 14/20, PPO Loss: -0.1219, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 3.4867, Reg Loss: 0.0000, CD Loss: 0.0000
[Online RL] Epoch 15/20, PPO Loss: -0.1279, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 2.4133, Reg Loss: 0.0000, CD Loss: 0.0000
[Online RL] Epoch 16/20, PPO Loss: -0.1237, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 3.6473, Reg Loss: 0.0000, CD Loss: 0.0360
[Online RL] Epoch 17/20, PPO Loss: -0.1276, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 4.2771, Reg Loss: 0.0000, CD Loss: 0.0000
[Online RL] Epoch 18/20, PPO Loss: -0.1242, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 2.8293, Reg Loss: 0.0000, CD Loss: 0.0362
[Online RL] Epoch 19/20, PPO Loss: -0.1280, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 2.2568, Reg Loss: 0.0000, CD Loss: 0.0000
[Online RL] Epoch 20/20, PPO Loss: -0.1254, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 3.9565, Reg Loss: 0.0000, CD Loss: 0.0000
[Plot] Saved: /nfs_global/S/yangrongzheng/RL100/3D-Diffusion-Policy/3D-Diffusion-Policy/plots/online_v_loss_iter_07.png
[Plot] Saved: /nfs_global/S/yangrongzheng/RL100/3D-Diffusion-Policy/3D-Diffusion-Policy/plots/online_ppo_loss_iter_07.png
[Plot] Saved: /nfs_global/S/yangrongzheng/RL100/3D-Diffusion-Policy/3D-Diffusion-Policy/plots/online_ppo_kl_iter_07.png
[Plot] Saved: /nfs_global/S/yangrongzheng/RL100/3D-Diffusion-Policy/3D-Diffusion-Policy/plots/online_ppo_clipfrac_iter_07.png
[Plot] Saved: /nfs_global/S/yangrongzheng/RL100/3D-Diffusion-Policy/3D-Diffusion-Policy/plots/online_ppo_gradnorm_iter_07.png
[Plot] Saved: /nfs_global/S/yangrongzheng/RL100/3D-Diffusion-Policy/3D-Diffusion-Policy/plots/online_cd_loss_iter_07.png
[Checkpoint] Saved to /nfs_global/S/yangrongzheng/RL100/3D-Diffusion-Policy/3D-Diffusion-Policy/checkpoints/online_iter_7.ckpt

[Online RL] Iteration 9/10

[RL100Trainer] Phase 2c: Collecting New Data (Iteration 9)
[Collect] 20 episodes, success=0.900, env_return=1188.34, rl_reward=0.90, steps=4000
[Data Collection] Success Rate: 0.900, EnvReturn: 1188.34, RLReward: 0.90, Episodes: 20, Steps: 4000
[Dataset] online collection: keeping 18/20 successful episodes (dropped 2 failures) before merge.
[Online RL] Epoch 1/20, PPO Loss: -0.0134, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 16.8947, Reg Loss: 0.0000, CD Loss: 0.0346
[Online RL] Epoch 2/20, PPO Loss: -0.0422, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 12.0708, Reg Loss: 0.0000, CD Loss: 0.0000
[Online RL] Epoch 3/20, PPO Loss: -0.0650, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 11.6673, Reg Loss: 0.0000, CD Loss: 0.0361
[Online RL] Epoch 4/20, PPO Loss: -0.0786, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 7.2641, Reg Loss: 0.0000, CD Loss: 0.0000
[Online RL] Epoch 5/20, PPO Loss: -0.0896, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 6.3210, Reg Loss: 0.0000, CD Loss: 0.0000
[Online RL] Epoch 6/20, PPO Loss: -0.0889, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 4.4556, Reg Loss: 0.0000, CD Loss: 0.0347
[Online RL] Epoch 7/20, PPO Loss: -0.1141, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 4.7858, Reg Loss: 0.0000, CD Loss: 0.0000
[Online RL] Epoch 8/20, PPO Loss: -0.1106, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 7.5427, Reg Loss: 0.0000, CD Loss: 0.0337
[Online RL] Epoch 9/20, PPO Loss: -0.1196, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 6.9651, Reg Loss: 0.0000, CD Loss: 0.0000
[Online RL] Epoch 10/20, PPO Loss: -0.1304, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 5.1090, Reg Loss: 0.0000, CD Loss: 0.0000
[Online RL] Epoch 11/20, PPO Loss: -0.1252, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 2.5035, Reg Loss: 0.0000, CD Loss: 0.0350
[Online RL] Epoch 12/20, PPO Loss: -0.1243, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 2.7023, Reg Loss: 0.0000, CD Loss: 0.0000
[Online RL] Epoch 13/20, PPO Loss: -0.1254, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 2.4068, Reg Loss: 0.0000, CD Loss: 0.0326
[Online RL] Epoch 14/20, PPO Loss: -0.1259, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 2.4803, Reg Loss: 0.0000, CD Loss: 0.0000
[Online RL] Epoch 15/20, PPO Loss: -0.1322, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 1.6044, Reg Loss: 0.0000, CD Loss: 0.0000
[Online RL] Epoch 16/20, PPO Loss: -0.1261, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 3.4817, Reg Loss: 0.0000, CD Loss: 0.0317
[Online RL] Epoch 17/20, PPO Loss: -0.1278, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 2.0640, Reg Loss: 0.0000, CD Loss: 0.0000
[Online RL] Epoch 18/20, PPO Loss: -0.1366, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 2.0449, Reg Loss: 0.0000, CD Loss: 0.0325
[Online RL] Epoch 19/20, PPO Loss: -0.1255, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 2.4714, Reg Loss: 0.0000, CD Loss: 0.0000
[Online RL] Epoch 20/20, PPO Loss: -0.1344, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 1.9986, Reg Loss: 0.0000, CD Loss: 0.0000
[Plot] Saved: /nfs_global/S/yangrongzheng/RL100/3D-Diffusion-Policy/3D-Diffusion-Policy/plots/online_v_loss_iter_08.png
[Plot] Saved: /nfs_global/S/yangrongzheng/RL100/3D-Diffusion-Policy/3D-Diffusion-Policy/plots/online_ppo_loss_iter_08.png
[Plot] Saved: /nfs_global/S/yangrongzheng/RL100/3D-Diffusion-Policy/3D-Diffusion-Policy/plots/online_ppo_kl_iter_08.png
[Plot] Saved: /nfs_global/S/yangrongzheng/RL100/3D-Diffusion-Policy/3D-Diffusion-Policy/plots/online_ppo_clipfrac_iter_08.png
[Plot] Saved: /nfs_global/S/yangrongzheng/RL100/3D-Diffusion-Policy/3D-Diffusion-Policy/plots/online_ppo_gradnorm_iter_08.png
[Plot] Saved: /nfs_global/S/yangrongzheng/RL100/3D-Diffusion-Policy/3D-Diffusion-Policy/plots/online_cd_loss_iter_08.png
[Checkpoint] Saved to /nfs_global/S/yangrongzheng/RL100/3D-Diffusion-Policy/3D-Diffusion-Policy/checkpoints/online_iter_8.ckpt

[Online RL] Iteration 10/10

[RL100Trainer] Phase 2c: Collecting New Data (Iteration 9)
[Collect] 20 episodes, success=0.950, env_return=1164.98, rl_reward=0.95, steps=4000
[Data Collection] Success Rate: 0.950, EnvReturn: 1164.98, RLReward: 0.95, Episodes: 20, Steps: 4000
[Dataset] online collection: keeping 19/20 successful episodes (dropped 1 failures) before merge.
[Online RL] Epoch 1/20, PPO Loss: 0.0014, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 30.6469, Reg Loss: 0.0000, CD Loss: 0.0317
[Online RL] Epoch 2/20, PPO Loss: -0.0282, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 15.8303, Reg Loss: 0.0000, CD Loss: 0.0000
[Online RL] Epoch 3/20, PPO Loss: -0.0482, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 10.9968, Reg Loss: 0.0000, CD Loss: 0.0296
[Online RL] Epoch 4/20, PPO Loss: -0.0678, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 15.7095, Reg Loss: 0.0000, CD Loss: 0.0000
[Online RL] Epoch 5/20, PPO Loss: -0.0809, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 9.6383, Reg Loss: 0.0000, CD Loss: 0.0000
[Online RL] Epoch 6/20, PPO Loss: -0.0875, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 7.3039, Reg Loss: 0.0000, CD Loss: 0.0322
[Online RL] Epoch 7/20, PPO Loss: -0.1036, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 5.8134, Reg Loss: 0.0000, CD Loss: 0.0000
[Online RL] Epoch 8/20, PPO Loss: -0.1009, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 10.4791, Reg Loss: 0.0000, CD Loss: 0.0301
[Online RL] Epoch 9/20, PPO Loss: -0.1148, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 5.5178, Reg Loss: 0.0000, CD Loss: 0.0000
[Online RL] Epoch 10/20, PPO Loss: -0.1182, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 3.7447, Reg Loss: 0.0000, CD Loss: 0.0000
[Online RL] Epoch 11/20, PPO Loss: -0.1257, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 3.3537, Reg Loss: 0.0000, CD Loss: 0.0296
[Online RL] Epoch 12/20, PPO Loss: -0.1168, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 4.2353, Reg Loss: 0.0000, CD Loss: 0.0000
[Online RL] Epoch 13/20, PPO Loss: -0.1317, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 3.6926, Reg Loss: 0.0000, CD Loss: 0.0279
[Online RL] Epoch 14/20, PPO Loss: -0.1227, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 3.2798, Reg Loss: 0.0000, CD Loss: 0.0000
[Online RL] Epoch 15/20, PPO Loss: -0.1222, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 3.6466, Reg Loss: 0.0000, CD Loss: 0.0000
[Online RL] Epoch 16/20, PPO Loss: -0.1258, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 3.8944, Reg Loss: 0.0000, CD Loss: 0.0298
[Online RL] Epoch 17/20, PPO Loss: -0.1235, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 3.5024, Reg Loss: 0.0000, CD Loss: 0.0000
[Online RL] Epoch 18/20, PPO Loss: -0.1302, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 3.5552, Reg Loss: 0.0000, CD Loss: 0.0271
[Online RL] Epoch 19/20, PPO Loss: -0.1310, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 1.7449, Reg Loss: 0.0000, CD Loss: 0.0000
[Online RL] Epoch 20/20, PPO Loss: -0.1288, KL: 0.000000, ClipFrac: 0.0000, GradNorm: 3.4002, Reg Loss: 0.0000, CD Loss: 0.0000
[Plot] Saved: /nfs_global/S/yangrongzheng/RL100/3D-Diffusion-Policy/3D-Diffusion-Policy/plots/online_v_loss_iter_09.png
[Plot] Saved: /nfs_global/S/yangrongzheng/RL100/3D-Diffusion-Policy/3D-Diffusion-Policy/plots/online_ppo_loss_iter_09.png
[Plot] Saved: /nfs_global/S/yangrongzheng/RL100/3D-Diffusion-Policy/3D-Diffusion-Policy/plots/online_ppo_kl_iter_09.png
[Plot] Saved: /nfs_global/S/yangrongzheng/RL100/3D-Diffusion-Policy/3D-Diffusion-Policy/plots/online_ppo_clipfrac_iter_09.png
[Plot] Saved: /nfs_global/S/yangrongzheng/RL100/3D-Diffusion-Policy/3D-Diffusion-Policy/plots/online_ppo_gradnorm_iter_09.png
[Plot] Saved: /nfs_global/S/yangrongzheng/RL100/3D-Diffusion-Policy/3D-Diffusion-Policy/plots/online_cd_loss_iter_09.png
[Checkpoint] Saved to /nfs_global/S/yangrongzheng/RL100/3D-Diffusion-Policy/3D-Diffusion-Policy/checkpoints/online_iter_9.ckpt

================================================================================
                         TRAINING COMPLETE!
================================================================================

[Checkpoint] Saved to /nfs_global/S/yangrongzheng/RL100/3D-Diffusion-Policy/3D-Diffusion-Policy/checkpoints/final.ckpt

[Evaluation] Running final evaluation...
test_mean_score: 0.81
test_mean_score: 0.68

================================================================================
                         FINAL RESULTS
================================================================================
[ddim]
mean_traj_rewards: 11834.1298
mean_success_rates: 0.8100
test_mean_score: 0.8100
SR_test_L3: 0.8367
SR_test_L5: 0.8320
[cm]
mean_traj_rewards: 10520.0417
mean_success_rates: 0.6800
test_mean_score: 0.6800
SR_test_L3: 0.8367
SR_test_L5: 0.8320

[Training] Complete! Checkpoints saved to:
  /nfs_global/S/yangrongzheng/RL100/3D-Diffusion-Policy/3D-Diffusion-Policy/checkpoints
Found 8 GPUs for rendering. Using device 0.
Job end at 2026-03-17 10:47:47
