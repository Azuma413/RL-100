Job start at 2026-03-09 00:03:35
Job run at:
   Static hostname: localhost.localdomain
Transient hostname: r8l40-a02
         Icon name: computer-server
           Chassis: server
        Machine ID: d7f5671651c94cdf81ff3115fae1ffa3
           Boot ID: 8d5c4fd19b9a4ce69f18a77f036b455a
  Operating System: Rocky Linux 8.7 (Green Obsidian)
       CPE OS Name: cpe:/o:rocky:rocky:8:GA
            Kernel: Linux 4.18.0-425.10.1.el8_7.x86_64
      Architecture: x86-64
Filesystem                                        Size  Used Avail Use% Mounted on
/dev/mapper/rl-root                               376G   24G  352G   7% /
/dev/nvme1n1p1                                    3.5T   26G  3.5T   1% /tmp
/dev/nvme3n1p1                                    3.5T   25G  3.5T   1% /local
/dev/mapper/rl-var                                512G   15G  498G   3% /var
/dev/nvme4n1p1                                    3.5T   39G  3.5T   2% /local/nfscache
/dev/nvme0n1p2                                    2.0G  366M  1.7G  18% /boot
/dev/nvme0n1p1                                    599M  5.8M  594M   1% /boot/efi
ssd.nas00.future.cn:/rocky8_home                   16G   15G  1.9G  89% /home
ssd.nas00.future.cn:/rocky8_workspace             400G     0  400G   0% /workspace
ssd.nas00.future.cn:/rocky8_tools                 5.0T   99G  5.0T   2% /tools
ssd.nas00.future.cn:/centos7_home                  16G  4.2G   12G  26% /centos7/home
ssd.nas00.future.cn:/centos7_workspace            400G     0  400G   0% /centos7/workspace
ssd.nas00.future.cn:/centos7_tools                5.0T  235G  4.8T   5% /centos7/tools
ssd.nas00.future.cn:/eda-tools                    8.0T  6.3T  1.8T  79% /centos7/eda-tools
hdd.nas00.future.cn:/share_personal               500G     0  500G   0% /share/personal
zone05.nas01.future.cn:/NAS_HPC_collab_codemodel   40T   37T  3.7T  91% /share/collab/codemodel
ext-zone00.nas02.future.cn:/nfs_global            404T  384T   20T  96% /nfs_global
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
    /nfs_global    269G   5120G   7168G            348k   5000k  10000k        

############### /lustre
Disk quotas for usr yangrongzheng (uid 6215):
     Filesystem    used   quota   limit   grace   files   quota   limit   grace
        /lustre      0k      8T     10T       -       0  3000000 36000000       -
uid 6215 is using default block quota setting
uid 6215 is using default file quota setting
name, driver_version, power.limit [W]
NVIDIA L40, 570.124.06, 275.00 W
NVIDIA L40, 570.124.06, 275.00 W
NVIDIA L40, 570.124.06, 275.00 W
NVIDIA L40, 570.124.06, 275.00 W
NVIDIA L40, 570.124.06, 275.00 W
NVIDIA L40, 570.124.06, 275.00 W
NVIDIA L40, 570.124.06, 275.00 W
NVIDIA L40, 570.124.06, 275.00 W
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
    num_points: 1024
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
  ppo_inner_steps: 4
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
[2026-03-09 00:04:02,148][diffusion_policy_3d.model.diffusion.conditional_unet1d][INFO] - number of parameters: 2.550744e+08
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
[2026-03-09 00:04:03,928][diffusion_policy_3d.model.diffusion.conditional_unet1d][INFO] - number of parameters: 2.550744e+08
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
[TransitionModel] Epoch   20 | train=-17.38631 | val=0.02387 | no-improve=1/5
[TransitionModel] Epoch   32 | train=-22.53318 | val=0.02358 | no-improve=5/5
[TransitionModel] Training complete. Elites=[5, 1, 4, 2, 6], val_loss=0.02135

[RL100Trainer] Phase 2a: Training IQL Critics (Iteration 0)
[IQL] Epoch 0/50, V Loss: 1.0819, Q Loss: 72.6253
[IQL] Epoch 1/50, V Loss: 0.5742, Q Loss: 27.4199
[IQL] Epoch 2/50, V Loss: 0.2064, Q Loss: 20.7127
[IQL] Epoch 3/50, V Loss: 0.1168, Q Loss: 19.4542
[IQL] Epoch 4/50, V Loss: 0.0923, Q Loss: 19.5260
[IQL] Epoch 5/50, V Loss: 0.0873, Q Loss: 19.9809
[IQL] Epoch 6/50, V Loss: 0.1151, Q Loss: 20.3995
[IQL] Epoch 7/50, V Loss: 0.2063, Q Loss: 20.7105
[IQL] Epoch 8/50, V Loss: 0.3277, Q Loss: 20.6855
[IQL] Epoch 9/50, V Loss: 0.3569, Q Loss: 20.5205
[IQL] Epoch 10/50, V Loss: 0.4019, Q Loss: 20.0146
[IQL] Epoch 11/50, V Loss: 0.4270, Q Loss: 19.4643
[IQL] Epoch 12/50, V Loss: 0.4312, Q Loss: 18.6849
[IQL] Epoch 13/50, V Loss: 0.3970, Q Loss: 17.8640
[IQL] Epoch 14/50, V Loss: 0.3263, Q Loss: 17.0483
[IQL] Epoch 15/50, V Loss: 0.2235, Q Loss: 16.2140
[IQL] Epoch 16/50, V Loss: 0.1698, Q Loss: 15.3123
[IQL] Epoch 17/50, V Loss: 0.1409, Q Loss: 14.5349
[IQL] Epoch 18/50, V Loss: 0.1287, Q Loss: 13.7305
[IQL] Epoch 19/50, V Loss: 0.1254, Q Loss: 13.1062
[IQL] Epoch 20/50, V Loss: 0.1239, Q Loss: 12.5030
[IQL] Epoch 21/50, V Loss: 0.1377, Q Loss: 11.8868
[IQL] Epoch 22/50, V Loss: 0.1411, Q Loss: 11.4261
[IQL] Epoch 23/50, V Loss: 0.1776, Q Loss: 10.8834
[IQL] Epoch 24/50, V Loss: 0.1190, Q Loss: 10.3586
[IQL] Epoch 25/50, V Loss: 0.1336, Q Loss: 9.8212
[IQL] Epoch 26/50, V Loss: 0.2082, Q Loss: 9.4246
[IQL] Epoch 27/50, V Loss: 0.2103, Q Loss: 8.9197
[IQL] Epoch 28/50, V Loss: 0.2277, Q Loss: 8.4257
[IQL] Epoch 29/50, V Loss: 0.2332, Q Loss: 7.9848
[IQL] Epoch 30/50, V Loss: 0.2630, Q Loss: 7.5471
[IQL] Epoch 31/50, V Loss: 0.2718, Q Loss: 7.1460
[IQL] Epoch 32/50, V Loss: 0.3168, Q Loss: 6.8213
[IQL] Epoch 33/50, V Loss: 0.3141, Q Loss: 6.4974
[IQL] Epoch 34/50, V Loss: 0.2845, Q Loss: 6.2434
[IQL] Epoch 35/50, V Loss: 0.3234, Q Loss: 5.9840
[IQL] Epoch 36/50, V Loss: 0.3246, Q Loss: 5.8475
[IQL] Epoch 37/50, V Loss: 0.2886, Q Loss: 5.6794
[IQL] Epoch 38/50, V Loss: 0.2798, Q Loss: 5.5013
[IQL] Epoch 39/50, V Loss: 0.2638, Q Loss: 5.4123
[IQL] Epoch 40/50, V Loss: 0.1824, Q Loss: 5.2302
[IQL] Epoch 41/50, V Loss: 0.1338, Q Loss: 5.0686
[IQL] Epoch 42/50, V Loss: 0.1289, Q Loss: 5.0071
[IQL] Epoch 43/50, V Loss: 0.1168, Q Loss: 4.8984
[IQL] Epoch 44/50, V Loss: 0.0780, Q Loss: 4.7725
[IQL] Epoch 45/50, V Loss: 0.1026, Q Loss: 4.6264
[IQL] Epoch 46/50, V Loss: 0.0875, Q Loss: 4.5983
[IQL] Epoch 47/50, V Loss: 0.0970, Q Loss: 4.4860
[IQL] Epoch 48/50, V Loss: 0.1007, Q Loss: 4.3584
[IQL] Epoch 49/50, V Loss: 0.1052, Q Loss: 4.2646

[RL100Trainer] Phase 2b: Offline RL Optimization (Iteration 0)
[OPE] Behavior policy value J_old = 18.5345
[Offline RL] Epoch 0/100, PPO Loss: 0.0087, CD Loss: 1.4627
[Offline RL] Epoch 1/100, PPO Loss: -0.0113, CD Loss: 0.1293
[Offline RL] Epoch 2/100, PPO Loss: -0.0163, CD Loss: 0.3441
[Offline RL] Epoch 3/100, PPO Loss: -0.0199, CD Loss: 0.1473
[Offline RL] Epoch 4/100, PPO Loss: -0.0222, CD Loss: 0.2038
[Offline RL] Epoch 5/100, PPO Loss: -0.0163, CD Loss: 0.2473
[Offline RL] Epoch 6/100, PPO Loss: -0.0225, CD Loss: 0.2322
[Offline RL] Epoch 7/100, PPO Loss: -0.0192, CD Loss: 0.1892
[Offline RL] Epoch 8/100, PPO Loss: -0.0142, CD Loss: 0.1810
[Offline RL] Epoch 9/100, PPO Loss: -0.0098, CD Loss: 0.2061
[Offline RL] Epoch 10/100, PPO Loss: -0.0207, CD Loss: 0.2187
[Offline RL] Epoch 11/100, PPO Loss: -0.0182, CD Loss: 0.2195
[Offline RL] Epoch 12/100, PPO Loss: -0.0222, CD Loss: 0.2199
[Offline RL] Epoch 13/100, PPO Loss: -0.0212, CD Loss: 0.2180
[Offline RL] Epoch 14/100, PPO Loss: -0.0193, CD Loss: 0.2139
[Offline RL] Epoch 15/100, PPO Loss: -0.0262, CD Loss: 0.2205
[Offline RL] Epoch 16/100, PPO Loss: -0.0207, CD Loss: 0.1958
[Offline RL] Epoch 17/100, PPO Loss: -0.0242, CD Loss: 0.1863
[Offline RL] Epoch 18/100, PPO Loss: -0.0222, CD Loss: 0.1890
[Offline RL] Epoch 19/100, PPO Loss: -0.0281, CD Loss: 0.2004
[Offline RL] Epoch 20/100, PPO Loss: -0.0280, CD Loss: 0.2087
[Offline RL] Epoch 21/100, PPO Loss: -0.0290, CD Loss: 0.2077
[Offline RL] Epoch 22/100, PPO Loss: -0.0271, CD Loss: 0.2044
[Offline RL] Epoch 23/100, PPO Loss: -0.0300, CD Loss: 0.2038
[Offline RL] Epoch 24/100, PPO Loss: -0.0305, CD Loss: 0.2053
[Offline RL] Epoch 25/100, PPO Loss: -0.0338, CD Loss: 0.2061
[Offline RL] Epoch 26/100, PPO Loss: -0.0297, CD Loss: 0.1981
[Offline RL] Epoch 27/100, PPO Loss: -0.0343, CD Loss: 0.1987
[Offline RL] Epoch 28/100, PPO Loss: -0.0331, CD Loss: 0.2013
[Offline RL] Epoch 29/100, PPO Loss: -0.0339, CD Loss: 0.1932
[Offline RL] Epoch 30/100, PPO Loss: -0.0245, CD Loss: 0.1942
[Offline RL] Epoch 31/100, PPO Loss: -0.0281, CD Loss: 0.1955
[Offline RL] Epoch 32/100, PPO Loss: -0.0324, CD Loss: 0.1941
[Offline RL] Epoch 33/100, PPO Loss: -0.0307, CD Loss: 0.1957
[Offline RL] Epoch 34/100, PPO Loss: -0.0340, CD Loss: 0.1896
[Offline RL] Epoch 35/100, PPO Loss: -0.0393, CD Loss: 0.1909
[Offline RL] Epoch 36/100, PPO Loss: -0.0392, CD Loss: 0.1872
[Offline RL] Epoch 37/100, PPO Loss: -0.0397, CD Loss: 0.1873
[Offline RL] Epoch 38/100, PPO Loss: -0.0398, CD Loss: 0.1785
[Offline RL] Epoch 39/100, PPO Loss: -0.0360, CD Loss: 0.1752
[Offline RL] Epoch 40/100, PPO Loss: -0.0422, CD Loss: 0.1814
[Offline RL] Epoch 41/100, PPO Loss: -0.0391, CD Loss: 0.1807
[Offline RL] Epoch 42/100, PPO Loss: -0.0412, CD Loss: 0.1821
[Offline RL] Epoch 43/100, PPO Loss: -0.0412, CD Loss: 0.1923
[Offline RL] Epoch 44/100, PPO Loss: -0.0452, CD Loss: 0.1889
[Offline RL] Epoch 45/100, PPO Loss: -0.0386, CD Loss: 0.1839
[Offline RL] Epoch 46/100, PPO Loss: -0.0434, CD Loss: 0.1832
[Offline RL] Epoch 47/100, PPO Loss: -0.0455, CD Loss: 0.1830
[Offline RL] Epoch 48/100, PPO Loss: -0.0420, CD Loss: 0.1816
[Offline RL] Epoch 49/100, PPO Loss: -0.0424, CD Loss: 0.1887
[Offline RL] Epoch 50/100, PPO Loss: -0.0468, CD Loss: 0.1952
[Offline RL] Epoch 51/100, PPO Loss: -0.0436, CD Loss: 0.1860
[Offline RL] Epoch 52/100, PPO Loss: -0.0423, CD Loss: 0.1875
[Offline RL] Epoch 53/100, PPO Loss: -0.0463, CD Loss: 0.1892
[Offline RL] Epoch 54/100, PPO Loss: -0.0437, CD Loss: 0.1896
[Offline RL] Epoch 55/100, PPO Loss: -0.0436, CD Loss: 0.1906
[Offline RL] Epoch 56/100, PPO Loss: -0.0437, CD Loss: 0.1883
[Offline RL] Epoch 57/100, PPO Loss: -0.0426, CD Loss: 0.1900
[Offline RL] Epoch 58/100, PPO Loss: -0.0414, CD Loss: 0.2000
[Offline RL] Epoch 59/100, PPO Loss: -0.0397, CD Loss: 0.2040
[Offline RL] Epoch 60/100, PPO Loss: -0.0428, CD Loss: 0.2032
[Offline RL] Epoch 61/100, PPO Loss: -0.0460, CD Loss: 0.2045
[Offline RL] Epoch 62/100, PPO Loss: -0.0447, CD Loss: 0.1986
[Offline RL] Epoch 63/100, PPO Loss: -0.0450, CD Loss: 0.2057
[Offline RL] Epoch 64/100, PPO Loss: -0.0417, CD Loss: 0.1996
[Offline RL] Epoch 65/100, PPO Loss: -0.0417, CD Loss: 0.1968
[Offline RL] Epoch 66/100, PPO Loss: -0.0399, CD Loss: 0.1927
[Offline RL] Epoch 67/100, PPO Loss: -0.0455, CD Loss: 0.1954
[Offline RL] Epoch 68/100, PPO Loss: -0.0393, CD Loss: 0.2108
[Offline RL] Epoch 69/100, PPO Loss: -0.0423, CD Loss: 0.2099
[Offline RL] Epoch 70/100, PPO Loss: -0.0408, CD Loss: 0.2182
[Offline RL] Epoch 71/100, PPO Loss: -0.0393, CD Loss: 0.2214
[Offline RL] Epoch 72/100, PPO Loss: -0.0398, CD Loss: 0.2208
[Offline RL] Epoch 73/100, PPO Loss: -0.0469, CD Loss: 0.2187
[Offline RL] Epoch 74/100, PPO Loss: -0.0417, CD Loss: 0.2152
[Offline RL] Epoch 75/100, PPO Loss: -0.0408, CD Loss: 0.2194
[Offline RL] Epoch 76/100, PPO Loss: -0.0427, CD Loss: 0.2332
[Offline RL] Epoch 77/100, PPO Loss: -0.0420, CD Loss: 0.2355
[Offline RL] Epoch 78/100, PPO Loss: -0.0391, CD Loss: 0.2309
[Offline RL] Epoch 79/100, PPO Loss: -0.0395, CD Loss: 0.2295
[Offline RL] Epoch 80/100, PPO Loss: -0.0425, CD Loss: 0.2287
[Offline RL] Epoch 81/100, PPO Loss: -0.0389, CD Loss: 0.2390
[Offline RL] Epoch 82/100, PPO Loss: -0.0370, CD Loss: 0.2315
[Offline RL] Epoch 83/100, PPO Loss: -0.0381, CD Loss: 0.2201
[Offline RL] Epoch 84/100, PPO Loss: -0.0375, CD Loss: 0.2251
[Offline RL] Epoch 85/100, PPO Loss: -0.0309, CD Loss: 0.2258
[Offline RL] Epoch 86/100, PPO Loss: -0.0369, CD Loss: 0.2133
[Offline RL] Epoch 87/100, PPO Loss: -0.0351, CD Loss: 0.2149
[Offline RL] Epoch 88/100, PPO Loss: -0.0372, CD Loss: 0.2120
[Offline RL] Epoch 89/100, PPO Loss: -0.0400, CD Loss: 0.2135
[Offline RL] Epoch 90/100, PPO Loss: -0.0370, CD Loss: 0.2053
[Offline RL] Epoch 91/100, PPO Loss: -0.0409, CD Loss: 0.2059
[Offline RL] Epoch 92/100, PPO Loss: -0.0391, CD Loss: 0.1953
[Offline RL] Epoch 93/100, PPO Loss: -0.0398, CD Loss: 0.2012
[Offline RL] Epoch 94/100, PPO Loss: -0.0381, CD Loss: 0.1963
[Offline RL] Epoch 95/100, PPO Loss: -0.0415, CD Loss: 0.2030
[Offline RL] Epoch 96/100, PPO Loss: -0.0454, CD Loss: 0.2077
[Offline RL] Epoch 97/100, PPO Loss: -0.0395, CD Loss: 0.2101
[Offline RL] Epoch 98/100, PPO Loss: -0.0407, CD Loss: 0.2045
[Offline RL] Epoch 99/100, PPO Loss: -0.0415, CD Loss: 0.2050
[OPE] Policy REJECTED: J_new=18.3836 ≤ J_old=18.5345 + δ=0.9267. Rolling back to behavior policy.

[RL100Trainer] Phase 2c: Collecting New Data (Iteration 0)
[Collect] 50 episodes, success=0.580, steps=1250
[Data Collection] Success Rate: 0.580, Reward: 10244.07, Episodes: 50, Steps: 1250
[Dataset] Merged 50 episodes (1250 steps) → total 3250 steps, 60 episodes

[RL100Trainer] Retraining IL on merged dataset...

============================================================
[RL100Trainer] Phase 1: Imitation Learning
============================================================

[IL] Epoch 0/100, Loss: 0.2533
[IL] Epoch 1/100, Loss: 0.1494
[IL] Epoch 2/100, Loss: 0.1103
[IL] Epoch 3/100, Loss: 0.0938
[IL] Epoch 4/100, Loss: 0.0866
[IL] Epoch 5/100, Loss: 0.0818
[IL] Epoch 6/100, Loss: 0.0709
[IL] Epoch 7/100, Loss: 0.0640
[IL] Epoch 8/100, Loss: 0.0666
[IL] Epoch 9/100, Loss: 0.0626
[IL] Epoch 10/100, Loss: 0.0596
[IL] Epoch 11/100, Loss: 0.0583
[IL] Epoch 12/100, Loss: 0.0549
[IL] Epoch 13/100, Loss: 0.0559
[IL] Epoch 14/100, Loss: 0.0541
[IL] Epoch 15/100, Loss: 0.0603
[IL] Epoch 16/100, Loss: 0.0547
[IL] Epoch 17/100, Loss: 0.0549
[IL] Epoch 18/100, Loss: 0.0532
[IL] Epoch 19/100, Loss: 0.0571
[IL] Epoch 20/100, Loss: 0.0561
[IL] Epoch 21/100, Loss: 0.0528
[IL] Epoch 22/100, Loss: 0.0510
[IL] Epoch 23/100, Loss: 0.0483
[IL] Epoch 24/100, Loss: 0.0489
[IL] Epoch 25/100, Loss: 0.0520
[IL] Epoch 26/100, Loss: 0.0511
[IL] Epoch 27/100, Loss: 0.0505
[IL] Epoch 28/100, Loss: 0.0476
[IL] Epoch 29/100, Loss: 0.0445
[IL] Epoch 30/100, Loss: 0.0525
[IL] Epoch 31/100, Loss: 0.0467
[IL] Epoch 32/100, Loss: 0.0505
[IL] Epoch 33/100, Loss: 0.0484
[IL] Epoch 34/100, Loss: 0.0464
[IL] Epoch 35/100, Loss: 0.0432
[IL] Epoch 36/100, Loss: 0.0513
[IL] Epoch 37/100, Loss: 0.0463
[IL] Epoch 38/100, Loss: 0.0415
[IL] Epoch 39/100, Loss: 0.0422
[IL] Epoch 40/100, Loss: 0.0433
[IL] Epoch 41/100, Loss: 0.0441
[IL] Epoch 42/100, Loss: 0.0424
[IL] Epoch 43/100, Loss: 0.0400
[IL] Epoch 44/100, Loss: 0.0422
[IL] Epoch 45/100, Loss: 0.0401
[IL] Epoch 46/100, Loss: 0.0410
[IL] Epoch 47/100, Loss: 0.0419
[IL] Epoch 48/100, Loss: 0.0471
[IL] Epoch 49/100, Loss: 0.0413
[IL] Epoch 50/100, Loss: 0.0379
[IL] Epoch 51/100, Loss: 0.0412
[IL] Epoch 52/100, Loss: 0.0404
[IL] Epoch 53/100, Loss: 0.0393
[IL] Epoch 54/100, Loss: 0.0500
[IL] Epoch 55/100, Loss: 0.0527
[IL] Epoch 56/100, Loss: 0.0443
[IL] Epoch 57/100, Loss: 0.0391
[IL] Epoch 58/100, Loss: 0.0484
[IL] Epoch 59/100, Loss: 0.0457
[IL] Epoch 60/100, Loss: 0.0432
[IL] Epoch 61/100, Loss: 0.0400
[IL] Epoch 62/100, Loss: 0.0425
[IL] Epoch 63/100, Loss: 0.0417
[IL] Epoch 64/100, Loss: 0.0407
[IL] Epoch 65/100, Loss: 0.0394
[IL] Epoch 66/100, Loss: 0.0389
[IL] Epoch 67/100, Loss: 0.0346
[IL] Epoch 68/100, Loss: 0.0364
[IL] Epoch 69/100, Loss: 0.0410
[IL] Epoch 70/100, Loss: 0.0398
[IL] Epoch 71/100, Loss: 0.0395
[IL] Epoch 72/100, Loss: 0.0454
[IL] Epoch 73/100, Loss: 0.0417
[IL] Epoch 74/100, Loss: 0.0380
[IL] Epoch 75/100, Loss: 0.0419
[IL] Epoch 76/100, Loss: 0.0436
[IL] Epoch 77/100, Loss: 0.0444
[IL] Epoch 78/100, Loss: 0.0413
[IL] Epoch 79/100, Loss: 0.0389
[IL] Epoch 80/100, Loss: 0.0394
[IL] Epoch 81/100, Loss: 0.0423
[IL] Epoch 82/100, Loss: 0.0428
[IL] Epoch 83/100, Loss: 0.0380
[IL] Epoch 84/100, Loss: 0.0384
[IL] Epoch 85/100, Loss: 0.0350
[IL] Epoch 86/100, Loss: 0.0353
[IL] Epoch 87/100, Loss: 0.0372
[IL] Epoch 88/100, Loss: 0.0328
[IL] Epoch 89/100, Loss: 0.0397
[IL] Epoch 90/100, Loss: 0.0369
[IL] Epoch 91/100, Loss: 0.0361
[IL] Epoch 92/100, Loss: 0.0332
[IL] Epoch 93/100, Loss: 0.0344
[IL] Epoch 94/100, Loss: 0.0329
[IL] Epoch 95/100, Loss: 0.0348
[IL] Epoch 96/100, Loss: 0.0349
[IL] Epoch 97/100, Loss: 0.0400
[IL] Epoch 98/100, Loss: 0.0398
[IL] Epoch 99/100, Loss: 0.0331
test_mean_score: 0.4
[IL] Eval - Success Rate: 0.400
[Checkpoint] Saved to /nfs_global/S/yangrongzheng/RL100/3D-Diffusion-Policy/3D-Diffusion-Policy/checkpoints/offline_iter_0.ckpt

================================================================================
               OFFLINE RL ITERATION 2/5
================================================================================


[RL100Trainer] Line 6 — Training Transition Model T_θ (Iteration 1)

[TransitionModel] Encoding dataset for transition model training...
[TransitionModel] Dataset: 2830 samples, input_dim=260, target_dim=257
[TransitionModel] Epoch    0 | train=527.10595 | val=134.93366 | no-improve=0/5
[TransitionModel] Epoch   20 | train=285.17086 | val=85.20940 | no-improve=0/5
[TransitionModel] Epoch   40 | train=68.59199 | val=30.56438 | no-improve=0/5
[TransitionModel] Epoch   60 | train=14.71509 | val=25.68891 | no-improve=0/5
[TransitionModel] Epoch   80 | train=-3.62421 | val=24.66347 | no-improve=0/5
[TransitionModel] Epoch   98 | train=-11.00864 | val=23.56863 | no-improve=5/5
[TransitionModel] Training complete. Elites=[3, 0, 1, 2, 4], val_loss=22.45370

[RL100Trainer] Phase 2a: Training IQL Critics (Iteration 1)
[IQL] Epoch 0/50, V Loss: 0.9774, Q Loss: 91596.8883
[IQL] Epoch 1/50, V Loss: 2.0513, Q Loss: 65055.5384
[IQL] Epoch 2/50, V Loss: 2.0152, Q Loss: 66185.5667
[IQL] Epoch 3/50, V Loss: 1.5816, Q Loss: 68979.3073
[IQL] Epoch 4/50, V Loss: 1.4940, Q Loss: 66741.1794
[IQL] Epoch 5/50, V Loss: 1.4942, Q Loss: 62942.1042
[IQL] Epoch 6/50, V Loss: 1.7559, Q Loss: 75545.8145
[IQL] Epoch 7/50, V Loss: 5.1625, Q Loss: 62239.7116
[IQL] Epoch 8/50, V Loss: 6.2285, Q Loss: 65085.6953
[IQL] Epoch 9/50, V Loss: 5.6262, Q Loss: 65233.1048
[IQL] Epoch 10/50, V Loss: 7.9432, Q Loss: 66984.8763
[IQL] Epoch 11/50, V Loss: 5.9373, Q Loss: 66719.5661
[IQL] Epoch 12/50, V Loss: 4.4085, Q Loss: 61259.7384
[IQL] Epoch 13/50, V Loss: 3.7102, Q Loss: 72022.2021
[IQL] Epoch 14/50, V Loss: 2.7229, Q Loss: 63699.4359
[IQL] Epoch 15/50, V Loss: 4.1760, Q Loss: 64624.3542
[IQL] Epoch 16/50, V Loss: 6.2812, Q Loss: 69432.8076
[IQL] Epoch 17/50, V Loss: 7.3566, Q Loss: 71567.2520
[IQL] Epoch 18/50, V Loss: 12.5961, Q Loss: 67347.3040
[IQL] Epoch 19/50, V Loss: 9.2526, Q Loss: 63366.4111
[IQL] Epoch 20/50, V Loss: 10.0267, Q Loss: 60201.9464
[IQL] Epoch 21/50, V Loss: 7.4754, Q Loss: 67799.7331
[IQL] Epoch 22/50, V Loss: 7.1978, Q Loss: 62583.5085
[IQL] Epoch 23/50, V Loss: 6.3616, Q Loss: 64730.3040
[IQL] Epoch 24/50, V Loss: 7.2682, Q Loss: 63926.7630
[IQL] Epoch 25/50, V Loss: 6.9425, Q Loss: 71263.4417
[IQL] Epoch 26/50, V Loss: 8.6834, Q Loss: 61146.9505
[IQL] Epoch 27/50, V Loss: 9.1235, Q Loss: 59794.8543
[IQL] Epoch 28/50, V Loss: 5.0279, Q Loss: 60677.1816
[IQL] Epoch 29/50, V Loss: 5.1545, Q Loss: 63452.7992
[IQL] Epoch 30/50, V Loss: 5.5566, Q Loss: 60721.1015
[IQL] Epoch 31/50, V Loss: 5.4138, Q Loss: 66479.7891
[IQL] Epoch 32/50, V Loss: 9.2650, Q Loss: 75503.4622
[IQL] Epoch 33/50, V Loss: 7.6555, Q Loss: 60078.8947
[IQL] Epoch 34/50, V Loss: 9.7351, Q Loss: 62260.8851
[IQL] Epoch 35/50, V Loss: 9.1145, Q Loss: 60130.1217
[IQL] Epoch 36/50, V Loss: 8.8396, Q Loss: 65081.7347
[IQL] Epoch 37/50, V Loss: 8.7154, Q Loss: 63254.7132
[IQL] Epoch 38/50, V Loss: 10.8305, Q Loss: 62420.6074
[IQL] Epoch 39/50, V Loss: 9.1152, Q Loss: 67099.3939
[IQL] Epoch 40/50, V Loss: 9.0630, Q Loss: 61614.5449
[IQL] Epoch 41/50, V Loss: 14.4339, Q Loss: 60029.1790
[IQL] Epoch 42/50, V Loss: 10.0412, Q Loss: 62687.9736
[IQL] Epoch 43/50, V Loss: 14.5134, Q Loss: 63621.9460
[IQL] Epoch 44/50, V Loss: 12.3498, Q Loss: 74192.1787
[IQL] Epoch 45/50, V Loss: 11.9947, Q Loss: 71557.5710
[IQL] Epoch 46/50, V Loss: 18.5494, Q Loss: 66484.2090
[IQL] Epoch 47/50, V Loss: 26.6463, Q Loss: 59607.4502
[IQL] Epoch 48/50, V Loss: 11.0325, Q Loss: 58900.2764
[IQL] Epoch 49/50, V Loss: 7.3724, Q Loss: 59344.6314

[RL100Trainer] Phase 2b: Offline RL Optimization (Iteration 1)
[OPE] Behavior policy value J_old = 84.6235
[Offline RL] Epoch 0/100, PPO Loss: -0.0310, CD Loss: 0.2104
[Offline RL] Epoch 1/100, PPO Loss: -0.0358, CD Loss: 0.1659
[Offline RL] Epoch 2/100, PPO Loss: -0.0288, CD Loss: 0.1389
[Offline RL] Epoch 3/100, PPO Loss: -0.0281, CD Loss: 0.0948
[Offline RL] Epoch 4/100, PPO Loss: -0.0261, CD Loss: 0.1129
[Offline RL] Epoch 5/100, PPO Loss: -0.0316, CD Loss: 0.1151
[Offline RL] Epoch 6/100, PPO Loss: -0.0350, CD Loss: 0.1326
[Offline RL] Epoch 7/100, PPO Loss: -0.0315, CD Loss: 0.1417
[Offline RL] Epoch 8/100, PPO Loss: -0.0361, CD Loss: 0.1620
[Offline RL] Epoch 9/100, PPO Loss: -0.0356, CD Loss: 0.1550
[Offline RL] Epoch 10/100, PPO Loss: -0.0323, CD Loss: 0.1450
[Offline RL] Epoch 11/100, PPO Loss: -0.0377, CD Loss: 0.1522
[Offline RL] Epoch 12/100, PPO Loss: -0.0362, CD Loss: 0.1472
[Offline RL] Epoch 13/100, PPO Loss: -0.0415, CD Loss: 0.1461
[Offline RL] Epoch 14/100, PPO Loss: -0.0390, CD Loss: 0.1475
[Offline RL] Epoch 15/100, PPO Loss: -0.0429, CD Loss: 0.1455
[Offline RL] Epoch 16/100, PPO Loss: -0.0385, CD Loss: 0.1251
[Offline RL] Epoch 17/100, PPO Loss: -0.0409, CD Loss: 0.1353
[Offline RL] Epoch 18/100, PPO Loss: -0.0432, CD Loss: 0.1399
[Offline RL] Epoch 19/100, PPO Loss: -0.0461, CD Loss: 0.1366
[Offline RL] Epoch 20/100, PPO Loss: -0.0403, CD Loss: 0.1416
[Offline RL] Epoch 21/100, PPO Loss: -0.0421, CD Loss: 0.1512
[Offline RL] Epoch 22/100, PPO Loss: -0.0414, CD Loss: 0.1479
[Offline RL] Epoch 23/100, PPO Loss: -0.0425, CD Loss: 0.1475
[Offline RL] Epoch 24/100, PPO Loss: -0.0449, CD Loss: 0.1515
[Offline RL] Epoch 25/100, PPO Loss: -0.0432, CD Loss: 0.1637
[Offline RL] Epoch 26/100, PPO Loss: -0.0430, CD Loss: 0.1594
[Offline RL] Epoch 27/100, PPO Loss: -0.0449, CD Loss: 0.1577
[Offline RL] Epoch 28/100, PPO Loss: -0.0433, CD Loss: 0.1584
[Offline RL] Epoch 29/100, PPO Loss: -0.0480, CD Loss: 0.1442
[Offline RL] Epoch 30/100, PPO Loss: -0.0438, CD Loss: 0.1367
[Offline RL] Epoch 31/100, PPO Loss: -0.0470, CD Loss: 0.1263
[Offline RL] Epoch 32/100, PPO Loss: -0.0467, CD Loss: 0.1290
[Offline RL] Epoch 33/100, PPO Loss: -0.0459, CD Loss: 0.1308
[Offline RL] Epoch 34/100, PPO Loss: -0.0471, CD Loss: 0.1277
[Offline RL] Epoch 35/100, PPO Loss: -0.0423, CD Loss: 0.1278
[Offline RL] Epoch 36/100, PPO Loss: -0.0437, CD Loss: 0.1223
[Offline RL] Epoch 37/100, PPO Loss: -0.0436, CD Loss: 0.1211
[Offline RL] Epoch 38/100, PPO Loss: -0.0428, CD Loss: 0.1236
[Offline RL] Epoch 39/100, PPO Loss: -0.0408, CD Loss: 0.1231
[Offline RL] Epoch 40/100, PPO Loss: -0.0467, CD Loss: 0.1285
[Offline RL] Epoch 41/100, PPO Loss: -0.0491, CD Loss: 0.1295
[Offline RL] Epoch 42/100, PPO Loss: -0.0495, CD Loss: 0.1289
[Offline RL] Epoch 43/100, PPO Loss: -0.0475, CD Loss: 0.1301
[Offline RL] Epoch 44/100, PPO Loss: -0.0487, CD Loss: 0.1235
[Offline RL] Epoch 45/100, PPO Loss: -0.0442, CD Loss: 0.1196
[Offline RL] Epoch 46/100, PPO Loss: -0.0441, CD Loss: 0.1152
[Offline RL] Epoch 47/100, PPO Loss: -0.0452, CD Loss: 0.1202
[Offline RL] Epoch 48/100, PPO Loss: -0.0412, CD Loss: 0.1215
[Offline RL] Epoch 49/100, PPO Loss: -0.0433, CD Loss: 0.1276
[Offline RL] Epoch 50/100, PPO Loss: -0.0437, CD Loss: 0.1202
[Offline RL] Epoch 51/100, PPO Loss: -0.0435, CD Loss: 0.1200
[Offline RL] Epoch 52/100, PPO Loss: -0.0451, CD Loss: 0.1162
[Offline RL] Epoch 53/100, PPO Loss: -0.0463, CD Loss: 0.1224
[Offline RL] Epoch 54/100, PPO Loss: -0.0442, CD Loss: 0.1256
[Offline RL] Epoch 55/100, PPO Loss: -0.0449, CD Loss: 0.1273
[Offline RL] Epoch 56/100, PPO Loss: -0.0503, CD Loss: 0.1300
[Offline RL] Epoch 57/100, PPO Loss: -0.0479, CD Loss: 0.1304
[Offline RL] Epoch 58/100, PPO Loss: -0.0456, CD Loss: 0.1374
[Offline RL] Epoch 59/100, PPO Loss: -0.0478, CD Loss: 0.1315
[Offline RL] Epoch 60/100, PPO Loss: -0.0417, CD Loss: 0.1324
[Offline RL] Epoch 61/100, PPO Loss: -0.0449, CD Loss: 0.1392
[Offline RL] Epoch 62/100, PPO Loss: -0.0385, CD Loss: 0.1420
[Offline RL] Epoch 63/100, PPO Loss: -0.0432, CD Loss: 0.1366
[Offline RL] Epoch 64/100, PPO Loss: -0.0421, CD Loss: 0.1345
[Offline RL] Epoch 65/100, PPO Loss: -0.0427, CD Loss: 0.1341
[Offline RL] Epoch 66/100, PPO Loss: -0.0437, CD Loss: 0.1377
[Offline RL] Epoch 67/100, PPO Loss: -0.0410, CD Loss: 0.1454
[Offline RL] Epoch 68/100, PPO Loss: -0.0414, CD Loss: 0.1447
[Offline RL] Epoch 69/100, PPO Loss: -0.0408, CD Loss: 0.1387
[Offline RL] Epoch 70/100, PPO Loss: -0.0387, CD Loss: 0.1371
[Offline RL] Epoch 71/100, PPO Loss: -0.0398, CD Loss: 0.1420
[Offline RL] Epoch 72/100, PPO Loss: -0.0459, CD Loss: 0.1319
[Offline RL] Epoch 73/100, PPO Loss: -0.0412, CD Loss: 0.1260
[Offline RL] Epoch 74/100, PPO Loss: -0.0420, CD Loss: 0.1304
[Offline RL] Epoch 75/100, PPO Loss: -0.0392, CD Loss: 0.1247
[Offline RL] Epoch 76/100, PPO Loss: -0.0415, CD Loss: 0.1289
[Offline RL] Epoch 77/100, PPO Loss: -0.0411, CD Loss: 0.1285
[Offline RL] Epoch 78/100, PPO Loss: -0.0391, CD Loss: 0.1276
[Offline RL] Epoch 79/100, PPO Loss: -0.0410, CD Loss: 0.1315
[Offline RL] Epoch 80/100, PPO Loss: -0.0405, CD Loss: 0.1346
[Offline RL] Epoch 81/100, PPO Loss: -0.0438, CD Loss: 0.1328
[Offline RL] Epoch 82/100, PPO Loss: -0.0432, CD Loss: 0.1427
[Offline RL] Epoch 83/100, PPO Loss: -0.0437, CD Loss: 0.1462
[Offline RL] Epoch 84/100, PPO Loss: -0.0391, CD Loss: 0.1519
[Offline RL] Epoch 85/100, PPO Loss: -0.0395, CD Loss: 0.1540
[Offline RL] Epoch 86/100, PPO Loss: -0.0402, CD Loss: 0.1587
[Offline RL] Epoch 87/100, PPO Loss: -0.0392, CD Loss: 0.1647
[Offline RL] Epoch 88/100, PPO Loss: -0.0405, CD Loss: 0.1626
[Offline RL] Epoch 89/100, PPO Loss: -0.0394, CD Loss: 0.1604
[Offline RL] Epoch 90/100, PPO Loss: -0.0370, CD Loss: 0.1527
[Offline RL] Epoch 91/100, PPO Loss: -0.0364, CD Loss: 0.1492
[Offline RL] Epoch 92/100, PPO Loss: -0.0364, CD Loss: 0.1413
[Offline RL] Epoch 93/100, PPO Loss: -0.0415, CD Loss: 0.1441
[Offline RL] Epoch 94/100, PPO Loss: -0.0366, CD Loss: 0.1393
[Offline RL] Epoch 95/100, PPO Loss: -0.0370, CD Loss: 0.1409
[Offline RL] Epoch 96/100, PPO Loss: -0.0405, CD Loss: 0.1459
[Offline RL] Epoch 97/100, PPO Loss: -0.0467, CD Loss: 0.1381
[Offline RL] Epoch 98/100, PPO Loss: -0.0428, CD Loss: 0.1341
[Offline RL] Epoch 99/100, PPO Loss: -0.0447, CD Loss: 0.1301
[OPE] Policy REJECTED: J_new=84.2773 ≤ J_old=84.6235 + δ=4.2312. Rolling back to behavior policy.

[RL100Trainer] Phase 2c: Collecting New Data (Iteration 1)
[Collect] 50 episodes, success=0.460, steps=1250
[Data Collection] Success Rate: 0.460, Reward: 10028.46, Episodes: 50, Steps: 1250
[Dataset] Merged 50 episodes (1250 steps) → total 4500 steps, 110 episodes

[RL100Trainer] Retraining IL on merged dataset...

============================================================
[RL100Trainer] Phase 1: Imitation Learning
============================================================

[IL] Epoch 0/100, Loss: 0.0535
[IL] Epoch 1/100, Loss: 0.0486
[IL] Epoch 2/100, Loss: 0.0507
[IL] Epoch 3/100, Loss: 0.0536
[IL] Epoch 4/100, Loss: 0.0502
[IL] Epoch 5/100, Loss: 0.0516
[IL] Epoch 6/100, Loss: 0.0457
[IL] Epoch 7/100, Loss: 0.0465
[IL] Epoch 8/100, Loss: 0.0447
[IL] Epoch 9/100, Loss: 0.0478
[IL] Epoch 10/100, Loss: 0.0471
[IL] Epoch 11/100, Loss: 0.0476
[IL] Epoch 12/100, Loss: 0.0444
[IL] Epoch 13/100, Loss: 0.0460
[IL] Epoch 14/100, Loss: 0.0439
[IL] Epoch 15/100, Loss: 0.0462
[IL] Epoch 16/100, Loss: 0.0466
[IL] Epoch 17/100, Loss: 0.0469
[IL] Epoch 18/100, Loss: 0.0455
[IL] Epoch 19/100, Loss: 0.0451
[IL] Epoch 20/100, Loss: 0.0486
[IL] Epoch 21/100, Loss: 0.0440
[IL] Epoch 22/100, Loss: 0.0428
[IL] Epoch 23/100, Loss: 0.0454
[IL] Epoch 24/100, Loss: 0.0435
[IL] Epoch 25/100, Loss: 0.0418
[IL] Epoch 26/100, Loss: 0.0435
[IL] Epoch 27/100, Loss: 0.0435
[IL] Epoch 28/100, Loss: 0.0423
[IL] Epoch 29/100, Loss: 0.0464
[IL] Epoch 30/100, Loss: 0.0454
[IL] Epoch 31/100, Loss: 0.0422
[IL] Epoch 32/100, Loss: 0.0422
[IL] Epoch 33/100, Loss: 0.0420
[IL] Epoch 34/100, Loss: 0.0400
[IL] Epoch 35/100, Loss: 0.0439
[IL] Epoch 36/100, Loss: 0.0398
[IL] Epoch 37/100, Loss: 0.0445
[IL] Epoch 38/100, Loss: 0.0413
[IL] Epoch 39/100, Loss: 0.0419
[IL] Epoch 40/100, Loss: 0.0430
[IL] Epoch 41/100, Loss: 0.0395
[IL] Epoch 42/100, Loss: 0.0432
[IL] Epoch 43/100, Loss: 0.0417
[IL] Epoch 44/100, Loss: 0.0422
[IL] Epoch 45/100, Loss: 0.0395
[IL] Epoch 46/100, Loss: 0.0381
[IL] Epoch 47/100, Loss: 0.0396
[IL] Epoch 48/100, Loss: 0.0389
[IL] Epoch 49/100, Loss: 0.0391
[IL] Epoch 50/100, Loss: 0.0431
[IL] Epoch 51/100, Loss: 0.0402
[IL] Epoch 52/100, Loss: 0.0413
[IL] Epoch 53/100, Loss: 0.0399
[IL] Epoch 54/100, Loss: 0.0409
[IL] Epoch 55/100, Loss: 0.0366
[IL] Epoch 56/100, Loss: 0.0401
[IL] Epoch 57/100, Loss: 0.0394
[IL] Epoch 58/100, Loss: 0.0392
[IL] Epoch 59/100, Loss: 0.0392
[IL] Epoch 60/100, Loss: 0.0385
[IL] Epoch 61/100, Loss: 0.0381
[IL] Epoch 62/100, Loss: 0.0387
[IL] Epoch 63/100, Loss: 0.0378
[IL] Epoch 64/100, Loss: 0.0391
[IL] Epoch 65/100, Loss: 0.0413
[IL] Epoch 66/100, Loss: 0.0386
[IL] Epoch 67/100, Loss: 0.0393
[IL] Epoch 68/100, Loss: 0.0378
[IL] Epoch 69/100, Loss: 0.0360
[IL] Epoch 70/100, Loss: 0.0377
[IL] Epoch 71/100, Loss: 0.0365
[IL] Epoch 72/100, Loss: 0.0366
[IL] Epoch 73/100, Loss: 0.0378
[IL] Epoch 74/100, Loss: 0.0368
[IL] Epoch 75/100, Loss: 0.0369
[IL] Epoch 76/100, Loss: 0.0386
[IL] Epoch 77/100, Loss: 0.0376
[IL] Epoch 78/100, Loss: 0.0373
[IL] Epoch 79/100, Loss: 0.0382
[IL] Epoch 80/100, Loss: 0.0365
[IL] Epoch 81/100, Loss: 0.0379
[IL] Epoch 82/100, Loss: 0.0381
[IL] Epoch 83/100, Loss: 0.0403
[IL] Epoch 84/100, Loss: 0.0372
[IL] Epoch 85/100, Loss: 0.0360
[IL] Epoch 86/100, Loss: 0.0340
[IL] Epoch 87/100, Loss: 0.0324
[IL] Epoch 88/100, Loss: 0.0351
[IL] Epoch 89/100, Loss: 0.0353
[IL] Epoch 90/100, Loss: 0.0357
[IL] Epoch 91/100, Loss: 0.0360
[IL] Epoch 92/100, Loss: 0.0364
[IL] Epoch 93/100, Loss: 0.0359
[IL] Epoch 94/100, Loss: 0.0360
[IL] Epoch 95/100, Loss: 0.0353
[IL] Epoch 96/100, Loss: 0.0361
[IL] Epoch 97/100, Loss: 0.0346
[IL] Epoch 98/100, Loss: 0.0338
[IL] Epoch 99/100, Loss: 0.0341
test_mean_score: 0.45
[IL] Eval - Success Rate: 0.450
[Checkpoint] Saved to /nfs_global/S/yangrongzheng/RL100/3D-Diffusion-Policy/3D-Diffusion-Policy/checkpoints/offline_iter_1.ckpt

================================================================================
               OFFLINE RL ITERATION 3/5
================================================================================


[RL100Trainer] Line 6 — Training Transition Model T_θ (Iteration 2)

[TransitionModel] Encoding dataset for transition model training...
[TransitionModel] Dataset: 3730 samples, input_dim=260, target_dim=257
[TransitionModel] Epoch    0 | train=140.53983 | val=60.61864 | no-improve=0/5
[TransitionModel] Epoch   20 | train=21.58519 | val=40.17780 | no-improve=0/5
[TransitionModel] Epoch   35 | train=4.82241 | val=39.76375 | no-improve=5/5
[TransitionModel] Training complete. Elites=[1, 0, 2, 5, 3], val_loss=38.03556

[RL100Trainer] Phase 2a: Training IQL Critics (Iteration 2)
[IQL] Epoch 0/50, V Loss: 36.8812, Q Loss: 96331.6146
[IQL] Epoch 1/50, V Loss: 30.6290, Q Loss: 96788.3307
[IQL] Epoch 2/50, V Loss: 14.2396, Q Loss: 95426.3943
[IQL] Epoch 3/50, V Loss: 17.7527, Q Loss: 95066.7724
[IQL] Epoch 4/50, V Loss: 23.5892, Q Loss: 94253.1313
[IQL] Epoch 5/50, V Loss: 22.5761, Q Loss: 95227.5365
[IQL] Epoch 6/50, V Loss: 32.2824, Q Loss: 95249.6031
[IQL] Epoch 7/50, V Loss: 28.2477, Q Loss: 94871.4922
[IQL] Epoch 8/50, V Loss: 22.1922, Q Loss: 93352.9370
[IQL] Epoch 9/50, V Loss: 19.5080, Q Loss: 93261.0573
[IQL] Epoch 10/50, V Loss: 23.6558, Q Loss: 93886.9052
[IQL] Epoch 11/50, V Loss: 25.5246, Q Loss: 92841.5115
[IQL] Epoch 12/50, V Loss: 31.9049, Q Loss: 92669.9625
[IQL] Epoch 13/50, V Loss: 20.5257, Q Loss: 93809.2875
[IQL] Epoch 14/50, V Loss: 23.7264, Q Loss: 93509.4760
[IQL] Epoch 15/50, V Loss: 34.2398, Q Loss: 92837.8036
[IQL] Epoch 16/50, V Loss: 29.0574, Q Loss: 92558.9458
[IQL] Epoch 17/50, V Loss: 24.0757, Q Loss: 92706.6875
[IQL] Epoch 18/50, V Loss: 33.3285, Q Loss: 92205.7984
[IQL] Epoch 19/50, V Loss: 42.4317, Q Loss: 92220.2531
[IQL] Epoch 20/50, V Loss: 40.4145, Q Loss: 91768.5104
[IQL] Epoch 21/50, V Loss: 45.0598, Q Loss: 91635.2609
[IQL] Epoch 22/50, V Loss: 43.3574, Q Loss: 92265.8432
[IQL] Epoch 23/50, V Loss: 39.2602, Q Loss: 92184.9826
[IQL] Epoch 24/50, V Loss: 37.6426, Q Loss: 90918.6503
[IQL] Epoch 25/50, V Loss: 48.6166, Q Loss: 91759.4641
[IQL] Epoch 26/50, V Loss: 36.2128, Q Loss: 91258.5995
[IQL] Epoch 27/50, V Loss: 33.8906, Q Loss: 91608.8255
[IQL] Epoch 28/50, V Loss: 34.3651, Q Loss: 91060.4786
[IQL] Epoch 29/50, V Loss: 36.3189, Q Loss: 90674.1562
[IQL] Epoch 30/50, V Loss: 43.9876, Q Loss: 91444.6901
[IQL] Epoch 31/50, V Loss: 42.0405, Q Loss: 90483.9276
[IQL] Epoch 32/50, V Loss: 51.7831, Q Loss: 90257.8687
[IQL] Epoch 33/50, V Loss: 51.7744, Q Loss: 91561.8552
[IQL] Epoch 34/50, V Loss: 45.3571, Q Loss: 90488.3365
[IQL] Epoch 35/50, V Loss: 51.1500, Q Loss: 89858.8990
[IQL] Epoch 36/50, V Loss: 52.5647, Q Loss: 90680.8729
[IQL] Epoch 37/50, V Loss: 64.2705, Q Loss: 89998.4464
[IQL] Epoch 38/50, V Loss: 46.6989, Q Loss: 89684.6240
[IQL] Epoch 39/50, V Loss: 59.4863, Q Loss: 89261.0641
[IQL] Epoch 40/50, V Loss: 61.5524, Q Loss: 89405.9083
[IQL] Epoch 41/50, V Loss: 55.7308, Q Loss: 89341.4563
[IQL] Epoch 42/50, V Loss: 53.9607, Q Loss: 88536.0240
[IQL] Epoch 43/50, V Loss: 68.7343, Q Loss: 88773.0234
[IQL] Epoch 44/50, V Loss: 58.1779, Q Loss: 88367.1661
[IQL] Epoch 45/50, V Loss: 58.4284, Q Loss: 87826.9435
[IQL] Epoch 46/50, V Loss: 60.0593, Q Loss: 89632.2875
[IQL] Epoch 47/50, V Loss: 67.9333, Q Loss: 87992.3448
[IQL] Epoch 48/50, V Loss: 71.2881, Q Loss: 87728.2453
[IQL] Epoch 49/50, V Loss: 72.0641, Q Loss: 88597.2490

[RL100Trainer] Phase 2b: Offline RL Optimization (Iteration 2)
[OPE] Behavior policy value J_old = 197.5842
[Offline RL] Epoch 0/100, PPO Loss: -0.0407, CD Loss: 0.1322
[Offline RL] Epoch 1/100, PPO Loss: -0.0366, CD Loss: 0.1386
[Offline RL] Epoch 2/100, PPO Loss: -0.0342, CD Loss: 0.1640
[Offline RL] Epoch 3/100, PPO Loss: -0.0292, CD Loss: 0.1331
[Offline RL] Epoch 4/100, PPO Loss: -0.0287, CD Loss: 0.1554
[Offline RL] Epoch 5/100, PPO Loss: -0.0311, CD Loss: 0.1802
[Offline RL] Epoch 6/100, PPO Loss: -0.0352, CD Loss: 0.1650
[Offline RL] Epoch 7/100, PPO Loss: -0.0325, CD Loss: 0.1689
[Offline RL] Epoch 8/100, PPO Loss: -0.0374, CD Loss: 0.1770
[Offline RL] Epoch 9/100, PPO Loss: -0.0390, CD Loss: 0.1604
[Offline RL] Epoch 10/100, PPO Loss: -0.0430, CD Loss: 0.1567
[Offline RL] Epoch 11/100, PPO Loss: -0.0468, CD Loss: 0.1599
[Offline RL] Epoch 12/100, PPO Loss: -0.0454, CD Loss: 0.1599
[Offline RL] Epoch 13/100, PPO Loss: -0.0433, CD Loss: 0.1590
[Offline RL] Epoch 14/100, PPO Loss: -0.0445, CD Loss: 0.1639
[Offline RL] Epoch 15/100, PPO Loss: -0.0460, CD Loss: 0.1708
[Offline RL] Epoch 16/100, PPO Loss: -0.0490, CD Loss: 0.1772
[Offline RL] Epoch 17/100, PPO Loss: -0.0461, CD Loss: 0.1660
[Offline RL] Epoch 18/100, PPO Loss: -0.0513, CD Loss: 0.1811
[Offline RL] Epoch 19/100, PPO Loss: -0.0514, CD Loss: 0.1789
[Offline RL] Epoch 20/100, PPO Loss: -0.0521, CD Loss: 0.1856
[Offline RL] Epoch 21/100, PPO Loss: -0.0544, CD Loss: 0.1888
[Offline RL] Epoch 22/100, PPO Loss: -0.0548, CD Loss: 0.1913
[Offline RL] Epoch 23/100, PPO Loss: -0.0509, CD Loss: 0.1860
[Offline RL] Epoch 24/100, PPO Loss: -0.0524, CD Loss: 0.1870
[Offline RL] Epoch 25/100, PPO Loss: -0.0505, CD Loss: 0.1887
[Offline RL] Epoch 26/100, PPO Loss: -0.0506, CD Loss: 0.1905
[Offline RL] Epoch 27/100, PPO Loss: -0.0532, CD Loss: 0.1876
[Offline RL] Epoch 28/100, PPO Loss: -0.0499, CD Loss: 0.1886
[Offline RL] Epoch 29/100, PPO Loss: -0.0531, CD Loss: 0.1932
[Offline RL] Epoch 30/100, PPO Loss: -0.0506, CD Loss: 0.1959
[Offline RL] Epoch 31/100, PPO Loss: -0.0518, CD Loss: 0.2000
[Offline RL] Epoch 32/100, PPO Loss: -0.0504, CD Loss: 0.1898
[Offline RL] Epoch 33/100, PPO Loss: -0.0552, CD Loss: 0.1873
[Offline RL] Epoch 34/100, PPO Loss: -0.0524, CD Loss: 0.1891
[Offline RL] Epoch 35/100, PPO Loss: -0.0494, CD Loss: 0.1848
[Offline RL] Epoch 36/100, PPO Loss: -0.0505, CD Loss: 0.1825
[Offline RL] Epoch 37/100, PPO Loss: -0.0491, CD Loss: 0.1797
[Offline RL] Epoch 38/100, PPO Loss: -0.0459, CD Loss: 0.1756
[Offline RL] Epoch 39/100, PPO Loss: -0.0502, CD Loss: 0.1761
[Offline RL] Epoch 40/100, PPO Loss: -0.0511, CD Loss: 0.1776
[Offline RL] Epoch 41/100, PPO Loss: -0.0510, CD Loss: 0.1798
[Offline RL] Epoch 42/100, PPO Loss: -0.0511, CD Loss: 0.1767
[Offline RL] Epoch 43/100, PPO Loss: -0.0498, CD Loss: 0.1827
[Offline RL] Epoch 44/100, PPO Loss: -0.0515, CD Loss: 0.1953
[Offline RL] Epoch 45/100, PPO Loss: -0.0530, CD Loss: 0.1979
[Offline RL] Epoch 46/100, PPO Loss: -0.0524, CD Loss: 0.1959
[Offline RL] Epoch 47/100, PPO Loss: -0.0538, CD Loss: 0.1917
[Offline RL] Epoch 48/100, PPO Loss: -0.0524, CD Loss: 0.1894
[Offline RL] Epoch 49/100, PPO Loss: -0.0539, CD Loss: 0.1768
[Offline RL] Epoch 50/100, PPO Loss: -0.0546, CD Loss: 0.1793
[Offline RL] Epoch 51/100, PPO Loss: -0.0527, CD Loss: 0.1886
[Offline RL] Epoch 52/100, PPO Loss: -0.0540, CD Loss: 0.1921
[Offline RL] Epoch 53/100, PPO Loss: -0.0519, CD Loss: 0.1891
[Offline RL] Epoch 54/100, PPO Loss: -0.0522, CD Loss: 0.1904
[Offline RL] Epoch 55/100, PPO Loss: -0.0535, CD Loss: 0.1799
[Offline RL] Epoch 56/100, PPO Loss: -0.0563, CD Loss: 0.1850
[Offline RL] Epoch 57/100, PPO Loss: -0.0566, CD Loss: 0.1816
[Offline RL] Epoch 58/100, PPO Loss: -0.0564, CD Loss: 0.1915
[Offline RL] Epoch 59/100, PPO Loss: -0.0579, CD Loss: 0.2029
[Offline RL] Epoch 60/100, PPO Loss: -0.0561, CD Loss: 0.2045
[Offline RL] Epoch 61/100, PPO Loss: -0.0552, CD Loss: 0.1980
[Offline RL] Epoch 62/100, PPO Loss: -0.0554, CD Loss: 0.1899
[Offline RL] Epoch 63/100, PPO Loss: -0.0546, CD Loss: 0.1983
[Offline RL] Epoch 64/100, PPO Loss: -0.0558, CD Loss: 0.2018
[Offline RL] Epoch 65/100, PPO Loss: -0.0550, CD Loss: 0.1918
[Offline RL] Epoch 66/100, PPO Loss: -0.0540, CD Loss: 0.1890
[Offline RL] Epoch 67/100, PPO Loss: -0.0527, CD Loss: 0.1911
[Offline RL] Epoch 68/100, PPO Loss: -0.0555, CD Loss: 0.1947
[Offline RL] Epoch 69/100, PPO Loss: -0.0561, CD Loss: 0.1923
[Offline RL] Epoch 70/100, PPO Loss: -0.0566, CD Loss: 0.1887
[Offline RL] Epoch 71/100, PPO Loss: -0.0559, CD Loss: 0.1800
[Offline RL] Epoch 72/100, PPO Loss: -0.0569, CD Loss: 0.1766
[Offline RL] Epoch 73/100, PPO Loss: -0.0574, CD Loss: 0.1738
[Offline RL] Epoch 74/100, PPO Loss: -0.0572, CD Loss: 0.1738
[Offline RL] Epoch 75/100, PPO Loss: -0.0535, CD Loss: 0.1780
[Offline RL] Epoch 76/100, PPO Loss: -0.0527, CD Loss: 0.1697
[Offline RL] Epoch 77/100, PPO Loss: -0.0562, CD Loss: 0.1674
[Offline RL] Epoch 78/100, PPO Loss: -0.0556, CD Loss: 0.1672
[Offline RL] Epoch 79/100, PPO Loss: -0.0535, CD Loss: 0.1682
[Offline RL] Epoch 80/100, PPO Loss: -0.0549, CD Loss: 0.1691
[Offline RL] Epoch 81/100, PPO Loss: -0.0538, CD Loss: 0.1742
[Offline RL] Epoch 82/100, PPO Loss: -0.0519, CD Loss: 0.1676
[Offline RL] Epoch 83/100, PPO Loss: -0.0482, CD Loss: 0.1723
[Offline RL] Epoch 84/100, PPO Loss: -0.0544, CD Loss: 0.1732
[Offline RL] Epoch 85/100, PPO Loss: -0.0509, CD Loss: 0.1734
[Offline RL] Epoch 86/100, PPO Loss: -0.0496, CD Loss: 0.1754
[Offline RL] Epoch 87/100, PPO Loss: -0.0531, CD Loss: 0.1688
[Offline RL] Epoch 88/100, PPO Loss: -0.0552, CD Loss: 0.1729
[Offline RL] Epoch 89/100, PPO Loss: -0.0547, CD Loss: 0.1754
[Offline RL] Epoch 90/100, PPO Loss: -0.0560, CD Loss: 0.1734
[Offline RL] Epoch 91/100, PPO Loss: -0.0552, CD Loss: 0.1785
[Offline RL] Epoch 92/100, PPO Loss: -0.0537, CD Loss: 0.1725
[Offline RL] Epoch 93/100, PPO Loss: -0.0526, CD Loss: 0.1789
[Offline RL] Epoch 94/100, PPO Loss: -0.0543, CD Loss: 0.1832
[Offline RL] Epoch 95/100, PPO Loss: -0.0540, CD Loss: 0.1850
[Offline RL] Epoch 96/100, PPO Loss: -0.0520, CD Loss: 0.1801
[Offline RL] Epoch 97/100, PPO Loss: -0.0529, CD Loss: 0.1882
[Offline RL] Epoch 98/100, PPO Loss: -0.0527, CD Loss: 0.1887
[Offline RL] Epoch 99/100, PPO Loss: -0.0533, CD Loss: 0.1901
[OPE] Policy REJECTED: J_new=200.0050 ≤ J_old=197.5842 + δ=9.8792. Rolling back to behavior policy.

[RL100Trainer] Phase 2c: Collecting New Data (Iteration 2)
[Collect] 50 episodes, success=0.500, steps=1250
[Data Collection] Success Rate: 0.500, Reward: 11725.52, Episodes: 50, Steps: 1250
[Dataset] Merged 50 episodes (1250 steps) → total 5750 steps, 160 episodes

[RL100Trainer] Retraining IL on merged dataset...

============================================================
[RL100Trainer] Phase 1: Imitation Learning
============================================================

[IL] Epoch 0/100, Loss: 0.0460
[IL] Epoch 1/100, Loss: 0.0470
[IL] Epoch 2/100, Loss: 0.0458
[IL] Epoch 3/100, Loss: 0.0461
[IL] Epoch 4/100, Loss: 0.0463
[IL] Epoch 5/100, Loss: 0.0474
[IL] Epoch 6/100, Loss: 0.0441
[IL] Epoch 7/100, Loss: 0.0436
[IL] Epoch 8/100, Loss: 0.0421
[IL] Epoch 9/100, Loss: 0.0465
[IL] Epoch 10/100, Loss: 0.0433
[IL] Epoch 11/100, Loss: 0.0440
[IL] Epoch 12/100, Loss: 0.0432
[IL] Epoch 13/100, Loss: 0.0423
[IL] Epoch 14/100, Loss: 0.0408
[IL] Epoch 15/100, Loss: 0.0416
[IL] Epoch 16/100, Loss: 0.0396
[IL] Epoch 17/100, Loss: 0.0421
[IL] Epoch 18/100, Loss: 0.0413
[IL] Epoch 19/100, Loss: 0.0428
[IL] Epoch 20/100, Loss: 0.0452
[IL] Epoch 21/100, Loss: 0.0437
[IL] Epoch 22/100, Loss: 0.0422
[IL] Epoch 23/100, Loss: 0.0408
[IL] Epoch 24/100, Loss: 0.0433
[IL] Epoch 25/100, Loss: 0.0433
[IL] Epoch 26/100, Loss: 0.0408
[IL] Epoch 27/100, Loss: 0.0430
[IL] Epoch 28/100, Loss: 0.0425
[IL] Epoch 29/100, Loss: 0.0390
[IL] Epoch 30/100, Loss: 0.0404
[IL] Epoch 31/100, Loss: 0.0447
[IL] Epoch 32/100, Loss: 0.0429
[IL] Epoch 33/100, Loss: 0.0448
[IL] Epoch 34/100, Loss: 0.0407
[IL] Epoch 35/100, Loss: 0.0386
[IL] Epoch 36/100, Loss: 0.0381
[IL] Epoch 37/100, Loss: 0.0393
[IL] Epoch 38/100, Loss: 0.0406
[IL] Epoch 39/100, Loss: 0.0404
[IL] Epoch 40/100, Loss: 0.0412
[IL] Epoch 41/100, Loss: 0.0415
[IL] Epoch 42/100, Loss: 0.0397
[IL] Epoch 43/100, Loss: 0.0402
[IL] Epoch 44/100, Loss: 0.0406
[IL] Epoch 45/100, Loss: 0.0388
[IL] Epoch 46/100, Loss: 0.0394
[IL] Epoch 47/100, Loss: 0.0394
[IL] Epoch 48/100, Loss: 0.0388
[IL] Epoch 49/100, Loss: 0.0378
[IL] Epoch 50/100, Loss: 0.0382
[IL] Epoch 51/100, Loss: 0.0406
[IL] Epoch 52/100, Loss: 0.0380
[IL] Epoch 53/100, Loss: 0.0396
[IL] Epoch 54/100, Loss: 0.0389
[IL] Epoch 55/100, Loss: 0.0448
[IL] Epoch 56/100, Loss: 0.0398
[IL] Epoch 57/100, Loss: 0.0426
[IL] Epoch 58/100, Loss: 0.0430
[IL] Epoch 59/100, Loss: 0.0394
[IL] Epoch 60/100, Loss: 0.0375
[IL] Epoch 61/100, Loss: 0.0406
[IL] Epoch 62/100, Loss: 0.0413
[IL] Epoch 63/100, Loss: 0.0408
[IL] Epoch 64/100, Loss: 0.0406
[IL] Epoch 65/100, Loss: 0.0404
[IL] Epoch 66/100, Loss: 0.0372
[IL] Epoch 67/100, Loss: 0.0399
[IL] Epoch 68/100, Loss: 0.0386
[IL] Epoch 69/100, Loss: 0.0372
[IL] Epoch 70/100, Loss: 0.0372
[IL] Epoch 71/100, Loss: 0.0401
[IL] Epoch 72/100, Loss: 0.0379
[IL] Epoch 73/100, Loss: 0.0361
[IL] Epoch 74/100, Loss: 0.0377
[IL] Epoch 75/100, Loss: 0.0367
[IL] Epoch 76/100, Loss: 0.0346
[IL] Epoch 77/100, Loss: 0.0360
[IL] Epoch 78/100, Loss: 0.0353
[IL] Epoch 79/100, Loss: 0.0369
[IL] Epoch 80/100, Loss: 0.0397
[IL] Epoch 81/100, Loss: 0.0379
[IL] Epoch 82/100, Loss: 0.0355
[IL] Epoch 83/100, Loss: 0.0371
[IL] Epoch 84/100, Loss: 0.0380
[IL] Epoch 85/100, Loss: 0.0364
[IL] Epoch 86/100, Loss: 0.0382
[IL] Epoch 87/100, Loss: 0.0369
[IL] Epoch 88/100, Loss: 0.0388
[IL] Epoch 89/100, Loss: 0.0414
[IL] Epoch 90/100, Loss: 0.0399
[IL] Epoch 91/100, Loss: 0.0381
[IL] Epoch 92/100, Loss: 0.0367
[IL] Epoch 93/100, Loss: 0.0350
[IL] Epoch 94/100, Loss: 0.0384
[IL] Epoch 95/100, Loss: 0.0398
[IL] Epoch 96/100, Loss: 0.0415
[IL] Epoch 97/100, Loss: 0.0401
[IL] Epoch 98/100, Loss: 0.0407
[IL] Epoch 99/100, Loss: 0.0364
test_mean_score: 0.55
[IL] Eval - Success Rate: 0.550
[Checkpoint] Saved to /nfs_global/S/yangrongzheng/RL100/3D-Diffusion-Policy/3D-Diffusion-Policy/checkpoints/offline_iter_2.ckpt

================================================================================
               OFFLINE RL ITERATION 4/5
================================================================================


[RL100Trainer] Line 6 — Training Transition Model T_θ (Iteration 3)

[TransitionModel] Encoding dataset for transition model training...
[TransitionModel] Dataset: 4630 samples, input_dim=260, target_dim=257
[TransitionModel] Epoch    0 | train=86.96143 | val=51.82836 | no-improve=0/5
[TransitionModel] Epoch   20 | train=14.43269 | val=32.58241 | no-improve=1/5
[TransitionModel] Epoch   40 | train=-1.32384 | val=32.49493 | no-improve=4/5
[TransitionModel] Epoch   48 | train=-4.17390 | val=32.28484 | no-improve=5/5
[TransitionModel] Training complete. Elites=[3, 1, 0, 5, 2], val_loss=30.07576

[RL100Trainer] Phase 2a: Training IQL Critics (Iteration 3)
[IQL] Epoch 0/50, V Loss: 116.0616, Q Loss: 114319.3014
[IQL] Epoch 1/50, V Loss: 109.2144, Q Loss: 121869.7484
[IQL] Epoch 2/50, V Loss: 109.2806, Q Loss: 118939.1201
[IQL] Epoch 3/50, V Loss: 79.5884, Q Loss: 120764.6575
[IQL] Epoch 4/50, V Loss: 98.1418, Q Loss: 113579.1756
[IQL] Epoch 5/50, V Loss: 115.0479, Q Loss: 115435.3035
[IQL] Epoch 6/50, V Loss: 120.6446, Q Loss: 117877.6016
[IQL] Epoch 7/50, V Loss: 112.4957, Q Loss: 110733.9192
[IQL] Epoch 8/50, V Loss: 125.6628, Q Loss: 110409.3405
[IQL] Epoch 9/50, V Loss: 96.9747, Q Loss: 110578.7029
[IQL] Epoch 10/50, V Loss: 109.1143, Q Loss: 120463.9470
[IQL] Epoch 11/50, V Loss: 128.6217, Q Loss: 115477.6472
[IQL] Epoch 12/50, V Loss: 87.9658, Q Loss: 111831.5617
[IQL] Epoch 13/50, V Loss: 105.1035, Q Loss: 112916.0798
[IQL] Epoch 14/50, V Loss: 115.0821, Q Loss: 112795.5156
[IQL] Epoch 15/50, V Loss: 99.1143, Q Loss: 108191.7229
[IQL] Epoch 16/50, V Loss: 101.3278, Q Loss: 113699.0900
[IQL] Epoch 17/50, V Loss: 92.9971, Q Loss: 113669.7105
[IQL] Epoch 18/50, V Loss: 125.2500, Q Loss: 111814.1990
[IQL] Epoch 19/50, V Loss: 148.5389, Q Loss: 110721.5999
[IQL] Epoch 20/50, V Loss: 150.4199, Q Loss: 110627.5761
[IQL] Epoch 21/50, V Loss: 205.8892, Q Loss: 115589.6887
[IQL] Epoch 22/50, V Loss: 175.3437, Q Loss: 112729.5370
[IQL] Epoch 23/50, V Loss: 156.9501, Q Loss: 113230.2200
[IQL] Epoch 24/50, V Loss: 243.9822, Q Loss: 111123.1188
[IQL] Epoch 25/50, V Loss: 191.3771, Q Loss: 110767.5522
[IQL] Epoch 26/50, V Loss: 138.6896, Q Loss: 111901.1036
[IQL] Epoch 27/50, V Loss: 148.3147, Q Loss: 107249.8995
Extracting GPU stats logs using atop has been completed on r8l40-a02.
Logs are being saved to: /nfs_global/S/yangrongzheng/atop-736093-r8l40-a02-gpustat.log
[IQL] Epoch 28/50, V Loss: 167.5218, Q Loss: 109795.8606
[IQL] Epoch 29/50, V Loss: 148.2174, Q Loss: 107736.5724
[IQL] Epoch 30/50, V Loss: 141.3819, Q Loss: 113056.3026
[IQL] Epoch 31/50, V Loss: 174.4190, Q Loss: 110699.8684
[IQL] Epoch 32/50, V Loss: 189.8547, Q Loss: 112441.0921
[IQL] Epoch 33/50, V Loss: 163.8002, Q Loss: 107589.1776
[IQL] Epoch 34/50, V Loss: 114.7118, Q Loss: 108674.5222
[IQL] Epoch 35/50, V Loss: 164.9826, Q Loss: 108452.9836
[IQL] Epoch 36/50, V Loss: 196.7621, Q Loss: 107481.3997
[IQL] Epoch 37/50, V Loss: 156.8619, Q Loss: 104779.3174
[IQL] Epoch 38/50, V Loss: 142.9861, Q Loss: 106536.3039
[IQL] Epoch 39/50, V Loss: 142.0054, Q Loss: 109359.7093
[IQL] Epoch 40/50, V Loss: 144.9460, Q Loss: 112312.3129
[IQL] Epoch 41/50, V Loss: 219.5191, Q Loss: 103996.0280
[IQL] Epoch 42/50, V Loss: 225.5044, Q Loss: 105970.0970
[IQL] Epoch 43/50, V Loss: 186.0070, Q Loss: 108077.6657
[IQL] Epoch 44/50, V Loss: 178.3458, Q Loss: 105215.8672
[IQL] Epoch 45/50, V Loss: 166.8696, Q Loss: 109957.1920
[IQL] Epoch 46/50, V Loss: 129.9415, Q Loss: 110583.2829
[IQL] Epoch 47/50, V Loss: 174.3991, Q Loss: 104304.7539
[IQL] Epoch 48/50, V Loss: 178.5903, Q Loss: 110311.8092
[IQL] Epoch 49/50, V Loss: 219.2496, Q Loss: 106667.2179

[RL100Trainer] Phase 2b: Offline RL Optimization (Iteration 3)
[OPE] Behavior policy value J_old = 378.3962
[Offline RL] Epoch 0/100, PPO Loss: -0.0366, CD Loss: 0.2227
[Offline RL] Epoch 1/100, PPO Loss: -0.0237, CD Loss: 0.2104
[Offline RL] Epoch 2/100, PPO Loss: -0.0261, CD Loss: 0.2132
[Offline RL] Epoch 3/100, PPO Loss: -0.0298, CD Loss: 0.2000
[Offline RL] Epoch 4/100, PPO Loss: -0.0295, CD Loss: 0.2286
[Offline RL] Epoch 5/100, PPO Loss: -0.0291, CD Loss: 0.2542
[Offline RL] Epoch 6/100, PPO Loss: -0.0315, CD Loss: 0.2217
[Offline RL] Epoch 7/100, PPO Loss: -0.0326, CD Loss: 0.2242
[Offline RL] Epoch 8/100, PPO Loss: -0.0308, CD Loss: 0.2190
[Offline RL] Epoch 9/100, PPO Loss: -0.0338, CD Loss: 0.2216
[Offline RL] Epoch 10/100, PPO Loss: -0.0374, CD Loss: 0.2270
[Offline RL] Epoch 11/100, PPO Loss: -0.0374, CD Loss: 0.2299
[Offline RL] Epoch 12/100, PPO Loss: -0.0358, CD Loss: 0.2305
[Offline RL] Epoch 13/100, PPO Loss: -0.0394, CD Loss: 0.2227
[Offline RL] Epoch 14/100, PPO Loss: -0.0384, CD Loss: 0.2204
[Offline RL] Epoch 15/100, PPO Loss: -0.0372, CD Loss: 0.2161
[Offline RL] Epoch 16/100, PPO Loss: -0.0402, CD Loss: 0.2224
[Offline RL] Epoch 17/100, PPO Loss: -0.0390, CD Loss: 0.2249
[Offline RL] Epoch 18/100, PPO Loss: -0.0408, CD Loss: 0.2156
[Offline RL] Epoch 19/100, PPO Loss: -0.0417, CD Loss: 0.2155
[Offline RL] Epoch 20/100, PPO Loss: -0.0388, CD Loss: 0.2120
[Offline RL] Epoch 21/100, PPO Loss: -0.0394, CD Loss: 0.2123
[Offline RL] Epoch 22/100, PPO Loss: -0.0414, CD Loss: 0.2213
[Offline RL] Epoch 23/100, PPO Loss: -0.0412, CD Loss: 0.2251
[Offline RL] Epoch 24/100, PPO Loss: -0.0390, CD Loss: 0.2095
[Offline RL] Epoch 25/100, PPO Loss: -0.0413, CD Loss: 0.2153
[Offline RL] Epoch 26/100, PPO Loss: -0.0419, CD Loss: 0.2158
[Offline RL] Epoch 27/100, PPO Loss: -0.0445, CD Loss: 0.2192
[Offline RL] Epoch 28/100, PPO Loss: -0.0413, CD Loss: 0.2196
[Offline RL] Epoch 29/100, PPO Loss: -0.0388, CD Loss: 0.2047
[Offline RL] Epoch 30/100, PPO Loss: -0.0377, CD Loss: 0.2188
[Offline RL] Epoch 31/100, PPO Loss: -0.0409, CD Loss: 0.2065
[Offline RL] Epoch 32/100, PPO Loss: -0.0440, CD Loss: 0.2047
[Offline RL] Epoch 33/100, PPO Loss: -0.0435, CD Loss: 0.1979
[Offline RL] Epoch 34/100, PPO Loss: -0.0408, CD Loss: 0.2070
[Offline RL] Epoch 35/100, PPO Loss: -0.0408, CD Loss: 0.2001
[Offline RL] Epoch 36/100, PPO Loss: -0.0405, CD Loss: 0.2068
[Offline RL] Epoch 37/100, PPO Loss: -0.0406, CD Loss: 0.2096
[Offline RL] Epoch 38/100, PPO Loss: -0.0382, CD Loss: 0.2018
[Offline RL] Epoch 39/100, PPO Loss: -0.0393, CD Loss: 0.2040
[Offline RL] Epoch 40/100, PPO Loss: -0.0395, CD Loss: 0.2073
[Offline RL] Epoch 41/100, PPO Loss: -0.0376, CD Loss: 0.2062
[Offline RL] Epoch 42/100, PPO Loss: -0.0376, CD Loss: 0.1987
[Offline RL] Epoch 43/100, PPO Loss: -0.0395, CD Loss: 0.2016
[Offline RL] Epoch 44/100, PPO Loss: -0.0382, CD Loss: 0.2092
[Offline RL] Epoch 45/100, PPO Loss: -0.0369, CD Loss: 0.2060
[Offline RL] Epoch 46/100, PPO Loss: -0.0369, CD Loss: 0.1991
[Offline RL] Epoch 47/100, PPO Loss: -0.0396, CD Loss: 0.1954
[Offline RL] Epoch 48/100, PPO Loss: -0.0335, CD Loss: 0.1976
[Offline RL] Epoch 49/100, PPO Loss: -0.0357, CD Loss: 0.1895
[Offline RL] Epoch 50/100, PPO Loss: -0.0370, CD Loss: 0.1969
[Offline RL] Epoch 51/100, PPO Loss: -0.0388, CD Loss: 0.1895
[Offline RL] Epoch 52/100, PPO Loss: -0.0349, CD Loss: 0.1900
[Offline RL] Epoch 53/100, PPO Loss: -0.0341, CD Loss: 0.1955
[Offline RL] Epoch 54/100, PPO Loss: -0.0352, CD Loss: 0.1867
[Offline RL] Epoch 55/100, PPO Loss: -0.0364, CD Loss: 0.1939
[Offline RL] Epoch 56/100, PPO Loss: -0.0380, CD Loss: 0.1960
[Offline RL] Epoch 57/100, PPO Loss: -0.0374, CD Loss: 0.1979
[Offline RL] Epoch 58/100, PPO Loss: -0.0359, CD Loss: 0.2018
[Offline RL] Epoch 59/100, PPO Loss: -0.0366, CD Loss: 0.1911
[Offline RL] Epoch 60/100, PPO Loss: -0.0367, CD Loss: 0.2000
[Offline RL] Epoch 61/100, PPO Loss: -0.0376, CD Loss: 0.2024
[Offline RL] Epoch 62/100, PPO Loss: -0.0365, CD Loss: 0.1991
[Offline RL] Epoch 63/100, PPO Loss: -0.0369, CD Loss: 0.1969
[Offline RL] Epoch 64/100, PPO Loss: -0.0387, CD Loss: 0.2040
[Offline RL] Epoch 65/100, PPO Loss: -0.0372, CD Loss: 0.1992
[Offline RL] Epoch 66/100, PPO Loss: -0.0385, CD Loss: 0.1884
[Offline RL] Epoch 67/100, PPO Loss: -0.0357, CD Loss: 0.1823
[Offline RL] Epoch 68/100, PPO Loss: -0.0381, CD Loss: 0.1786
[Offline RL] Epoch 69/100, PPO Loss: -0.0373, CD Loss: 0.1845
[Offline RL] Epoch 70/100, PPO Loss: -0.0330, CD Loss: 0.1860
[Offline RL] Epoch 71/100, PPO Loss: -0.0371, CD Loss: 0.1846
[Offline RL] Epoch 72/100, PPO Loss: -0.0335, CD Loss: 0.1888
[Offline RL] Epoch 73/100, PPO Loss: -0.0374, CD Loss: 0.1916
[Offline RL] Epoch 74/100, PPO Loss: -0.0343, CD Loss: 0.1885
[Offline RL] Epoch 75/100, PPO Loss: -0.0345, CD Loss: 0.1846
[Offline RL] Epoch 76/100, PPO Loss: -0.0341, CD Loss: 0.1901
[Offline RL] Epoch 77/100, PPO Loss: -0.0355, CD Loss: 0.1829
[Offline RL] Epoch 78/100, PPO Loss: -0.0344, CD Loss: 0.1928
[Offline RL] Epoch 79/100, PPO Loss: -0.0317, CD Loss: 0.1882
[Offline RL] Epoch 80/100, PPO Loss: -0.0343, CD Loss: 0.1921
[Offline RL] Epoch 81/100, PPO Loss: -0.0331, CD Loss: 0.2004
[Offline RL] Epoch 82/100, PPO Loss: -0.0360, CD Loss: 0.2120
[Offline RL] Epoch 83/100, PPO Loss: -0.0350, CD Loss: 0.2076
[Offline RL] Epoch 84/100, PPO Loss: -0.0334, CD Loss: 0.2190
[Offline RL] Epoch 85/100, PPO Loss: -0.0357, CD Loss: 0.2096
[Offline RL] Epoch 86/100, PPO Loss: -0.0333, CD Loss: 0.2253
[Offline RL] Epoch 87/100, PPO Loss: -0.0312, CD Loss: 0.2146
[Offline RL] Epoch 88/100, PPO Loss: -0.0345, CD Loss: 0.2030
[Offline RL] Epoch 89/100, PPO Loss: -0.0333, CD Loss: 0.2071
[Offline RL] Epoch 90/100, PPO Loss: -0.0343, CD Loss: 0.2098
[Offline RL] Epoch 91/100, PPO Loss: -0.0342, CD Loss: 0.2131
[Offline RL] Epoch 92/100, PPO Loss: -0.0324, CD Loss: 0.2250
[Offline RL] Epoch 93/100, PPO Loss: -0.0337, CD Loss: 0.2306
[Offline RL] Epoch 94/100, PPO Loss: -0.0337, CD Loss: 0.2362
[Offline RL] Epoch 95/100, PPO Loss: -0.0310, CD Loss: 0.2430
[Offline RL] Epoch 96/100, PPO Loss: -0.0315, CD Loss: 0.2596
[Offline RL] Epoch 97/100, PPO Loss: -0.0293, CD Loss: 0.2679
[Offline RL] Epoch 98/100, PPO Loss: -0.0342, CD Loss: 0.2614
[Offline RL] Epoch 99/100, PPO Loss: -0.0318, CD Loss: 0.2774
[OPE] Policy REJECTED: J_new=362.5428 ≤ J_old=378.3962 + δ=18.9198. Rolling back to behavior policy.

[RL100Trainer] Phase 2c: Collecting New Data (Iteration 3)
[Collect] 50 episodes, success=0.500, steps=1250
[Data Collection] Success Rate: 0.500, Reward: 10623.79, Episodes: 50, Steps: 1250
[Dataset] Merged 50 episodes (1250 steps) → total 7000 steps, 210 episodes

[RL100Trainer] Retraining IL on merged dataset...

============================================================
[RL100Trainer] Phase 1: Imitation Learning
============================================================

[IL] Epoch 0/100, Loss: 0.0494
[IL] Epoch 1/100, Loss: 0.0455
[IL] Epoch 2/100, Loss: 0.0451
[IL] Epoch 3/100, Loss: 0.0444
[IL] Epoch 4/100, Loss: 0.0440
[IL] Epoch 5/100, Loss: 0.0460
[IL] Epoch 6/100, Loss: 0.0438
[IL] Epoch 7/100, Loss: 0.0433
[IL] Epoch 8/100, Loss: 0.0417
[IL] Epoch 9/100, Loss: 0.0400
[IL] Epoch 10/100, Loss: 0.0398
[IL] Epoch 11/100, Loss: 0.0415
[IL] Epoch 12/100, Loss: 0.0417
[IL] Epoch 13/100, Loss: 0.0410
[IL] Epoch 14/100, Loss: 0.0409
[IL] Epoch 15/100, Loss: 0.0391
[IL] Epoch 16/100, Loss: 0.0385
[IL] Epoch 17/100, Loss: 0.0389
[IL] Epoch 18/100, Loss: 0.0399
[IL] Epoch 19/100, Loss: 0.0388
[IL] Epoch 20/100, Loss: 0.0407
[IL] Epoch 21/100, Loss: 0.0379
[IL] Epoch 22/100, Loss: 0.0371
[IL] Epoch 23/100, Loss: 0.0389
[IL] Epoch 24/100, Loss: 0.0386
[IL] Epoch 25/100, Loss: 0.0383
[IL] Epoch 26/100, Loss: 0.0410
[IL] Epoch 27/100, Loss: 0.0393
[IL] Epoch 28/100, Loss: 0.0387
[IL] Epoch 29/100, Loss: 0.0389
[IL] Epoch 30/100, Loss: 0.0384
[IL] Epoch 31/100, Loss: 0.0374
[IL] Epoch 32/100, Loss: 0.0368
[IL] Epoch 33/100, Loss: 0.0353
[IL] Epoch 34/100, Loss: 0.0364
[IL] Epoch 35/100, Loss: 0.0372
[IL] Epoch 36/100, Loss: 0.0365
[IL] Epoch 37/100, Loss: 0.0378
[IL] Epoch 38/100, Loss: 0.0364
[IL] Epoch 39/100, Loss: 0.0356
[IL] Epoch 40/100, Loss: 0.0365
[IL] Epoch 41/100, Loss: 0.0368
[IL] Epoch 42/100, Loss: 0.0365
[IL] Epoch 43/100, Loss: 0.0357
[IL] Epoch 44/100, Loss: 0.0365
[IL] Epoch 45/100, Loss: 0.0378
[IL] Epoch 46/100, Loss: 0.0359
[IL] Epoch 47/100, Loss: 0.0337
[IL] Epoch 48/100, Loss: 0.0370
[IL] Epoch 49/100, Loss: 0.0358
[IL] Epoch 50/100, Loss: 0.0345
[IL] Epoch 51/100, Loss: 0.0352
[IL] Epoch 52/100, Loss: 0.0338
[IL] Epoch 53/100, Loss: 0.0352
[IL] Epoch 54/100, Loss: 0.0334
[IL] Epoch 55/100, Loss: 0.0356
[IL] Epoch 56/100, Loss: 0.0350
[IL] Epoch 57/100, Loss: 0.0322
[IL] Epoch 58/100, Loss: 0.0334
[IL] Epoch 59/100, Loss: 0.0340
[IL] Epoch 60/100, Loss: 0.0336
[IL] Epoch 61/100, Loss: 0.0334
[IL] Epoch 62/100, Loss: 0.0343
[IL] Epoch 63/100, Loss: 0.0341
[IL] Epoch 64/100, Loss: 0.0319
[IL] Epoch 65/100, Loss: 0.0339
[IL] Epoch 66/100, Loss: 0.0333
[IL] Epoch 67/100, Loss: 0.0314
[IL] Epoch 68/100, Loss: 0.0342
[IL] Epoch 69/100, Loss: 0.0324
[IL] Epoch 70/100, Loss: 0.0328
[IL] Epoch 71/100, Loss: 0.0327
[IL] Epoch 72/100, Loss: 0.0316
[IL] Epoch 73/100, Loss: 0.0322
[IL] Epoch 74/100, Loss: 0.0324
[IL] Epoch 75/100, Loss: 0.0330
[IL] Epoch 76/100, Loss: 0.0317
[IL] Epoch 77/100, Loss: 0.0302
[IL] Epoch 78/100, Loss: 0.0295
[IL] Epoch 79/100, Loss: 0.0303
[IL] Epoch 80/100, Loss: 0.0321
[IL] Epoch 81/100, Loss: 0.0305
[IL] Epoch 82/100, Loss: 0.0317
[IL] Epoch 83/100, Loss: 0.0312
[IL] Epoch 84/100, Loss: 0.0300
[IL] Epoch 85/100, Loss: 0.0305
[IL] Epoch 86/100, Loss: 0.0307
[IL] Epoch 87/100, Loss: 0.0304
[IL] Epoch 88/100, Loss: 0.0315
[IL] Epoch 89/100, Loss: 0.0300
[IL] Epoch 90/100, Loss: 0.0290
[IL] Epoch 91/100, Loss: 0.0296
[IL] Epoch 92/100, Loss: 0.0286
[IL] Epoch 93/100, Loss: 0.0299
[IL] Epoch 94/100, Loss: 0.0287
[IL] Epoch 95/100, Loss: 0.0288
[IL] Epoch 96/100, Loss: 0.0299
[IL] Epoch 97/100, Loss: 0.0290
[IL] Epoch 98/100, Loss: 0.0312
[IL] Epoch 99/100, Loss: 0.0290
test_mean_score: 0.6
[IL] Eval - Success Rate: 0.600
[Checkpoint] Saved to /nfs_global/S/yangrongzheng/RL100/3D-Diffusion-Policy/3D-Diffusion-Policy/checkpoints/offline_iter_3.ckpt

================================================================================
               OFFLINE RL ITERATION 5/5
================================================================================


[RL100Trainer] Line 6 — Training Transition Model T_θ (Iteration 4)

[TransitionModel] Encoding dataset for transition model training...
[TransitionModel] Dataset: 5530 samples, input_dim=260, target_dim=257
[TransitionModel] Epoch    0 | train=43.18086 | val=39.36451 | no-improve=0/5
[TransitionModel] Epoch   20 | train=-1.13824 | val=27.00580 | no-improve=0/5
[TransitionModel] Epoch   40 | train=-11.36303 | val=26.04936 | no-improve=5/5
[TransitionModel] Training complete. Elites=[0, 1, 3, 5, 4], val_loss=25.22212

[RL100Trainer] Phase 2a: Training IQL Critics (Iteration 4)
[IQL] Epoch 0/50, V Loss: 269.6182, Q Loss: 121632.4925
[IQL] Epoch 1/50, V Loss: 264.4717, Q Loss: 121601.3445
[IQL] Epoch 2/50, V Loss: 251.8965, Q Loss: 120948.4308
[IQL] Epoch 3/50, V Loss: 237.3330, Q Loss: 120658.9237
[IQL] Epoch 4/50, V Loss: 380.6528, Q Loss: 120054.8761
[IQL] Epoch 5/50, V Loss: 386.3570, Q Loss: 119146.8196
[IQL] Epoch 6/50, V Loss: 216.1519, Q Loss: 119249.9901
[IQL] Epoch 7/50, V Loss: 291.4838, Q Loss: 119248.5742
[IQL] Epoch 8/50, V Loss: 292.4865, Q Loss: 118555.4808
[IQL] Epoch 9/50, V Loss: 273.2509, Q Loss: 120303.9258
[IQL] Epoch 10/50, V Loss: 296.5982, Q Loss: 118263.6424
[IQL] Epoch 11/50, V Loss: 288.5420, Q Loss: 118881.3139
[IQL] Epoch 12/50, V Loss: 227.9842, Q Loss: 118591.9219
[IQL] Epoch 13/50, V Loss: 240.8218, Q Loss: 118848.9854
[IQL] Epoch 14/50, V Loss: 315.8887, Q Loss: 117719.1573
[IQL] Epoch 15/50, V Loss: 431.5653, Q Loss: 116912.2436
[IQL] Epoch 16/50, V Loss: 379.6107, Q Loss: 116705.7472
[IQL] Epoch 17/50, V Loss: 254.4786, Q Loss: 117658.8438
[IQL] Epoch 18/50, V Loss: 220.5109, Q Loss: 116681.7230
[IQL] Epoch 19/50, V Loss: 214.5761, Q Loss: 115430.1541
[IQL] Epoch 20/50, V Loss: 234.4649, Q Loss: 115830.1861
[IQL] Epoch 21/50, V Loss: 227.1784, Q Loss: 114984.9638
[IQL] Epoch 22/50, V Loss: 212.5553, Q Loss: 115576.0920
[IQL] Epoch 23/50, V Loss: 214.4889, Q Loss: 116305.6644
[IQL] Epoch 24/50, V Loss: 330.6261, Q Loss: 115824.3746
[IQL] Epoch 25/50, V Loss: 361.8985, Q Loss: 116044.8888
[IQL] Epoch 26/50, V Loss: 298.4409, Q Loss: 116329.1420
[IQL] Epoch 27/50, V Loss: 274.0613, Q Loss: 114486.7216
[IQL] Epoch 28/50, V Loss: 236.4382, Q Loss: 114688.6815
[IQL] Epoch 29/50, V Loss: 238.4064, Q Loss: 114051.8445
[IQL] Epoch 30/50, V Loss: 278.5669, Q Loss: 115066.8569
[IQL] Epoch 31/50, V Loss: 247.2319, Q Loss: 113470.7635
[IQL] Epoch 32/50, V Loss: 289.5869, Q Loss: 113887.9641
[IQL] Epoch 33/50, V Loss: 428.7439, Q Loss: 112985.7809
[IQL] Epoch 34/50, V Loss: 294.6582, Q Loss: 112781.2908
[IQL] Epoch 35/50, V Loss: 475.9462, Q Loss: 115070.1509
[IQL] Epoch 36/50, V Loss: 537.7758, Q Loss: 114559.7120
[IQL] Epoch 37/50, V Loss: 478.9322, Q Loss: 113210.5675
[IQL] Epoch 38/50, V Loss: 397.4099, Q Loss: 112373.5366
[IQL] Epoch 39/50, V Loss: 296.2236, Q Loss: 112531.6275
[IQL] Epoch 40/50, V Loss: 214.1454, Q Loss: 113397.8945
[IQL] Epoch 41/50, V Loss: 217.2551, Q Loss: 113438.7344
[IQL] Epoch 42/50, V Loss: 236.8248, Q Loss: 110246.1974
[IQL] Epoch 43/50, V Loss: 322.9654, Q Loss: 113014.9229
[IQL] Epoch 44/50, V Loss: 372.3597, Q Loss: 111943.1925
[IQL] Epoch 45/50, V Loss: 416.4559, Q Loss: 111563.8601
[IQL] Epoch 46/50, V Loss: 335.5054, Q Loss: 111361.3459
[IQL] Epoch 47/50, V Loss: 288.9267, Q Loss: 111875.0366
[IQL] Epoch 48/50, V Loss: 325.8266, Q Loss: 110379.0415
[IQL] Epoch 49/50, V Loss: 400.9082, Q Loss: 111053.3359

[RL100Trainer] Phase 2b: Offline RL Optimization (Iteration 4)
[OPE] Behavior policy value J_old = 607.9909
[Offline RL] Epoch 0/100, PPO Loss: -0.0460, CD Loss: 0.1754
[Offline RL] Epoch 1/100, PPO Loss: -0.0300, CD Loss: 0.2181
[Offline RL] Epoch 2/100, PPO Loss: -0.0312, CD Loss: 0.2028
[Offline RL] Epoch 3/100, PPO Loss: -0.0276, CD Loss: 0.2210
[Offline RL] Epoch 4/100, PPO Loss: -0.0284, CD Loss: 0.2313
[Offline RL] Epoch 5/100, PPO Loss: -0.0246, CD Loss: 0.2268
[Offline RL] Epoch 6/100, PPO Loss: -0.0290, CD Loss: 0.2256
[Offline RL] Epoch 7/100, PPO Loss: -0.0314, CD Loss: 0.2324
[Offline RL] Epoch 8/100, PPO Loss: -0.0272, CD Loss: 0.2300
[Offline RL] Epoch 9/100, PPO Loss: -0.0306, CD Loss: 0.2140
[Offline RL] Epoch 10/100, PPO Loss: -0.0322, CD Loss: 0.2179
[Offline RL] Epoch 11/100, PPO Loss: -0.0301, CD Loss: 0.2303
[Offline RL] Epoch 12/100, PPO Loss: -0.0280, CD Loss: 0.2268
[Offline RL] Epoch 13/100, PPO Loss: -0.0311, CD Loss: 0.2450
[Offline RL] Epoch 14/100, PPO Loss: -0.0284, CD Loss: 0.2366
[Offline RL] Epoch 15/100, PPO Loss: -0.0305, CD Loss: 0.2328
[Offline RL] Epoch 16/100, PPO Loss: -0.0272, CD Loss: 0.2289
[Offline RL] Epoch 17/100, PPO Loss: -0.0283, CD Loss: 0.2386
[Offline RL] Epoch 18/100, PPO Loss: -0.0310, CD Loss: 0.2404
[Offline RL] Epoch 19/100, PPO Loss: -0.0279, CD Loss: 0.2378
[Offline RL] Epoch 20/100, PPO Loss: -0.0277, CD Loss: 0.2301
[Offline RL] Epoch 21/100, PPO Loss: -0.0297, CD Loss: 0.2191
[Offline RL] Epoch 22/100, PPO Loss: -0.0315, CD Loss: 0.2167
[Offline RL] Epoch 23/100, PPO Loss: -0.0335, CD Loss: 0.2201
[Offline RL] Epoch 24/100, PPO Loss: -0.0342, CD Loss: 0.2239
[Offline RL] Epoch 25/100, PPO Loss: -0.0351, CD Loss: 0.2262
[Offline RL] Epoch 26/100, PPO Loss: -0.0357, CD Loss: 0.2366
[Offline RL] Epoch 27/100, PPO Loss: -0.0385, CD Loss: 0.2303
[Offline RL] Epoch 28/100, PPO Loss: -0.0371, CD Loss: 0.2234
[Offline RL] Epoch 29/100, PPO Loss: -0.0372, CD Loss: 0.2180
[Offline RL] Epoch 30/100, PPO Loss: -0.0387, CD Loss: 0.2174
[Offline RL] Epoch 31/100, PPO Loss: -0.0384, CD Loss: 0.2245
[Offline RL] Epoch 32/100, PPO Loss: -0.0406, CD Loss: 0.2294
[Offline RL] Epoch 33/100, PPO Loss: -0.0418, CD Loss: 0.2231
[Offline RL] Epoch 34/100, PPO Loss: -0.0394, CD Loss: 0.2309
[Offline RL] Epoch 35/100, PPO Loss: -0.0412, CD Loss: 0.2253
[Offline RL] Epoch 36/100, PPO Loss: -0.0423, CD Loss: 0.2148
[Offline RL] Epoch 37/100, PPO Loss: -0.0418, CD Loss: 0.2167
[Offline RL] Epoch 38/100, PPO Loss: -0.0426, CD Loss: 0.2171
[Offline RL] Epoch 39/100, PPO Loss: -0.0444, CD Loss: 0.2191
[Offline RL] Epoch 40/100, PPO Loss: -0.0402, CD Loss: 0.2194
[Offline RL] Epoch 41/100, PPO Loss: -0.0398, CD Loss: 0.2275
[Offline RL] Epoch 42/100, PPO Loss: -0.0385, CD Loss: 0.2309
[Offline RL] Epoch 43/100, PPO Loss: -0.0377, CD Loss: 0.2335
[Offline RL] Epoch 44/100, PPO Loss: -0.0390, CD Loss: 0.2359
[Offline RL] Epoch 45/100, PPO Loss: -0.0351, CD Loss: 0.2307
[Offline RL] Epoch 46/100, PPO Loss: -0.0361, CD Loss: 0.2232
[Offline RL] Epoch 47/100, PPO Loss: -0.0333, CD Loss: 0.2331
[Offline RL] Epoch 48/100, PPO Loss: -0.0307, CD Loss: 0.2440
[Offline RL] Epoch 49/100, PPO Loss: -0.0335, CD Loss: 0.2522
[Offline RL] Epoch 50/100, PPO Loss: -0.0340, CD Loss: 0.2520
[Offline RL] Epoch 51/100, PPO Loss: -0.0311, CD Loss: 0.2494
[Offline RL] Epoch 52/100, PPO Loss: -0.0326, CD Loss: 0.2476
[Offline RL] Epoch 53/100, PPO Loss: -0.0324, CD Loss: 0.2438
[Offline RL] Epoch 54/100, PPO Loss: -0.0353, CD Loss: 0.2420
[Offline RL] Epoch 55/100, PPO Loss: -0.0347, CD Loss: 0.2376
[Offline RL] Epoch 56/100, PPO Loss: -0.0334, CD Loss: 0.2318
[Offline RL] Epoch 57/100, PPO Loss: -0.0340, CD Loss: 0.2421
[Offline RL] Epoch 58/100, PPO Loss: -0.0339, CD Loss: 0.2475
[Offline RL] Epoch 59/100, PPO Loss: -0.0338, CD Loss: 0.2435
[Offline RL] Epoch 60/100, PPO Loss: -0.0325, CD Loss: 0.2385
[Offline RL] Epoch 61/100, PPO Loss: -0.0334, CD Loss: 0.2304
[Offline RL] Epoch 62/100, PPO Loss: -0.0321, CD Loss: 0.2303
[Offline RL] Epoch 63/100, PPO Loss: -0.0290, CD Loss: 0.2296
[Offline RL] Epoch 64/100, PPO Loss: -0.0263, CD Loss: 0.2344
[Offline RL] Epoch 65/100, PPO Loss: -0.0300, CD Loss: 0.2409
[Offline RL] Epoch 66/100, PPO Loss: -0.0285, CD Loss: 0.2420
[Offline RL] Epoch 67/100, PPO Loss: -0.0275, CD Loss: 0.2345
[Offline RL] Epoch 68/100, PPO Loss: -0.0280, CD Loss: 0.2316
[Offline RL] Epoch 69/100, PPO Loss: -0.0277, CD Loss: 0.2240
[Offline RL] Epoch 70/100, PPO Loss: -0.0298, CD Loss: 0.2260
[Offline RL] Epoch 71/100, PPO Loss: -0.0298, CD Loss: 0.2202
[Offline RL] Epoch 72/100, PPO Loss: -0.0296, CD Loss: 0.2186
[Offline RL] Epoch 73/100, PPO Loss: -0.0248, CD Loss: 0.2117
[Offline RL] Epoch 74/100, PPO Loss: -0.0260, CD Loss: 0.2066
[Offline RL] Epoch 75/100, PPO Loss: -0.0274, CD Loss: 0.2088
[Offline RL] Epoch 76/100, PPO Loss: -0.0274, CD Loss: 0.2094
[Offline RL] Epoch 77/100, PPO Loss: -0.0294, CD Loss: 0.2099
[Offline RL] Epoch 78/100, PPO Loss: -0.0238, CD Loss: 0.2232
[Offline RL] Epoch 79/100, PPO Loss: -0.0279, CD Loss: 0.2214
[Offline RL] Epoch 80/100, PPO Loss: -0.0275, CD Loss: 0.2262
[Offline RL] Epoch 81/100, PPO Loss: -0.0280, CD Loss: 0.2326
[Offline RL] Epoch 82/100, PPO Loss: -0.0267, CD Loss: 0.2337
[Offline RL] Epoch 83/100, PPO Loss: -0.0256, CD Loss: 0.2335
[Offline RL] Epoch 84/100, PPO Loss: -0.0274, CD Loss: 0.2335
[Offline RL] Epoch 85/100, PPO Loss: -0.0247, CD Loss: 0.2364
[Offline RL] Epoch 86/100, PPO Loss: -0.0258, CD Loss: 0.2454
[Offline RL] Epoch 87/100, PPO Loss: -0.0276, CD Loss: 0.2459
[Offline RL] Epoch 88/100, PPO Loss: -0.0244, CD Loss: 0.2399
[Offline RL] Epoch 89/100, PPO Loss: -0.0259, CD Loss: 0.2306
[Offline RL] Epoch 90/100, PPO Loss: -0.0242, CD Loss: 0.2248
[Offline RL] Epoch 91/100, PPO Loss: -0.0244, CD Loss: 0.2361
[Offline RL] Epoch 92/100, PPO Loss: -0.0246, CD Loss: 0.2353
[Offline RL] Epoch 93/100, PPO Loss: -0.0209, CD Loss: 0.2238
[Offline RL] Epoch 94/100, PPO Loss: -0.0218, CD Loss: 0.2219
[Offline RL] Epoch 95/100, PPO Loss: -0.0233, CD Loss: 0.2275
[Offline RL] Epoch 96/100, PPO Loss: -0.0247, CD Loss: 0.2334
[Offline RL] Epoch 97/100, PPO Loss: -0.0248, CD Loss: 0.2275
[Offline RL] Epoch 98/100, PPO Loss: -0.0275, CD Loss: 0.2178
[Offline RL] Epoch 99/100, PPO Loss: -0.0264, CD Loss: 0.2174
[OPE] Policy REJECTED: J_new=600.2727 ≤ J_old=607.9909 + δ=30.3995. Rolling back to behavior policy.

[RL100Trainer] Phase 2c: Collecting New Data (Iteration 4)
[Collect] 50 episodes, success=0.600, steps=1250
[Data Collection] Success Rate: 0.600, Reward: 11985.84, Episodes: 50, Steps: 1250
[Dataset] Merged 50 episodes (1250 steps) → total 8250 steps, 260 episodes

[RL100Trainer] Retraining IL on merged dataset...

============================================================
[RL100Trainer] Phase 1: Imitation Learning
============================================================

[IL] Epoch 0/100, Loss: 0.0365
[IL] Epoch 1/100, Loss: 0.0381
[IL] Epoch 2/100, Loss: 0.0368
[IL] Epoch 3/100, Loss: 0.0377
[IL] Epoch 4/100, Loss: 0.0374
[IL] Epoch 5/100, Loss: 0.0399
[IL] Epoch 6/100, Loss: 0.0397
[IL] Epoch 7/100, Loss: 0.0364
[IL] Epoch 8/100, Loss: 0.0329
[IL] Epoch 9/100, Loss: 0.0335
[IL] Epoch 10/100, Loss: 0.0365
[IL] Epoch 11/100, Loss: 0.0362
[IL] Epoch 12/100, Loss: 0.0333
[IL] Epoch 13/100, Loss: 0.0344
[IL] Epoch 14/100, Loss: 0.0336
[IL] Epoch 15/100, Loss: 0.0326
[IL] Epoch 16/100, Loss: 0.0328
[IL] Epoch 17/100, Loss: 0.0333
[IL] Epoch 18/100, Loss: 0.0320
[IL] Epoch 19/100, Loss: 0.0322
[IL] Epoch 20/100, Loss: 0.0328
[IL] Epoch 21/100, Loss: 0.0348
[IL] Epoch 22/100, Loss: 0.0308
[IL] Epoch 23/100, Loss: 0.0314
[IL] Epoch 24/100, Loss: 0.0306
[IL] Epoch 25/100, Loss: 0.0319
[IL] Epoch 26/100, Loss: 0.0329
[IL] Epoch 27/100, Loss: 0.0310
[IL] Epoch 28/100, Loss: 0.0287
[IL] Epoch 29/100, Loss: 0.0319
[IL] Epoch 30/100, Loss: 0.0317
[IL] Epoch 31/100, Loss: 0.0324
[IL] Epoch 32/100, Loss: 0.0321
[IL] Epoch 33/100, Loss: 0.0334
[IL] Epoch 34/100, Loss: 0.0330
[IL] Epoch 35/100, Loss: 0.0301
[IL] Epoch 36/100, Loss: 0.0310
[IL] Epoch 37/100, Loss: 0.0314
[IL] Epoch 38/100, Loss: 0.0314
[IL] Epoch 39/100, Loss: 0.0318
[IL] Epoch 40/100, Loss: 0.0299
[IL] Epoch 41/100, Loss: 0.0342
[IL] Epoch 42/100, Loss: 0.0315
[IL] Epoch 43/100, Loss: 0.0310
[IL] Epoch 44/100, Loss: 0.0288
[IL] Epoch 45/100, Loss: 0.0277
[IL] Epoch 46/100, Loss: 0.0288
[IL] Epoch 47/100, Loss: 0.0295
[IL] Epoch 48/100, Loss: 0.0295
[IL] Epoch 49/100, Loss: 0.0288
[IL] Epoch 50/100, Loss: 0.0317
[IL] Epoch 51/100, Loss: 0.0285
[IL] Epoch 52/100, Loss: 0.0289
[IL] Epoch 53/100, Loss: 0.0294
[IL] Epoch 54/100, Loss: 0.0283
[IL] Epoch 55/100, Loss: 0.0270
[IL] Epoch 56/100, Loss: 0.0286
[IL] Epoch 57/100, Loss: 0.0309
[IL] Epoch 58/100, Loss: 0.0272
[IL] Epoch 59/100, Loss: 0.0308
[IL] Epoch 60/100, Loss: 0.0294
[IL] Epoch 61/100, Loss: 0.0282
[IL] Epoch 62/100, Loss: 0.0298
[IL] Epoch 63/100, Loss: 0.0279
[IL] Epoch 64/100, Loss: 0.0277
[IL] Epoch 65/100, Loss: 0.0265
[IL] Epoch 66/100, Loss: 0.0303
[IL] Epoch 67/100, Loss: 0.0304
[IL] Epoch 68/100, Loss: 0.0312
[IL] Epoch 69/100, Loss: 0.0296
[IL] Epoch 70/100, Loss: 0.0292
[IL] Epoch 71/100, Loss: 0.0300
[IL] Epoch 72/100, Loss: 0.0296
[IL] Epoch 73/100, Loss: 0.0307
[IL] Epoch 74/100, Loss: 0.0285
[IL] Epoch 75/100, Loss: 0.0286
[IL] Epoch 76/100, Loss: 0.0269
[IL] Epoch 77/100, Loss: 0.0252
[IL] Epoch 78/100, Loss: 0.0268
[IL] Epoch 79/100, Loss: 0.0279
[IL] Epoch 80/100, Loss: 0.0279
[IL] Epoch 81/100, Loss: 0.0270
[IL] Epoch 82/100, Loss: 0.0271
[IL] Epoch 83/100, Loss: 0.0280
[IL] Epoch 84/100, Loss: 0.0279
[IL] Epoch 85/100, Loss: 0.0274
[IL] Epoch 86/100, Loss: 0.0273
[IL] Epoch 87/100, Loss: 0.0251
[IL] Epoch 88/100, Loss: 0.0253
[IL] Epoch 89/100, Loss: 0.0242
[IL] Epoch 90/100, Loss: 0.0253
[IL] Epoch 91/100, Loss: 0.0266
[IL] Epoch 92/100, Loss: 0.0257
[IL] Epoch 93/100, Loss: 0.0261
[IL] Epoch 94/100, Loss: 0.0239
[IL] Epoch 95/100, Loss: 0.0251
[IL] Epoch 96/100, Loss: 0.0251
[IL] Epoch 97/100, Loss: 0.0261
[IL] Epoch 98/100, Loss: 0.0269
[IL] Epoch 99/100, Loss: 0.0286
test_mean_score: 0.75
[IL] Eval - Success Rate: 0.750
[Checkpoint] Saved to /nfs_global/S/yangrongzheng/RL100/3D-Diffusion-Policy/3D-Diffusion-Policy/checkpoints/offline_iter_4.ckpt

================================================================================
                         TRAINING COMPLETE!
================================================================================

[Checkpoint] Saved to /nfs_global/S/yangrongzheng/RL100/3D-Diffusion-Policy/3D-Diffusion-Policy/checkpoints/final.ckpt

[Evaluation] Running final evaluation...
test_mean_score: 0.7

================================================================================
                         FINAL RESULTS
================================================================================
mean_traj_rewards: 13600.8065
mean_success_rates: 0.7000
test_mean_score: 0.7000
SR_test_L3: 0.6833
SR_test_L5: 0.6100

[Training] Complete! Checkpoints saved to:
  /nfs_global/S/yangrongzheng/RL100/3D-Diffusion-Policy/3D-Diffusion-Policy/checkpoints
Found 8 GPUs for rendering. Using device 0.
Extracting GPU stats logs using atop has been completed on r8l40-a02.
Logs are being saved to: /nfs_global/S/yangrongzheng/atop-736093-r8l40-a02-gpustat.log
Job end at 2026-03-09 06:27:38
