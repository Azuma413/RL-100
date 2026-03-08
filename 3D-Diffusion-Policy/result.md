Job start at 2026-03-07 01:05:17
Job run at:
   Static hostname: localhost.localdomain
Transient hostname: r8a100-d00
         Icon name: computer-server
           Chassis: server
        Machine ID: 9f3314fbfacf4ce99a336456babce1ff
           Boot ID: d3568b353029413fac5ddc040dcd700c
  Operating System: Rocky Linux 8.7 (Green Obsidian)
       CPE OS Name: cpe:/o:rocky:rocky:8:GA
            Kernel: Linux 4.18.0-425.10.1.el8_7.x86_64
      Architecture: x86-64
Filesystem                                        Size  Used Avail Use% Mounted on
/dev/mapper/rl-root                               1.5T   35G  1.5T   3% /
/dev/nvme1n1p1                                    3.5T   26G  3.5T   1% /tmp
/dev/nvme0n1p1                                    7.0T   50G  7.0T   1% /local
/dev/nvme1n1p2                                    3.5T  395G  3.2T  12% /local/nfscache
/dev/sda2                                         2.0G  305M  1.7G  15% /boot
/dev/mapper/rl-var                                2.0T   42G  2.0T   3% /var
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
ext-zone00.nas02.future.cn:/nfs_global            404T  391T   13T  97% /nfs_global
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
          /home  14449M  16384M  20480M            168k       0       0        

############### /workspace
Disk quotas for user yangrongzheng (uid 6215): 
     Filesystem   space   quota   limit   grace   files   quota   limit   grace
     /workspace      0K    400G    500G               1       0       0        

############### /nfs_global
Disk quotas for user yangrongzheng (uid 6215): 
     Filesystem   space   quota   limit   grace   files   quota   limit   grace
    /nfs_global    227G   5120G   7168G            348k   5000k  10000k        

############### /lustre
Disk quotas for usr yangrongzheng (uid 6215):
     Filesystem    used   quota   limit   grace   files   quota   limit   grace
        /lustre      0k      8T     10T       -       0  3000000 36000000       -
uid 6215 is using default block quota setting
uid 6215 is using default file quota setting
name, driver_version, power.limit [W]
NVIDIA A100 80GB PCIe, 570.124.06, 300.00 W
NVIDIA A100 80GB PCIe, 570.124.06, 300.00 W
NVIDIA A100 80GB PCIe, 570.124.06, 300.00 W
NVIDIA A100 80GB PCIe, 570.124.06, [Unknown Error]
NVIDIA A100 80GB PCIe, 570.124.06, 300.00 W
NVIDIA A100 80GB PCIe, 570.124.06, 300.00 W
NVIDIA A100 80GB PCIe, 570.124.06, 300.00 W
NVIDIA A100 80GB PCIe, 570.124.06, 300.00 W
Using GPU(s) 0,1,2,3,4,5,6,7
This job is assigned the following resources by SLURM:
CPU_IDs=0-127 GRES=gpu:8(IDX:0-7)
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
    eval_episodes: 20
    n_obs_steps: ${n_obs_steps}
    n_action_steps: ${n_action_steps}
    fps: 10
    n_envs: null
    n_train: null
    n_test: null
    task_name: ${task_name}
    device: ${training.device}
    use_point_crop: ${policy.use_point_crop}
  dataset:
    _target_: diffusion_policy_3d.dataset.metaworld_dataset.MetaworldDataset
    zarr_path: data/metaworld_dial-turn_expert.zarr
    horizon: ${horizon}
    pad_before: ${eval:'${n_obs_steps}-1'}
    pad_after: ${eval:'${n_action_steps}-1'}
    seed: 42
    val_ratio: 0.02
    max_train_episodes: 90
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
  beta_recon: 1.0
  beta_kl: 0.001
  ppo_clip_eps: 0.2
  sigma_min: 0.01
  sigma_max: 0.8
  use_variance_clip: true
critics:
  hidden_dims:
  - 256
  - 256
  - 256
  gamma: 0.99
  tau: 0.7
  target_update_tau: 0.005
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
  num_offline_iterations: 5
  critic_epochs: 50
  ppo_epochs: 100
  collection_episodes: 50
  cd_every: 5
  run_online_rl: false
  online_rl_iterations: 10
  online_collection_episodes: 20
  gradient_accumulate_every: 1
  max_grad_norm: 1.0
  log_every: 10
  eval_every: 100
  checkpoint_every: 200
  resume: true
  resume_path: /nfs_global/S/yangrongzheng/RL100/3D-Diffusion-Policy/3D-Diffusion-Policy/checkpoints/after_il.ckpt
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
Replay Buffer: state, shape (2000, 9), dtype float32, range -0.13~0.87
Replay Buffer: action, shape (2000, 4), dtype float32, range -1.45~1.66
Replay Buffer: point_cloud, shape (2000, 1024, 6), dtype float32, range -0.91~255.00
Replay Buffer: reward, shape (2000,), dtype float32, range 0.02~10.00
Replay Buffer: done, shape (2000,), dtype float32, range 0.00~1.00
--------------------------
[Setup] Dataset loaded: 1737 episodes
[Setup] Initializing environment runner...
[MetaWorldEnv] use_point_crop: True
[Setup] Environment runner initialized

[Setup] Initializing RL100Trainer...
[RL100Trainer] Initializing RL100Policy...
[DP3Encoder] point cloud shape: [512, 3]
[DP3Encoder] state shape: [9]
[DP3Encoder] imagination point shape: None
[DP3Encoder] use_recon_vib: False
[DP3Encoder] beta_recon: 1.0, beta_kl: 0.001
[PointNetEncoderXYZ] use_layernorm: True
[PointNetEncoderXYZ] use_final_norm: layernorm
[PointNetEncoderXYZ] use_vib: False
[DP3Encoder] output dim: 128
[DiffusionUnetHybridPointcloudPolicy] use_pc_color: False
[DiffusionUnetHybridPointcloudPolicy] pointnet_type: pointnet
[2026-03-07 01:05:45,276][diffusion_policy_3d.model.diffusion.conditional_unet1d][INFO] - number of parameters: 2.550744e+08
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
[2026-03-07 01:05:50,092][diffusion_policy_3d.model.diffusion.conditional_unet1d][INFO] - number of parameters: 2.550744e+08
[RL100Trainer] Initializing Transition Model T_θ(s'|s,a)...
[Setup] RL100Trainer initialized

[Setup] Resuming from checkpoint: /nfs_global/S/yangrongzheng/RL100/3D-Diffusion-Policy/3D-Diffusion-Policy/checkpoints/after_il.ckpt
[TransitionModel] Checkpoint loaded.
[Checkpoint] Loaded from /nfs_global/S/yangrongzheng/RL100/3D-Diffusion-Policy/3D-Diffusion-Policy/checkpoints/after_il.ckpt
[Setup] IL phase will be skipped — starting directly from offline RL.

[Training] Starting RL-100 pipeline...

================================================================================
                    RL-100 TRAINING PIPELINE
================================================================================


[RL100Trainer] Skipping IL phase — loaded from checkpoint.
[RL100Trainer] Normalizer synced from dataset. Resuming offline RL from iteration 0.

================================================================================
               OFFLINE RL ITERATION 1/5
================================================================================


[RL100Trainer] Line 6 — Training Transition Model T_θ (Iteration 0)

[TransitionModel] Encoding dataset for transition model training...
[TransitionModel] Dataset: 1737 samples, input_dim=260, target_dim=257
[TransitionModel] Epoch    0 | train=26.03706 | val=0.20146 | no-improve=0/5
[TransitionModel] Epoch   20 | train=-16.69954 | val=0.02303 | no-improve=0/5
[TransitionModel] Epoch   29 | train=-20.80154 | val=0.02360 | no-improve=5/5
[TransitionModel] Training complete. Elites=[4, 1, 0, 6, 5], val_loss=0.02121

[RL100Trainer] Phase 2a: Training IQL Critics (Iteration 0)
[IQL] Epoch 0/50, V Loss: 1.0818, Q Loss: 72.6413
[IQL] Epoch 1/50, V Loss: 0.5742, Q Loss: 27.4248
[IQL] Epoch 2/50, V Loss: 0.2064, Q Loss: 20.7119
[IQL] Epoch 3/50, V Loss: 0.1169, Q Loss: 19.4387
[IQL] Epoch 4/50, V Loss: 0.0925, Q Loss: 19.5409
[IQL] Epoch 5/50, V Loss: 0.0874, Q Loss: 19.9777
[IQL] Epoch 6/50, V Loss: 0.1144, Q Loss: 20.4409
[IQL] Epoch 7/50, V Loss: 0.2035, Q Loss: 20.7104
[IQL] Epoch 8/50, V Loss: 0.3218, Q Loss: 20.7128
[IQL] Epoch 9/50, V Loss: 0.3503, Q Loss: 20.5607
[IQL] Epoch 10/50, V Loss: 0.3939, Q Loss: 20.0587
[IQL] Epoch 11/50, V Loss: 0.4207, Q Loss: 19.5079
[IQL] Epoch 12/50, V Loss: 0.4207, Q Loss: 18.7363
[IQL] Epoch 13/50, V Loss: 0.3938, Q Loss: 17.8859
[IQL] Epoch 14/50, V Loss: 0.3281, Q Loss: 17.0859
[IQL] Epoch 15/50, V Loss: 0.2277, Q Loss: 16.2435
[IQL] Epoch 16/50, V Loss: 0.1734, Q Loss: 15.3443
[IQL] Epoch 17/50, V Loss: 0.1409, Q Loss: 14.5458
[IQL] Epoch 18/50, V Loss: 0.1286, Q Loss: 13.7541
[IQL] Epoch 19/50, V Loss: 0.1248, Q Loss: 13.1150
[IQL] Epoch 20/50, V Loss: 0.1220, Q Loss: 12.5207
[IQL] Epoch 21/50, V Loss: 0.1347, Q Loss: 11.8639
[IQL] Epoch 22/50, V Loss: 0.1354, Q Loss: 11.4073
[IQL] Epoch 23/50, V Loss: 0.1704, Q Loss: 10.8694
[IQL] Epoch 24/50, V Loss: 0.1183, Q Loss: 10.3632
[IQL] Epoch 25/50, V Loss: 0.1305, Q Loss: 9.8351
[IQL] Epoch 26/50, V Loss: 0.2075, Q Loss: 9.4308
[IQL] Epoch 27/50, V Loss: 0.2080, Q Loss: 8.9174
[IQL] Epoch 28/50, V Loss: 0.2307, Q Loss: 8.4185
[IQL] Epoch 29/50, V Loss: 0.2322, Q Loss: 7.9959
[IQL] Epoch 30/50, V Loss: 0.2629, Q Loss: 7.5556
[IQL] Epoch 31/50, V Loss: 0.2674, Q Loss: 7.1652
[IQL] Epoch 32/50, V Loss: 0.3123, Q Loss: 6.8194
[IQL] Epoch 33/50, V Loss: 0.3123, Q Loss: 6.5122
[IQL] Epoch 34/50, V Loss: 0.2839, Q Loss: 6.2486
[IQL] Epoch 35/50, V Loss: 0.3174, Q Loss: 5.9960
[IQL] Epoch 36/50, V Loss: 0.3213, Q Loss: 5.8419
[IQL] Epoch 37/50, V Loss: 0.2826, Q Loss: 5.6744
[IQL] Epoch 38/50, V Loss: 0.2649, Q Loss: 5.4965
[IQL] Epoch 39/50, V Loss: 0.2453, Q Loss: 5.3804
[IQL] Epoch 40/50, V Loss: 0.1730, Q Loss: 5.2171
[IQL] Epoch 41/50, V Loss: 0.1222, Q Loss: 5.1058
[IQL] Epoch 42/50, V Loss: 0.1224, Q Loss: 5.0297
[IQL] Epoch 43/50, V Loss: 0.1161, Q Loss: 4.8885
[IQL] Epoch 44/50, V Loss: 0.0813, Q Loss: 4.7754
[IQL] Epoch 45/50, V Loss: 0.1115, Q Loss: 4.6584
[IQL] Epoch 46/50, V Loss: 0.1133, Q Loss: 4.6289
[IQL] Epoch 47/50, V Loss: 0.1048, Q Loss: 4.5075
[IQL] Epoch 48/50, V Loss: 0.1217, Q Loss: 4.3859
[IQL] Epoch 49/50, V Loss: 0.1236, Q Loss: 4.3207

[RL100Trainer] Phase 2b: Offline RL Optimization (Iteration 0)
[Offline RL] Epoch 0/100, PPO Loss: -1.4812, CD Loss: 1.7602
[Offline RL] Epoch 1/100, PPO Loss: -2.1669, CD Loss: 0.2856
[Offline RL] Epoch 2/100, PPO Loss: -2.5105, CD Loss: 0.9463
[Offline RL] Epoch 3/100, PPO Loss: -3.2491, CD Loss: 0.6704
[Offline RL] Epoch 4/100, PPO Loss: -3.5499, CD Loss: 0.5340
[Offline RL] Epoch 5/100, PPO Loss: -3.6847, CD Loss: 0.5160
[Offline RL] Epoch 6/100, PPO Loss: -3.7367, CD Loss: 0.3295
[Offline RL] Epoch 7/100, PPO Loss: -3.5350, CD Loss: 0.3323
[Offline RL] Epoch 8/100, PPO Loss: -3.2772, CD Loss: 0.1937
[Offline RL] Epoch 9/100, PPO Loss: -2.8473, CD Loss: 0.1825
[Offline RL] Epoch 10/100, PPO Loss: -2.5623, CD Loss: 0.5673
[Offline RL] Epoch 11/100, PPO Loss: -2.5065, CD Loss: 0.5793
[Offline RL] Epoch 12/100, PPO Loss: -2.8217, CD Loss: 0.4569
[Offline RL] Epoch 13/100, PPO Loss: -3.8517, CD Loss: 0.4440
[Offline RL] Epoch 14/100, PPO Loss: -4.7755, CD Loss: 0.1902
[Offline RL] Epoch 15/100, PPO Loss: -5.4540, CD Loss: 0.1733
[Offline RL] Epoch 16/100, PPO Loss: -5.7363, CD Loss: 0.2176
[Offline RL] Epoch 17/100, PPO Loss: -5.8934, CD Loss: 0.2449
[Offline RL] Epoch 18/100, PPO Loss: -5.7979, CD Loss: 0.2261
[Offline RL] Epoch 19/100, PPO Loss: -5.7610, CD Loss: 0.1790
[Offline RL] Epoch 20/100, PPO Loss: -5.9766, CD Loss: 0.1323
[Offline RL] Epoch 21/100, PPO Loss: -6.0704, CD Loss: 0.1208
[Offline RL] Epoch 22/100, PPO Loss: -6.0027, CD Loss: 0.1430
[Offline RL] Epoch 23/100, PPO Loss: -5.8060, CD Loss: 0.1725
[Offline RL] Epoch 24/100, PPO Loss: -5.8146, CD Loss: 0.1828
[Offline RL] Epoch 25/100, PPO Loss: -5.7709, CD Loss: 0.1760
[Offline RL] Epoch 26/100, PPO Loss: -5.6664, CD Loss: 0.1492
[Offline RL] Epoch 27/100, PPO Loss: -5.4608, CD Loss: 0.1807
[Offline RL] Epoch 28/100, PPO Loss: -5.3584, CD Loss: 0.1583
[Offline RL] Epoch 29/100, PPO Loss: -5.1686, CD Loss: 0.3678
[Offline RL] Epoch 30/100, PPO Loss: -4.8681, CD Loss: 0.5351
[Offline RL] Epoch 31/100, PPO Loss: -4.4578, CD Loss: 0.5174
[Offline RL] Epoch 32/100, PPO Loss: -4.3101, CD Loss: 0.3377
[Offline RL] Epoch 33/100, PPO Loss: -4.1915, CD Loss: 0.2826
[Offline RL] Epoch 34/100, PPO Loss: -4.1916, CD Loss: 0.2694
[Offline RL] Epoch 35/100, PPO Loss: -4.4886, CD Loss: 0.2151
[Offline RL] Epoch 36/100, PPO Loss: -4.6827, CD Loss: 0.1717
[Offline RL] Epoch 37/100, PPO Loss: -4.7818, CD Loss: 0.1845
[Offline RL] Epoch 38/100, PPO Loss: -4.8125, CD Loss: 0.1766
[Offline RL] Epoch 39/100, PPO Loss: -4.7743, CD Loss: 0.2151
[Offline RL] Epoch 40/100, PPO Loss: -4.8661, CD Loss: 0.2410
[Offline RL] Epoch 41/100, PPO Loss: -5.1778, CD Loss: 0.2583
[Offline RL] Epoch 42/100, PPO Loss: -5.3170, CD Loss: 0.2599
[Offline RL] Epoch 43/100, PPO Loss: -5.2300, CD Loss: 0.2068
[Offline RL] Epoch 44/100, PPO Loss: -5.2545, CD Loss: 0.2003
[Offline RL] Epoch 45/100, PPO Loss: -5.5965, CD Loss: 0.2107
[Offline RL] Epoch 46/100, PPO Loss: -5.6981, CD Loss: 0.2519
[Offline RL] Epoch 47/100, PPO Loss: -5.4535, CD Loss: 0.1557
[Offline RL] Epoch 48/100, PPO Loss: -5.1309, CD Loss: 0.2278
[Offline RL] Epoch 49/100, PPO Loss: -5.0358, CD Loss: 0.2585
[Offline RL] Epoch 50/100, PPO Loss: -5.1377, CD Loss: 0.2190
[Offline RL] Epoch 51/100, PPO Loss: -5.1237, CD Loss: 0.2485
[Offline RL] Epoch 52/100, PPO Loss: -5.1186, CD Loss: 0.2054
[Offline RL] Epoch 53/100, PPO Loss: -5.2164, CD Loss: 0.1518
[Offline RL] Epoch 54/100, PPO Loss: -5.2763, CD Loss: 0.1633
[Offline RL] Epoch 55/100, PPO Loss: -5.6540, CD Loss: 0.2087
[Offline RL] Epoch 56/100, PPO Loss: -5.9118, CD Loss: 0.2643
[Offline RL] Epoch 57/100, PPO Loss: -6.0528, CD Loss: 0.2331
[Offline RL] Epoch 58/100, PPO Loss: -6.2704, CD Loss: 0.1994
[Offline RL] Epoch 59/100, PPO Loss: -6.2132, CD Loss: 0.1913
[Offline RL] Epoch 60/100, PPO Loss: -5.6076, CD Loss: 0.1654
[Offline RL] Epoch 61/100, PPO Loss: -5.0401, CD Loss: 0.1473
[Offline RL] Epoch 62/100, PPO Loss: -4.6371, CD Loss: 0.1450
[Offline RL] Epoch 63/100, PPO Loss: -4.5175, CD Loss: 0.1358
[Offline RL] Epoch 64/100, PPO Loss: -4.3821, CD Loss: 0.1468
[Offline RL] Epoch 65/100, PPO Loss: -4.2210, CD Loss: 0.2148
[Offline RL] Epoch 66/100, PPO Loss: -3.8407, CD Loss: 0.2236
[Offline RL] Epoch 67/100, PPO Loss: -3.6248, CD Loss: 0.1331
[Offline RL] Epoch 68/100, PPO Loss: -3.5181, CD Loss: 0.1036
[Offline RL] Epoch 69/100, PPO Loss: -3.5449, CD Loss: 0.1259
[Offline RL] Epoch 70/100, PPO Loss: -3.6232, CD Loss: 0.1418
[Offline RL] Epoch 71/100, PPO Loss: -3.7076, CD Loss: 0.2704
[Offline RL] Epoch 72/100, PPO Loss: -3.8607, CD Loss: 0.2720
[Offline RL] Epoch 73/100, PPO Loss: -3.9174, CD Loss: 0.4549
[Offline RL] Epoch 74/100, PPO Loss: -3.9329, CD Loss: 0.4491
[Offline RL] Epoch 75/100, PPO Loss: -3.8753, CD Loss: 0.3900
[Offline RL] Epoch 76/100, PPO Loss: -3.6877, CD Loss: 0.3436
[Offline RL] Epoch 77/100, PPO Loss: -3.6742, CD Loss: 0.3156
[Offline RL] Epoch 78/100, PPO Loss: -3.7444, CD Loss: 0.3019
[Offline RL] Epoch 79/100, PPO Loss: -3.5074, CD Loss: 0.2979
[Offline RL] Epoch 80/100, PPO Loss: -3.3454, CD Loss: 0.2345
[Offline RL] Epoch 81/100, PPO Loss: -3.0632, CD Loss: 0.2312
[Offline RL] Epoch 82/100, PPO Loss: -2.9463, CD Loss: 0.2768
[Offline RL] Epoch 83/100, PPO Loss: -3.1345, CD Loss: 0.2231
[Offline RL] Epoch 84/100, PPO Loss: -3.3650, CD Loss: 0.2105
[Offline RL] Epoch 85/100, PPO Loss: -3.3465, CD Loss: 0.1874
[Offline RL] Epoch 86/100, PPO Loss: -3.2537, CD Loss: 0.1724
[Offline RL] Epoch 87/100, PPO Loss: -3.0548, CD Loss: 0.1710
[Offline RL] Epoch 88/100, PPO Loss: -3.1519, CD Loss: 0.1575
[Offline RL] Epoch 89/100, PPO Loss: -3.4182, CD Loss: 0.1441
[Offline RL] Epoch 90/100, PPO Loss: -3.5374, CD Loss: 0.1338
[Offline RL] Epoch 91/100, PPO Loss: -3.5654, CD Loss: 0.1919
[Offline RL] Epoch 92/100, PPO Loss: -3.5641, CD Loss: 0.1583
[Offline RL] Epoch 93/100, PPO Loss: -3.5625, CD Loss: 0.1713
[Offline RL] Epoch 94/100, PPO Loss: -3.3668, CD Loss: 0.2770
[Offline RL] Epoch 95/100, PPO Loss: -3.1189, CD Loss: 0.2622
[Offline RL] Epoch 96/100, PPO Loss: -2.6847, CD Loss: 0.1783
[Offline RL] Epoch 97/100, PPO Loss: -2.2556, CD Loss: 0.2194
[Offline RL] Epoch 98/100, PPO Loss: -1.5618, CD Loss: 0.4608
[Offline RL] Epoch 99/100, PPO Loss: -0.8251, CD Loss: 0.4442

[RL100Trainer] Phase 2c: Collecting New Data (Iteration 0)
test_mean_score: 0.0
[Data Collection] Success Rate: 0.000, Reward: 461.15

[RL100Trainer] Retraining IL on merged dataset...

============================================================
[RL100Trainer] Phase 1: Imitation Learning
============================================================

[IL] Epoch 0/100, Loss: 13.8166
[IL] Epoch 1/100, Loss: 2.1850
[IL] Epoch 2/100, Loss: 1.4179
[IL] Epoch 3/100, Loss: 1.1752
[IL] Epoch 4/100, Loss: 1.0350
[IL] Epoch 5/100, Loss: 1.0348
[IL] Epoch 6/100, Loss: 1.0140
[IL] Epoch 7/100, Loss: 1.0126
[IL] Epoch 8/100, Loss: 1.0021
[IL] Epoch 9/100, Loss: 1.0105
[IL] Epoch 10/100, Loss: 1.0050
[IL] Epoch 11/100, Loss: 0.9918
[IL] Epoch 12/100, Loss: 1.0112
[IL] Epoch 13/100, Loss: 0.9975
[IL] Epoch 14/100, Loss: 0.9998
[IL] Epoch 15/100, Loss: 1.0039
[IL] Epoch 16/100, Loss: 0.9963
[IL] Epoch 17/100, Loss: 1.0003
[IL] Epoch 18/100, Loss: 1.0024
[IL] Epoch 19/100, Loss: 1.0051
[IL] Epoch 20/100, Loss: 1.0013
[IL] Epoch 21/100, Loss: 1.0054
[IL] Epoch 22/100, Loss: 1.0062
[IL] Epoch 23/100, Loss: 1.0070
[IL] Epoch 24/100, Loss: 0.9991
[IL] Epoch 25/100, Loss: 1.0007
[IL] Epoch 26/100, Loss: 1.0064
[IL] Epoch 27/100, Loss: 0.9996
[IL] Epoch 28/100, Loss: 0.9979
[IL] Epoch 29/100, Loss: 0.9988
[IL] Epoch 30/100, Loss: 1.0050
[IL] Epoch 31/100, Loss: 0.9979
[IL] Epoch 32/100, Loss: 1.0027
[IL] Epoch 33/100, Loss: 1.0040
[IL] Epoch 34/100, Loss: 0.9965
[IL] Epoch 35/100, Loss: 0.9998
[IL] Epoch 36/100, Loss: 1.0007
[IL] Epoch 37/100, Loss: 1.0017
[IL] Epoch 38/100, Loss: 1.0012
[IL] Epoch 39/100, Loss: 0.9978
[IL] Epoch 40/100, Loss: 1.0005
[IL] Epoch 41/100, Loss: 1.0011
[IL] Epoch 42/100, Loss: 1.0044
[IL] Epoch 43/100, Loss: 1.0009
[IL] Epoch 44/100, Loss: 1.0004
[IL] Epoch 45/100, Loss: 0.9994
[IL] Epoch 46/100, Loss: 0.9982
[IL] Epoch 47/100, Loss: 1.0063
[IL] Epoch 48/100, Loss: 0.9987
[IL] Epoch 49/100, Loss: 0.9881
[IL] Epoch 50/100, Loss: 0.9957
[IL] Epoch 51/100, Loss: 1.0033
[IL] Epoch 52/100, Loss: 0.9951
[IL] Epoch 53/100, Loss: 0.9972
[IL] Epoch 54/100, Loss: 1.0042
[IL] Epoch 55/100, Loss: 0.9990
[IL] Epoch 56/100, Loss: 1.0016
[IL] Epoch 57/100, Loss: 0.9992
[IL] Epoch 58/100, Loss: 0.9972
[IL] Epoch 59/100, Loss: 1.0106
[IL] Epoch 60/100, Loss: 0.9996
[IL] Epoch 61/100, Loss: 1.0029
[IL] Epoch 62/100, Loss: 1.0023
[IL] Epoch 63/100, Loss: 0.9960
[IL] Epoch 64/100, Loss: 0.9926
[IL] Epoch 65/100, Loss: 0.9926
[IL] Epoch 66/100, Loss: 0.9951
[IL] Epoch 67/100, Loss: 0.9997
[IL] Epoch 68/100, Loss: 1.0086
[IL] Epoch 69/100, Loss: 1.0023
[IL] Epoch 70/100, Loss: 1.0000
[IL] Epoch 71/100, Loss: 1.0049
[IL] Epoch 72/100, Loss: 1.0032
[IL] Epoch 73/100, Loss: 1.0030
[IL] Epoch 74/100, Loss: 0.9938
[IL] Epoch 75/100, Loss: 1.0014
[IL] Epoch 76/100, Loss: 1.0004
[IL] Epoch 77/100, Loss: 1.0020
[IL] Epoch 78/100, Loss: 1.0110
[IL] Epoch 79/100, Loss: 1.0002
[IL] Epoch 80/100, Loss: 0.9995
[IL] Epoch 81/100, Loss: 0.9976
[IL] Epoch 82/100, Loss: 1.0065
[IL] Epoch 83/100, Loss: 1.0049
[IL] Epoch 84/100, Loss: 1.0006
[IL] Epoch 85/100, Loss: 1.0040
[IL] Epoch 86/100, Loss: 0.9996
[IL] Epoch 87/100, Loss: 0.9946
[IL] Epoch 88/100, Loss: 1.0013
[IL] Epoch 89/100, Loss: 1.0030
[IL] Epoch 90/100, Loss: 0.9978
[IL] Epoch 91/100, Loss: 0.9961
[IL] Epoch 92/100, Loss: 0.9950
[IL] Epoch 93/100, Loss: 1.0040
[IL] Epoch 94/100, Loss: 0.9937
[IL] Epoch 95/100, Loss: 0.9968
[IL] Epoch 96/100, Loss: 1.0015
[IL] Epoch 97/100, Loss: 1.0058
[IL] Epoch 98/100, Loss: 0.9944
[IL] Epoch 99/100, Loss: 0.9993
test_mean_score: 0.0
[IL] Eval - Success Rate: 0.000
[Checkpoint] Saved to /nfs_global/S/yangrongzheng/RL100/3D-Diffusion-Policy/3D-Diffusion-Policy/checkpoints/offline_iter_0.ckpt

================================================================================
               OFFLINE RL ITERATION 2/5
================================================================================


[RL100Trainer] Line 6 — Training Transition Model T_θ (Iteration 1)

[TransitionModel] Encoding dataset for transition model training...
[TransitionModel] Dataset: 1737 samples, input_dim=260, target_dim=257
[TransitionModel] Epoch    0 | train=-16.49345 | val=0.02293 | no-improve=0/5
[TransitionModel] Epoch   15 | train=-23.43632 | val=0.02353 | no-improve=5/5
[TransitionModel] Training complete. Elites=[6, 2, 3, 5, 4], val_loss=0.02169

[RL100Trainer] Phase 2a: Training IQL Critics (Iteration 1)
[IQL] Epoch 0/50, V Loss: 1.5846, Q Loss: 10.0149
[IQL] Epoch 1/50, V Loss: 1.4507, Q Loss: 4.7294
[IQL] Epoch 2/50, V Loss: 0.8113, Q Loss: 3.4107
[IQL] Epoch 3/50, V Loss: 0.8406, Q Loss: 2.8230
[IQL] Epoch 4/50, V Loss: 0.8133, Q Loss: 2.5877
[IQL] Epoch 5/50, V Loss: 0.6688, Q Loss: 2.5465
[IQL] Epoch 6/50, V Loss: 0.5602, Q Loss: 2.5735
[IQL] Epoch 7/50, V Loss: 0.4726, Q Loss: 2.8173
[IQL] Epoch 8/50, V Loss: 0.4107, Q Loss: 3.0092
[IQL] Epoch 9/50, V Loss: 0.2458, Q Loss: 3.3361
[IQL] Epoch 10/50, V Loss: 0.1703, Q Loss: 3.6096
[IQL] Epoch 11/50, V Loss: 0.1518, Q Loss: 3.7753
[IQL] Epoch 12/50, V Loss: 0.1377, Q Loss: 3.9780
[IQL] Epoch 13/50, V Loss: 0.2423, Q Loss: 4.0817
[IQL] Epoch 14/50, V Loss: 0.1211, Q Loss: 4.1202
[IQL] Epoch 15/50, V Loss: 0.1625, Q Loss: 4.0998
[IQL] Epoch 16/50, V Loss: 0.1659, Q Loss: 4.1031
[IQL] Epoch 17/50, V Loss: 0.1599, Q Loss: 4.0623
[IQL] Epoch 18/50, V Loss: 0.1280, Q Loss: 3.9905
[IQL] Epoch 19/50, V Loss: 0.1928, Q Loss: 3.9572
[IQL] Epoch 20/50, V Loss: 0.1467, Q Loss: 3.9014
[IQL] Epoch 21/50, V Loss: 0.1915, Q Loss: 3.8810
[IQL] Epoch 22/50, V Loss: 0.1403, Q Loss: 3.7943
[IQL] Epoch 23/50, V Loss: 0.2114, Q Loss: 3.7352
[IQL] Epoch 24/50, V Loss: 0.1961, Q Loss: 3.6657
[IQL] Epoch 25/50, V Loss: 0.2368, Q Loss: 3.5969
[IQL] Epoch 26/50, V Loss: 0.1555, Q Loss: 3.6014
[IQL] Epoch 27/50, V Loss: 0.1964, Q Loss: 3.5582
[IQL] Epoch 28/50, V Loss: 0.1545, Q Loss: 3.4416
[IQL] Epoch 29/50, V Loss: 0.1694, Q Loss: 3.3313
[IQL] Epoch 30/50, V Loss: 0.1549, Q Loss: 3.3118
[IQL] Epoch 31/50, V Loss: 0.1845, Q Loss: 3.1564
[IQL] Epoch 32/50, V Loss: 0.2096, Q Loss: 3.0951
[IQL] Epoch 33/50, V Loss: 0.1676, Q Loss: 3.0505
[IQL] Epoch 34/50, V Loss: 0.2043, Q Loss: 3.0574
[IQL] Epoch 35/50, V Loss: 0.1909, Q Loss: 3.0883
[IQL] Epoch 36/50, V Loss: 0.2413, Q Loss: 3.1501
[IQL] Epoch 37/50, V Loss: 0.4596, Q Loss: 3.1434
[IQL] Epoch 38/50, V Loss: 0.3203, Q Loss: 3.0507
[IQL] Epoch 39/50, V Loss: 0.3691, Q Loss: 3.1752
[IQL] Epoch 40/50, V Loss: 0.2052, Q Loss: 2.9802
[IQL] Epoch 41/50, V Loss: 0.1719, Q Loss: 2.9593
[IQL] Epoch 42/50, V Loss: 0.2525, Q Loss: 2.8052
[IQL] Epoch 43/50, V Loss: 0.2257, Q Loss: 2.7173
[IQL] Epoch 44/50, V Loss: 0.4275, Q Loss: 3.0328
[IQL] Epoch 45/50, V Loss: 0.2310, Q Loss: 2.8518
[IQL] Epoch 46/50, V Loss: 0.2112, Q Loss: 2.7672
[IQL] Epoch 47/50, V Loss: 0.1934, Q Loss: 2.5865
[IQL] Epoch 48/50, V Loss: 0.4112, Q Loss: 2.8920
[IQL] Epoch 49/50, V Loss: 0.3981, Q Loss: 2.7750

[RL100Trainer] Phase 2b: Offline RL Optimization (Iteration 1)
[Offline RL] Epoch 0/100, PPO Loss: 2.1010, CD Loss: 0.9958
[Offline RL] Epoch 1/100, PPO Loss: 2.1007, CD Loss: 0.9699
[Offline RL] Epoch 2/100, PPO Loss: 2.1075, CD Loss: 0.9493
[Offline RL] Epoch 3/100, PPO Loss: 2.0977, CD Loss: 0.9475
[Offline RL] Epoch 4/100, PPO Loss: 2.1209, CD Loss: 0.9487
[Offline RL] Epoch 5/100, PPO Loss: 2.1241, CD Loss: 0.9481
[Offline RL] Epoch 6/100, PPO Loss: 2.1488, CD Loss: 0.9162
[Offline RL] Epoch 7/100, PPO Loss: 2.1392, CD Loss: 0.8880
[Offline RL] Epoch 8/100, PPO Loss: 2.1174, CD Loss: 0.8524
[Offline RL] Epoch 9/100, PPO Loss: 2.0847, CD Loss: 0.8496
[Offline RL] Epoch 10/100, PPO Loss: 2.0496, CD Loss: 0.8377
[Offline RL] Epoch 11/100, PPO Loss: 2.0407, CD Loss: 0.8468
[Offline RL] Epoch 12/100, PPO Loss: 2.0622, CD Loss: 0.8327
[Offline RL] Epoch 13/100, PPO Loss: 2.0288, CD Loss: 0.8329
[Offline RL] Epoch 14/100, PPO Loss: 2.0355, CD Loss: 0.8431
[Offline RL] Epoch 15/100, PPO Loss: 1.9665, CD Loss: 0.8588
[Offline RL] Epoch 16/100, PPO Loss: 2.0126, CD Loss: 0.8771
[Offline RL] Epoch 17/100, PPO Loss: 2.0424, CD Loss: 0.8780
[Offline RL] Epoch 18/100, PPO Loss: 2.0397, CD Loss: 0.8841
[Offline RL] Epoch 19/100, PPO Loss: 2.1034, CD Loss: 0.8762
[Offline RL] Epoch 20/100, PPO Loss: 2.1293, CD Loss: 0.8711
[Offline RL] Epoch 21/100, PPO Loss: 2.1202, CD Loss: 0.8676
[Offline RL] Epoch 22/100, PPO Loss: 2.1551, CD Loss: 0.8524
[Offline RL] Epoch 23/100, PPO Loss: 2.1725, CD Loss: 0.8371
[Offline RL] Epoch 24/100, PPO Loss: 2.1828, CD Loss: 0.8332
[Offline RL] Epoch 25/100, PPO Loss: 2.1275, CD Loss: 0.8343
[Offline RL] Epoch 26/100, PPO Loss: 2.1220, CD Loss: 0.8215
[Offline RL] Epoch 27/100, PPO Loss: 2.1160, CD Loss: 0.8192
[Offline RL] Epoch 28/100, PPO Loss: 2.0283, CD Loss: 0.7947
[Offline RL] Epoch 29/100, PPO Loss: 1.9251, CD Loss: 0.7738
[Offline RL] Epoch 30/100, PPO Loss: 1.9438, CD Loss: 0.7645
[Offline RL] Epoch 31/100, PPO Loss: 1.9037, CD Loss: 0.7650
[Offline RL] Epoch 32/100, PPO Loss: 1.9098, CD Loss: 0.7572
[Offline RL] Epoch 33/100, PPO Loss: 1.9480, CD Loss: 0.7612
[Offline RL] Epoch 34/100, PPO Loss: 2.0239, CD Loss: 0.7582
[Offline RL] Epoch 35/100, PPO Loss: 2.0079, CD Loss: 0.7672
[Offline RL] Epoch 36/100, PPO Loss: 2.0015, CD Loss: 0.7759
[Offline RL] Epoch 37/100, PPO Loss: 1.9863, CD Loss: 0.7709
[Offline RL] Epoch 38/100, PPO Loss: 1.9238, CD Loss: 0.7533
[Offline RL] Epoch 39/100, PPO Loss: 1.9695, CD Loss: 0.7452
[Offline RL] Epoch 40/100, PPO Loss: 2.0110, CD Loss: 0.7402
[Offline RL] Epoch 41/100, PPO Loss: 2.0202, CD Loss: 0.7004
[Offline RL] Epoch 42/100, PPO Loss: 2.0267, CD Loss: 0.6857
[Offline RL] Epoch 43/100, PPO Loss: 2.0224, CD Loss: 0.6506
[Offline RL] Epoch 44/100, PPO Loss: 2.0431, CD Loss: 0.6507
[Offline RL] Epoch 45/100, PPO Loss: 2.0491, CD Loss: 0.6474
[Offline RL] Epoch 46/100, PPO Loss: 2.0471, CD Loss: 0.6288
[Offline RL] Epoch 47/100, PPO Loss: 2.0619, CD Loss: 0.6275
[Offline RL] Epoch 48/100, PPO Loss: 2.1030, CD Loss: 0.6241
[Offline RL] Epoch 49/100, PPO Loss: 2.1551, CD Loss: 0.6309
[Offline RL] Epoch 50/100, PPO Loss: 2.2048, CD Loss: 0.6166
[Offline RL] Epoch 51/100, PPO Loss: 2.1100, CD Loss: 0.6302
[Offline RL] Epoch 52/100, PPO Loss: 2.0433, CD Loss: 0.6360
[Offline RL] Epoch 53/100, PPO Loss: 1.9964, CD Loss: 0.6567
[Offline RL] Epoch 54/100, PPO Loss: 2.0188, CD Loss: 0.6520
[Offline RL] Epoch 55/100, PPO Loss: 2.0898, CD Loss: 0.6436
[Offline RL] Epoch 56/100, PPO Loss: 2.0582, CD Loss: 0.6499
[Offline RL] Epoch 57/100, PPO Loss: 2.2161, CD Loss: 0.6426
[Offline RL] Epoch 58/100, PPO Loss: 2.3109, CD Loss: 0.6367
[Offline RL] Epoch 59/100, PPO Loss: 2.3655, CD Loss: 0.6148
[Offline RL] Epoch 60/100, PPO Loss: 2.4258, CD Loss: 0.6021
[Offline RL] Epoch 61/100, PPO Loss: 2.3152, CD Loss: 0.5724
[Offline RL] Epoch 62/100, PPO Loss: 2.2714, CD Loss: 0.5545
[Offline RL] Epoch 63/100, PPO Loss: 2.2835, CD Loss: 0.5432
[Offline RL] Epoch 64/100, PPO Loss: 2.3639, CD Loss: 0.5340
[Offline RL] Epoch 65/100, PPO Loss: 2.3284, CD Loss: 0.5421
[Offline RL] Epoch 66/100, PPO Loss: 2.2560, CD Loss: 0.5505
[Offline RL] Epoch 67/100, PPO Loss: 2.2376, CD Loss: 0.5477
[Offline RL] Epoch 68/100, PPO Loss: 2.2025, CD Loss: 0.5651
[Offline RL] Epoch 69/100, PPO Loss: 2.1360, CD Loss: 0.5503
[Offline RL] Epoch 70/100, PPO Loss: 2.0750, CD Loss: 0.5635
[Offline RL] Epoch 71/100, PPO Loss: 2.0841, CD Loss: 0.5417
[Offline RL] Epoch 72/100, PPO Loss: 2.1076, CD Loss: 0.5474
[Offline RL] Epoch 73/100, PPO Loss: 2.0904, CD Loss: 0.5326
[Offline RL] Epoch 74/100, PPO Loss: 2.1111, CD Loss: 0.5276
[Offline RL] Epoch 75/100, PPO Loss: 2.1182, CD Loss: 0.5346
[Offline RL] Epoch 76/100, PPO Loss: 2.0821, CD Loss: 0.5438
[Offline RL] Epoch 77/100, PPO Loss: 2.0795, CD Loss: 0.5476
[Offline RL] Epoch 78/100, PPO Loss: 2.0323, CD Loss: 0.5632
[Offline RL] Epoch 79/100, PPO Loss: 2.0720, CD Loss: 0.5533
[Offline RL] Epoch 80/100, PPO Loss: 2.1643, CD Loss: 0.5846
[Offline RL] Epoch 81/100, PPO Loss: 2.1827, CD Loss: 0.6026
[Offline RL] Epoch 82/100, PPO Loss: 2.1197, CD Loss: 0.5904
[Offline RL] Epoch 83/100, PPO Loss: 2.1939, CD Loss: 0.6081
[Offline RL] Epoch 84/100, PPO Loss: 2.2508, CD Loss: 0.6118
[Offline RL] Epoch 85/100, PPO Loss: 2.3374, CD Loss: 0.5963
[Offline RL] Epoch 86/100, PPO Loss: 2.4166, CD Loss: 0.5855
[Offline RL] Epoch 87/100, PPO Loss: 2.5137, CD Loss: 0.6037
[Offline RL] Epoch 88/100, PPO Loss: 2.4401, CD Loss: 0.5987
[Offline RL] Epoch 89/100, PPO Loss: 2.3097, CD Loss: 0.6110
[Offline RL] Epoch 90/100, PPO Loss: 2.2675, CD Loss: 0.6083
[Offline RL] Epoch 91/100, PPO Loss: 2.2457, CD Loss: 0.6252
[Offline RL] Epoch 92/100, PPO Loss: 2.0843, CD Loss: 0.6474
[Offline RL] Epoch 93/100, PPO Loss: 1.9746, CD Loss: 0.6594
[Offline RL] Epoch 94/100, PPO Loss: 1.7867, CD Loss: 0.6719
[Offline RL] Epoch 95/100, PPO Loss: 1.6654, CD Loss: 0.6739
[Offline RL] Epoch 96/100, PPO Loss: 1.5985, CD Loss: 0.6764
[Offline RL] Epoch 97/100, PPO Loss: 1.5024, CD Loss: 0.6791
[Offline RL] Epoch 98/100, PPO Loss: 1.5309, CD Loss: 0.6841
[Offline RL] Epoch 99/100, PPO Loss: 1.5446, CD Loss: 0.6791

[RL100Trainer] Phase 2c: Collecting New Data (Iteration 1)
test_mean_score: 0.0
[Data Collection] Success Rate: 0.000, Reward: 2261.75

[RL100Trainer] Retraining IL on merged dataset...

============================================================
[RL100Trainer] Phase 1: Imitation Learning
============================================================

[IL] Epoch 0/100, Loss: 1.5396
[IL] Epoch 1/100, Loss: 1.1089
[IL] Epoch 2/100, Loss: 1.0957
[IL] Epoch 3/100, Loss: 1.0358
[IL] Epoch 4/100, Loss: 1.0206
[IL] Epoch 5/100, Loss: 1.0061
[IL] Epoch 6/100, Loss: 1.0093
[IL] Epoch 7/100, Loss: 1.0058
[IL] Epoch 8/100, Loss: 1.0021
[IL] Epoch 9/100, Loss: 1.0025
[IL] Epoch 10/100, Loss: 0.9992
[IL] Epoch 11/100, Loss: 0.9924
[IL] Epoch 12/100, Loss: 1.0039
[IL] Epoch 13/100, Loss: 0.9974
[IL] Epoch 14/100, Loss: 0.9980
[IL] Epoch 15/100, Loss: 1.0060
[IL] Epoch 16/100, Loss: 1.0013
[IL] Epoch 17/100, Loss: 1.0038
[IL] Epoch 18/100, Loss: 1.0056
[IL] Epoch 19/100, Loss: 0.9999
[IL] Epoch 20/100, Loss: 1.0049
[IL] Epoch 21/100, Loss: 0.9993
[IL] Epoch 22/100, Loss: 1.0012
[IL] Epoch 23/100, Loss: 0.9954
[IL] Epoch 24/100, Loss: 0.9995
[IL] Epoch 25/100, Loss: 0.9972
[IL] Epoch 26/100, Loss: 0.9978
[IL] Epoch 27/100, Loss: 1.0056
[IL] Epoch 28/100, Loss: 1.0070
[IL] Epoch 29/100, Loss: 1.0051
[IL] Epoch 30/100, Loss: 0.9997
[IL] Epoch 31/100, Loss: 0.9968
[IL] Epoch 32/100, Loss: 0.9945
[IL] Epoch 33/100, Loss: 0.9963
[IL] Epoch 34/100, Loss: 1.0000
[IL] Epoch 35/100, Loss: 0.9977
[IL] Epoch 36/100, Loss: 1.0003
[IL] Epoch 37/100, Loss: 1.0032
[IL] Epoch 38/100, Loss: 0.9993
[IL] Epoch 39/100, Loss: 1.0062
[IL] Epoch 40/100, Loss: 0.9955
[IL] Epoch 41/100, Loss: 0.9973
[IL] Epoch 42/100, Loss: 1.0046
[IL] Epoch 43/100, Loss: 1.0014
[IL] Epoch 44/100, Loss: 0.9962
[IL] Epoch 45/100, Loss: 0.9994
[IL] Epoch 46/100, Loss: 1.0039
[IL] Epoch 47/100, Loss: 0.9969
[IL] Epoch 48/100, Loss: 1.0020
[IL] Epoch 49/100, Loss: 0.9933
[IL] Epoch 50/100, Loss: 1.0038
[IL] Epoch 51/100, Loss: 1.0013
[IL] Epoch 52/100, Loss: 1.0057
[IL] Epoch 53/100, Loss: 1.0012
[IL] Epoch 54/100, Loss: 1.0061
[IL] Epoch 55/100, Loss: 0.9960
[IL] Epoch 56/100, Loss: 1.0029
[IL] Epoch 57/100, Loss: 0.9981
[IL] Epoch 58/100, Loss: 0.9978
[IL] Epoch 59/100, Loss: 0.9917
[IL] Epoch 60/100, Loss: 1.0094
[IL] Epoch 61/100, Loss: 1.0000
[IL] Epoch 62/100, Loss: 0.9993
[IL] Epoch 63/100, Loss: 1.0051
[IL] Epoch 64/100, Loss: 0.9987
[IL] Epoch 65/100, Loss: 0.9953
[IL] Epoch 66/100, Loss: 0.9943
[IL] Epoch 67/100, Loss: 0.9990
[IL] Epoch 68/100, Loss: 0.9923
[IL] Epoch 69/100, Loss: 1.0075
[IL] Epoch 70/100, Loss: 0.9895
[IL] Epoch 71/100, Loss: 0.9966
[IL] Epoch 72/100, Loss: 0.9976
[IL] Epoch 73/100, Loss: 0.9991
[IL] Epoch 74/100, Loss: 0.9973
[IL] Epoch 75/100, Loss: 0.9983
[IL] Epoch 76/100, Loss: 0.9904
[IL] Epoch 77/100, Loss: 1.0008
[IL] Epoch 78/100, Loss: 0.9898
[IL] Epoch 79/100, Loss: 0.9923
[IL] Epoch 80/100, Loss: 1.0026
[IL] Epoch 81/100, Loss: 0.9893
[IL] Epoch 82/100, Loss: 0.9847
[IL] Epoch 83/100, Loss: 0.9812
[IL] Epoch 84/100, Loss: 0.9800
[IL] Epoch 85/100, Loss: 0.9849
[IL] Epoch 86/100, Loss: 0.9776
[IL] Epoch 87/100, Loss: 0.9775
[IL] Epoch 88/100, Loss: 0.9732
[IL] Epoch 89/100, Loss: 0.9802
[IL] Epoch 90/100, Loss: 0.9777
[IL] Epoch 91/100, Loss: 0.9727
[IL] Epoch 92/100, Loss: 0.9740
[IL] Epoch 93/100, Loss: 0.9733
[IL] Epoch 94/100, Loss: 0.9655
[IL] Epoch 95/100, Loss: 0.9758
[IL] Epoch 96/100, Loss: 0.9721
[IL] Epoch 97/100, Loss: 0.9683
[IL] Epoch 98/100, Loss: 0.9653
[IL] Epoch 99/100, Loss: 0.9711
test_mean_score: 0.0
[IL] Eval - Success Rate: 0.000
[Checkpoint] Saved to /nfs_global/S/yangrongzheng/RL100/3D-Diffusion-Policy/3D-Diffusion-Policy/checkpoints/offline_iter_1.ckpt

================================================================================
               OFFLINE RL ITERATION 3/5
================================================================================


[RL100Trainer] Line 6 — Training Transition Model T_θ (Iteration 2)

[TransitionModel] Encoding dataset for transition model training...
[TransitionModel] Dataset: 1737 samples, input_dim=260, target_dim=257
[TransitionModel] Epoch    0 | train=-18.92480 | val=0.02427 | no-improve=0/5
[TransitionModel] Epoch   20 | train=-25.87673 | val=0.02318 | no-improve=1/5
[TransitionModel] Epoch   24 | train=-27.72689 | val=0.02381 | no-improve=5/5
[TransitionModel] Training complete. Elites=[1, 0, 6, 5, 4], val_loss=0.02151

[RL100Trainer] Phase 2a: Training IQL Critics (Iteration 2)
[IQL] Epoch 0/50, V Loss: 34.7488, Q Loss: 59.1847
[IQL] Epoch 1/50, V Loss: 14.3055, Q Loss: 19.1437
[IQL] Epoch 2/50, V Loss: 5.3807, Q Loss: 13.4223
[IQL] Epoch 3/50, V Loss: 0.8903, Q Loss: 9.8240
[IQL] Epoch 4/50, V Loss: 0.9454, Q Loss: 7.0360
[IQL] Epoch 5/50, V Loss: 0.7045, Q Loss: 5.9635
[IQL] Epoch 6/50, V Loss: 0.7089, Q Loss: 5.4024
[IQL] Epoch 7/50, V Loss: 0.6808, Q Loss: 4.9142
[IQL] Epoch 8/50, V Loss: 0.5932, Q Loss: 4.6536
[IQL] Epoch 9/50, V Loss: 0.5206, Q Loss: 4.3631
[IQL] Epoch 10/50, V Loss: 0.5912, Q Loss: 4.1138
[IQL] Epoch 11/50, V Loss: 0.5915, Q Loss: 3.8566
[IQL] Epoch 12/50, V Loss: 0.5855, Q Loss: 3.6821
[IQL] Epoch 13/50, V Loss: 0.6017, Q Loss: 3.5232
[IQL] Epoch 14/50, V Loss: 0.6181, Q Loss: 3.3667
[IQL] Epoch 15/50, V Loss: 0.6428, Q Loss: 3.3103
[IQL] Epoch 16/50, V Loss: 0.6533, Q Loss: 3.2757
[IQL] Epoch 17/50, V Loss: 0.6438, Q Loss: 3.1684
[IQL] Epoch 18/50, V Loss: 0.6405, Q Loss: 3.1209
[IQL] Epoch 19/50, V Loss: 0.5980, Q Loss: 3.0649
[IQL] Epoch 20/50, V Loss: 0.6664, Q Loss: 3.0306
[IQL] Epoch 21/50, V Loss: 0.6098, Q Loss: 3.0776
[IQL] Epoch 22/50, V Loss: 0.5902, Q Loss: 2.9365
[IQL] Epoch 23/50, V Loss: 0.5469, Q Loss: 2.8841
[IQL] Epoch 24/50, V Loss: 0.5703, Q Loss: 2.9112
[IQL] Epoch 25/50, V Loss: 0.5292, Q Loss: 2.8885
[IQL] Epoch 26/50, V Loss: 0.5027, Q Loss: 2.9020
[IQL] Epoch 27/50, V Loss: 0.4854, Q Loss: 2.8582
[IQL] Epoch 28/50, V Loss: 0.4586, Q Loss: 2.8497
[IQL] Epoch 29/50, V Loss: 0.4199, Q Loss: 2.8121
[IQL] Epoch 30/50, V Loss: 0.4341, Q Loss: 2.7733
[IQL] Epoch 31/50, V Loss: 0.5032, Q Loss: 2.8792
[IQL] Epoch 32/50, V Loss: 0.6236, Q Loss: 2.8981
[IQL] Epoch 33/50, V Loss: 0.3983, Q Loss: 2.7682
[IQL] Epoch 34/50, V Loss: 0.2831, Q Loss: 2.8456
[IQL] Epoch 35/50, V Loss: 0.2505, Q Loss: 2.8004
[IQL] Epoch 36/50, V Loss: 0.2129, Q Loss: 2.7964
[IQL] Epoch 37/50, V Loss: 0.2036, Q Loss: 2.7504
[IQL] Epoch 38/50, V Loss: 0.1914, Q Loss: 2.6862
[IQL] Epoch 39/50, V Loss: 0.2055, Q Loss: 2.7029
[IQL] Epoch 40/50, V Loss: 0.4323, Q Loss: 2.7384
[IQL] Epoch 41/50, V Loss: 0.5273, Q Loss: 2.7115
[IQL] Epoch 42/50, V Loss: 0.2433, Q Loss: 2.7336
[IQL] Epoch 43/50, V Loss: 0.3611, Q Loss: 2.6411
[IQL] Epoch 44/50, V Loss: 0.2456, Q Loss: 2.7119
[IQL] Epoch 45/50, V Loss: 0.1963, Q Loss: 2.5130
[IQL] Epoch 46/50, V Loss: 0.2650, Q Loss: 2.5990
[IQL] Epoch 47/50, V Loss: 0.2791, Q Loss: 2.5716
[IQL] Epoch 48/50, V Loss: 0.1804, Q Loss: 2.4672
[IQL] Epoch 49/50, V Loss: 0.1838, Q Loss: 2.4532

[RL100Trainer] Phase 2b: Offline RL Optimization (Iteration 2)
[Offline RL] Epoch 0/100, PPO Loss: 0.0061, CD Loss: 0.9342
[Offline RL] Epoch 1/100, PPO Loss: -0.5944, CD Loss: 0.8866
[Offline RL] Epoch 2/100, PPO Loss: -0.3983, CD Loss: 0.8388
[Offline RL] Epoch 3/100, PPO Loss: -0.3590, CD Loss: 0.7918
[Offline RL] Epoch 4/100, PPO Loss: -0.1838, CD Loss: 0.7975
[Offline RL] Epoch 5/100, PPO Loss: 0.1537, CD Loss: 0.8125
[Offline RL] Epoch 6/100, PPO Loss: 0.2753, CD Loss: 0.8343
[Offline RL] Epoch 7/100, PPO Loss: 0.1790, CD Loss: 0.8391
[Offline RL] Epoch 8/100, PPO Loss: -0.1619, CD Loss: 0.8506
[Offline RL] Epoch 9/100, PPO Loss: -0.4972, CD Loss: 0.8351
[Offline RL] Epoch 10/100, PPO Loss: -0.8159, CD Loss: 0.8200
[Offline RL] Epoch 11/100, PPO Loss: -0.9879, CD Loss: 0.8004
[Offline RL] Epoch 12/100, PPO Loss: -1.0198, CD Loss: 0.7889
[Offline RL] Epoch 13/100, PPO Loss: -1.0907, CD Loss: 0.7712
[Offline RL] Epoch 14/100, PPO Loss: -1.3458, CD Loss: 0.7643
[Offline RL] Epoch 15/100, PPO Loss: -1.4660, CD Loss: 0.7255
[Offline RL] Epoch 16/100, PPO Loss: -1.4693, CD Loss: 0.7099
[Offline RL] Epoch 17/100, PPO Loss: -1.4249, CD Loss: 0.6691
[Offline RL] Epoch 18/100, PPO Loss: -1.2116, CD Loss: 0.6480
[Offline RL] Epoch 19/100, PPO Loss: -1.1519, CD Loss: 0.6345
[Offline RL] Epoch 20/100, PPO Loss: -1.2814, CD Loss: 0.6141
[Offline RL] Epoch 21/100, PPO Loss: -1.6187, CD Loss: 0.6275
[Offline RL] Epoch 22/100, PPO Loss: -1.7003, CD Loss: 0.6128
[Offline RL] Epoch 23/100, PPO Loss: -1.7675, CD Loss: 0.5747
[Offline RL] Epoch 24/100, PPO Loss: -1.4721, CD Loss: 0.5754
[Offline RL] Epoch 25/100, PPO Loss: -1.3494, CD Loss: 0.5457
[Offline RL] Epoch 26/100, PPO Loss: -1.4760, CD Loss: 0.5564
[Offline RL] Epoch 27/100, PPO Loss: -1.7698, CD Loss: 0.5663
[Offline RL] Epoch 28/100, PPO Loss: -2.2894, CD Loss: 0.5736
[Offline RL] Epoch 29/100, PPO Loss: -2.4454, CD Loss: 0.5760
[Offline RL] Epoch 30/100, PPO Loss: -2.3634, CD Loss: 0.5766
[Offline RL] Epoch 31/100, PPO Loss: -2.3908, CD Loss: 0.5713
[Offline RL] Epoch 32/100, PPO Loss: -2.4062, CD Loss: 0.5819
[Offline RL] Epoch 33/100, PPO Loss: -2.6950, CD Loss: 0.5746
[Offline RL] Epoch 34/100, PPO Loss: -3.0811, CD Loss: 0.5772
[Offline RL] Epoch 35/100, PPO Loss: -3.1819, CD Loss: 0.5487
[Offline RL] Epoch 36/100, PPO Loss: -3.2422, CD Loss: 0.5427
[Offline RL] Epoch 37/100, PPO Loss: -3.1185, CD Loss: 0.5545
[Offline RL] Epoch 38/100, PPO Loss: -2.9470, CD Loss: 0.5519
[Offline RL] Epoch 39/100, PPO Loss: -3.0843, CD Loss: 0.5466
[Offline RL] Epoch 40/100, PPO Loss: -3.2206, CD Loss: 0.5377
[Offline RL] Epoch 41/100, PPO Loss: -2.7708, CD Loss: 0.5314
[Offline RL] Epoch 42/100, PPO Loss: -2.2501, CD Loss: 0.5372
[Offline RL] Epoch 43/100, PPO Loss: -2.2347, CD Loss: 0.5417
[Offline RL] Epoch 44/100, PPO Loss: -2.5291, CD Loss: 0.5523
[Offline RL] Epoch 45/100, PPO Loss: -2.4480, CD Loss: 0.5669
[Offline RL] Epoch 46/100, PPO Loss: -2.2984, CD Loss: 0.5873
[Offline RL] Epoch 47/100, PPO Loss: -2.2810, CD Loss: 0.5906
[Offline RL] Epoch 48/100, PPO Loss: -2.3138, CD Loss: 0.5826
[Offline RL] Epoch 49/100, PPO Loss: -2.6324, CD Loss: 0.5784
[Offline RL] Epoch 50/100, PPO Loss: -2.7045, CD Loss: 0.5807
[Offline RL] Epoch 51/100, PPO Loss: -2.3298, CD Loss: 0.5790
[Offline RL] Epoch 52/100, PPO Loss: -1.9595, CD Loss: 0.6044
[Offline RL] Epoch 53/100, PPO Loss: -1.7808, CD Loss: 0.6312
[Offline RL] Epoch 54/100, PPO Loss: -2.0157, CD Loss: 0.6423
[Offline RL] Epoch 55/100, PPO Loss: -2.1606, CD Loss: 0.6288
[Offline RL] Epoch 56/100, PPO Loss: -2.3549, CD Loss: 0.6110
[Offline RL] Epoch 57/100, PPO Loss: -2.4160, CD Loss: 0.5908
[Offline RL] Epoch 58/100, PPO Loss: -2.4748, CD Loss: 0.5828
[Offline RL] Epoch 59/100, PPO Loss: -2.3985, CD Loss: 0.5778
[Offline RL] Epoch 60/100, PPO Loss: -2.2281, CD Loss: 0.5584
[Offline RL] Epoch 61/100, PPO Loss: -2.0113, CD Loss: 0.5334
[Offline RL] Epoch 62/100, PPO Loss: -1.5844, CD Loss: 0.5276
[Offline RL] Epoch 63/100, PPO Loss: -1.2564, CD Loss: 0.5347
[Offline RL] Epoch 64/100, PPO Loss: -0.9636, CD Loss: 0.5473
[Offline RL] Epoch 65/100, PPO Loss: -0.4501, CD Loss: 0.5500
[Offline RL] Epoch 66/100, PPO Loss: -0.1400, CD Loss: 0.5565
[Offline RL] Epoch 67/100, PPO Loss: -0.0328, CD Loss: 0.5763
[Offline RL] Epoch 68/100, PPO Loss: 0.0882, CD Loss: 0.5859
[Offline RL] Epoch 69/100, PPO Loss: 0.0560, CD Loss: 0.5824
[Offline RL] Epoch 70/100, PPO Loss: 0.1764, CD Loss: 0.5766
[Offline RL] Epoch 71/100, PPO Loss: 0.1964, CD Loss: 0.5693
[Offline RL] Epoch 72/100, PPO Loss: 0.2326, CD Loss: 0.5945
[Offline RL] Epoch 73/100, PPO Loss: 0.3717, CD Loss: 0.6136
[Offline RL] Epoch 74/100, PPO Loss: 0.5871, CD Loss: 0.6197
[Offline RL] Epoch 75/100, PPO Loss: 0.6927, CD Loss: 0.6282
[Offline RL] Epoch 76/100, PPO Loss: 0.7776, CD Loss: 0.6410
[Offline RL] Epoch 77/100, PPO Loss: 0.8044, CD Loss: 0.6379
[Offline RL] Epoch 78/100, PPO Loss: 0.8596, CD Loss: 0.6463
[Offline RL] Epoch 79/100, PPO Loss: 0.9735, CD Loss: 0.6405
[Offline RL] Epoch 80/100, PPO Loss: 0.9943, CD Loss: 0.6323
[Offline RL] Epoch 81/100, PPO Loss: 0.4094, CD Loss: 0.6261
[Offline RL] Epoch 82/100, PPO Loss: -0.0127, CD Loss: 0.6191
[Offline RL] Epoch 83/100, PPO Loss: -0.2013, CD Loss: 0.6319
[Offline RL] Epoch 84/100, PPO Loss: -0.3369, CD Loss: 0.6357
[Offline RL] Epoch 85/100, PPO Loss: -0.3910, CD Loss: 0.6347
[Offline RL] Epoch 86/100, PPO Loss: -0.4383, CD Loss: 0.6096
[Offline RL] Epoch 87/100, PPO Loss: -0.4633, CD Loss: 0.5847
[Offline RL] Epoch 88/100, PPO Loss: -0.5741, CD Loss: 0.5808
[Offline RL] Epoch 89/100, PPO Loss: -0.8150, CD Loss: 0.5591
[Offline RL] Epoch 90/100, PPO Loss: -1.1144, CD Loss: 0.5529
[Offline RL] Epoch 91/100, PPO Loss: -1.3888, CD Loss: 0.5581
[Offline RL] Epoch 92/100, PPO Loss: -1.5420, CD Loss: 0.5693
[Offline RL] Epoch 93/100, PPO Loss: -1.4848, CD Loss: 0.5579
[Offline RL] Epoch 94/100, PPO Loss: -1.4108, CD Loss: 0.5591
[Offline RL] Epoch 95/100, PPO Loss: -1.3425, CD Loss: 0.5423
[Offline RL] Epoch 96/100, PPO Loss: -1.3131, CD Loss: 0.5261
[Offline RL] Epoch 97/100, PPO Loss: -1.0441, CD Loss: 0.5245
[Offline RL] Epoch 98/100, PPO Loss: -0.9767, CD Loss: 0.5202
[Offline RL] Epoch 99/100, PPO Loss: -1.1760, CD Loss: 0.5218

[RL100Trainer] Phase 2c: Collecting New Data (Iteration 2)
test_mean_score: 0.0
[Data Collection] Success Rate: 0.000, Reward: 842.13

[RL100Trainer] Retraining IL on merged dataset...

============================================================
[RL100Trainer] Phase 1: Imitation Learning
============================================================

[IL] Epoch 0/100, Loss: 1.7888
[IL] Epoch 1/100, Loss: 1.0878
[IL] Epoch 2/100, Loss: 1.1464
[IL] Epoch 3/100, Loss: 1.0351
[IL] Epoch 4/100, Loss: 1.0190
[IL] Epoch 5/100, Loss: 1.0167
[IL] Epoch 6/100, Loss: 1.0005
[IL] Epoch 7/100, Loss: 0.9947
[IL] Epoch 8/100, Loss: 1.0017
[IL] Epoch 9/100, Loss: 0.9910
[IL] Epoch 10/100, Loss: 0.9830
[IL] Epoch 11/100, Loss: 0.9873
[IL] Epoch 12/100, Loss: 0.9750
[IL] Epoch 13/100, Loss: 0.9808
[IL] Epoch 14/100, Loss: 0.9713
[IL] Epoch 15/100, Loss: 0.9705
[IL] Epoch 16/100, Loss: 0.9732
[IL] Epoch 17/100, Loss: 0.9717
[IL] Epoch 18/100, Loss: 0.9764
[IL] Epoch 19/100, Loss: 0.9700
[IL] Epoch 20/100, Loss: 0.9643
[IL] Epoch 21/100, Loss: 0.9681
[IL] Epoch 22/100, Loss: 0.9614
[IL] Epoch 23/100, Loss: 0.9644
[IL] Epoch 24/100, Loss: 0.9684
[IL] Epoch 25/100, Loss: 0.9612
[IL] Epoch 26/100, Loss: 0.9633
[IL] Epoch 27/100, Loss: 0.9649
[IL] Epoch 28/100, Loss: 0.9578
[IL] Epoch 29/100, Loss: 0.9687
[IL] Epoch 30/100, Loss: 0.9613
[IL] Epoch 31/100, Loss: 0.9678
[IL] Epoch 32/100, Loss: 0.9620
[IL] Epoch 33/100, Loss: 0.9601
[IL] Epoch 34/100, Loss: 0.9567
[IL] Epoch 35/100, Loss: 0.9521
[IL] Epoch 36/100, Loss: 0.9549
[IL] Epoch 37/100, Loss: 0.9409
[IL] Epoch 38/100, Loss: 0.9265
[IL] Epoch 39/100, Loss: 0.9144
[IL] Epoch 40/100, Loss: 0.9155
[IL] Epoch 41/100, Loss: 0.9025
[IL] Epoch 42/100, Loss: 0.9000
[IL] Epoch 43/100, Loss: 0.9030
[IL] Epoch 44/100, Loss: 0.8935
[IL] Epoch 45/100, Loss: 0.8925
[IL] Epoch 46/100, Loss: 0.9017
[IL] Epoch 47/100, Loss: 0.8937
[IL] Epoch 48/100, Loss: 0.8908
[IL] Epoch 49/100, Loss: 0.8938
[IL] Epoch 50/100, Loss: 0.8892
[IL] Epoch 51/100, Loss: 0.8936
[IL] Epoch 52/100, Loss: 0.8948
[IL] Epoch 53/100, Loss: 0.8930
[IL] Epoch 54/100, Loss: 0.8940
[IL] Epoch 55/100, Loss: 0.8828
[IL] Epoch 56/100, Loss: 0.8891
[IL] Epoch 57/100, Loss: 0.8875
[IL] Epoch 58/100, Loss: 0.8881
[IL] Epoch 59/100, Loss: 0.8890
[IL] Epoch 60/100, Loss: 0.8800
[IL] Epoch 61/100, Loss: 0.8865
[IL] Epoch 62/100, Loss: 0.8817
[IL] Epoch 63/100, Loss: 0.8871
[IL] Epoch 64/100, Loss: 0.8816
[IL] Epoch 65/100, Loss: 0.8833
[IL] Epoch 66/100, Loss: 0.8828
[IL] Epoch 67/100, Loss: 0.8819
[IL] Epoch 68/100, Loss: 0.8804
[IL] Epoch 69/100, Loss: 0.8708
[IL] Epoch 70/100, Loss: 0.8719
[IL] Epoch 71/100, Loss: 0.8804
[IL] Epoch 72/100, Loss: 0.8802
[IL] Epoch 73/100, Loss: 0.8740
[IL] Epoch 74/100, Loss: 0.8754
[IL] Epoch 75/100, Loss: 0.8743
[IL] Epoch 76/100, Loss: 0.8699
[IL] Epoch 77/100, Loss: 0.8721
[IL] Epoch 78/100, Loss: 0.8708
[IL] Epoch 79/100, Loss: 0.8637
[IL] Epoch 80/100, Loss: 0.8679
[IL] Epoch 81/100, Loss: 0.8685
[IL] Epoch 82/100, Loss: 0.8694
[IL] Epoch 83/100, Loss: 0.8675
[IL] Epoch 84/100, Loss: 0.8671
[IL] Epoch 85/100, Loss: 0.8720
[IL] Epoch 86/100, Loss: 0.8714
[IL] Epoch 87/100, Loss: 0.8679
[IL] Epoch 88/100, Loss: 0.8620
[IL] Epoch 89/100, Loss: 0.8621
[IL] Epoch 90/100, Loss: 0.8621
[IL] Epoch 91/100, Loss: 0.8658
[IL] Epoch 92/100, Loss: 0.8624
[IL] Epoch 93/100, Loss: 0.8559
[IL] Epoch 94/100, Loss: 0.8526
[IL] Epoch 95/100, Loss: 0.8552
[IL] Epoch 96/100, Loss: 0.8634
[IL] Epoch 97/100, Loss: 0.8623
[IL] Epoch 98/100, Loss: 0.8607
[IL] Epoch 99/100, Loss: 0.8563
test_mean_score: 0.0
[IL] Eval - Success Rate: 0.000
[Checkpoint] Saved to /nfs_global/S/yangrongzheng/RL100/3D-Diffusion-Policy/3D-Diffusion-Policy/checkpoints/offline_iter_2.ckpt

================================================================================
               OFFLINE RL ITERATION 4/5
================================================================================


[RL100Trainer] Line 6 — Training Transition Model T_θ (Iteration 3)

[TransitionModel] Encoding dataset for transition model training...
[TransitionModel] Dataset: 1737 samples, input_dim=260, target_dim=257
[TransitionModel] Epoch    0 | train=-22.45279 | val=0.02526 | no-improve=0/5
[TransitionModel] Epoch   20 | train=-33.11844 | val=0.02369 | no-improve=0/5
[TransitionModel] Epoch   25 | train=-31.79946 | val=0.02335 | no-improve=5/5
[TransitionModel] Training complete. Elites=[0, 6, 5, 4, 2], val_loss=0.02263

[RL100Trainer] Phase 2a: Training IQL Critics (Iteration 3)
[IQL] Epoch 0/50, V Loss: 0.3973, Q Loss: 2.8745
[IQL] Epoch 1/50, V Loss: 0.3887, Q Loss: 2.5372
[IQL] Epoch 2/50, V Loss: 0.4770, Q Loss: 2.5877
[IQL] Epoch 3/50, V Loss: 0.2251, Q Loss: 2.5379
[IQL] Epoch 4/50, V Loss: 0.2594, Q Loss: 2.4081
[IQL] Epoch 5/50, V Loss: 0.3225, Q Loss: 2.4410
[IQL] Epoch 6/50, V Loss: 0.3216, Q Loss: 2.6534
[IQL] Epoch 7/50, V Loss: 0.2747, Q Loss: 2.4996
[IQL] Epoch 8/50, V Loss: 0.2210, Q Loss: 2.4351
[IQL] Epoch 9/50, V Loss: 0.2271, Q Loss: 2.4314
[IQL] Epoch 10/50, V Loss: 0.2312, Q Loss: 2.4075
[IQL] Epoch 11/50, V Loss: 0.2292, Q Loss: 2.3295
[IQL] Epoch 12/50, V Loss: 0.2725, Q Loss: 2.3148
[IQL] Epoch 13/50, V Loss: 0.2998, Q Loss: 2.3158
[IQL] Epoch 14/50, V Loss: 0.2710, Q Loss: 2.2669
[IQL] Epoch 15/50, V Loss: 0.2465, Q Loss: 2.2345
[IQL] Epoch 16/50, V Loss: 0.3283, Q Loss: 2.2869
[IQL] Epoch 17/50, V Loss: 0.2751, Q Loss: 2.3052
[IQL] Epoch 18/50, V Loss: 0.4561, Q Loss: 2.4500
[IQL] Epoch 19/50, V Loss: 0.3156, Q Loss: 2.3405
[IQL] Epoch 20/50, V Loss: 0.4577, Q Loss: 2.4927
[IQL] Epoch 21/50, V Loss: 0.3811, Q Loss: 2.4882
[IQL] Epoch 22/50, V Loss: 0.4418, Q Loss: 2.4774
[IQL] Epoch 23/50, V Loss: 0.4175, Q Loss: 2.3535
[IQL] Epoch 24/50, V Loss: 0.3311, Q Loss: 2.2627
[IQL] Epoch 25/50, V Loss: 0.3590, Q Loss: 2.3201
[IQL] Epoch 26/50, V Loss: 0.3338, Q Loss: 2.3151
[IQL] Epoch 27/50, V Loss: 0.4290, Q Loss: 2.4205
[IQL] Epoch 28/50, V Loss: 0.3165, Q Loss: 2.2339
[IQL] Epoch 29/50, V Loss: 0.3054, Q Loss: 2.1294
[IQL] Epoch 30/50, V Loss: 0.2701, Q Loss: 2.1572
[IQL] Epoch 31/50, V Loss: 0.3404, Q Loss: 2.2561
[IQL] Epoch 32/50, V Loss: 0.2843, Q Loss: 2.3012
[IQL] Epoch 33/50, V Loss: 0.3445, Q Loss: 2.2175
[IQL] Epoch 34/50, V Loss: 0.3495, Q Loss: 2.1218
[IQL] Epoch 35/50, V Loss: 0.4103, Q Loss: 2.1268
[IQL] Epoch 36/50, V Loss: 0.3547, Q Loss: 2.2807
[IQL] Epoch 37/50, V Loss: 0.4871, Q Loss: 2.4442
[IQL] Epoch 38/50, V Loss: 0.4606, Q Loss: 2.3080
[IQL] Epoch 39/50, V Loss: 0.5470, Q Loss: 2.4671
[IQL] Epoch 40/50, V Loss: 0.7708, Q Loss: 2.8393
[IQL] Epoch 41/50, V Loss: 0.5154, Q Loss: 2.5037
[IQL] Epoch 42/50, V Loss: 0.7472, Q Loss: 2.2755
[IQL] Epoch 43/50, V Loss: 0.4558, Q Loss: 2.2371
[IQL] Epoch 44/50, V Loss: 0.3319, Q Loss: 2.1784
[IQL] Epoch 45/50, V Loss: 0.3282, Q Loss: 2.0151
[IQL] Epoch 46/50, V Loss: 0.4269, Q Loss: 2.2146
[IQL] Epoch 47/50, V Loss: 0.3842, Q Loss: 2.2547
[IQL] Epoch 48/50, V Loss: 0.8549, Q Loss: 2.7127
[IQL] Epoch 49/50, V Loss: 0.5066, Q Loss: 2.3475

[RL100Trainer] Phase 2b: Offline RL Optimization (Iteration 3)
[Offline RL] Epoch 0/100, PPO Loss: -3.7254, CD Loss: 0.9441
[Offline RL] Epoch 1/100, PPO Loss: -1.5386, CD Loss: 0.9183
[Offline RL] Epoch 2/100, PPO Loss: 1.2688, CD Loss: 0.8559
[Offline RL] Epoch 3/100, PPO Loss: 3.4372, CD Loss: 0.8067
[Offline RL] Epoch 4/100, PPO Loss: 4.5210, CD Loss: 0.8061
[Offline RL] Epoch 5/100, PPO Loss: 4.9680, CD Loss: 0.8070
[Offline RL] Epoch 6/100, PPO Loss: 5.8732, CD Loss: 0.8329
[Offline RL] Epoch 7/100, PPO Loss: 6.5080, CD Loss: 0.8523
[Offline RL] Epoch 8/100, PPO Loss: 6.8616, CD Loss: 0.8518
[Offline RL] Epoch 9/100, PPO Loss: 7.2376, CD Loss: 0.8472
[Offline RL] Epoch 10/100, PPO Loss: 7.4246, CD Loss: 0.8338
[Offline RL] Epoch 11/100, PPO Loss: 7.5405, CD Loss: 0.8357
[Offline RL] Epoch 12/100, PPO Loss: 7.4359, CD Loss: 0.8426
[Offline RL] Epoch 13/100, PPO Loss: 7.5681, CD Loss: 0.8429
[Offline RL] Epoch 14/100, PPO Loss: 7.5776, CD Loss: 0.8257
[Offline RL] Epoch 15/100, PPO Loss: 7.3701, CD Loss: 0.8039
[Offline RL] Epoch 16/100, PPO Loss: 7.0377, CD Loss: 0.7836
[Offline RL] Epoch 17/100, PPO Loss: 6.4025, CD Loss: 0.7913
[Offline RL] Epoch 18/100, PPO Loss: 6.1234, CD Loss: 0.8058
[Offline RL] Epoch 19/100, PPO Loss: 6.1776, CD Loss: 0.8092
[Offline RL] Epoch 20/100, PPO Loss: 6.2558, CD Loss: 0.8076
[Offline RL] Epoch 21/100, PPO Loss: 6.2879, CD Loss: 0.8163
[Offline RL] Epoch 22/100, PPO Loss: 6.3319, CD Loss: 0.8059
[Offline RL] Epoch 23/100, PPO Loss: 6.3470, CD Loss: 0.8090
[Offline RL] Epoch 24/100, PPO Loss: 6.2610, CD Loss: 0.7943
[Offline RL] Epoch 25/100, PPO Loss: 6.4552, CD Loss: 0.7953
[Offline RL] Epoch 26/100, PPO Loss: 6.8218, CD Loss: 0.7977
[Offline RL] Epoch 27/100, PPO Loss: 7.1779, CD Loss: 0.8100
[Offline RL] Epoch 28/100, PPO Loss: 7.4438, CD Loss: 0.7872
[Offline RL] Epoch 29/100, PPO Loss: 7.4993, CD Loss: 0.7764
[Offline RL] Epoch 30/100, PPO Loss: 7.7432, CD Loss: 0.7667
[Offline RL] Epoch 31/100, PPO Loss: 7.7434, CD Loss: 0.7423
[Offline RL] Epoch 32/100, PPO Loss: 7.9576, CD Loss: 0.7128
[Offline RL] Epoch 33/100, PPO Loss: 8.3158, CD Loss: 0.6919
[Offline RL] Epoch 34/100, PPO Loss: 8.7055, CD Loss: 0.6867
[Offline RL] Epoch 35/100, PPO Loss: 8.9089, CD Loss: 0.6853
[Offline RL] Epoch 36/100, PPO Loss: 9.1209, CD Loss: 0.6840
[Offline RL] Epoch 37/100, PPO Loss: 9.2844, CD Loss: 0.6628
[Offline RL] Epoch 38/100, PPO Loss: 9.4661, CD Loss: 0.6407
[Offline RL] Epoch 39/100, PPO Loss: 9.7580, CD Loss: 0.6447
[Offline RL] Epoch 40/100, PPO Loss: 10.2803, CD Loss: 0.6314
[Offline RL] Epoch 41/100, PPO Loss: 10.2090, CD Loss: 0.6248
[Offline RL] Epoch 42/100, PPO Loss: 10.7614, CD Loss: 0.6307
[Offline RL] Epoch 43/100, PPO Loss: 11.6343, CD Loss: 0.6153
[Offline RL] Epoch 44/100, PPO Loss: 11.6491, CD Loss: 0.6186
[Offline RL] Epoch 45/100, PPO Loss: 11.1420, CD Loss: 0.6273
[Offline RL] Epoch 46/100, PPO Loss: 11.1187, CD Loss: 0.6301
[Offline RL] Epoch 47/100, PPO Loss: 11.2811, CD Loss: 0.6370
[Offline RL] Epoch 48/100, PPO Loss: 11.6623, CD Loss: 0.6493
[Offline RL] Epoch 49/100, PPO Loss: 12.3747, CD Loss: 0.6547
[Offline RL] Epoch 50/100, PPO Loss: 12.6571, CD Loss: 0.6698
[Offline RL] Epoch 51/100, PPO Loss: 12.4174, CD Loss: 0.6867
[Offline RL] Epoch 52/100, PPO Loss: 11.9732, CD Loss: 0.7015
[Offline RL] Epoch 53/100, PPO Loss: 11.4604, CD Loss: 0.6887
[Offline RL] Epoch 54/100, PPO Loss: 10.9888, CD Loss: 0.6739
[Offline RL] Epoch 55/100, PPO Loss: 10.6283, CD Loss: 0.6567
[Offline RL] Epoch 56/100, PPO Loss: 10.3800, CD Loss: 0.6671
[Offline RL] Epoch 57/100, PPO Loss: 10.3930, CD Loss: 0.6590
[Offline RL] Epoch 58/100, PPO Loss: 10.8629, CD Loss: 0.6490
[Offline RL] Epoch 59/100, PPO Loss: 11.6366, CD Loss: 0.6448
[Offline RL] Epoch 60/100, PPO Loss: 12.0905, CD Loss: 0.6409
[Offline RL] Epoch 61/100, PPO Loss: 12.2664, CD Loss: 0.6404
[Offline RL] Epoch 62/100, PPO Loss: 12.2733, CD Loss: 0.6584
[Offline RL] Epoch 63/100, PPO Loss: 12.4805, CD Loss: 0.6549
[Offline RL] Epoch 64/100, PPO Loss: 12.8845, CD Loss: 0.6280
[Offline RL] Epoch 65/100, PPO Loss: 13.1974, CD Loss: 0.6325
[Offline RL] Epoch 66/100, PPO Loss: 13.2372, CD Loss: 0.6348
[Offline RL] Epoch 67/100, PPO Loss: 13.4135, CD Loss: 0.6397
[Offline RL] Epoch 68/100, PPO Loss: 13.7705, CD Loss: 0.6565
[Offline RL] Epoch 69/100, PPO Loss: 13.9097, CD Loss: 0.6640
[Offline RL] Epoch 70/100, PPO Loss: 14.0638, CD Loss: 0.6715
[Offline RL] Epoch 71/100, PPO Loss: 14.1456, CD Loss: 0.6936
[Offline RL] Epoch 72/100, PPO Loss: 14.2544, CD Loss: 0.6983
[Offline RL] Epoch 73/100, PPO Loss: 14.6314, CD Loss: 0.6780
[Offline RL] Epoch 74/100, PPO Loss: 15.1243, CD Loss: 0.6855
[Offline RL] Epoch 75/100, PPO Loss: 16.0107, CD Loss: 0.6899
[Offline RL] Epoch 76/100, PPO Loss: 16.6450, CD Loss: 0.6879
[Offline RL] Epoch 77/100, PPO Loss: 16.6976, CD Loss: 0.6808
[Offline RL] Epoch 78/100, PPO Loss: 16.0145, CD Loss: 0.6652
[Offline RL] Epoch 79/100, PPO Loss: 15.4155, CD Loss: 0.6623
[Offline RL] Epoch 80/100, PPO Loss: 14.8799, CD Loss: 0.6605
[Offline RL] Epoch 81/100, PPO Loss: 14.2512, CD Loss: 0.6636
[Offline RL] Epoch 82/100, PPO Loss: 13.3689, CD Loss: 0.6671
[Offline RL] Epoch 83/100, PPO Loss: 12.6193, CD Loss: 0.6644
[Offline RL] Epoch 84/100, PPO Loss: 11.7489, CD Loss: 0.6784
[Offline RL] Epoch 85/100, PPO Loss: 10.9390, CD Loss: 0.6804
[Offline RL] Epoch 86/100, PPO Loss: 10.7676, CD Loss: 0.6709
[Offline RL] Epoch 87/100, PPO Loss: 10.9629, CD Loss: 0.6632
[Offline RL] Epoch 88/100, PPO Loss: 11.5530, CD Loss: 0.6698
[Offline RL] Epoch 89/100, PPO Loss: 11.9217, CD Loss: 0.6698
[Offline RL] Epoch 90/100, PPO Loss: 12.8896, CD Loss: 0.6795
[Offline RL] Epoch 91/100, PPO Loss: 13.4136, CD Loss: 0.7154
[Offline RL] Epoch 92/100, PPO Loss: 13.7333, CD Loss: 0.7329
[Offline RL] Epoch 93/100, PPO Loss: 14.2602, CD Loss: 0.7462
[Offline RL] Epoch 94/100, PPO Loss: 14.6690, CD Loss: 0.7527
[Offline RL] Epoch 95/100, PPO Loss: 14.9647, CD Loss: 0.7536
[Offline RL] Epoch 96/100, PPO Loss: 15.4180, CD Loss: 0.7520
[Offline RL] Epoch 97/100, PPO Loss: 16.0879, CD Loss: 0.7516
[Offline RL] Epoch 98/100, PPO Loss: 16.1211, CD Loss: 0.7532
[Offline RL] Epoch 99/100, PPO Loss: 15.7502, CD Loss: 0.7458

[RL100Trainer] Phase 2c: Collecting New Data (Iteration 3)
test_mean_score: 0.0
[Data Collection] Success Rate: 0.000, Reward: 879.93

[RL100Trainer] Retraining IL on merged dataset...

============================================================
[RL100Trainer] Phase 1: Imitation Learning
============================================================

[IL] Epoch 0/100, Loss: 1.6196
[IL] Epoch 1/100, Loss: 1.0669
[IL] Epoch 2/100, Loss: 1.0961
[IL] Epoch 3/100, Loss: 1.0259
[IL] Epoch 4/100, Loss: 1.0183
[IL] Epoch 5/100, Loss: 1.0074
[IL] Epoch 6/100, Loss: 0.9963
[IL] Epoch 7/100, Loss: 0.9987
[IL] Epoch 8/100, Loss: 0.9977
[IL] Epoch 9/100, Loss: 0.9943
[IL] Epoch 10/100, Loss: 0.9959
[IL] Epoch 11/100, Loss: 0.9940
[IL] Epoch 12/100, Loss: 0.9802
[IL] Epoch 13/100, Loss: 0.9635
[IL] Epoch 14/100, Loss: 0.9503
[IL] Epoch 15/100, Loss: 0.9370
[IL] Epoch 16/100, Loss: 0.9204
[IL] Epoch 17/100, Loss: 0.9206
[IL] Epoch 18/100, Loss: 0.9173
[IL] Epoch 19/100, Loss: 0.9134
[IL] Epoch 20/100, Loss: 0.9183
[IL] Epoch 21/100, Loss: 0.9088
[IL] Epoch 22/100, Loss: 0.9013
[IL] Epoch 23/100, Loss: 0.8864
[IL] Epoch 24/100, Loss: 0.8861
[IL] Epoch 25/100, Loss: 0.8811
[IL] Epoch 26/100, Loss: 0.8765
[IL] Epoch 27/100, Loss: 0.8725
[IL] Epoch 28/100, Loss: 0.8702
[IL] Epoch 29/100, Loss: 0.8658
[IL] Epoch 30/100, Loss: 0.8617
[IL] Epoch 31/100, Loss: 0.8645
[IL] Epoch 32/100, Loss: 0.8635
[IL] Epoch 33/100, Loss: 0.8631
[IL] Epoch 34/100, Loss: 0.8587
[IL] Epoch 35/100, Loss: 0.8606
[IL] Epoch 36/100, Loss: 0.8527
[IL] Epoch 37/100, Loss: 0.8584
[IL] Epoch 38/100, Loss: 0.8504
[IL] Epoch 39/100, Loss: 0.8567
[IL] Epoch 40/100, Loss: 0.8491
[IL] Epoch 41/100, Loss: 0.8502
[IL] Epoch 42/100, Loss: 0.8537
[IL] Epoch 43/100, Loss: 0.8508
[IL] Epoch 44/100, Loss: 0.8481
[IL] Epoch 45/100, Loss: 0.8470
[IL] Epoch 46/100, Loss: 0.8456
[IL] Epoch 47/100, Loss: 0.8462
[IL] Epoch 48/100, Loss: 0.8520
[IL] Epoch 49/100, Loss: 0.8421
[IL] Epoch 50/100, Loss: 0.8465
[IL] Epoch 51/100, Loss: 0.8546
[IL] Epoch 52/100, Loss: 0.8436
[IL] Epoch 53/100, Loss: 0.8397
[IL] Epoch 54/100, Loss: 0.8479
[IL] Epoch 55/100, Loss: 0.8420
[IL] Epoch 56/100, Loss: 0.8494
[IL] Epoch 57/100, Loss: 0.8533
[IL] Epoch 58/100, Loss: 0.8522
[IL] Epoch 59/100, Loss: 0.8509
[IL] Epoch 60/100, Loss: 0.8444
[IL] Epoch 61/100, Loss: 0.8527
[IL] Epoch 62/100, Loss: 0.8379
[IL] Epoch 63/100, Loss: 0.8363
[IL] Epoch 64/100, Loss: 0.8482
[IL] Epoch 65/100, Loss: 0.8461
[IL] Epoch 66/100, Loss: 0.8445
[IL] Epoch 67/100, Loss: 0.8430
[IL] Epoch 68/100, Loss: 0.8392
[IL] Epoch 69/100, Loss: 0.8348
[IL] Epoch 70/100, Loss: 0.8372
[IL] Epoch 71/100, Loss: 0.8379
[IL] Epoch 72/100, Loss: 0.8384
[IL] Epoch 73/100, Loss: 0.8313
[IL] Epoch 74/100, Loss: 0.8380
[IL] Epoch 75/100, Loss: 0.8379
[IL] Epoch 76/100, Loss: 0.8351
[IL] Epoch 77/100, Loss: 0.8382
[IL] Epoch 78/100, Loss: 0.8394
[IL] Epoch 79/100, Loss: 0.8424
[IL] Epoch 80/100, Loss: 0.8373
[IL] Epoch 81/100, Loss: 0.8451
[IL] Epoch 82/100, Loss: 0.8369
[IL] Epoch 83/100, Loss: 0.8397
[IL] Epoch 84/100, Loss: 0.8401
[IL] Epoch 85/100, Loss: 0.8362
[IL] Epoch 86/100, Loss: 0.8370
[IL] Epoch 87/100, Loss: 0.8381
[IL] Epoch 88/100, Loss: 0.8260
[IL] Epoch 89/100, Loss: 0.8339
[IL] Epoch 90/100, Loss: 0.8404
[IL] Epoch 91/100, Loss: 0.8352
[IL] Epoch 92/100, Loss: 0.8324
[IL] Epoch 93/100, Loss: 0.8364
[IL] Epoch 94/100, Loss: 0.8320
[IL] Epoch 95/100, Loss: 0.8411
[IL] Epoch 96/100, Loss: 0.8328
[IL] Epoch 97/100, Loss: 0.8236
[IL] Epoch 98/100, Loss: 0.8321
[IL] Epoch 99/100, Loss: 0.8304
test_mean_score: 0.0
[IL] Eval - Success Rate: 0.000
[Checkpoint] Saved to /nfs_global/S/yangrongzheng/RL100/3D-Diffusion-Policy/3D-Diffusion-Policy/checkpoints/offline_iter_3.ckpt

================================================================================
               OFFLINE RL ITERATION 5/5
================================================================================


[RL100Trainer] Line 6 — Training Transition Model T_θ (Iteration 4)

[TransitionModel] Encoding dataset for transition model training...
[TransitionModel] Dataset: 1737 samples, input_dim=260, target_dim=257
[TransitionModel] Epoch    0 | train=-28.18105 | val=0.02303 | no-improve=0/5
[TransitionModel] Epoch   20 | train=-35.10041 | val=0.02243 | no-improve=5/5
[TransitionModel] Training complete. Elites=[0, 5, 4, 6, 2], val_loss=0.02190

[RL100Trainer] Phase 2a: Training IQL Critics (Iteration 4)
[IQL] Epoch 0/50, V Loss: 0.5403, Q Loss: 3.1406
[IQL] Epoch 1/50, V Loss: 0.8410, Q Loss: 2.7762
[IQL] Epoch 2/50, V Loss: 0.7318, Q Loss: 2.4309
[IQL] Epoch 3/50, V Loss: 0.6503, Q Loss: 2.3549
[IQL] Epoch 4/50, V Loss: 0.5396, Q Loss: 2.4607
[IQL] Epoch 5/50, V Loss: 0.6507, Q Loss: 2.6161
[IQL] Epoch 6/50, V Loss: 0.4472, Q Loss: 2.5043
[IQL] Epoch 7/50, V Loss: 0.4591, Q Loss: 2.1523
[IQL] Epoch 8/50, V Loss: 0.4866, Q Loss: 2.1814
[IQL] Epoch 9/50, V Loss: 1.1670, Q Loss: 2.3240
[IQL] Epoch 10/50, V Loss: 0.7277, Q Loss: 2.2997
[IQL] Epoch 11/50, V Loss: 0.3280, Q Loss: 2.2260
[IQL] Epoch 12/50, V Loss: 0.5530, Q Loss: 2.5482
[IQL] Epoch 13/50, V Loss: 0.7010, Q Loss: 2.4988
[IQL] Epoch 14/50, V Loss: 0.5112, Q Loss: 2.5134
[IQL] Epoch 15/50, V Loss: 0.9117, Q Loss: 2.7575
[IQL] Epoch 16/50, V Loss: 0.5158, Q Loss: 2.5449
[IQL] Epoch 17/50, V Loss: 0.3573, Q Loss: 2.2511
[IQL] Epoch 18/50, V Loss: 0.7862, Q Loss: 2.4230
[IQL] Epoch 19/50, V Loss: 0.6304, Q Loss: 2.3675
[IQL] Epoch 20/50, V Loss: 0.4223, Q Loss: 2.3005
[IQL] Epoch 21/50, V Loss: 0.4726, Q Loss: 2.1567
[IQL] Epoch 22/50, V Loss: 0.3652, Q Loss: 2.3874
[IQL] Epoch 23/50, V Loss: 0.8043, Q Loss: 2.4089
[IQL] Epoch 24/50, V Loss: 0.5814, Q Loss: 2.6165
[IQL] Epoch 25/50, V Loss: 0.5085, Q Loss: 2.4866
[IQL] Epoch 26/50, V Loss: 0.6011, Q Loss: 2.2763
[IQL] Epoch 27/50, V Loss: 0.6738, Q Loss: 2.2334
[IQL] Epoch 28/50, V Loss: 1.0241, Q Loss: 2.6758
[IQL] Epoch 29/50, V Loss: 0.6221, Q Loss: 2.2998
[IQL] Epoch 30/50, V Loss: 0.4945, Q Loss: 2.1919
[IQL] Epoch 31/50, V Loss: 0.6082, Q Loss: 2.3999
[IQL] Epoch 32/50, V Loss: 0.4674, Q Loss: 2.2414
[IQL] Epoch 33/50, V Loss: 0.4010, Q Loss: 2.2148
[IQL] Epoch 34/50, V Loss: 0.3385, Q Loss: 2.0723
[IQL] Epoch 35/50, V Loss: 0.4131, Q Loss: 2.2198
[IQL] Epoch 36/50, V Loss: 0.3864, Q Loss: 2.2354
[IQL] Epoch 37/50, V Loss: 0.5629, Q Loss: 2.3678
[IQL] Epoch 38/50, V Loss: 0.4574, Q Loss: 2.3628
[IQL] Epoch 39/50, V Loss: 0.5983, Q Loss: 2.4994
[IQL] Epoch 40/50, V Loss: 0.8227, Q Loss: 2.5378
[IQL] Epoch 41/50, V Loss: 0.4825, Q Loss: 2.2527
[IQL] Epoch 42/50, V Loss: 0.8970, Q Loss: 2.7011
[IQL] Epoch 43/50, V Loss: 0.7484, Q Loss: 2.7442
[IQL] Epoch 44/50, V Loss: 1.3210, Q Loss: 3.1333
[IQL] Epoch 45/50, V Loss: 0.8413, Q Loss: 2.9242
[IQL] Epoch 46/50, V Loss: 1.3921, Q Loss: 3.1489
[IQL] Epoch 47/50, V Loss: 1.7515, Q Loss: 4.0207
[IQL] Epoch 48/50, V Loss: 1.4639, Q Loss: 3.4654
[IQL] Epoch 49/50, V Loss: 1.1737, Q Loss: 3.0102

[RL100Trainer] Phase 2b: Offline RL Optimization (Iteration 4)
[Offline RL] Epoch 0/100, PPO Loss: -9.5919, CD Loss: 0.7313
[Offline RL] Epoch 1/100, PPO Loss: -12.1899, CD Loss: 0.7239
[Offline RL] Epoch 2/100, PPO Loss: -13.5309, CD Loss: 0.6969
[Offline RL] Epoch 3/100, PPO Loss: -14.8386, CD Loss: 0.7600
[Offline RL] Epoch 4/100, PPO Loss: -15.2187, CD Loss: 0.7619
[Offline RL] Epoch 5/100, PPO Loss: -15.2406, CD Loss: 0.7583
[Offline RL] Epoch 6/100, PPO Loss: -15.4311, CD Loss: 0.7381
[Offline RL] Epoch 7/100, PPO Loss: -15.8168, CD Loss: 0.7379
[Offline RL] Epoch 8/100, PPO Loss: -16.1154, CD Loss: 0.7329
[Offline RL] Epoch 9/100, PPO Loss: -16.2420, CD Loss: 0.7176
[Offline RL] Epoch 10/100, PPO Loss: -16.1347, CD Loss: 0.6932
[Offline RL] Epoch 11/100, PPO Loss: -16.0056, CD Loss: 0.6939
[Offline RL] Epoch 12/100, PPO Loss: -15.4482, CD Loss: 0.7126
[Offline RL] Epoch 13/100, PPO Loss: -15.1408, CD Loss: 0.6994
[Offline RL] Epoch 14/100, PPO Loss: -14.8503, CD Loss: 0.6742
[Offline RL] Epoch 15/100, PPO Loss: -14.1282, CD Loss: 0.6538
[Offline RL] Epoch 16/100, PPO Loss: -13.5576, CD Loss: 0.6186
[Offline RL] Epoch 17/100, PPO Loss: -13.8062, CD Loss: 0.6189
[Offline RL] Epoch 18/100, PPO Loss: -13.6773, CD Loss: 0.6274
[Offline RL] Epoch 19/100, PPO Loss: -13.6519, CD Loss: 0.5594
[Offline RL] Epoch 20/100, PPO Loss: -14.2084, CD Loss: 0.4045
[Offline RL] Epoch 21/100, PPO Loss: -15.8002, CD Loss: 0.5555
[Offline RL] Epoch 22/100, PPO Loss: -18.1323, CD Loss: 0.4702
[Offline RL] Epoch 23/100, PPO Loss: -20.8087, CD Loss: 0.6631
[Offline RL] Epoch 24/100, PPO Loss: -22.6713, CD Loss: 0.6878
[Offline RL] Epoch 25/100, PPO Loss: -23.7509, CD Loss: 0.6618
[Offline RL] Epoch 26/100, PPO Loss: -24.8921, CD Loss: 0.6618
[Offline RL] Epoch 27/100, PPO Loss: -25.8862, CD Loss: 0.6377
[Offline RL] Epoch 28/100, PPO Loss: -26.8454, CD Loss: 0.6176
[Offline RL] Epoch 29/100, PPO Loss: -27.4019, CD Loss: 0.6039
[Offline RL] Epoch 30/100, PPO Loss: -27.6583, CD Loss: 0.5997
[Offline RL] Epoch 31/100, PPO Loss: -27.8642, CD Loss: 0.5922
[Offline RL] Epoch 32/100, PPO Loss: -27.2433, CD Loss: 0.5922
[Offline RL] Epoch 33/100, PPO Loss: -25.7233, CD Loss: 0.6085
[Offline RL] Epoch 34/100, PPO Loss: -25.0134, CD Loss: 0.6109
[Offline RL] Epoch 35/100, PPO Loss: -24.6823, CD Loss: 0.6005
[Offline RL] Epoch 36/100, PPO Loss: -24.7482, CD Loss: 0.5863
[Offline RL] Epoch 37/100, PPO Loss: -24.6393, CD Loss: 0.5578
[Offline RL] Epoch 38/100, PPO Loss: -23.9146, CD Loss: 0.5369
[Offline RL] Epoch 39/100, PPO Loss: -22.3624, CD Loss: 0.5045
[Offline RL] Epoch 40/100, PPO Loss: -18.7989, CD Loss: 0.5667
[Offline RL] Epoch 41/100, PPO Loss: -14.5904, CD Loss: 0.6858
[Offline RL] Epoch 42/100, PPO Loss: -11.6176, CD Loss: 0.6873
[Offline RL] Epoch 43/100, PPO Loss: -12.3090, CD Loss: 0.7345
[Offline RL] Epoch 44/100, PPO Loss: -12.0281, CD Loss: 0.7457
[Offline RL] Epoch 45/100, PPO Loss: -10.5312, CD Loss: 0.7934
[Offline RL] Epoch 46/100, PPO Loss: -9.8525, CD Loss: 0.8114
[Offline RL] Epoch 47/100, PPO Loss: -9.1321, CD Loss: 0.7921
[Offline RL] Epoch 48/100, PPO Loss: -8.5818, CD Loss: 0.7665
[Offline RL] Epoch 49/100, PPO Loss: -8.2020, CD Loss: 0.7448
[Offline RL] Epoch 50/100, PPO Loss: -7.7533, CD Loss: 0.7328
[Offline RL] Epoch 51/100, PPO Loss: -7.6787, CD Loss: 0.7342
[Offline RL] Epoch 52/100, PPO Loss: -7.6211, CD Loss: 0.7326
[Offline RL] Epoch 53/100, PPO Loss: -7.3481, CD Loss: 0.7259
[Offline RL] Epoch 54/100, PPO Loss: -7.2812, CD Loss: 0.7069
[Offline RL] Epoch 55/100, PPO Loss: -7.3060, CD Loss: 0.7189
[Offline RL] Epoch 56/100, PPO Loss: -7.4300, CD Loss: 0.7098
[Offline RL] Epoch 57/100, PPO Loss: -7.7598, CD Loss: 0.7096
[Offline RL] Epoch 58/100, PPO Loss: -7.6263, CD Loss: 0.6924
[Offline RL] Epoch 59/100, PPO Loss: -7.3336, CD Loss: 0.6839
[Offline RL] Epoch 60/100, PPO Loss: -7.0696, CD Loss: 0.6870
[Offline RL] Epoch 61/100, PPO Loss: -6.6777, CD Loss: 0.7101
[Offline RL] Epoch 62/100, PPO Loss: -6.3024, CD Loss: 0.7405
[Offline RL] Epoch 63/100, PPO Loss: -5.9976, CD Loss: 0.7584
[Offline RL] Epoch 64/100, PPO Loss: -5.6805, CD Loss: 0.7553
[Offline RL] Epoch 65/100, PPO Loss: -5.5818, CD Loss: 0.7595
[Offline RL] Epoch 66/100, PPO Loss: -5.7027, CD Loss: 0.7545
[Offline RL] Epoch 67/100, PPO Loss: -5.6914, CD Loss: 0.7588
[Offline RL] Epoch 68/100, PPO Loss: -5.3736, CD Loss: 0.7582
[Offline RL] Epoch 69/100, PPO Loss: -5.0994, CD Loss: 0.7664
[Offline RL] Epoch 70/100, PPO Loss: -5.0890, CD Loss: 0.7813
[Offline RL] Epoch 71/100, PPO Loss: -4.8107, CD Loss: 0.7816
[Offline RL] Epoch 72/100, PPO Loss: -4.5826, CD Loss: 0.7851
[Offline RL] Epoch 73/100, PPO Loss: -4.2944, CD Loss: 0.7872
[Offline RL] Epoch 74/100, PPO Loss: -4.1437, CD Loss: 0.7591
[Offline RL] Epoch 75/100, PPO Loss: -4.3542, CD Loss: 0.7303
[Offline RL] Epoch 76/100, PPO Loss: -4.5039, CD Loss: 0.7176
[Offline RL] Epoch 77/100, PPO Loss: -4.8370, CD Loss: 0.6996
[Offline RL] Epoch 78/100, PPO Loss: -4.8854, CD Loss: 0.7132
[Offline RL] Epoch 79/100, PPO Loss: -4.8170, CD Loss: 0.7236
[Offline RL] Epoch 80/100, PPO Loss: -4.5835, CD Loss: 0.7255
[Offline RL] Epoch 81/100, PPO Loss: -4.6269, CD Loss: 0.7476
[Offline RL] Epoch 82/100, PPO Loss: -4.4765, CD Loss: 0.7318
[Offline RL] Epoch 83/100, PPO Loss: -4.6167, CD Loss: 0.7109
[Offline RL] Epoch 84/100, PPO Loss: -4.8956, CD Loss: 0.6945
[Offline RL] Epoch 85/100, PPO Loss: -5.2160, CD Loss: 0.6202
[Offline RL] Epoch 86/100, PPO Loss: -5.2369, CD Loss: 1.3840
[Offline RL] Epoch 87/100, PPO Loss: -4.6280, CD Loss: 0.9815
[Offline RL] Epoch 88/100, PPO Loss: -3.3108, CD Loss: 0.6642
[Offline RL] Epoch 89/100, PPO Loss: -2.1497, CD Loss: 0.6865
[Offline RL] Epoch 90/100, PPO Loss: -2.2276, CD Loss: 0.7347
[Offline RL] Epoch 91/100, PPO Loss: -3.0011, CD Loss: 0.7493
[Offline RL] Epoch 92/100, PPO Loss: -4.5782, CD Loss: 0.7440
[Offline RL] Epoch 93/100, PPO Loss: -6.5426, CD Loss: 0.7185
[Offline RL] Epoch 94/100, PPO Loss: -7.4599, CD Loss: 0.7082
[Offline RL] Epoch 95/100, PPO Loss: -7.3590, CD Loss: 0.7088
[Offline RL] Epoch 96/100, PPO Loss: -7.9927, CD Loss: 0.7129
[Offline RL] Epoch 97/100, PPO Loss: -8.8038, CD Loss: 0.6833
[Offline RL] Epoch 98/100, PPO Loss: -8.1442, CD Loss: 0.6490
[Offline RL] Epoch 99/100, PPO Loss: -7.5737, CD Loss: 0.6457

[RL100Trainer] Phase 2c: Collecting New Data (Iteration 4)
test_mean_score: 0.0
[Data Collection] Success Rate: 0.000, Reward: 1730.34

[RL100Trainer] Retraining IL on merged dataset...

============================================================
[RL100Trainer] Phase 1: Imitation Learning
============================================================

[IL] Epoch 0/100, Loss: 3.7141
[IL] Epoch 1/100, Loss: 1.0600
[IL] Epoch 2/100, Loss: 1.0345
[IL] Epoch 3/100, Loss: 1.0197
[IL] Epoch 4/100, Loss: 1.0112
[IL] Epoch 5/100, Loss: 1.0102
[IL] Epoch 6/100, Loss: 1.0105
[IL] Epoch 7/100, Loss: 0.9945
[IL] Epoch 8/100, Loss: 1.0047
[IL] Epoch 9/100, Loss: 0.9989
[IL] Epoch 10/100, Loss: 0.9957
[IL] Epoch 11/100, Loss: 0.9976
[IL] Epoch 12/100, Loss: 1.0031
[IL] Epoch 13/100, Loss: 0.9940
[IL] Epoch 14/100, Loss: 0.9951
[IL] Epoch 15/100, Loss: 0.9966
[IL] Epoch 16/100, Loss: 0.9831
[IL] Epoch 17/100, Loss: 0.9851
[IL] Epoch 18/100, Loss: 0.9830
[IL] Epoch 19/100, Loss: 0.9817
[IL] Epoch 20/100, Loss: 0.9738
[IL] Epoch 21/100, Loss: 0.9822
[IL] Epoch 22/100, Loss: 0.9786
[IL] Epoch 23/100, Loss: 0.9742
[IL] Epoch 24/100, Loss: 0.9792
[IL] Epoch 25/100, Loss: 0.9697
[IL] Epoch 26/100, Loss: 0.9771
[IL] Epoch 27/100, Loss: 0.9665
[IL] Epoch 28/100, Loss: 0.9672
[IL] Epoch 29/100, Loss: 0.9722
[IL] Epoch 30/100, Loss: 0.9718
[IL] Epoch 31/100, Loss: 0.9596
[IL] Epoch 32/100, Loss: 0.9634
[IL] Epoch 33/100, Loss: 0.9631
[IL] Epoch 34/100, Loss: 0.9714
[IL] Epoch 35/100, Loss: 0.9694
[IL] Epoch 36/100, Loss: 0.9684
[IL] Epoch 37/100, Loss: 0.9684
[IL] Epoch 38/100, Loss: 0.9626
[IL] Epoch 39/100, Loss: 0.9590
[IL] Epoch 40/100, Loss: 0.9646
[IL] Epoch 41/100, Loss: 0.9593
[IL] Epoch 42/100, Loss: 0.9611
[IL] Epoch 43/100, Loss: 0.9584
[IL] Epoch 44/100, Loss: 0.9564
[IL] Epoch 45/100, Loss: 0.9591
[IL] Epoch 46/100, Loss: 0.9611
[IL] Epoch 47/100, Loss: 0.9565
[IL] Epoch 48/100, Loss: 0.9562
[IL] Epoch 49/100, Loss: 0.9591
[IL] Epoch 50/100, Loss: 0.9515
[IL] Epoch 51/100, Loss: 0.9456
[IL] Epoch 52/100, Loss: 0.9370
[IL] Epoch 53/100, Loss: 0.9389
[IL] Epoch 54/100, Loss: 0.9396
[IL] Epoch 55/100, Loss: 0.9355
[IL] Epoch 56/100, Loss: 0.9253
[IL] Epoch 57/100, Loss: 0.9244
[IL] Epoch 58/100, Loss: 0.9168
[IL] Epoch 59/100, Loss: 0.9112
[IL] Epoch 60/100, Loss: 0.9021
[IL] Epoch 61/100, Loss: 0.9029
[IL] Epoch 62/100, Loss: 0.8972
[IL] Epoch 63/100, Loss: 0.9052
[IL] Epoch 64/100, Loss: 0.9093
[IL] Epoch 65/100, Loss: 0.8988
[IL] Epoch 66/100, Loss: 0.8953
[IL] Epoch 67/100, Loss: 0.9012
[IL] Epoch 68/100, Loss: 0.8949
[IL] Epoch 69/100, Loss: 0.9022
[IL] Epoch 70/100, Loss: 0.8946
[IL] Epoch 71/100, Loss: 0.8989
[IL] Epoch 72/100, Loss: 0.8920
[IL] Epoch 73/100, Loss: 0.8970
[IL] Epoch 74/100, Loss: 0.8869
[IL] Epoch 75/100, Loss: 0.8966
[IL] Epoch 76/100, Loss: 0.8867
[IL] Epoch 77/100, Loss: 0.8915
[IL] Epoch 78/100, Loss: 0.8871
[IL] Epoch 79/100, Loss: 0.8967
[IL] Epoch 80/100, Loss: 0.8871
[IL] Epoch 81/100, Loss: 0.8962
[IL] Epoch 82/100, Loss: 0.8845
[IL] Epoch 83/100, Loss: 0.8844
[IL] Epoch 84/100, Loss: 0.8828
[IL] Epoch 85/100, Loss: 0.8846
[IL] Epoch 86/100, Loss: 0.8913
[IL] Epoch 87/100, Loss: 0.8794
[IL] Epoch 88/100, Loss: 0.8836
[IL] Epoch 89/100, Loss: 0.8789
[IL] Epoch 90/100, Loss: 0.8902
[IL] Epoch 91/100, Loss: 0.9007
[IL] Epoch 92/100, Loss: 0.8886
[IL] Epoch 93/100, Loss: 0.8842
[IL] Epoch 94/100, Loss: 0.8814
[IL] Epoch 95/100, Loss: 0.8766
[IL] Epoch 96/100, Loss: 0.8740
[IL] Epoch 97/100, Loss: 0.8754
[IL] Epoch 98/100, Loss: 0.8649
[IL] Epoch 99/100, Loss: 0.8671
test_mean_score: 0.0
[IL] Eval - Success Rate: 0.000
[Checkpoint] Saved to /nfs_global/S/yangrongzheng/RL100/3D-Diffusion-Policy/3D-Diffusion-Policy/checkpoints/offline_iter_4.ckpt

================================================================================
                         TRAINING COMPLETE!
================================================================================

[Checkpoint] Saved to /nfs_global/S/yangrongzheng/RL100/3D-Diffusion-Policy/3D-Diffusion-Policy/checkpoints/final.ckpt

[Evaluation] Running final evaluation...
test_mean_score: 0.0

================================================================================
                         FINAL RESULTS
================================================================================
mean_traj_rewards: 1696.9359
mean_success_rates: 0.0000
test_mean_score: 0.0000
SR_test_L3: 0.0000
SR_test_L5: 0.0000

[Training] Complete! Checkpoints saved to:
  /nfs_global/S/yangrongzheng/RL100/3D-Diffusion-Policy/3D-Diffusion-Policy/checkpoints
Found 8 GPUs for rendering. Using device 0.
Job end at 2026-03-07 02:30:39
