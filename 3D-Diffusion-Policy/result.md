Job start at 2026-03-10 10:38:28
Job run at:
   Static hostname: localhost.localdomain
Transient hostname: r8l40s-a11
         Icon name: computer-server
           Chassis: server
        Machine ID: 6d64668955af443ca689bb9c980cae79
           Boot ID: 4f8b0fdd05674adb8a39f9342b0eacdd
  Operating System: Rocky Linux 8.7 (Green Obsidian)
       CPE OS Name: cpe:/o:rocky:rocky:8:GA
            Kernel: Linux 4.18.0-425.10.1.el8_7.x86_64
      Architecture: x86-64
Filesystem                                        Size  Used Avail Use% Mounted on
/dev/mapper/rl-root                               376G   30G  347G   8% /
/dev/nvme1n1p1                                    1.8T   13G  1.8T   1% /tmp
/dev/nvme0n1p2                                    2.0G  367M  1.7G  18% /boot
/dev/nvme2n1p1                                    3.5T   25G  3.5T   1% /local
/dev/mapper/rl-var                                512G   26G  487G   5% /var
/dev/nvme0n1p1                                    599M  5.8M  594M   1% /boot/efi
/dev/nvme1n1p2                                    1.8T   14G  1.8T   1% /local/nfscache
ssd.nas00.future.cn:/rocky8_home                   16G   15G  1.9G  89% /home
ssd.nas00.future.cn:/rocky8_workspace             400G     0  400G   0% /workspace
ssd.nas00.future.cn:/rocky8_tools                 5.0T   99G  5.0T   2% /tools
ssd.nas00.future.cn:/centos7_home                  16G  4.2G   12G  26% /centos7/home
ssd.nas00.future.cn:/centos7_workspace            400G     0  400G   0% /centos7/workspace
ssd.nas00.future.cn:/centos7_tools                5.0T  235G  4.8T   5% /centos7/tools
ssd.nas00.future.cn:/eda-tools                    8.0T  6.3T  1.8T  79% /centos7/eda-tools
hdd.nas00.future.cn:/share_personal               500G     0  500G   0% /share/personal
zone05.nas01.future.cn:/NAS_HPC_collab_codemodel   40T   37T  3.7T  91% /share/collab/codemodel
ext-zone00.nas02.future.cn:/nfs_global            404T  389T   15T  97% /nfs_global
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
          /home  14445M  16384M  20480M            168k       0       0        

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
NVIDIA L40S, 570.124.06, 325.00 W
NVIDIA L40S, 570.124.06, 325.00 W
NVIDIA L40S, 570.124.06, 325.00 W
NVIDIA L40S, 570.124.06, 325.00 W
NVIDIA L40S, 570.124.06, 325.00 W
NVIDIA L40S, 570.124.06, 325.00 W
NVIDIA L40S, 570.124.06, 325.00 W
NVIDIA L40S, 570.124.06, 325.00 W
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
  beta_recon: 1.0
  beta_kl: 0.001
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
  critic_epochs: 150
  ppo_epochs: 100
  ppo_inner_steps: 4
  collection_episodes: 50
  cd_every: 5
  rl_policy_lr: 1.0e-05
  run_online_rl: false
  online_rl_iterations: 10
  online_collection_episodes: 20
  gradient_accumulate_every: 1
  max_grad_norm: 1.0
  log_every: 10
  eval_every: 100
  checkpoint_every: 200
  resume: false
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
[2026-03-10 10:39:12,190][diffusion_policy_3d.model.diffusion.conditional_unet1d][INFO] - number of parameters: 2.550744e+08
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
[2026-03-10 10:39:14,673][diffusion_policy_3d.model.diffusion.conditional_unet1d][INFO] - number of parameters: 2.550744e+08
[RL100Trainer] Initializing Transition Model T_θ(s'|s,a)...
[Setup] RL100Trainer initialized

[Training] Starting RL-100 pipeline...

================================================================================
                    RL-100 TRAINING PIPELINE
================================================================================


============================================================
[RL100Trainer] Phase 1: Imitation Learning
============================================================

[IL] Epoch 0/1000, Loss: 1.4012
[IL] Epoch 1/1000, Loss: 1.0213
[IL] Epoch 2/1000, Loss: 0.9956
[IL] Epoch 3/1000, Loss: 0.9800
[IL] Epoch 4/1000, Loss: 0.9310
[IL] Epoch 5/1000, Loss: 0.7587
[IL] Epoch 6/1000, Loss: 0.4621
[IL] Epoch 7/1000, Loss: 0.3875
[IL] Epoch 8/1000, Loss: 0.2571
[IL] Epoch 9/1000, Loss: 0.2066
[IL] Epoch 10/1000, Loss: 0.1760
[IL] Epoch 11/1000, Loss: 0.1581
[IL] Epoch 12/1000, Loss: 0.1441
[IL] Epoch 13/1000, Loss: 0.1256
[IL] Epoch 14/1000, Loss: 0.1192
[IL] Epoch 15/1000, Loss: 0.1091
[IL] Epoch 16/1000, Loss: 0.1029
[IL] Epoch 17/1000, Loss: 0.0952
[IL] Epoch 18/1000, Loss: 0.0903
[IL] Epoch 19/1000, Loss: 0.0812
[IL] Epoch 20/1000, Loss: 0.0804
[IL] Epoch 21/1000, Loss: 0.0782
[IL] Epoch 22/1000, Loss: 0.0742
[IL] Epoch 23/1000, Loss: 0.0757
[IL] Epoch 24/1000, Loss: 0.0729
[IL] Epoch 25/1000, Loss: 0.0707
[IL] Epoch 26/1000, Loss: 0.0683
[IL] Epoch 27/1000, Loss: 0.0636
[IL] Epoch 28/1000, Loss: 0.0636
[IL] Epoch 29/1000, Loss: 0.0672
[IL] Epoch 30/1000, Loss: 0.0638
[IL] Epoch 31/1000, Loss: 0.0637
[IL] Epoch 32/1000, Loss: 0.0599
[IL] Epoch 33/1000, Loss: 0.0593
[IL] Epoch 34/1000, Loss: 0.0627
[IL] Epoch 35/1000, Loss: 0.0604
[IL] Epoch 36/1000, Loss: 0.0558
[IL] Epoch 37/1000, Loss: 0.0547
[IL] Epoch 38/1000, Loss: 0.0566
[IL] Epoch 39/1000, Loss: 0.0536
[IL] Epoch 40/1000, Loss: 0.0533
[IL] Epoch 41/1000, Loss: 0.0508
[IL] Epoch 42/1000, Loss: 0.0536
[IL] Epoch 43/1000, Loss: 0.0526
[IL] Epoch 44/1000, Loss: 0.0498
[IL] Epoch 45/1000, Loss: 0.0490
[IL] Epoch 46/1000, Loss: 0.0526
[IL] Epoch 47/1000, Loss: 0.0530
[IL] Epoch 48/1000, Loss: 0.0512
[IL] Epoch 49/1000, Loss: 0.0496
[IL] Epoch 50/1000, Loss: 0.0460
[IL] Epoch 51/1000, Loss: 0.0455
[IL] Epoch 52/1000, Loss: 0.0433
[IL] Epoch 53/1000, Loss: 0.0459
[IL] Epoch 54/1000, Loss: 0.0463
[IL] Epoch 55/1000, Loss: 0.0438
[IL] Epoch 56/1000, Loss: 0.0440
[IL] Epoch 57/1000, Loss: 0.0428
[IL] Epoch 58/1000, Loss: 0.0446
[IL] Epoch 59/1000, Loss: 0.0423
[IL] Epoch 60/1000, Loss: 0.0452
[IL] Epoch 61/1000, Loss: 0.0445
[IL] Epoch 62/1000, Loss: 0.0420
[IL] Epoch 63/1000, Loss: 0.0418
[IL] Epoch 64/1000, Loss: 0.0408
[IL] Epoch 65/1000, Loss: 0.0415
[IL] Epoch 66/1000, Loss: 0.0392
[IL] Epoch 67/1000, Loss: 0.0405
[IL] Epoch 68/1000, Loss: 0.0417
[IL] Epoch 69/1000, Loss: 0.0405
[IL] Epoch 70/1000, Loss: 0.0392
[IL] Epoch 71/1000, Loss: 0.0403
[IL] Epoch 72/1000, Loss: 0.0388
[IL] Epoch 73/1000, Loss: 0.0404
[IL] Epoch 74/1000, Loss: 0.0382
[IL] Epoch 75/1000, Loss: 0.0381
[IL] Epoch 76/1000, Loss: 0.0369
[IL] Epoch 77/1000, Loss: 0.0358
[IL] Epoch 78/1000, Loss: 0.0358
[IL] Epoch 79/1000, Loss: 0.0375
[IL] Epoch 80/1000, Loss: 0.0369
[IL] Epoch 81/1000, Loss: 0.0372
[IL] Epoch 82/1000, Loss: 0.0364
[IL] Epoch 83/1000, Loss: 0.0380
[IL] Epoch 84/1000, Loss: 0.0366
[IL] Epoch 85/1000, Loss: 0.0370
[IL] Epoch 86/1000, Loss: 0.0396
[IL] Epoch 87/1000, Loss: 0.0353
[IL] Epoch 88/1000, Loss: 0.0358
[IL] Epoch 89/1000, Loss: 0.0352
[IL] Epoch 90/1000, Loss: 0.0340
[IL] Epoch 91/1000, Loss: 0.0336
[IL] Epoch 92/1000, Loss: 0.0341
[IL] Epoch 93/1000, Loss: 0.0320
[IL] Epoch 94/1000, Loss: 0.0317
[IL] Epoch 95/1000, Loss: 0.0330
[IL] Epoch 96/1000, Loss: 0.0342
[IL] Epoch 97/1000, Loss: 0.0317
[IL] Epoch 98/1000, Loss: 0.0346
[IL] Epoch 99/1000, Loss: 0.0334
test_mean_score: 0.2
[IL] Eval - Success Rate: 0.200
[IL] Epoch 100/1000, Loss: 0.0319
[IL] Epoch 101/1000, Loss: 0.0353
[IL] Epoch 102/1000, Loss: 0.0346
[IL] Epoch 103/1000, Loss: 0.0354
[IL] Epoch 104/1000, Loss: 0.0340
[IL] Epoch 105/1000, Loss: 0.0305
[IL] Epoch 106/1000, Loss: 0.0323
[IL] Epoch 107/1000, Loss: 0.0306
[IL] Epoch 108/1000, Loss: 0.0311
[IL] Epoch 109/1000, Loss: 0.0317
[IL] Epoch 110/1000, Loss: 0.0335
[IL] Epoch 111/1000, Loss: 0.0316
[IL] Epoch 112/1000, Loss: 0.0311
[IL] Epoch 113/1000, Loss: 0.0309
[IL] Epoch 114/1000, Loss: 0.0295
[IL] Epoch 115/1000, Loss: 0.0296
[IL] Epoch 116/1000, Loss: 0.0294
[IL] Epoch 117/1000, Loss: 0.0287
[IL] Epoch 118/1000, Loss: 0.0302
[IL] Epoch 119/1000, Loss: 0.0294
[IL] Epoch 120/1000, Loss: 0.0287
[IL] Epoch 121/1000, Loss: 0.0301
[IL] Epoch 122/1000, Loss: 0.0278
[IL] Epoch 123/1000, Loss: 0.0288
[IL] Epoch 124/1000, Loss: 0.0286
[IL] Epoch 125/1000, Loss: 0.0273
[IL] Epoch 126/1000, Loss: 0.0269
[IL] Epoch 127/1000, Loss: 0.0264
[IL] Epoch 128/1000, Loss: 0.0270
[IL] Epoch 129/1000, Loss: 0.0285
[IL] Epoch 130/1000, Loss: 0.0287
[IL] Epoch 131/1000, Loss: 0.0282
[IL] Epoch 132/1000, Loss: 0.0277
[IL] Epoch 133/1000, Loss: 0.0287
[IL] Epoch 134/1000, Loss: 0.0294
[IL] Epoch 135/1000, Loss: 0.0280
[IL] Epoch 136/1000, Loss: 0.0280
[IL] Epoch 137/1000, Loss: 0.0274
[IL] Epoch 138/1000, Loss: 0.0260
[IL] Epoch 139/1000, Loss: 0.0277
[IL] Epoch 140/1000, Loss: 0.0263
[IL] Epoch 141/1000, Loss: 0.0260
[IL] Epoch 142/1000, Loss: 0.0301
[IL] Epoch 143/1000, Loss: 0.0278
[IL] Epoch 144/1000, Loss: 0.0261
[IL] Epoch 145/1000, Loss: 0.0285
[IL] Epoch 146/1000, Loss: 0.0257
[IL] Epoch 147/1000, Loss: 0.0257
[IL] Epoch 148/1000, Loss: 0.0260
[IL] Epoch 149/1000, Loss: 0.0242
[IL] Epoch 150/1000, Loss: 0.0263
[IL] Epoch 151/1000, Loss: 0.0273
[IL] Epoch 152/1000, Loss: 0.0253
[IL] Epoch 153/1000, Loss: 0.0257
[IL] Epoch 154/1000, Loss: 0.0241
[IL] Epoch 155/1000, Loss: 0.0254
[IL] Epoch 156/1000, Loss: 0.0253
[IL] Epoch 157/1000, Loss: 0.0268
[IL] Epoch 158/1000, Loss: 0.0256
[IL] Epoch 159/1000, Loss: 0.0245
[IL] Epoch 160/1000, Loss: 0.0248
[IL] Epoch 161/1000, Loss: 0.0232
[IL] Epoch 162/1000, Loss: 0.0225
[IL] Epoch 163/1000, Loss: 0.0259
[IL] Epoch 164/1000, Loss: 0.0233
[IL] Epoch 165/1000, Loss: 0.0230
[IL] Epoch 166/1000, Loss: 0.0230
[IL] Epoch 167/1000, Loss: 0.0235
[IL] Epoch 168/1000, Loss: 0.0243
[IL] Epoch 169/1000, Loss: 0.0247
[IL] Epoch 170/1000, Loss: 0.0251
[IL] Epoch 171/1000, Loss: 0.0231
[IL] Epoch 172/1000, Loss: 0.0222
[IL] Epoch 173/1000, Loss: 0.0228
[IL] Epoch 174/1000, Loss: 0.0212
[IL] Epoch 175/1000, Loss: 0.0221
[IL] Epoch 176/1000, Loss: 0.0228
[IL] Epoch 177/1000, Loss: 0.0210
[IL] Epoch 178/1000, Loss: 0.0218
[IL] Epoch 179/1000, Loss: 0.0225
[IL] Epoch 180/1000, Loss: 0.0220
[IL] Epoch 181/1000, Loss: 0.0220
[IL] Epoch 182/1000, Loss: 0.0221
[IL] Epoch 183/1000, Loss: 0.0214
[IL] Epoch 184/1000, Loss: 0.0231
[IL] Epoch 185/1000, Loss: 0.0220
[IL] Epoch 186/1000, Loss: 0.0208
[IL] Epoch 187/1000, Loss: 0.0185
[IL] Epoch 188/1000, Loss: 0.0219
[IL] Epoch 189/1000, Loss: 0.0216
[IL] Epoch 190/1000, Loss: 0.0224
[IL] Epoch 191/1000, Loss: 0.0208
[IL] Epoch 192/1000, Loss: 0.0193
[IL] Epoch 193/1000, Loss: 0.0197
[IL] Epoch 194/1000, Loss: 0.0204
[IL] Epoch 195/1000, Loss: 0.0221
[IL] Epoch 196/1000, Loss: 0.0215
[IL] Epoch 197/1000, Loss: 0.0208
[IL] Epoch 198/1000, Loss: 0.0206
[IL] Epoch 199/1000, Loss: 0.0199
test_mean_score: 0.15
[IL] Eval - Success Rate: 0.150
[IL] Epoch 200/1000, Loss: 0.0218
[IL] Epoch 201/1000, Loss: 0.0216
[IL] Epoch 202/1000, Loss: 0.0212
[IL] Epoch 203/1000, Loss: 0.0218
[IL] Epoch 204/1000, Loss: 0.0196
[IL] Epoch 205/1000, Loss: 0.0210
[IL] Epoch 206/1000, Loss: 0.0207
[IL] Epoch 207/1000, Loss: 0.0213
[IL] Epoch 208/1000, Loss: 0.0195
[IL] Epoch 209/1000, Loss: 0.0203
[IL] Epoch 210/1000, Loss: 0.0214
[IL] Epoch 211/1000, Loss: 0.0208
[IL] Epoch 212/1000, Loss: 0.0200
[IL] Epoch 213/1000, Loss: 0.0193
[IL] Epoch 214/1000, Loss: 0.0173
[IL] Epoch 215/1000, Loss: 0.0183
[IL] Epoch 216/1000, Loss: 0.0188
[IL] Epoch 217/1000, Loss: 0.0178
[IL] Epoch 218/1000, Loss: 0.0201
[IL] Epoch 219/1000, Loss: 0.0188
[IL] Epoch 220/1000, Loss: 0.0190
[IL] Epoch 221/1000, Loss: 0.0211
[IL] Epoch 222/1000, Loss: 0.0200
[IL] Epoch 223/1000, Loss: 0.0197
[IL] Epoch 224/1000, Loss: 0.0173
[IL] Epoch 225/1000, Loss: 0.0193
[IL] Epoch 226/1000, Loss: 0.0203
[IL] Epoch 227/1000, Loss: 0.0197
[IL] Epoch 228/1000, Loss: 0.0193
[IL] Epoch 229/1000, Loss: 0.0191
[IL] Epoch 230/1000, Loss: 0.0182
[IL] Epoch 231/1000, Loss: 0.0194
[IL] Epoch 232/1000, Loss: 0.0177
[IL] Epoch 233/1000, Loss: 0.0181
[IL] Epoch 234/1000, Loss: 0.0180
[IL] Epoch 235/1000, Loss: 0.0169
[IL] Epoch 236/1000, Loss: 0.0177
[IL] Epoch 237/1000, Loss: 0.0185
[IL] Epoch 238/1000, Loss: 0.0183
[IL] Epoch 239/1000, Loss: 0.0185
[IL] Epoch 240/1000, Loss: 0.0194
[IL] Epoch 241/1000, Loss: 0.0186
[IL] Epoch 242/1000, Loss: 0.0167
[IL] Epoch 243/1000, Loss: 0.0173
[IL] Epoch 244/1000, Loss: 0.0183
[IL] Epoch 245/1000, Loss: 0.0177
[IL] Epoch 246/1000, Loss: 0.0193
[IL] Epoch 247/1000, Loss: 0.0182
[IL] Epoch 248/1000, Loss: 0.0188
[IL] Epoch 249/1000, Loss: 0.0170
[IL] Epoch 250/1000, Loss: 0.0191
[IL] Epoch 251/1000, Loss: 0.0170
[IL] Epoch 252/1000, Loss: 0.0178
[IL] Epoch 253/1000, Loss: 0.0171
[IL] Epoch 254/1000, Loss: 0.0153
[IL] Epoch 255/1000, Loss: 0.0173
[IL] Epoch 256/1000, Loss: 0.0187
[IL] Epoch 257/1000, Loss: 0.0179
[IL] Epoch 258/1000, Loss: 0.0166
[IL] Epoch 259/1000, Loss: 0.0179
[IL] Epoch 260/1000, Loss: 0.0175
[IL] Epoch 261/1000, Loss: 0.0169
[IL] Epoch 262/1000, Loss: 0.0166
[IL] Epoch 263/1000, Loss: 0.0166
[IL] Epoch 264/1000, Loss: 0.0156
[IL] Epoch 265/1000, Loss: 0.0174
[IL] Epoch 266/1000, Loss: 0.0146
[IL] Epoch 267/1000, Loss: 0.0155
[IL] Epoch 268/1000, Loss: 0.0149
[IL] Epoch 269/1000, Loss: 0.0158
[IL] Epoch 270/1000, Loss: 0.0176
[IL] Epoch 271/1000, Loss: 0.0165
[IL] Epoch 272/1000, Loss: 0.0159
[IL] Epoch 273/1000, Loss: 0.0163
[IL] Epoch 274/1000, Loss: 0.0149
[IL] Epoch 275/1000, Loss: 0.0165
[IL] Epoch 276/1000, Loss: 0.0164
[IL] Epoch 277/1000, Loss: 0.0157
[IL] Epoch 278/1000, Loss: 0.0165
[IL] Epoch 279/1000, Loss: 0.0161
[IL] Epoch 280/1000, Loss: 0.0167
[IL] Epoch 281/1000, Loss: 0.0172
[IL] Epoch 282/1000, Loss: 0.0158
[IL] Epoch 283/1000, Loss: 0.0165
[IL] Epoch 284/1000, Loss: 0.0169
[IL] Epoch 285/1000, Loss: 0.0178
[IL] Epoch 286/1000, Loss: 0.0178
[IL] Epoch 287/1000, Loss: 0.0166
[IL] Epoch 288/1000, Loss: 0.0168
[IL] Epoch 289/1000, Loss: 0.0167
[IL] Epoch 290/1000, Loss: 0.0162
[IL] Epoch 291/1000, Loss: 0.0156
[IL] Epoch 292/1000, Loss: 0.0144
[IL] Epoch 293/1000, Loss: 0.0157
[IL] Epoch 294/1000, Loss: 0.0180
[IL] Epoch 295/1000, Loss: 0.0158
[IL] Epoch 296/1000, Loss: 0.0152
[IL] Epoch 297/1000, Loss: 0.0156
[IL] Epoch 298/1000, Loss: 0.0149
[IL] Epoch 299/1000, Loss: 0.0150
test_mean_score: 0.15
[IL] Eval - Success Rate: 0.150
[IL] Epoch 300/1000, Loss: 0.0160
[IL] Epoch 301/1000, Loss: 0.0163
[IL] Epoch 302/1000, Loss: 0.0160
[IL] Epoch 303/1000, Loss: 0.0144
[IL] Epoch 304/1000, Loss: 0.0145
[IL] Epoch 305/1000, Loss: 0.0148
[IL] Epoch 306/1000, Loss: 0.0151
[IL] Epoch 307/1000, Loss: 0.0146
[IL] Epoch 308/1000, Loss: 0.0147
[IL] Epoch 309/1000, Loss: 0.0142
[IL] Epoch 310/1000, Loss: 0.0141
[IL] Epoch 311/1000, Loss: 0.0149
[IL] Epoch 312/1000, Loss: 0.0141
[IL] Epoch 313/1000, Loss: 0.0149
[IL] Epoch 314/1000, Loss: 0.0140
[IL] Epoch 315/1000, Loss: 0.0149
[IL] Epoch 316/1000, Loss: 0.0139
[IL] Epoch 317/1000, Loss: 0.0146
[IL] Epoch 318/1000, Loss: 0.0140
[IL] Epoch 319/1000, Loss: 0.0138
[IL] Epoch 320/1000, Loss: 0.0147
[IL] Epoch 321/1000, Loss: 0.0158
[IL] Epoch 322/1000, Loss: 0.0143
[IL] Epoch 323/1000, Loss: 0.0144
[IL] Epoch 324/1000, Loss: 0.0148
[IL] Epoch 325/1000, Loss: 0.0144
[IL] Epoch 326/1000, Loss: 0.0143
[IL] Epoch 327/1000, Loss: 0.0159
[IL] Epoch 328/1000, Loss: 0.0166
[IL] Epoch 329/1000, Loss: 0.0164
[IL] Epoch 330/1000, Loss: 0.0159
[IL] Epoch 331/1000, Loss: 0.0162
[IL] Epoch 332/1000, Loss: 0.0151
[IL] Epoch 333/1000, Loss: 0.0150
[IL] Epoch 334/1000, Loss: 0.0135
[IL] Epoch 335/1000, Loss: 0.0144
[IL] Epoch 336/1000, Loss: 0.0145
[IL] Epoch 337/1000, Loss: 0.0146
[IL] Epoch 338/1000, Loss: 0.0143
[IL] Epoch 339/1000, Loss: 0.0126
[IL] Epoch 340/1000, Loss: 0.0146
[IL] Epoch 341/1000, Loss: 0.0142
[IL] Epoch 342/1000, Loss: 0.0144
[IL] Epoch 343/1000, Loss: 0.0150
[IL] Epoch 344/1000, Loss: 0.0141
[IL] Epoch 345/1000, Loss: 0.0126
[IL] Epoch 346/1000, Loss: 0.0143
[IL] Epoch 347/1000, Loss: 0.0139
[IL] Epoch 348/1000, Loss: 0.0144
[IL] Epoch 349/1000, Loss: 0.0133
[IL] Epoch 350/1000, Loss: 0.0151
[IL] Epoch 351/1000, Loss: 0.0145
[IL] Epoch 352/1000, Loss: 0.0132
[IL] Epoch 353/1000, Loss: 0.0140
[IL] Epoch 354/1000, Loss: 0.0142
[IL] Epoch 355/1000, Loss: 0.0150
[IL] Epoch 356/1000, Loss: 0.0141
[IL] Epoch 357/1000, Loss: 0.0133
[IL] Epoch 358/1000, Loss: 0.0137
[IL] Epoch 359/1000, Loss: 0.0149
[IL] Epoch 360/1000, Loss: 0.0145
[IL] Epoch 361/1000, Loss: 0.0137
[IL] Epoch 362/1000, Loss: 0.0130
[IL] Epoch 363/1000, Loss: 0.0135
[IL] Epoch 364/1000, Loss: 0.0124
[IL] Epoch 365/1000, Loss: 0.0120
[IL] Epoch 366/1000, Loss: 0.0137
[IL] Epoch 367/1000, Loss: 0.0136
[IL] Epoch 368/1000, Loss: 0.0139
[IL] Epoch 369/1000, Loss: 0.0142
[IL] Epoch 370/1000, Loss: 0.0145
[IL] Epoch 371/1000, Loss: 0.0135
[IL] Epoch 372/1000, Loss: 0.0130
[IL] Epoch 373/1000, Loss: 0.0134
[IL] Epoch 374/1000, Loss: 0.0126
[IL] Epoch 375/1000, Loss: 0.0132
[IL] Epoch 376/1000, Loss: 0.0133
[IL] Epoch 377/1000, Loss: 0.0137
[IL] Epoch 378/1000, Loss: 0.0128
[IL] Epoch 379/1000, Loss: 0.0126
[IL] Epoch 380/1000, Loss: 0.0124
[IL] Epoch 381/1000, Loss: 0.0133
[IL] Epoch 382/1000, Loss: 0.0136
[IL] Epoch 383/1000, Loss: 0.0131
[IL] Epoch 384/1000, Loss: 0.0136
[IL] Epoch 385/1000, Loss: 0.0130
[IL] Epoch 386/1000, Loss: 0.0131
[IL] Epoch 387/1000, Loss: 0.0131
[IL] Epoch 388/1000, Loss: 0.0124
[IL] Epoch 389/1000, Loss: 0.0123
[IL] Epoch 390/1000, Loss: 0.0125
[IL] Epoch 391/1000, Loss: 0.0133
[IL] Epoch 392/1000, Loss: 0.0143
[IL] Epoch 393/1000, Loss: 0.0135
[IL] Epoch 394/1000, Loss: 0.0130
[IL] Epoch 395/1000, Loss: 0.0129
[IL] Epoch 396/1000, Loss: 0.0122
[IL] Epoch 397/1000, Loss: 0.0126
[IL] Epoch 398/1000, Loss: 0.0133
[IL] Epoch 399/1000, Loss: 0.0143
test_mean_score: 0.5
[IL] Eval - Success Rate: 0.500
[IL] Epoch 400/1000, Loss: 0.0131
[IL] Epoch 401/1000, Loss: 0.0130
[IL] Epoch 402/1000, Loss: 0.0119
[IL] Epoch 403/1000, Loss: 0.0122
[IL] Epoch 404/1000, Loss: 0.0137
[IL] Epoch 405/1000, Loss: 0.0131
[IL] Epoch 406/1000, Loss: 0.0131
[IL] Epoch 407/1000, Loss: 0.0130
[IL] Epoch 408/1000, Loss: 0.0122
[IL] Epoch 409/1000, Loss: 0.0116
[IL] Epoch 410/1000, Loss: 0.0119
[IL] Epoch 411/1000, Loss: 0.0126
[IL] Epoch 412/1000, Loss: 0.0117
[IL] Epoch 413/1000, Loss: 0.0122
[IL] Epoch 414/1000, Loss: 0.0115
[IL] Epoch 415/1000, Loss: 0.0114
[IL] Epoch 416/1000, Loss: 0.0109
[IL] Epoch 417/1000, Loss: 0.0127
[IL] Epoch 418/1000, Loss: 0.0122
[IL] Epoch 419/1000, Loss: 0.0119
[IL] Epoch 420/1000, Loss: 0.0110
[IL] Epoch 421/1000, Loss: 0.0117
[IL] Epoch 422/1000, Loss: 0.0135
[IL] Epoch 423/1000, Loss: 0.0136
[IL] Epoch 424/1000, Loss: 0.0134
[IL] Epoch 425/1000, Loss: 0.0124
[IL] Epoch 426/1000, Loss: 0.0123
[IL] Epoch 427/1000, Loss: 0.0124
[IL] Epoch 428/1000, Loss: 0.0127
[IL] Epoch 429/1000, Loss: 0.0115
[IL] Epoch 430/1000, Loss: 0.0119
[IL] Epoch 431/1000, Loss: 0.0112
[IL] Epoch 432/1000, Loss: 0.0122
[IL] Epoch 433/1000, Loss: 0.0114
[IL] Epoch 434/1000, Loss: 0.0114
[IL] Epoch 435/1000, Loss: 0.0115
[IL] Epoch 436/1000, Loss: 0.0125
[IL] Epoch 437/1000, Loss: 0.0130
[IL] Epoch 438/1000, Loss: 0.0130
[IL] Epoch 439/1000, Loss: 0.0139
[IL] Epoch 440/1000, Loss: 0.0133
[IL] Epoch 441/1000, Loss: 0.0127
[IL] Epoch 442/1000, Loss: 0.0121
[IL] Epoch 443/1000, Loss: 0.0124
[IL] Epoch 444/1000, Loss: 0.0113
[IL] Epoch 445/1000, Loss: 0.0119
[IL] Epoch 446/1000, Loss: 0.0112
[IL] Epoch 447/1000, Loss: 0.0114
[IL] Epoch 448/1000, Loss: 0.0104
[IL] Epoch 449/1000, Loss: 0.0113
[IL] Epoch 450/1000, Loss: 0.0124
[IL] Epoch 451/1000, Loss: 0.0117
[IL] Epoch 452/1000, Loss: 0.0114
[IL] Epoch 453/1000, Loss: 0.0122
[IL] Epoch 454/1000, Loss: 0.0107
[IL] Epoch 455/1000, Loss: 0.0114
[IL] Epoch 456/1000, Loss: 0.0125
[IL] Epoch 457/1000, Loss: 0.0117
[IL] Epoch 458/1000, Loss: 0.0111
[IL] Epoch 459/1000, Loss: 0.0109
[IL] Epoch 460/1000, Loss: 0.0116
[IL] Epoch 461/1000, Loss: 0.0104
[IL] Epoch 462/1000, Loss: 0.0110
[IL] Epoch 463/1000, Loss: 0.0117
[IL] Epoch 464/1000, Loss: 0.0108
[IL] Epoch 465/1000, Loss: 0.0103
[IL] Epoch 466/1000, Loss: 0.0109
[IL] Epoch 467/1000, Loss: 0.0107
[IL] Epoch 468/1000, Loss: 0.0117
[IL] Epoch 469/1000, Loss: 0.0128
[IL] Epoch 470/1000, Loss: 0.0122
[IL] Epoch 471/1000, Loss: 0.0116
[IL] Epoch 472/1000, Loss: 0.0103
[IL] Epoch 473/1000, Loss: 0.0102
[IL] Epoch 474/1000, Loss: 0.0105
[IL] Epoch 475/1000, Loss: 0.0114
[IL] Epoch 476/1000, Loss: 0.0116
[IL] Epoch 477/1000, Loss: 0.0114
[IL] Epoch 478/1000, Loss: 0.0105
[IL] Epoch 479/1000, Loss: 0.0096
[IL] Epoch 480/1000, Loss: 0.0096
[IL] Epoch 481/1000, Loss: 0.0106
[IL] Epoch 482/1000, Loss: 0.0108
[IL] Epoch 483/1000, Loss: 0.0124
[IL] Epoch 484/1000, Loss: 0.0116
[IL] Epoch 485/1000, Loss: 0.0112
[IL] Epoch 486/1000, Loss: 0.0116
[IL] Epoch 487/1000, Loss: 0.0116
[IL] Epoch 488/1000, Loss: 0.0104
[IL] Epoch 489/1000, Loss: 0.0103
[IL] Epoch 490/1000, Loss: 0.0108
[IL] Epoch 491/1000, Loss: 0.0109
[IL] Epoch 492/1000, Loss: 0.0120
[IL] Epoch 493/1000, Loss: 0.0117
[IL] Epoch 494/1000, Loss: 0.0109
[IL] Epoch 495/1000, Loss: 0.0118
[IL] Epoch 496/1000, Loss: 0.0102
[IL] Epoch 497/1000, Loss: 0.0120
[IL] Epoch 498/1000, Loss: 0.0116
[IL] Epoch 499/1000, Loss: 0.0121
test_mean_score: 0.55
[IL] Eval - Success Rate: 0.550
[IL] Epoch 500/1000, Loss: 0.0109
[IL] Epoch 501/1000, Loss: 0.0115
[IL] Epoch 502/1000, Loss: 0.0106
[IL] Epoch 503/1000, Loss: 0.0114
[IL] Epoch 504/1000, Loss: 0.0100
[IL] Epoch 505/1000, Loss: 0.0094
[IL] Epoch 506/1000, Loss: 0.0098
[IL] Epoch 507/1000, Loss: 0.0095
[IL] Epoch 508/1000, Loss: 0.0101
[IL] Epoch 509/1000, Loss: 0.0099
[IL] Epoch 510/1000, Loss: 0.0094
[IL] Epoch 511/1000, Loss: 0.0113
[IL] Epoch 512/1000, Loss: 0.0135
[IL] Epoch 513/1000, Loss: 0.0115
[IL] Epoch 514/1000, Loss: 0.0106
[IL] Epoch 515/1000, Loss: 0.0108
[IL] Epoch 516/1000, Loss: 0.0111
[IL] Epoch 517/1000, Loss: 0.0111
[IL] Epoch 518/1000, Loss: 0.0111
[IL] Epoch 519/1000, Loss: 0.0132
[IL] Epoch 520/1000, Loss: 0.0107
[IL] Epoch 521/1000, Loss: 0.0101
[IL] Epoch 522/1000, Loss: 0.0093
[IL] Epoch 523/1000, Loss: 0.0104
[IL] Epoch 524/1000, Loss: 0.0102
[IL] Epoch 525/1000, Loss: 0.0091
[IL] Epoch 526/1000, Loss: 0.0090
[IL] Epoch 527/1000, Loss: 0.0097
[IL] Epoch 528/1000, Loss: 0.0096
[IL] Epoch 529/1000, Loss: 0.0107
[IL] Epoch 530/1000, Loss: 0.0109
[IL] Epoch 531/1000, Loss: 0.0104
[IL] Epoch 532/1000, Loss: 0.0097
[IL] Epoch 533/1000, Loss: 0.0099
[IL] Epoch 534/1000, Loss: 0.0105
[IL] Epoch 535/1000, Loss: 0.0109
[IL] Epoch 536/1000, Loss: 0.0103
[IL] Epoch 537/1000, Loss: 0.0107
[IL] Epoch 538/1000, Loss: 0.0109
[IL] Epoch 539/1000, Loss: 0.0126
[IL] Epoch 540/1000, Loss: 0.0131
[IL] Epoch 541/1000, Loss: 0.0103
[IL] Epoch 542/1000, Loss: 0.0104
[IL] Epoch 543/1000, Loss: 0.0099
[IL] Epoch 544/1000, Loss: 0.0096
[IL] Epoch 545/1000, Loss: 0.0097
[IL] Epoch 546/1000, Loss: 0.0097
[IL] Epoch 547/1000, Loss: 0.0107
[IL] Epoch 548/1000, Loss: 0.0095
[IL] Epoch 549/1000, Loss: 0.0095
[IL] Epoch 550/1000, Loss: 0.0095
[IL] Epoch 551/1000, Loss: 0.0096
[IL] Epoch 552/1000, Loss: 0.0093
[IL] Epoch 553/1000, Loss: 0.0088
[IL] Epoch 554/1000, Loss: 0.0091
[IL] Epoch 555/1000, Loss: 0.0098
[IL] Epoch 556/1000, Loss: 0.0099
[IL] Epoch 557/1000, Loss: 0.0108
[IL] Epoch 558/1000, Loss: 0.0095
[IL] Epoch 559/1000, Loss: 0.0095
[IL] Epoch 560/1000, Loss: 0.0092
[IL] Epoch 561/1000, Loss: 0.0093
[IL] Epoch 562/1000, Loss: 0.0096
[IL] Epoch 563/1000, Loss: 0.0093
[IL] Epoch 564/1000, Loss: 0.0108
[IL] Epoch 565/1000, Loss: 0.0104
[IL] Epoch 566/1000, Loss: 0.0097
[IL] Epoch 567/1000, Loss: 0.0094
[IL] Epoch 568/1000, Loss: 0.0089
[IL] Epoch 569/1000, Loss: 0.0090
[IL] Epoch 570/1000, Loss: 0.0092
[IL] Epoch 571/1000, Loss: 0.0089
[IL] Epoch 572/1000, Loss: 0.0088
[IL] Epoch 573/1000, Loss: 0.0089
[IL] Epoch 574/1000, Loss: 0.0101
[IL] Epoch 575/1000, Loss: 0.0102
[IL] Epoch 576/1000, Loss: 0.0102
[IL] Epoch 577/1000, Loss: 0.0096
[IL] Epoch 578/1000, Loss: 0.0107
[IL] Epoch 579/1000, Loss: 0.0112
[IL] Epoch 580/1000, Loss: 0.0105
[IL] Epoch 581/1000, Loss: 0.0102
[IL] Epoch 582/1000, Loss: 0.0088
[IL] Epoch 583/1000, Loss: 0.0080
[IL] Epoch 584/1000, Loss: 0.0085
[IL] Epoch 585/1000, Loss: 0.0090
[IL] Epoch 586/1000, Loss: 0.0092
[IL] Epoch 587/1000, Loss: 0.0104
[IL] Epoch 588/1000, Loss: 0.0095
[IL] Epoch 589/1000, Loss: 0.0091
[IL] Epoch 590/1000, Loss: 0.0092
[IL] Epoch 591/1000, Loss: 0.0100
[IL] Epoch 592/1000, Loss: 0.0098
[IL] Epoch 593/1000, Loss: 0.0092
[IL] Epoch 594/1000, Loss: 0.0103
[IL] Epoch 595/1000, Loss: 0.0089
[IL] Epoch 596/1000, Loss: 0.0080
[IL] Epoch 597/1000, Loss: 0.0087
[IL] Epoch 598/1000, Loss: 0.0094
[IL] Epoch 599/1000, Loss: 0.0092
test_mean_score: 0.65
[IL] Eval - Success Rate: 0.650
[IL] Epoch 600/1000, Loss: 0.0103
[IL] Epoch 601/1000, Loss: 0.0104
[IL] Epoch 602/1000, Loss: 0.0098
[IL] Epoch 603/1000, Loss: 0.0092
[IL] Epoch 604/1000, Loss: 0.0101
[IL] Epoch 605/1000, Loss: 0.0103
[IL] Epoch 606/1000, Loss: 0.0102
[IL] Epoch 607/1000, Loss: 0.0099
[IL] Epoch 608/1000, Loss: 0.0090
[IL] Epoch 609/1000, Loss: 0.0084
[IL] Epoch 610/1000, Loss: 0.0093
[IL] Epoch 611/1000, Loss: 0.0097
[IL] Epoch 612/1000, Loss: 0.0109
[IL] Epoch 613/1000, Loss: 0.0098
[IL] Epoch 614/1000, Loss: 0.0100
[IL] Epoch 615/1000, Loss: 0.0105
[IL] Epoch 616/1000, Loss: 0.0089
[IL] Epoch 617/1000, Loss: 0.0087
[IL] Epoch 618/1000, Loss: 0.0101
[IL] Epoch 619/1000, Loss: 0.0095
[IL] Epoch 620/1000, Loss: 0.0093
[IL] Epoch 621/1000, Loss: 0.0086
[IL] Epoch 622/1000, Loss: 0.0092
[IL] Epoch 623/1000, Loss: 0.0081
[IL] Epoch 624/1000, Loss: 0.0097
[IL] Epoch 625/1000, Loss: 0.0098
[IL] Epoch 626/1000, Loss: 0.0091
[IL] Epoch 627/1000, Loss: 0.0095
[IL] Epoch 628/1000, Loss: 0.0089
[IL] Epoch 629/1000, Loss: 0.0094
[IL] Epoch 630/1000, Loss: 0.0086
[IL] Epoch 631/1000, Loss: 0.0090
[IL] Epoch 632/1000, Loss: 0.0090
[IL] Epoch 633/1000, Loss: 0.0100
[IL] Epoch 634/1000, Loss: 0.0096
[IL] Epoch 635/1000, Loss: 0.0093
[IL] Epoch 636/1000, Loss: 0.0089
[IL] Epoch 637/1000, Loss: 0.0079
[IL] Epoch 638/1000, Loss: 0.0076
[IL] Epoch 639/1000, Loss: 0.0100
[IL] Epoch 640/1000, Loss: 0.0105
[IL] Epoch 641/1000, Loss: 0.0101
[IL] Epoch 642/1000, Loss: 0.0092
[IL] Epoch 643/1000, Loss: 0.0099
[IL] Epoch 644/1000, Loss: 0.0108
[IL] Epoch 645/1000, Loss: 0.0092
[IL] Epoch 646/1000, Loss: 0.0098
[IL] Epoch 647/1000, Loss: 0.0102
[IL] Epoch 648/1000, Loss: 0.0096
[IL] Epoch 649/1000, Loss: 0.0094
[IL] Epoch 650/1000, Loss: 0.0093
[IL] Epoch 651/1000, Loss: 0.0089
[IL] Epoch 652/1000, Loss: 0.0078
[IL] Epoch 653/1000, Loss: 0.0080
[IL] Epoch 654/1000, Loss: 0.0084
[IL] Epoch 655/1000, Loss: 0.0080
[IL] Epoch 656/1000, Loss: 0.0094
[IL] Epoch 657/1000, Loss: 0.0097
[IL] Epoch 658/1000, Loss: 0.0099
[IL] Epoch 659/1000, Loss: 0.0094
[IL] Epoch 660/1000, Loss: 0.0098
[IL] Epoch 661/1000, Loss: 0.0089
[IL] Epoch 662/1000, Loss: 0.0092
[IL] Epoch 663/1000, Loss: 0.0094
[IL] Epoch 664/1000, Loss: 0.0096
[IL] Epoch 665/1000, Loss: 0.0083
[IL] Epoch 666/1000, Loss: 0.0103
[IL] Epoch 667/1000, Loss: 0.0100
[IL] Epoch 668/1000, Loss: 0.0089
[IL] Epoch 669/1000, Loss: 0.0090
[IL] Epoch 670/1000, Loss: 0.0106
[IL] Epoch 671/1000, Loss: 0.0092
[IL] Epoch 672/1000, Loss: 0.0095
[IL] Epoch 673/1000, Loss: 0.0094
[IL] Epoch 674/1000, Loss: 0.0084
[IL] Epoch 675/1000, Loss: 0.0081
[IL] Epoch 676/1000, Loss: 0.0082
[IL] Epoch 677/1000, Loss: 0.0098
[IL] Epoch 678/1000, Loss: 0.0096
[IL] Epoch 679/1000, Loss: 0.0092
[IL] Epoch 680/1000, Loss: 0.0093
[IL] Epoch 681/1000, Loss: 0.0090
[IL] Epoch 682/1000, Loss: 0.0086
[IL] Epoch 683/1000, Loss: 0.0088
[IL] Epoch 684/1000, Loss: 0.0076
[IL] Epoch 685/1000, Loss: 0.0086
[IL] Epoch 686/1000, Loss: 0.0103
[IL] Epoch 687/1000, Loss: 0.0096
[IL] Epoch 688/1000, Loss: 0.0087
[IL] Epoch 689/1000, Loss: 0.0077
[IL] Epoch 690/1000, Loss: 0.0087
[IL] Epoch 691/1000, Loss: 0.0083
[IL] Epoch 692/1000, Loss: 0.0088
[IL] Epoch 693/1000, Loss: 0.0094
[IL] Epoch 694/1000, Loss: 0.0089
[IL] Epoch 695/1000, Loss: 0.0085
[IL] Epoch 696/1000, Loss: 0.0081
[IL] Epoch 697/1000, Loss: 0.0081
[IL] Epoch 698/1000, Loss: 0.0084
[IL] Epoch 699/1000, Loss: 0.0078
test_mean_score: 0.5
[IL] Eval - Success Rate: 0.500
[IL] Epoch 700/1000, Loss: 0.0075
[IL] Epoch 701/1000, Loss: 0.0081
[IL] Epoch 702/1000, Loss: 0.0085
[IL] Epoch 703/1000, Loss: 0.0078
[IL] Epoch 704/1000, Loss: 0.0087
[IL] Epoch 705/1000, Loss: 0.0091
[IL] Epoch 706/1000, Loss: 0.0090
[IL] Epoch 707/1000, Loss: 0.0089
[IL] Epoch 708/1000, Loss: 0.0080
[IL] Epoch 709/1000, Loss: 0.0076
[IL] Epoch 710/1000, Loss: 0.0078
[IL] Epoch 711/1000, Loss: 0.0072
[IL] Epoch 712/1000, Loss: 0.0081
[IL] Epoch 713/1000, Loss: 0.0072
[IL] Epoch 714/1000, Loss: 0.0070
[IL] Epoch 715/1000, Loss: 0.0083
[IL] Epoch 716/1000, Loss: 0.0089
[IL] Epoch 717/1000, Loss: 0.0086
[IL] Epoch 718/1000, Loss: 0.0083
[IL] Epoch 719/1000, Loss: 0.0080
[IL] Epoch 720/1000, Loss: 0.0080
[IL] Epoch 721/1000, Loss: 0.0076
[IL] Epoch 722/1000, Loss: 0.0082
[IL] Epoch 723/1000, Loss: 0.0081
[IL] Epoch 724/1000, Loss: 0.0087
[IL] Epoch 725/1000, Loss: 0.0083
[IL] Epoch 726/1000, Loss: 0.0087
[IL] Epoch 727/1000, Loss: 0.0084
[IL] Epoch 728/1000, Loss: 0.0082
[IL] Epoch 729/1000, Loss: 0.0087
[IL] Epoch 730/1000, Loss: 0.0084
[IL] Epoch 731/1000, Loss: 0.0082
[IL] Epoch 732/1000, Loss: 0.0085
[IL] Epoch 733/1000, Loss: 0.0081
[IL] Epoch 734/1000, Loss: 0.0080
[IL] Epoch 735/1000, Loss: 0.0089
[IL] Epoch 736/1000, Loss: 0.0082
[IL] Epoch 737/1000, Loss: 0.0089
[IL] Epoch 738/1000, Loss: 0.0082
[IL] Epoch 739/1000, Loss: 0.0086
[IL] Epoch 740/1000, Loss: 0.0090
[IL] Epoch 741/1000, Loss: 0.0088
[IL] Epoch 742/1000, Loss: 0.0094
[IL] Epoch 743/1000, Loss: 0.0091
[IL] Epoch 744/1000, Loss: 0.0106
[IL] Epoch 745/1000, Loss: 0.0097
[IL] Epoch 746/1000, Loss: 0.0081
[IL] Epoch 747/1000, Loss: 0.0073
[IL] Epoch 748/1000, Loss: 0.0091
[IL] Epoch 749/1000, Loss: 0.0087
[IL] Epoch 750/1000, Loss: 0.0083
[IL] Epoch 751/1000, Loss: 0.0070
[IL] Epoch 752/1000, Loss: 0.0085
[IL] Epoch 753/1000, Loss: 0.0080
[IL] Epoch 754/1000, Loss: 0.0080
[IL] Epoch 755/1000, Loss: 0.0074
[IL] Epoch 756/1000, Loss: 0.0066
[IL] Epoch 757/1000, Loss: 0.0088
[IL] Epoch 758/1000, Loss: 0.0079
[IL] Epoch 759/1000, Loss: 0.0080
[IL] Epoch 760/1000, Loss: 0.0083
[IL] Epoch 761/1000, Loss: 0.0080
[IL] Epoch 762/1000, Loss: 0.0076
[IL] Epoch 763/1000, Loss: 0.0069
[IL] Epoch 764/1000, Loss: 0.0072
[IL] Epoch 765/1000, Loss: 0.0070
[IL] Epoch 766/1000, Loss: 0.0075
[IL] Epoch 767/1000, Loss: 0.0079
[IL] Epoch 768/1000, Loss: 0.0077
[IL] Epoch 769/1000, Loss: 0.0084
[IL] Epoch 770/1000, Loss: 0.0080
[IL] Epoch 771/1000, Loss: 0.0085
[IL] Epoch 772/1000, Loss: 0.0091
[IL] Epoch 773/1000, Loss: 0.0081
[IL] Epoch 774/1000, Loss: 0.0079
[IL] Epoch 775/1000, Loss: 0.0083
[IL] Epoch 776/1000, Loss: 0.0076
[IL] Epoch 777/1000, Loss: 0.0081
[IL] Epoch 778/1000, Loss: 0.0085
[IL] Epoch 779/1000, Loss: 0.0089
[IL] Epoch 780/1000, Loss: 0.0091
[IL] Epoch 781/1000, Loss: 0.0088
[IL] Epoch 782/1000, Loss: 0.0080
[IL] Epoch 783/1000, Loss: 0.0076
[IL] Epoch 784/1000, Loss: 0.0074
[IL] Epoch 785/1000, Loss: 0.0073
[IL] Epoch 786/1000, Loss: 0.0084
[IL] Epoch 787/1000, Loss: 0.0076
[IL] Epoch 788/1000, Loss: 0.0074
[IL] Epoch 789/1000, Loss: 0.0087
[IL] Epoch 790/1000, Loss: 0.0082
[IL] Epoch 791/1000, Loss: 0.0084
[IL] Epoch 792/1000, Loss: 0.0075
[IL] Epoch 793/1000, Loss: 0.0068
[IL] Epoch 794/1000, Loss: 0.0080
[IL] Epoch 795/1000, Loss: 0.0082
[IL] Epoch 796/1000, Loss: 0.0086
[IL] Epoch 797/1000, Loss: 0.0077
[IL] Epoch 798/1000, Loss: 0.0078
[IL] Epoch 799/1000, Loss: 0.0073
test_mean_score: 0.6
[IL] Eval - Success Rate: 0.600
[IL] Epoch 800/1000, Loss: 0.0067
[IL] Epoch 801/1000, Loss: 0.0079
[IL] Epoch 802/1000, Loss: 0.0085
[IL] Epoch 803/1000, Loss: 0.0081
[IL] Epoch 804/1000, Loss: 0.0079
[IL] Epoch 805/1000, Loss: 0.0080
[IL] Epoch 806/1000, Loss: 0.0078
[IL] Epoch 807/1000, Loss: 0.0078
[IL] Epoch 808/1000, Loss: 0.0082
[IL] Epoch 809/1000, Loss: 0.0089
[IL] Epoch 810/1000, Loss: 0.0083
[IL] Epoch 811/1000, Loss: 0.0079
[IL] Epoch 812/1000, Loss: 0.0075
[IL] Epoch 813/1000, Loss: 0.0074
[IL] Epoch 814/1000, Loss: 0.0077
[IL] Epoch 815/1000, Loss: 0.0086
[IL] Epoch 816/1000, Loss: 0.0094
[IL] Epoch 817/1000, Loss: 0.0089
[IL] Epoch 818/1000, Loss: 0.0084
[IL] Epoch 819/1000, Loss: 0.0089
[IL] Epoch 820/1000, Loss: 0.0086
[IL] Epoch 821/1000, Loss: 0.0081
[IL] Epoch 822/1000, Loss: 0.0079
[IL] Epoch 823/1000, Loss: 0.0084
[IL] Epoch 824/1000, Loss: 0.0077
[IL] Epoch 825/1000, Loss: 0.0075
[IL] Epoch 826/1000, Loss: 0.0072
[IL] Epoch 827/1000, Loss: 0.0070
[IL] Epoch 828/1000, Loss: 0.0069
[IL] Epoch 829/1000, Loss: 0.0071
[IL] Epoch 830/1000, Loss: 0.0079
[IL] Epoch 831/1000, Loss: 0.0074
[IL] Epoch 832/1000, Loss: 0.0077
[IL] Epoch 833/1000, Loss: 0.0068
[IL] Epoch 834/1000, Loss: 0.0071
[IL] Epoch 835/1000, Loss: 0.0081
[IL] Epoch 836/1000, Loss: 0.0074
[IL] Epoch 837/1000, Loss: 0.0082
[IL] Epoch 838/1000, Loss: 0.0072
[IL] Epoch 839/1000, Loss: 0.0084
[IL] Epoch 840/1000, Loss: 0.0070
[IL] Epoch 841/1000, Loss: 0.0069
[IL] Epoch 842/1000, Loss: 0.0084
[IL] Epoch 843/1000, Loss: 0.0076
[IL] Epoch 844/1000, Loss: 0.0082
[IL] Epoch 845/1000, Loss: 0.0083
[IL] Epoch 846/1000, Loss: 0.0072
[IL] Epoch 847/1000, Loss: 0.0076
[IL] Epoch 848/1000, Loss: 0.0079
[IL] Epoch 849/1000, Loss: 0.0079
[IL] Epoch 850/1000, Loss: 0.0073
[IL] Epoch 851/1000, Loss: 0.0074
[IL] Epoch 852/1000, Loss: 0.0071
[IL] Epoch 853/1000, Loss: 0.0071
[IL] Epoch 854/1000, Loss: 0.0069
[IL] Epoch 855/1000, Loss: 0.0071
[IL] Epoch 856/1000, Loss: 0.0068
[IL] Epoch 857/1000, Loss: 0.0062
[IL] Epoch 858/1000, Loss: 0.0066
[IL] Epoch 859/1000, Loss: 0.0066
[IL] Epoch 860/1000, Loss: 0.0075
[IL] Epoch 861/1000, Loss: 0.0080
[IL] Epoch 862/1000, Loss: 0.0078
[IL] Epoch 863/1000, Loss: 0.0084
[IL] Epoch 864/1000, Loss: 0.0078
[IL] Epoch 865/1000, Loss: 0.0071
[IL] Epoch 866/1000, Loss: 0.0065
[IL] Epoch 867/1000, Loss: 0.0066
[IL] Epoch 868/1000, Loss: 0.0064
[IL] Epoch 869/1000, Loss: 0.0064
[IL] Epoch 870/1000, Loss: 0.0063
[IL] Epoch 871/1000, Loss: 0.0076
[IL] Epoch 872/1000, Loss: 0.0077
[IL] Epoch 873/1000, Loss: 0.0069
[IL] Epoch 874/1000, Loss: 0.0080
[IL] Epoch 875/1000, Loss: 0.0073
[IL] Epoch 876/1000, Loss: 0.0086
[IL] Epoch 877/1000, Loss: 0.0065
[IL] Epoch 878/1000, Loss: 0.0066
[IL] Epoch 879/1000, Loss: 0.0068
[IL] Epoch 880/1000, Loss: 0.0080
[IL] Epoch 881/1000, Loss: 0.0071
[IL] Epoch 882/1000, Loss: 0.0068
[IL] Epoch 883/1000, Loss: 0.0067
[IL] Epoch 884/1000, Loss: 0.0064
[IL] Epoch 885/1000, Loss: 0.0068
[IL] Epoch 886/1000, Loss: 0.0083
[IL] Epoch 887/1000, Loss: 0.0090
[IL] Epoch 888/1000, Loss: 0.0082
[IL] Epoch 889/1000, Loss: 0.0077
[IL] Epoch 890/1000, Loss: 0.0081
[IL] Epoch 891/1000, Loss: 0.0076
[IL] Epoch 892/1000, Loss: 0.0074
[IL] Epoch 893/1000, Loss: 0.0072
[IL] Epoch 894/1000, Loss: 0.0069
[IL] Epoch 895/1000, Loss: 0.0065
[IL] Epoch 896/1000, Loss: 0.0073
[IL] Epoch 897/1000, Loss: 0.0073
[IL] Epoch 898/1000, Loss: 0.0075
[IL] Epoch 899/1000, Loss: 0.0079
test_mean_score: 0.5
[IL] Eval - Success Rate: 0.500
[IL] Epoch 900/1000, Loss: 0.0087
[IL] Epoch 901/1000, Loss: 0.0081
[IL] Epoch 902/1000, Loss: 0.0081
[IL] Epoch 903/1000, Loss: 0.0066
[IL] Epoch 904/1000, Loss: 0.0070
[IL] Epoch 905/1000, Loss: 0.0073
[IL] Epoch 906/1000, Loss: 0.0066
[IL] Epoch 907/1000, Loss: 0.0080
[IL] Epoch 908/1000, Loss: 0.0080
[IL] Epoch 909/1000, Loss: 0.0068
[IL] Epoch 910/1000, Loss: 0.0066
[IL] Epoch 911/1000, Loss: 0.0078
[IL] Epoch 912/1000, Loss: 0.0073
[IL] Epoch 913/1000, Loss: 0.0071
[IL] Epoch 914/1000, Loss: 0.0072
[IL] Epoch 915/1000, Loss: 0.0073
[IL] Epoch 916/1000, Loss: 0.0072
[IL] Epoch 917/1000, Loss: 0.0068
[IL] Epoch 918/1000, Loss: 0.0081
[IL] Epoch 919/1000, Loss: 0.0075
[IL] Epoch 920/1000, Loss: 0.0078
[IL] Epoch 921/1000, Loss: 0.0073
[IL] Epoch 922/1000, Loss: 0.0070
[IL] Epoch 923/1000, Loss: 0.0070
[IL] Epoch 924/1000, Loss: 0.0078
[IL] Epoch 925/1000, Loss: 0.0071
[IL] Epoch 926/1000, Loss: 0.0066
[IL] Epoch 927/1000, Loss: 0.0066
[IL] Epoch 928/1000, Loss: 0.0068
[IL] Epoch 929/1000, Loss: 0.0067
[IL] Epoch 930/1000, Loss: 0.0071
[IL] Epoch 931/1000, Loss: 0.0075
[IL] Epoch 932/1000, Loss: 0.0073
[IL] Epoch 933/1000, Loss: 0.0068
[IL] Epoch 934/1000, Loss: 0.0071
[IL] Epoch 935/1000, Loss: 0.0074
[IL] Epoch 936/1000, Loss: 0.0080
[IL] Epoch 937/1000, Loss: 0.0066
[IL] Epoch 938/1000, Loss: 0.0068
[IL] Epoch 939/1000, Loss: 0.0075
[IL] Epoch 940/1000, Loss: 0.0062
[IL] Epoch 941/1000, Loss: 0.0066
[IL] Epoch 942/1000, Loss: 0.0057
[IL] Epoch 943/1000, Loss: 0.0054
[IL] Epoch 944/1000, Loss: 0.0057
[IL] Epoch 945/1000, Loss: 0.0057
[IL] Epoch 946/1000, Loss: 0.0060
[IL] Epoch 947/1000, Loss: 0.0061
[IL] Epoch 948/1000, Loss: 0.0071
[IL] Epoch 949/1000, Loss: 0.0074
[IL] Epoch 950/1000, Loss: 0.0068
[IL] Epoch 951/1000, Loss: 0.0067
[IL] Epoch 952/1000, Loss: 0.0066
[IL] Epoch 953/1000, Loss: 0.0069
[IL] Epoch 954/1000, Loss: 0.0070
[IL] Epoch 955/1000, Loss: 0.0062
[IL] Epoch 956/1000, Loss: 0.0070
[IL] Epoch 957/1000, Loss: 0.0072
[IL] Epoch 958/1000, Loss: 0.0068
[IL] Epoch 959/1000, Loss: 0.0068
[IL] Epoch 960/1000, Loss: 0.0082
[IL] Epoch 961/1000, Loss: 0.0079
[IL] Epoch 962/1000, Loss: 0.0068
[IL] Epoch 963/1000, Loss: 0.0064
[IL] Epoch 964/1000, Loss: 0.0065
[IL] Epoch 965/1000, Loss: 0.0065
[IL] Epoch 966/1000, Loss: 0.0068
[IL] Epoch 967/1000, Loss: 0.0065
[IL] Epoch 968/1000, Loss: 0.0070
[IL] Epoch 969/1000, Loss: 0.0075
[IL] Epoch 970/1000, Loss: 0.0067
[IL] Epoch 971/1000, Loss: 0.0064
[IL] Epoch 972/1000, Loss: 0.0057
[IL] Epoch 973/1000, Loss: 0.0061
[IL] Epoch 974/1000, Loss: 0.0063
[IL] Epoch 975/1000, Loss: 0.0057
[IL] Epoch 976/1000, Loss: 0.0057
[IL] Epoch 977/1000, Loss: 0.0060
[IL] Epoch 978/1000, Loss: 0.0070
[IL] Epoch 979/1000, Loss: 0.0079
[IL] Epoch 980/1000, Loss: 0.0069
[IL] Epoch 981/1000, Loss: 0.0075
[IL] Epoch 982/1000, Loss: 0.0065
[IL] Epoch 983/1000, Loss: 0.0070
[IL] Epoch 984/1000, Loss: 0.0067
[IL] Epoch 985/1000, Loss: 0.0062
[IL] Epoch 986/1000, Loss: 0.0067
[IL] Epoch 987/1000, Loss: 0.0064
[IL] Epoch 988/1000, Loss: 0.0073
[IL] Epoch 989/1000, Loss: 0.0064
[IL] Epoch 990/1000, Loss: 0.0070
[IL] Epoch 991/1000, Loss: 0.0058
[IL] Epoch 992/1000, Loss: 0.0066
[IL] Epoch 993/1000, Loss: 0.0072
[IL] Epoch 994/1000, Loss: 0.0062
[IL] Epoch 995/1000, Loss: 0.0072
[IL] Epoch 996/1000, Loss: 0.0064
[IL] Epoch 997/1000, Loss: 0.0064
[IL] Epoch 998/1000, Loss: 0.0062
[IL] Epoch 999/1000, Loss: 0.0063
test_mean_score: 0.5
[IL] Eval - Success Rate: 0.500
[Checkpoint] Saved to /nfs_global/S/yangrongzheng/RL100/3D-Diffusion-Policy/3D-Diffusion-Policy/checkpoints/after_il.ckpt

================================================================================
               OFFLINE RL ITERATION 1/5
================================================================================


[RL100Trainer] Line 6 — Training Transition Model T_θ (Iteration 0)

[TransitionModel] Encoding dataset for transition model training...
[TransitionModel] Dataset: 1737 samples, input_dim=260, target_dim=257
[TransitionModel] Epoch    0 | train=166.31556 | val=13.04852 | no-improve=0/5
[TransitionModel] Epoch   20 | train=10.33563 | val=4.48348 | no-improve=0/5
[TransitionModel] Epoch   40 | train=-6.41741 | val=1.48884 | no-improve=0/5
[TransitionModel] Epoch   60 | train=-18.23827 | val=0.79272 | no-improve=0/5
[TransitionModel] Epoch   80 | train=-20.33372 | val=0.61779 | no-improve=0/5
[TransitionModel] Epoch  100 | train=-24.67020 | val=0.58678 | no-improve=2/5
[TransitionModel] Epoch  120 | train=-27.54537 | val=0.43111 | no-improve=3/5
[TransitionModel] Epoch  140 | train=-28.64167 | val=0.35057 | no-improve=0/5
[TransitionModel] Epoch  160 | train=-30.08974 | val=0.30211 | no-improve=1/5
[TransitionModel] Epoch  180 | train=-30.72729 | val=0.24576 | no-improve=0/5
[TransitionModel] Training complete. Elites=[5, 6, 3, 0, 2], val_loss=0.19619

[RL100Trainer] Phase 2a: Training IQL Critics (Iteration 0)
[IQL] Epoch 0/150, V Loss: 1.1101, Q Loss: 6419.0883
[IQL] Epoch 1/150, V Loss: 0.7083, Q Loss: 5843.3140
[IQL] Epoch 2/150, V Loss: 0.3394, Q Loss: 5683.9169
[IQL] Epoch 3/150, V Loss: 0.2315, Q Loss: 5637.9480
[IQL] Epoch 4/150, V Loss: 0.2051, Q Loss: 5636.5730
[IQL] Epoch 5/150, V Loss: 0.2160, Q Loss: 5634.4362
[IQL] Epoch 6/150, V Loss: 0.2439, Q Loss: 5626.7944
[IQL] Epoch 7/150, V Loss: 0.2748, Q Loss: 5643.1088
[IQL] Epoch 8/150, V Loss: 0.2960, Q Loss: 5640.3897
[IQL] Epoch 9/150, V Loss: 0.3089, Q Loss: 5636.8846
[IQL] Epoch 10/150, V Loss: 0.3173, Q Loss: 5628.6896
[IQL] Epoch 11/150, V Loss: 0.3228, Q Loss: 5602.1484
[IQL] Epoch 12/150, V Loss: 0.3258, Q Loss: 5573.8926
[IQL] Epoch 13/150, V Loss: 0.3265, Q Loss: 5551.8549
[IQL] Epoch 14/150, V Loss: 0.3245, Q Loss: 5530.6991
[IQL] Epoch 15/150, V Loss: 0.3208, Q Loss: 5506.4447
[IQL] Epoch 16/150, V Loss: 0.3191, Q Loss: 5467.5539
[IQL] Epoch 17/150, V Loss: 0.3174, Q Loss: 5427.0567
[IQL] Epoch 18/150, V Loss: 0.3158, Q Loss: 5384.5212
[IQL] Epoch 19/150, V Loss: 0.3136, Q Loss: 5357.2279
[IQL] Epoch 20/150, V Loss: 0.3107, Q Loss: 5337.5306
[IQL] Epoch 21/150, V Loss: 0.3083, Q Loss: 5299.7944
[IQL] Epoch 22/150, V Loss: 0.3071, Q Loss: 5268.2767
[IQL] Epoch 23/150, V Loss: 0.3056, Q Loss: 5210.1106
[IQL] Epoch 24/150, V Loss: 0.3040, Q Loss: 5164.8269
[IQL] Epoch 25/150, V Loss: 0.3021, Q Loss: 5135.0258
[IQL] Epoch 26/150, V Loss: 0.2994, Q Loss: 5096.3048
[IQL] Epoch 27/150, V Loss: 0.2968, Q Loss: 5045.8816
[IQL] Epoch 28/150, V Loss: 0.2944, Q Loss: 5004.1380
[IQL] Epoch 29/150, V Loss: 0.2921, Q Loss: 4976.4049
[IQL] Epoch 30/150, V Loss: 0.2899, Q Loss: 4931.2390
[IQL] Epoch 31/150, V Loss: 0.2874, Q Loss: 4902.1230
[IQL] Epoch 32/150, V Loss: 0.2858, Q Loss: 4852.3283
[IQL] Epoch 33/150, V Loss: 0.2842, Q Loss: 4825.0811
[IQL] Epoch 34/150, V Loss: 0.2813, Q Loss: 4788.9199
[IQL] Epoch 35/150, V Loss: 0.2793, Q Loss: 4749.3291
[IQL] Epoch 36/150, V Loss: 0.2779, Q Loss: 4711.6251
[IQL] Epoch 37/150, V Loss: 0.2751, Q Loss: 4695.9204
[IQL] Epoch 38/150, V Loss: 0.2730, Q Loss: 4651.7985
[IQL] Epoch 39/150, V Loss: 0.2720, Q Loss: 4599.8358
[IQL] Epoch 40/150, V Loss: 0.2713, Q Loss: 4565.5038
[IQL] Epoch 41/150, V Loss: 0.2691, Q Loss: 4542.0511
[IQL] Epoch 42/150, V Loss: 0.2656, Q Loss: 4507.0607
[IQL] Epoch 43/150, V Loss: 0.2625, Q Loss: 4480.0415
[IQL] Epoch 44/150, V Loss: 0.2602, Q Loss: 4441.9059
[IQL] Epoch 45/150, V Loss: 0.2596, Q Loss: 4407.7885
[IQL] Epoch 46/150, V Loss: 0.2594, Q Loss: 4380.0235
[IQL] Epoch 47/150, V Loss: 0.2570, Q Loss: 4345.7751
[IQL] Epoch 48/150, V Loss: 0.2539, Q Loss: 4328.6096
[IQL] Epoch 49/150, V Loss: 0.2521, Q Loss: 4278.5440
[IQL] Epoch 50/150, V Loss: 0.2515, Q Loss: 4254.1687
[IQL] Epoch 51/150, V Loss: 0.2491, Q Loss: 4233.0773
[IQL] Epoch 52/150, V Loss: 0.2468, Q Loss: 4203.0190
[IQL] Epoch 53/150, V Loss: 0.2458, Q Loss: 4172.5960
[IQL] Epoch 54/150, V Loss: 0.2438, Q Loss: 4144.6651
[IQL] Epoch 55/150, V Loss: 0.2420, Q Loss: 4110.5164
[IQL] Epoch 56/150, V Loss: 0.2406, Q Loss: 4088.7646
[IQL] Epoch 57/150, V Loss: 0.2385, Q Loss: 4068.2951
[IQL] Epoch 58/150, V Loss: 0.2366, Q Loss: 4033.5738
[IQL] Epoch 59/150, V Loss: 0.2352, Q Loss: 4023.3795
[IQL] Epoch 60/150, V Loss: 0.2335, Q Loss: 3987.0046
[IQL] Epoch 61/150, V Loss: 0.2320, Q Loss: 3968.5908
[IQL] Epoch 62/150, V Loss: 0.2303, Q Loss: 3933.1333
[IQL] Epoch 63/150, V Loss: 0.2287, Q Loss: 3912.4382
[IQL] Epoch 64/150, V Loss: 0.2269, Q Loss: 3896.1123
[IQL] Epoch 65/150, V Loss: 0.2254, Q Loss: 3857.7089
[IQL] Epoch 66/150, V Loss: 0.2245, Q Loss: 3837.0017
[IQL] Epoch 67/150, V Loss: 0.2222, Q Loss: 3816.3375
[IQL] Epoch 68/150, V Loss: 0.2202, Q Loss: 3795.9012
[IQL] Epoch 69/150, V Loss: 0.2182, Q Loss: 3773.8278
[IQL] Epoch 70/150, V Loss: 0.2173, Q Loss: 3747.7752
[IQL] Epoch 71/150, V Loss: 0.2157, Q Loss: 3731.9892
[IQL] Epoch 72/150, V Loss: 0.2143, Q Loss: 3703.0668
[IQL] Epoch 73/150, V Loss: 0.2133, Q Loss: 3679.4124
[IQL] Epoch 74/150, V Loss: 0.2113, Q Loss: 3663.5840
[IQL] Epoch 75/150, V Loss: 0.2093, Q Loss: 3641.4469
[IQL] Epoch 76/150, V Loss: 0.2082, Q Loss: 3610.0809
[IQL] Epoch 77/150, V Loss: 0.2069, Q Loss: 3595.7747
[IQL] Epoch 78/150, V Loss: 0.2052, Q Loss: 3575.1028
[IQL] Epoch 79/150, V Loss: 0.2030, Q Loss: 3554.1763
[IQL] Epoch 80/150, V Loss: 0.2016, Q Loss: 3544.9286
[IQL] Epoch 81/150, V Loss: 0.2011, Q Loss: 3513.0687
[IQL] Epoch 82/150, V Loss: 0.2000, Q Loss: 3494.3901
[IQL] Epoch 83/150, V Loss: 0.1979, Q Loss: 3480.2975
[IQL] Epoch 84/150, V Loss: 0.1957, Q Loss: 3459.9441
[IQL] Epoch 85/150, V Loss: 0.1944, Q Loss: 3441.0476
[IQL] Epoch 86/150, V Loss: 0.1947, Q Loss: 3408.5158
[IQL] Epoch 87/150, V Loss: 0.1930, Q Loss: 3406.3566
[IQL] Epoch 88/150, V Loss: 0.1905, Q Loss: 3380.4735
[IQL] Epoch 89/150, V Loss: 0.1896, Q Loss: 3362.5881
[IQL] Epoch 90/150, V Loss: 0.1889, Q Loss: 3343.2193
[IQL] Epoch 91/150, V Loss: 0.1867, Q Loss: 3323.7947
[IQL] Epoch 92/150, V Loss: 0.1854, Q Loss: 3309.4376
[IQL] Epoch 93/150, V Loss: 0.1836, Q Loss: 3296.8359
[IQL] Epoch 94/150, V Loss: 0.1825, Q Loss: 3282.9005
[IQL] Epoch 95/150, V Loss: 0.1832, Q Loss: 3254.4200
[IQL] Epoch 96/150, V Loss: 0.1831, Q Loss: 3239.7482
[IQL] Epoch 97/150, V Loss: 0.1845, Q Loss: 3224.9532
[IQL] Epoch 98/150, V Loss: 0.1941, Q Loss: 3198.8439
[IQL] Epoch 99/150, V Loss: 0.2389, Q Loss: 3190.9028
[IQL] Epoch 100/150, V Loss: 0.4217, Q Loss: 3174.4603
[IQL] Epoch 101/150, V Loss: 0.7637, Q Loss: 3157.4474
[IQL] Epoch 102/150, V Loss: 0.9695, Q Loss: 3128.8668
[IQL] Epoch 103/150, V Loss: 0.6553, Q Loss: 3113.6604
[IQL] Epoch 104/150, V Loss: 0.6513, Q Loss: 3096.0732
[IQL] Epoch 105/150, V Loss: 0.2707, Q Loss: 3080.1586
[IQL] Epoch 106/150, V Loss: 0.1767, Q Loss: 3059.5970
[IQL] Epoch 107/150, V Loss: 0.1917, Q Loss: 3050.8284
[IQL] Epoch 108/150, V Loss: 0.1840, Q Loss: 3032.6124
[IQL] Epoch 109/150, V Loss: 0.2238, Q Loss: 3017.8373
[IQL] Epoch 110/150, V Loss: 0.2700, Q Loss: 2995.2840
[IQL] Epoch 111/150, V Loss: 0.2263, Q Loss: 2989.8395
[IQL] Epoch 112/150, V Loss: 0.1920, Q Loss: 2965.3310
[IQL] Epoch 113/150, V Loss: 0.1725, Q Loss: 2949.5655
[IQL] Epoch 114/150, V Loss: 0.1834, Q Loss: 2938.7010
[IQL] Epoch 115/150, V Loss: 0.1948, Q Loss: 2929.2868
[IQL] Epoch 116/150, V Loss: 0.2006, Q Loss: 2907.6643
[IQL] Epoch 117/150, V Loss: 0.2562, Q Loss: 2890.2334
[IQL] Epoch 118/150, V Loss: 0.2360, Q Loss: 2880.0035
[IQL] Epoch 119/150, V Loss: 0.1947, Q Loss: 2867.8548
[IQL] Epoch 120/150, V Loss: 0.2662, Q Loss: 2849.7622
[IQL] Epoch 121/150, V Loss: 0.2242, Q Loss: 2836.3352
[IQL] Epoch 122/150, V Loss: 0.2035, Q Loss: 2814.0478
[IQL] Epoch 123/150, V Loss: 0.1762, Q Loss: 2811.3116
[IQL] Epoch 124/150, V Loss: 0.1688, Q Loss: 2794.7815
[IQL] Epoch 125/150, V Loss: 0.2208, Q Loss: 2776.9717
[IQL] Epoch 126/150, V Loss: 0.2565, Q Loss: 2759.6420
[IQL] Epoch 127/150, V Loss: 0.2758, Q Loss: 2744.5575
[IQL] Epoch 128/150, V Loss: 0.2154, Q Loss: 2731.4000
[IQL] Epoch 129/150, V Loss: 0.2946, Q Loss: 2721.4530
[IQL] Epoch 130/150, V Loss: 0.2249, Q Loss: 2708.7509
[IQL] Epoch 131/150, V Loss: 0.1946, Q Loss: 2686.6313
[IQL] Epoch 132/150, V Loss: 0.2532, Q Loss: 2678.7755
[IQL] Epoch 133/150, V Loss: 0.2542, Q Loss: 2665.6437
[IQL] Epoch 134/150, V Loss: 0.2432, Q Loss: 2647.6292
[IQL] Epoch 135/150, V Loss: 0.2526, Q Loss: 2639.2451
[IQL] Epoch 136/150, V Loss: 0.2257, Q Loss: 2626.5832
[IQL] Epoch 137/150, V Loss: 0.4397, Q Loss: 2615.0077
[IQL] Epoch 138/150, V Loss: 0.5216, Q Loss: 2592.0461
[IQL] Epoch 139/150, V Loss: 0.4935, Q Loss: 2581.3480
[IQL] Epoch 140/150, V Loss: 0.4595, Q Loss: 2574.2212
[IQL] Epoch 141/150, V Loss: 0.2754, Q Loss: 2554.8918
[IQL] Epoch 142/150, V Loss: 0.1959, Q Loss: 2541.9028
[IQL] Epoch 143/150, V Loss: 0.2384, Q Loss: 2534.3536
[IQL] Epoch 144/150, V Loss: 0.4238, Q Loss: 2517.3712
[IQL] Epoch 145/150, V Loss: 0.5360, Q Loss: 2508.3905
[IQL] Epoch 146/150, V Loss: 0.6691, Q Loss: 2494.9529
[IQL] Epoch 147/150, V Loss: 0.8220, Q Loss: 2476.4185
[IQL] Epoch 148/150, V Loss: 0.4051, Q Loss: 2464.3228
[IQL] Epoch 149/150, V Loss: 0.3705, Q Loss: 2456.6135

[RL100Trainer] Phase 2b: Offline RL Optimization (Iteration 0)
[OPE] Behavior policy value J_old = 87.8477
[RL PPO] Reducing policy LR: 1.00e-04 → 1.00e-05
[Offline RL] Epoch 0/100, PPO Loss: -0.0223, CD Loss: 1.4514
[Offline RL] Epoch 1/100, PPO Loss: -0.0227, CD Loss: 0.1179
[Offline RL] Epoch 2/100, PPO Loss: -0.0212, CD Loss: 0.3375
[Offline RL] Epoch 3/100, PPO Loss: -0.0208, CD Loss: 0.1021
[Offline RL] Epoch 4/100, PPO Loss: -0.0222, CD Loss: 0.1052
[Offline RL] Epoch 5/100, PPO Loss: -0.0226, CD Loss: 0.1525
[Offline RL] Epoch 6/100, PPO Loss: -0.0228, CD Loss: 0.1195
[Offline RL] Epoch 7/100, PPO Loss: -0.0221, CD Loss: 0.0838
[Offline RL] Epoch 8/100, PPO Loss: -0.0214, CD Loss: 0.0882
[Offline RL] Epoch 9/100, PPO Loss: -0.0223, CD Loss: 0.0966
[Offline RL] Epoch 10/100, PPO Loss: -0.0225, CD Loss: 0.0911
[Offline RL] Epoch 11/100, PPO Loss: -0.0227, CD Loss: 0.0751
[Offline RL] Epoch 12/100, PPO Loss: -0.0220, CD Loss: 0.0717
[Offline RL] Epoch 13/100, PPO Loss: -0.0221, CD Loss: 0.0689
[Offline RL] Epoch 14/100, PPO Loss: -0.0218, CD Loss: 0.0717
[Offline RL] Epoch 15/100, PPO Loss: -0.0227, CD Loss: 0.0734
[Offline RL] Epoch 16/100, PPO Loss: -0.0217, CD Loss: 0.0801
[Offline RL] Epoch 17/100, PPO Loss: -0.0211, CD Loss: 0.0729
[Offline RL] Epoch 18/100, PPO Loss: -0.0209, CD Loss: 0.0638
[Offline RL] Epoch 19/100, PPO Loss: -0.0202, CD Loss: 0.0689
[Offline RL] Epoch 20/100, PPO Loss: -0.0201, CD Loss: 0.0689
[Offline RL] Epoch 21/100, PPO Loss: -0.0216, CD Loss: 0.0693
[Offline RL] Epoch 22/100, PPO Loss: -0.0217, CD Loss: 0.0690
[Offline RL] Epoch 23/100, PPO Loss: -0.0197, CD Loss: 0.0659
[Offline RL] Epoch 24/100, PPO Loss: -0.0206, CD Loss: 0.0682
[Offline RL] Epoch 25/100, PPO Loss: -0.0211, CD Loss: 0.0688
[Offline RL] Epoch 26/100, PPO Loss: -0.0223, CD Loss: 0.0824
[Offline RL] Epoch 27/100, PPO Loss: -0.0198, CD Loss: 0.0868
[Offline RL] Epoch 28/100, PPO Loss: -0.0196, CD Loss: 0.0824
[Offline RL] Epoch 29/100, PPO Loss: -0.0203, CD Loss: 0.0782
[Offline RL] Epoch 30/100, PPO Loss: -0.0201, CD Loss: 0.0761
[Offline RL] Epoch 31/100, PPO Loss: -0.0212, CD Loss: 0.0731
[Offline RL] Epoch 32/100, PPO Loss: -0.0225, CD Loss: 0.0745
[Offline RL] Epoch 33/100, PPO Loss: -0.0209, CD Loss: 0.0747
[Offline RL] Epoch 34/100, PPO Loss: -0.0206, CD Loss: 0.0667
[Offline RL] Epoch 35/100, PPO Loss: -0.0206, CD Loss: 0.0635
[Offline RL] Epoch 36/100, PPO Loss: -0.0216, CD Loss: 0.0600
[Offline RL] Epoch 37/100, PPO Loss: -0.0194, CD Loss: 0.0600
[Offline RL] Epoch 38/100, PPO Loss: -0.0212, CD Loss: 0.0600
[Offline RL] Epoch 39/100, PPO Loss: -0.0204, CD Loss: 0.0597
[Offline RL] Epoch 40/100, PPO Loss: -0.0209, CD Loss: 0.0643
[Offline RL] Epoch 41/100, PPO Loss: -0.0201, CD Loss: 0.0625
[Offline RL] Epoch 42/100, PPO Loss: -0.0203, CD Loss: 0.0624
[Offline RL] Epoch 43/100, PPO Loss: -0.0201, CD Loss: 0.0704
[Offline RL] Epoch 44/100, PPO Loss: -0.0176, CD Loss: 0.0685
[Offline RL] Epoch 45/100, PPO Loss: -0.0208, CD Loss: 0.0643
[Offline RL] Epoch 46/100, PPO Loss: -0.0189, CD Loss: 0.0665
[Offline RL] Epoch 47/100, PPO Loss: -0.0191, CD Loss: 0.0630
[Offline RL] Epoch 48/100, PPO Loss: -0.0201, CD Loss: 0.0621
[Offline RL] Epoch 49/100, PPO Loss: -0.0190, CD Loss: 0.0623
[Offline RL] Epoch 50/100, PPO Loss: -0.0186, CD Loss: 0.0627
[Offline RL] Epoch 51/100, PPO Loss: -0.0202, CD Loss: 0.0655
[Offline RL] Epoch 52/100, PPO Loss: -0.0182, CD Loss: 0.0673
[Offline RL] Epoch 53/100, PPO Loss: -0.0178, CD Loss: 0.0663
[Offline RL] Epoch 54/100, PPO Loss: -0.0187, CD Loss: 0.0680
[Offline RL] Epoch 55/100, PPO Loss: -0.0178, CD Loss: 0.0700
[Offline RL] Epoch 56/100, PPO Loss: -0.0180, CD Loss: 0.0735
[Offline RL] Epoch 57/100, PPO Loss: -0.0190, CD Loss: 0.0645
[Offline RL] Epoch 58/100, PPO Loss: -0.0167, CD Loss: 0.0726
[Offline RL] Epoch 59/100, PPO Loss: -0.0179, CD Loss: 0.0701
[Offline RL] Epoch 60/100, PPO Loss: -0.0182, CD Loss: 0.0693
[Offline RL] Epoch 61/100, PPO Loss: -0.0171, CD Loss: 0.0696
[Offline RL] Epoch 62/100, PPO Loss: -0.0168, CD Loss: 0.0733
[Offline RL] Epoch 63/100, PPO Loss: -0.0181, CD Loss: 0.0716
[Offline RL] Epoch 64/100, PPO Loss: -0.0175, CD Loss: 0.0738
[Offline RL] Epoch 65/100, PPO Loss: -0.0171, CD Loss: 0.0712
[Offline RL] Epoch 66/100, PPO Loss: -0.0179, CD Loss: 0.0791
[Offline RL] Epoch 67/100, PPO Loss: -0.0182, CD Loss: 0.0793
[Offline RL] Epoch 68/100, PPO Loss: -0.0185, CD Loss: 0.0754
[Offline RL] Epoch 69/100, PPO Loss: -0.0180, CD Loss: 0.0742
[Offline RL] Epoch 70/100, PPO Loss: -0.0170, CD Loss: 0.0709
[Offline RL] Epoch 71/100, PPO Loss: -0.0170, CD Loss: 0.0710
[Offline RL] Epoch 72/100, PPO Loss: -0.0176, CD Loss: 0.0702
[Offline RL] Epoch 73/100, PPO Loss: -0.0166, CD Loss: 0.0733
[Offline RL] Epoch 74/100, PPO Loss: -0.0147, CD Loss: 0.0738
[Offline RL] Epoch 75/100, PPO Loss: -0.0168, CD Loss: 0.0760
[Offline RL] Epoch 76/100, PPO Loss: -0.0154, CD Loss: 0.0866
[Offline RL] Epoch 77/100, PPO Loss: -0.0160, CD Loss: 0.0864
[Offline RL] Epoch 78/100, PPO Loss: -0.0168, CD Loss: 0.0761
[Offline RL] Epoch 79/100, PPO Loss: -0.0168, CD Loss: 0.0728
[Offline RL] Epoch 80/100, PPO Loss: -0.0160, CD Loss: 0.0665
[Offline RL] Epoch 81/100, PPO Loss: -0.0172, CD Loss: 0.0625
[Offline RL] Epoch 82/100, PPO Loss: -0.0164, CD Loss: 0.0577
[Offline RL] Epoch 83/100, PPO Loss: -0.0166, CD Loss: 0.0589
[Offline RL] Epoch 84/100, PPO Loss: -0.0173, CD Loss: 0.0554
[Offline RL] Epoch 85/100, PPO Loss: -0.0173, CD Loss: 0.0610
[Offline RL] Epoch 86/100, PPO Loss: -0.0170, CD Loss: 0.0612
[Offline RL] Epoch 87/100, PPO Loss: -0.0174, CD Loss: 0.0618
[Offline RL] Epoch 88/100, PPO Loss: -0.0165, CD Loss: 0.0631
[Offline RL] Epoch 89/100, PPO Loss: -0.0167, CD Loss: 0.0694
[Offline RL] Epoch 90/100, PPO Loss: -0.0165, CD Loss: 0.0647
[Offline RL] Epoch 91/100, PPO Loss: -0.0162, CD Loss: 0.0689
[Offline RL] Epoch 92/100, PPO Loss: -0.0178, CD Loss: 0.0691
[Offline RL] Epoch 93/100, PPO Loss: -0.0162, CD Loss: 0.0715
[Offline RL] Epoch 94/100, PPO Loss: -0.0160, CD Loss: 0.0738
[Offline RL] Epoch 95/100, PPO Loss: -0.0186, CD Loss: 0.0736
[Offline RL] Epoch 96/100, PPO Loss: -0.0162, CD Loss: 0.0797
[Offline RL] Epoch 97/100, PPO Loss: -0.0182, CD Loss: 0.0732
[Offline RL] Epoch 98/100, PPO Loss: -0.0168, CD Loss: 0.0730
[Offline RL] Epoch 99/100, PPO Loss: -0.0180, CD Loss: 0.0749
[OPE] Policy REJECTED: J_new=87.8294 ≤ J_old=87.8477 + δ=4.3924. Rolling back to behavior policy.

[RL100Trainer] Phase 2c: Collecting New Data (Iteration 0)
[Collect] 50 episodes, success=0.500, steps=1250
[Data Collection] Success Rate: 0.500, Reward: 10176.40, Episodes: 50, Steps: 1250
[Dataset] Merged 50 episodes (1250 steps) → total 3250 steps, 60 episodes

[RL100Trainer] Retraining IL on merged dataset...

============================================================
[RL100Trainer] Phase 1: Imitation Learning
============================================================

[IL] Epoch 0/100, Loss: 0.2075
[IL] Epoch 1/100, Loss: 0.1505
[IL] Epoch 2/100, Loss: 0.1286
[IL] Epoch 3/100, Loss: 0.1223
[IL] Epoch 4/100, Loss: 0.1051
[IL] Epoch 5/100, Loss: 0.1040
[IL] Epoch 6/100, Loss: 0.0924
[IL] Epoch 7/100, Loss: 0.0863
[IL] Epoch 8/100, Loss: 0.0951
[IL] Epoch 9/100, Loss: 0.0898
[IL] Epoch 10/100, Loss: 0.0911
[IL] Epoch 11/100, Loss: 0.0869
[IL] Epoch 12/100, Loss: 0.0790
[IL] Epoch 13/100, Loss: 0.0885
[IL] Epoch 14/100, Loss: 0.0879
[IL] Epoch 15/100, Loss: 0.0778
[IL] Epoch 16/100, Loss: 0.0855
[IL] Epoch 17/100, Loss: 0.0812
[IL] Epoch 18/100, Loss: 0.0797
[IL] Epoch 19/100, Loss: 0.0737
[IL] Epoch 20/100, Loss: 0.0755
[IL] Epoch 21/100, Loss: 0.0671
[IL] Epoch 22/100, Loss: 0.0730
[IL] Epoch 23/100, Loss: 0.0710
[IL] Epoch 24/100, Loss: 0.0650
[IL] Epoch 25/100, Loss: 0.0678
[IL] Epoch 26/100, Loss: 0.0665
[IL] Epoch 27/100, Loss: 0.0633
[IL] Epoch 28/100, Loss: 0.0649
[IL] Epoch 29/100, Loss: 0.0772
[IL] Epoch 30/100, Loss: 0.0633
[IL] Epoch 31/100, Loss: 0.0618
[IL] Epoch 32/100, Loss: 0.0666
[IL] Epoch 33/100, Loss: 0.0613
[IL] Epoch 34/100, Loss: 0.0633
[IL] Epoch 35/100, Loss: 0.0678
[IL] Epoch 36/100, Loss: 0.0637
[IL] Epoch 37/100, Loss: 0.0671
[IL] Epoch 38/100, Loss: 0.0551
[IL] Epoch 39/100, Loss: 0.0587
[IL] Epoch 40/100, Loss: 0.0605
[IL] Epoch 41/100, Loss: 0.0609
[IL] Epoch 42/100, Loss: 0.0578
[IL] Epoch 43/100, Loss: 0.0662
[IL] Epoch 44/100, Loss: 0.0625
[IL] Epoch 45/100, Loss: 0.0601
[IL] Epoch 46/100, Loss: 0.0591
[IL] Epoch 47/100, Loss: 0.0520
[IL] Epoch 48/100, Loss: 0.0574
[IL] Epoch 49/100, Loss: 0.0623
[IL] Epoch 50/100, Loss: 0.0556
[IL] Epoch 51/100, Loss: 0.0511
[IL] Epoch 52/100, Loss: 0.0546
[IL] Epoch 53/100, Loss: 0.0521
[IL] Epoch 54/100, Loss: 0.0549
[IL] Epoch 55/100, Loss: 0.0564
[IL] Epoch 56/100, Loss: 0.0579
[IL] Epoch 57/100, Loss: 0.0574
[IL] Epoch 58/100, Loss: 0.0541
[IL] Epoch 59/100, Loss: 0.0564
[IL] Epoch 60/100, Loss: 0.0521
[IL] Epoch 61/100, Loss: 0.0555
[IL] Epoch 62/100, Loss: 0.0568
[IL] Epoch 63/100, Loss: 0.0499
[IL] Epoch 64/100, Loss: 0.0527
[IL] Epoch 65/100, Loss: 0.0553
[IL] Epoch 66/100, Loss: 0.0499
[IL] Epoch 67/100, Loss: 0.0512
[IL] Epoch 68/100, Loss: 0.0579
[IL] Epoch 69/100, Loss: 0.0537
[IL] Epoch 70/100, Loss: 0.0501
[IL] Epoch 71/100, Loss: 0.0492
[IL] Epoch 72/100, Loss: 0.0526
[IL] Epoch 73/100, Loss: 0.0493
[IL] Epoch 74/100, Loss: 0.0531
[IL] Epoch 75/100, Loss: 0.0520
[IL] Epoch 76/100, Loss: 0.0569
[IL] Epoch 77/100, Loss: 0.0494
[IL] Epoch 78/100, Loss: 0.0489
[IL] Epoch 79/100, Loss: 0.0511
[IL] Epoch 80/100, Loss: 0.0489
[IL] Epoch 81/100, Loss: 0.0516
[IL] Epoch 82/100, Loss: 0.0529
[IL] Epoch 83/100, Loss: 0.0491
[IL] Epoch 84/100, Loss: 0.0493
[IL] Epoch 85/100, Loss: 0.0622
[IL] Epoch 86/100, Loss: 0.0514
[IL] Epoch 87/100, Loss: 0.0462
[IL] Epoch 88/100, Loss: 0.0492
[IL] Epoch 89/100, Loss: 0.0494
[IL] Epoch 90/100, Loss: 0.0429
[IL] Epoch 91/100, Loss: 0.0472
[IL] Epoch 92/100, Loss: 0.0520
[IL] Epoch 93/100, Loss: 0.0450
[IL] Epoch 94/100, Loss: 0.0485
[IL] Epoch 95/100, Loss: 0.0527
[IL] Epoch 96/100, Loss: 0.0457
[IL] Epoch 97/100, Loss: 0.0459
[IL] Epoch 98/100, Loss: 0.0464
[IL] Epoch 99/100, Loss: 0.0461
test_mean_score: 0.05
[IL] Eval - Success Rate: 0.050
[Checkpoint] Saved to /nfs_global/S/yangrongzheng/RL100/3D-Diffusion-Policy/3D-Diffusion-Policy/checkpoints/offline_iter_0.ckpt

================================================================================
               OFFLINE RL ITERATION 2/5
================================================================================


[RL100Trainer] Line 6 — Training Transition Model T_θ (Iteration 1)

[TransitionModel] Encoding dataset for transition model training...
[TransitionModel] Dataset: 2830 samples, input_dim=260, target_dim=257
[TransitionModel] Epoch    0 | train=59265.41927 | val=16912.75195 | no-improve=0/5
[TransitionModel] Epoch   20 | train=8579.28554 | val=4634.10049 | no-improve=0/5
[TransitionModel] Epoch   40 | train=2773.64510 | val=3564.03354 | no-improve=1/5
[TransitionModel] Epoch   60 | train=1669.23503 | val=3188.55381 | no-improve=0/5
[TransitionModel] Epoch   80 | train=1019.52093 | val=3105.37612 | no-improve=0/5
[TransitionModel] Epoch  100 | train=670.54162 | val=2955.11543 | no-improve=0/5
[TransitionModel] Epoch  109 | train=534.19619 | val=3058.27485 | no-improve=5/5
[TransitionModel] Training complete. Elites=[2, 3, 5, 0, 1], val_loss=2832.90635

[RL100Trainer] Phase 2a: Training IQL Critics (Iteration 1)
[IQL] Epoch 0/150, V Loss: 3.2374, Q Loss: 9883996.0417
[IQL] Epoch 1/150, V Loss: 12.0692, Q Loss: 8672715.2500
[IQL] Epoch 2/150, V Loss: 13.3322, Q Loss: 10107323.0000
[IQL] Epoch 3/150, V Loss: 12.5308, Q Loss: 8318092.4792
[IQL] Epoch 4/150, V Loss: 10.8387, Q Loss: 9090964.4167
[IQL] Epoch 5/150, V Loss: 9.4969, Q Loss: 8443590.5417
[IQL] Epoch 6/150, V Loss: 8.9978, Q Loss: 8375533.5833
[IQL] Epoch 7/150, V Loss: 9.2293, Q Loss: 9269464.4583
[IQL] Epoch 8/150, V Loss: 9.6238, Q Loss: 8348514.4167
[IQL] Epoch 9/150, V Loss: 9.5940, Q Loss: 8270401.7083
[IQL] Epoch 10/150, V Loss: 9.1648, Q Loss: 9491457.4167
[IQL] Epoch 11/150, V Loss: 9.3549, Q Loss: 8210180.7292
[IQL] Epoch 12/150, V Loss: 9.2900, Q Loss: 8092776.0684
[IQL] Epoch 13/150, V Loss: 8.5411, Q Loss: 8528904.2917
[IQL] Epoch 14/150, V Loss: 8.2978, Q Loss: 8603637.5833
[IQL] Epoch 15/150, V Loss: 8.7962, Q Loss: 9081539.9583
[IQL] Epoch 16/150, V Loss: 9.3697, Q Loss: 8734438.2500
[IQL] Epoch 17/150, V Loss: 9.5999, Q Loss: 9448788.2083
[IQL] Epoch 18/150, V Loss: 9.6731, Q Loss: 8256750.6250
[IQL] Epoch 19/150, V Loss: 9.1599, Q Loss: 8092679.4714
[IQL] Epoch 20/150, V Loss: 8.4308, Q Loss: 8345005.4583
[IQL] Epoch 21/150, V Loss: 8.2131, Q Loss: 9220147.9583
[IQL] Epoch 22/150, V Loss: 8.7211, Q Loss: 9528233.1250
[IQL] Epoch 23/150, V Loss: 9.3904, Q Loss: 8428730.9167
[IQL] Epoch 24/150, V Loss: 9.4102, Q Loss: 8078422.2995
[IQL] Epoch 25/150, V Loss: 8.5096, Q Loss: 8538126.7500
[IQL] Epoch 26/150, V Loss: 8.1181, Q Loss: 8488907.9583
[IQL] Epoch 27/150, V Loss: 8.2799, Q Loss: 9035447.7500
[IQL] Epoch 28/150, V Loss: 8.6369, Q Loss: 8729721.8750
[IQL] Epoch 29/150, V Loss: 8.7113, Q Loss: 8281616.7083
[IQL] Epoch 30/150, V Loss: 8.5712, Q Loss: 8559246.9583
[IQL] Epoch 31/150, V Loss: 8.2883, Q Loss: 8382226.2083
[IQL] Epoch 32/150, V Loss: 8.4144, Q Loss: 8766640.8333
[IQL] Epoch 33/150, V Loss: 8.5508, Q Loss: 8166074.9896
[IQL] Epoch 34/150, V Loss: 8.4329, Q Loss: 9475889.3333
[IQL] Epoch 35/150, V Loss: 8.6391, Q Loss: 8822849.0833
[IQL] Epoch 36/150, V Loss: 9.0320, Q Loss: 8433181.2083
[IQL] Epoch 37/150, V Loss: 9.0931, Q Loss: 8157212.7917
[IQL] Epoch 38/150, V Loss: 8.5738, Q Loss: 8696506.9583
[IQL] Epoch 39/150, V Loss: 8.4694, Q Loss: 9006894.3333
[IQL] Epoch 40/150, V Loss: 8.7541, Q Loss: 8550545.3750
[IQL] Epoch 41/150, V Loss: 8.7977, Q Loss: 8217158.4167
[IQL] Epoch 42/150, V Loss: 8.3662, Q Loss: 8613434.4167
[IQL] Epoch 43/150, V Loss: 8.1733, Q Loss: 9005952.2917
[IQL] Epoch 44/150, V Loss: 8.4527, Q Loss: 9170449.6667
[IQL] Epoch 45/150, V Loss: 8.9002, Q Loss: 8895772.8333
[IQL] Epoch 46/150, V Loss: 9.1564, Q Loss: 8291104.4167
[IQL] Epoch 47/150, V Loss: 8.7074, Q Loss: 8575926.4167
[IQL] Epoch 48/150, V Loss: 8.3747, Q Loss: 8656366.4583
[IQL] Epoch 49/150, V Loss: 8.4528, Q Loss: 8473375.3333
[IQL] Epoch 50/150, V Loss: 8.4908, Q Loss: 8313640.1667
[IQL] Epoch 51/150, V Loss: 8.4608, Q Loss: 9641768.1667
[IQL] Epoch 52/150, V Loss: 8.7564, Q Loss: 8703990.2500
[IQL] Epoch 53/150, V Loss: 8.8414, Q Loss: 8313812.6250
[IQL] Epoch 54/150, V Loss: 8.4737, Q Loss: 9128774.6667
[IQL] Epoch 55/150, V Loss: 8.5348, Q Loss: 8614979.4167
[IQL] Epoch 56/150, V Loss: 8.7147, Q Loss: 8802238.2083
[IQL] Epoch 57/150, V Loss: 8.7528, Q Loss: 8984755.7917
[IQL] Epoch 58/150, V Loss: 8.7859, Q Loss: 8519513.9167
[IQL] Epoch 59/150, V Loss: 8.7132, Q Loss: 8809392.9167
[IQL] Epoch 60/150, V Loss: 8.5781, Q Loss: 10221521.7500
[IQL] Epoch 61/150, V Loss: 9.0845, Q Loss: 10232735.1250
[IQL] Epoch 62/150, V Loss: 9.7822, Q Loss: 8942652.0417
[IQL] Epoch 63/150, V Loss: 9.9291, Q Loss: 8684759.4167
[IQL] Epoch 64/150, V Loss: 9.4334, Q Loss: 8069087.2318
[IQL] Epoch 65/150, V Loss: 8.6158, Q Loss: 8864607.6667
[IQL] Epoch 66/150, V Loss: 7.9273, Q Loss: 8702254.2500
[IQL] Epoch 67/150, V Loss: 8.1490, Q Loss: 8126058.8646
[IQL] Epoch 68/150, V Loss: 8.1661, Q Loss: 9375034.2500
[IQL] Epoch 69/150, V Loss: 8.1744, Q Loss: 9418073.8333
[IQL] Epoch 70/150, V Loss: 8.9001, Q Loss: 9232918.2083
[IQL] Epoch 71/150, V Loss: 9.1916, Q Loss: 8614598.6250
[IQL] Epoch 72/150, V Loss: 8.7649, Q Loss: 8256312.3333
[IQL] Epoch 73/150, V Loss: 8.3305, Q Loss: 8053900.9281
[IQL] Epoch 74/150, V Loss: 7.5656, Q Loss: 9550077.2083
[IQL] Epoch 75/150, V Loss: 7.9815, Q Loss: 8182747.2500
[IQL] Epoch 76/150, V Loss: 8.3023, Q Loss: 8495745.1250
[IQL] Epoch 77/150, V Loss: 8.0322, Q Loss: 8807754.0833
[IQL] Epoch 78/150, V Loss: 7.8565, Q Loss: 8709064.5417
[IQL] Epoch 79/150, V Loss: 7.9732, Q Loss: 8995542.0833
[IQL] Epoch 80/150, V Loss: 8.3063, Q Loss: 8261587.9792
[IQL] Epoch 81/150, V Loss: 8.1104, Q Loss: 9311007.1250
[IQL] Epoch 82/150, V Loss: 7.9859, Q Loss: 8131283.5833
[IQL] Epoch 83/150, V Loss: 7.8654, Q Loss: 8979084.7500
[IQL] Epoch 84/150, V Loss: 7.8463, Q Loss: 8404211.5417
[IQL] Epoch 85/150, V Loss: 7.8051, Q Loss: 8575287.0417
[IQL] Epoch 86/150, V Loss: 7.7734, Q Loss: 8283147.4167
[IQL] Epoch 87/150, V Loss: 7.6077, Q Loss: 9634959.7500
[IQL] Epoch 88/150, V Loss: 8.0215, Q Loss: 8460024.4167
[IQL] Epoch 89/150, V Loss: 8.1508, Q Loss: 8804320.6667
[IQL] Epoch 90/150, V Loss: 7.9340, Q Loss: 10356442.7083
[IQL] Epoch 91/150, V Loss: 8.4462, Q Loss: 8141606.3854
[IQL] Epoch 92/150, V Loss: 8.6332, Q Loss: 8039060.3783
[IQL] Epoch 93/150, V Loss: 7.8865, Q Loss: 9097118.5833
[IQL] Epoch 94/150, V Loss: 7.6793, Q Loss: 9408963.4167
[IQL] Epoch 95/150, V Loss: 8.0684, Q Loss: 8819762.0833
[IQL] Epoch 96/150, V Loss: 8.3038, Q Loss: 8430452.1250
[IQL] Epoch 97/150, V Loss: 8.1091, Q Loss: 8900841.4167
[IQL] Epoch 98/150, V Loss: 7.9541, Q Loss: 8085655.6354
[IQL] Epoch 99/150, V Loss: 7.6122, Q Loss: 8351422.8333
[IQL] Epoch 100/150, V Loss: 7.3002, Q Loss: 8372727.4583
[IQL] Epoch 101/150, V Loss: 7.1862, Q Loss: 8344953.9167
[IQL] Epoch 102/150, V Loss: 7.2278, Q Loss: 8177797.6667
[IQL] Epoch 103/150, V Loss: 7.3974, Q Loss: 8345014.5833
[IQL] Epoch 104/150, V Loss: 7.3503, Q Loss: 8495869.3750
[IQL] Epoch 105/150, V Loss: 7.5157, Q Loss: 8558312.9167
[IQL] Epoch 106/150, V Loss: 7.8804, Q Loss: 8030000.8373
[IQL] Epoch 107/150, V Loss: 7.5489, Q Loss: 8803400.5417
[IQL] Epoch 108/150, V Loss: 7.4428, Q Loss: 9216476.2500
[IQL] Epoch 109/150, V Loss: 7.7923, Q Loss: 9034692.9167
[IQL] Epoch 110/150, V Loss: 8.1017, Q Loss: 9472113.0000
[IQL] Epoch 111/150, V Loss: 8.5115, Q Loss: 8538191.3750
[IQL] Epoch 112/150, V Loss: 8.5964, Q Loss: 8172897.8125
[IQL] Epoch 113/150, V Loss: 7.9975, Q Loss: 8172502.5417
[IQL] Epoch 114/150, V Loss: 7.3327, Q Loss: 9005921.9583
[IQL] Epoch 115/150, V Loss: 7.4221, Q Loss: 8477228.2917
[IQL] Epoch 116/150, V Loss: 7.6841, Q Loss: 9164274.0000
[IQL] Epoch 117/150, V Loss: 7.8639, Q Loss: 8732735.0000
[IQL] Epoch 118/150, V Loss: 7.7445, Q Loss: 8819398.4583
[IQL] Epoch 119/150, V Loss: 7.8917, Q Loss: 8037728.7656
[IQL] Epoch 120/150, V Loss: 7.5688, Q Loss: 8871445.8750
[IQL] Epoch 121/150, V Loss: 7.5018, Q Loss: 8683826.1667
[IQL] Epoch 122/150, V Loss: 7.5973, Q Loss: 8624861.5000
[IQL] Epoch 123/150, V Loss: 7.6710, Q Loss: 8134489.3542
[IQL] Epoch 124/150, V Loss: 7.3400, Q Loss: 8451033.8333
[IQL] Epoch 125/150, V Loss: 7.1476, Q Loss: 8862242.9167
[IQL] Epoch 126/150, V Loss: 7.7054, Q Loss: 8767102.7500
[IQL] Epoch 127/150, V Loss: 7.8076, Q Loss: 8231250.1250
[IQL] Epoch 128/150, V Loss: 7.4521, Q Loss: 8765981.4583
[IQL] Epoch 129/150, V Loss: 7.0970, Q Loss: 9333482.7917
[IQL] Epoch 130/150, V Loss: 7.4271, Q Loss: 8806763.6250
[IQL] Epoch 131/150, V Loss: 7.8821, Q Loss: 9218871.9583
[IQL] Epoch 132/150, V Loss: 8.4951, Q Loss: 9687697.8333
[IQL] Epoch 133/150, V Loss: 8.6019, Q Loss: 9409786.8333
[IQL] Epoch 134/150, V Loss: 8.5319, Q Loss: 8360445.9583
[IQL] Epoch 135/150, V Loss: 8.1673, Q Loss: 8309431.0833
[IQL] Epoch 136/150, V Loss: 7.4345, Q Loss: 8925245.1667
[IQL] Epoch 137/150, V Loss: 7.3586, Q Loss: 9769204.2083
[IQL] Epoch 138/150, V Loss: 7.8022, Q Loss: 8230016.0833
[IQL] Epoch 139/150, V Loss: 7.9001, Q Loss: 9427362.7917
[IQL] Epoch 140/150, V Loss: 7.9934, Q Loss: 9112730.7917
[IQL] Epoch 141/150, V Loss: 8.0024, Q Loss: 8283518.7083
[IQL] Epoch 142/150, V Loss: 7.6635, Q Loss: 8027732.5443
[IQL] Epoch 143/150, V Loss: 7.0516, Q Loss: 8639207.2083
[IQL] Epoch 144/150, V Loss: 7.0755, Q Loss: 8607703.8750
[IQL] Epoch 145/150, V Loss: 7.3827, Q Loss: 8765984.2500
[IQL] Epoch 146/150, V Loss: 7.5481, Q Loss: 8083936.8125
[IQL] Epoch 147/150, V Loss: 7.2857, Q Loss: 8834020.5833
[IQL] Epoch 148/150, V Loss: 7.1591, Q Loss: 8251544.6875
[IQL] Epoch 149/150, V Loss: 7.1564, Q Loss: 8814577.0000

[RL100Trainer] Phase 2b: Offline RL Optimization (Iteration 1)
[OPE] Behavior policy value J_old = 505.9097
[Offline RL] Epoch 0/100, PPO Loss: -0.0258, CD Loss: 0.1087
[Offline RL] Epoch 1/100, PPO Loss: -0.0237, CD Loss: 0.0939
[Offline RL] Epoch 2/100, PPO Loss: -0.0207, CD Loss: 0.0977
[Offline RL] Epoch 3/100, PPO Loss: -0.0226, CD Loss: 0.0804
[Offline RL] Epoch 4/100, PPO Loss: -0.0258, CD Loss: 0.0946
[Offline RL] Epoch 5/100, PPO Loss: -0.0229, CD Loss: 0.0776
[Offline RL] Epoch 6/100, PPO Loss: -0.0226, CD Loss: 0.0727
[Offline RL] Epoch 7/100, PPO Loss: -0.0221, CD Loss: 0.0667
[Offline RL] Epoch 8/100, PPO Loss: -0.0193, CD Loss: 0.0692
[Offline RL] Epoch 9/100, PPO Loss: -0.0218, CD Loss: 0.0732
[Offline RL] Epoch 10/100, PPO Loss: -0.0233, CD Loss: 0.0642
[Offline RL] Epoch 11/100, PPO Loss: -0.0227, CD Loss: 0.0645
[Offline RL] Epoch 12/100, PPO Loss: -0.0209, CD Loss: 0.0694
[Offline RL] Epoch 13/100, PPO Loss: -0.0217, CD Loss: 0.0670
[Offline RL] Epoch 14/100, PPO Loss: -0.0195, CD Loss: 0.0760
[Offline RL] Epoch 15/100, PPO Loss: -0.0223, CD Loss: 0.0723
[Offline RL] Epoch 16/100, PPO Loss: -0.0204, CD Loss: 0.0687
[Offline RL] Epoch 17/100, PPO Loss: -0.0229, CD Loss: 0.0772
[Offline RL] Epoch 18/100, PPO Loss: -0.0207, CD Loss: 0.0761
[Offline RL] Epoch 19/100, PPO Loss: -0.0214, CD Loss: 0.0833
[Offline RL] Epoch 20/100, PPO Loss: -0.0196, CD Loss: 0.0808
[Offline RL] Epoch 21/100, PPO Loss: -0.0205, CD Loss: 0.0828
[Offline RL] Epoch 22/100, PPO Loss: -0.0188, CD Loss: 0.0756
[Offline RL] Epoch 23/100, PPO Loss: -0.0192, CD Loss: 0.0801
[Offline RL] Epoch 24/100, PPO Loss: -0.0182, CD Loss: 0.0753
[Offline RL] Epoch 25/100, PPO Loss: -0.0214, CD Loss: 0.0742
[Offline RL] Epoch 26/100, PPO Loss: -0.0209, CD Loss: 0.0881
[Offline RL] Epoch 27/100, PPO Loss: -0.0217, CD Loss: 0.0783
[Offline RL] Epoch 28/100, PPO Loss: -0.0217, CD Loss: 0.0781
[Offline RL] Epoch 29/100, PPO Loss: -0.0227, CD Loss: 0.0802
[Offline RL] Epoch 30/100, PPO Loss: -0.0220, CD Loss: 0.0740
[Offline RL] Epoch 31/100, PPO Loss: -0.0216, CD Loss: 0.0701
[Offline RL] Epoch 32/100, PPO Loss: -0.0233, CD Loss: 0.0716
[Offline RL] Epoch 33/100, PPO Loss: -0.0190, CD Loss: 0.0760
[Offline RL] Epoch 34/100, PPO Loss: -0.0181, CD Loss: 0.0777
[Offline RL] Epoch 35/100, PPO Loss: -0.0190, CD Loss: 0.0754
[Offline RL] Epoch 36/100, PPO Loss: -0.0191, CD Loss: 0.0751
[Offline RL] Epoch 37/100, PPO Loss: -0.0184, CD Loss: 0.0801
[Offline RL] Epoch 38/100, PPO Loss: -0.0180, CD Loss: 0.0798
[Offline RL] Epoch 39/100, PPO Loss: -0.0185, CD Loss: 0.0776
[Offline RL] Epoch 40/100, PPO Loss: -0.0196, CD Loss: 0.0840
[Offline RL] Epoch 41/100, PPO Loss: -0.0170, CD Loss: 0.0928
[Offline RL] Epoch 42/100, PPO Loss: -0.0180, CD Loss: 0.1005
[Offline RL] Epoch 43/100, PPO Loss: -0.0160, CD Loss: 0.0981
[Offline RL] Epoch 44/100, PPO Loss: -0.0161, CD Loss: 0.0996
[Offline RL] Epoch 45/100, PPO Loss: -0.0182, CD Loss: 0.1080
[Offline RL] Epoch 46/100, PPO Loss: -0.0164, CD Loss: 0.1043
[Offline RL] Epoch 47/100, PPO Loss: -0.0152, CD Loss: 0.1084
[Offline RL] Epoch 48/100, PPO Loss: -0.0168, CD Loss: 0.1165
[Offline RL] Epoch 49/100, PPO Loss: -0.0197, CD Loss: 0.1081
[Offline RL] Epoch 50/100, PPO Loss: -0.0158, CD Loss: 0.1073
[Offline RL] Epoch 51/100, PPO Loss: -0.0159, CD Loss: 0.1048
[Offline RL] Epoch 52/100, PPO Loss: -0.0189, CD Loss: 0.1044
[Offline RL] Epoch 53/100, PPO Loss: -0.0161, CD Loss: 0.1085
[Offline RL] Epoch 54/100, PPO Loss: -0.0181, CD Loss: 0.1137
[Offline RL] Epoch 55/100, PPO Loss: -0.0156, CD Loss: 0.1122
[Offline RL] Epoch 56/100, PPO Loss: -0.0169, CD Loss: 0.1084
[Offline RL] Epoch 57/100, PPO Loss: -0.0184, CD Loss: 0.1054
[Offline RL] Epoch 58/100, PPO Loss: -0.0162, CD Loss: 0.1122
[Offline RL] Epoch 59/100, PPO Loss: -0.0171, CD Loss: 0.1198
[Offline RL] Epoch 60/100, PPO Loss: -0.0161, CD Loss: 0.1193
[Offline RL] Epoch 61/100, PPO Loss: -0.0142, CD Loss: 0.1229
[Offline RL] Epoch 62/100, PPO Loss: -0.0158, CD Loss: 0.1280
[Offline RL] Epoch 63/100, PPO Loss: -0.0164, CD Loss: 0.1246
[Offline RL] Epoch 64/100, PPO Loss: -0.0173, CD Loss: 0.1246
[Offline RL] Epoch 65/100, PPO Loss: -0.0157, CD Loss: 0.1272
[Offline RL] Epoch 66/100, PPO Loss: -0.0167, CD Loss: 0.1336
[Offline RL] Epoch 67/100, PPO Loss: -0.0175, CD Loss: 0.1427
[Offline RL] Epoch 68/100, PPO Loss: -0.0198, CD Loss: 0.1516
[Offline RL] Epoch 69/100, PPO Loss: -0.0157, CD Loss: 0.1483
[Offline RL] Epoch 70/100, PPO Loss: -0.0172, CD Loss: 0.1454
[Offline RL] Epoch 71/100, PPO Loss: -0.0162, CD Loss: 0.1372
[Offline RL] Epoch 72/100, PPO Loss: -0.0152, CD Loss: 0.1361
[Offline RL] Epoch 73/100, PPO Loss: -0.0165, CD Loss: 0.1388
[Offline RL] Epoch 74/100, PPO Loss: -0.0165, CD Loss: 0.1373
[Offline RL] Epoch 75/100, PPO Loss: -0.0160, CD Loss: 0.1411
[Offline RL] Epoch 76/100, PPO Loss: -0.0176, CD Loss: 0.1384
[Offline RL] Epoch 77/100, PPO Loss: -0.0154, CD Loss: 0.1388
[Offline RL] Epoch 78/100, PPO Loss: -0.0159, CD Loss: 0.1388
[Offline RL] Epoch 79/100, PPO Loss: -0.0166, CD Loss: 0.1405
[Offline RL] Epoch 80/100, PPO Loss: -0.0163, CD Loss: 0.1456
[Offline RL] Epoch 81/100, PPO Loss: -0.0159, CD Loss: 0.1340
[Offline RL] Epoch 82/100, PPO Loss: -0.0173, CD Loss: 0.1373
[Offline RL] Epoch 83/100, PPO Loss: -0.0175, CD Loss: 0.1332
[Offline RL] Epoch 84/100, PPO Loss: -0.0171, CD Loss: 0.1303
[Offline RL] Epoch 85/100, PPO Loss: -0.0178, CD Loss: 0.1330
[Offline RL] Epoch 86/100, PPO Loss: -0.0152, CD Loss: 0.1351
[Offline RL] Epoch 87/100, PPO Loss: -0.0174, CD Loss: 0.1257
[Offline RL] Epoch 88/100, PPO Loss: -0.0180, CD Loss: 0.1168
[Offline RL] Epoch 89/100, PPO Loss: -0.0164, CD Loss: 0.1160
[Offline RL] Epoch 90/100, PPO Loss: -0.0171, CD Loss: 0.1056
[Offline RL] Epoch 91/100, PPO Loss: -0.0144, CD Loss: 0.1096
[Offline RL] Epoch 92/100, PPO Loss: -0.0180, CD Loss: 0.1155
[Offline RL] Epoch 93/100, PPO Loss: -0.0170, CD Loss: 0.1209
[Offline RL] Epoch 94/100, PPO Loss: -0.0176, CD Loss: 0.1191
[Offline RL] Epoch 95/100, PPO Loss: -0.0183, CD Loss: 0.1122
[Offline RL] Epoch 96/100, PPO Loss: -0.0175, CD Loss: 0.1242
[Offline RL] Epoch 97/100, PPO Loss: -0.0152, CD Loss: 0.1174
[Offline RL] Epoch 98/100, PPO Loss: -0.0176, CD Loss: 0.1271
[Offline RL] Epoch 99/100, PPO Loss: -0.0170, CD Loss: 0.1085
[OPE] Policy REJECTED: J_new=505.9098 ≤ J_old=505.9097 + δ=25.2955. Rolling back to behavior policy.

[RL100Trainer] Phase 2c: Collecting New Data (Iteration 1)
[Collect] 50 episodes, success=0.060, steps=1250
[Data Collection] Success Rate: 0.060, Reward: 8598.07, Episodes: 50, Steps: 1250
[Dataset] Merged 50 episodes (1250 steps) → total 4500 steps, 110 episodes

[RL100Trainer] Retraining IL on merged dataset...

============================================================
[RL100Trainer] Phase 1: Imitation Learning
============================================================

[IL] Epoch 0/100, Loss: 0.0709
[IL] Epoch 1/100, Loss: 0.0706
[IL] Epoch 2/100, Loss: 0.0670
[IL] Epoch 3/100, Loss: 0.0673
[IL] Epoch 4/100, Loss: 0.0678
[IL] Epoch 5/100, Loss: 0.0672
[IL] Epoch 6/100, Loss: 0.0669
[IL] Epoch 7/100, Loss: 0.0636
[IL] Epoch 8/100, Loss: 0.0675
[IL] Epoch 9/100, Loss: 0.0635
[IL] Epoch 10/100, Loss: 0.0657
[IL] Epoch 11/100, Loss: 0.0635
[IL] Epoch 12/100, Loss: 0.0614
[IL] Epoch 13/100, Loss: 0.0689
[IL] Epoch 14/100, Loss: 0.0666
[IL] Epoch 15/100, Loss: 0.0631
[IL] Epoch 16/100, Loss: 0.0595
[IL] Epoch 17/100, Loss: 0.0657
[IL] Epoch 18/100, Loss: 0.0670
[IL] Epoch 19/100, Loss: 0.0626
[IL] Epoch 20/100, Loss: 0.0652
[IL] Epoch 21/100, Loss: 0.0630
[IL] Epoch 22/100, Loss: 0.0634
[IL] Epoch 23/100, Loss: 0.0659
[IL] Epoch 24/100, Loss: 0.0636
[IL] Epoch 25/100, Loss: 0.0586
[IL] Epoch 26/100, Loss: 0.0640
[IL] Epoch 27/100, Loss: 0.0576
[IL] Epoch 28/100, Loss: 0.0590
[IL] Epoch 29/100, Loss: 0.0636
[IL] Epoch 30/100, Loss: 0.0608
[IL] Epoch 31/100, Loss: 0.0618
[IL] Epoch 32/100, Loss: 0.0586
[IL] Epoch 33/100, Loss: 0.0624
[IL] Epoch 34/100, Loss: 0.0611
[IL] Epoch 35/100, Loss: 0.0664
[IL] Epoch 36/100, Loss: 0.0595
[IL] Epoch 37/100, Loss: 0.0575
[IL] Epoch 38/100, Loss: 0.0624
[IL] Epoch 39/100, Loss: 0.0598
[IL] Epoch 40/100, Loss: 0.0603
[IL] Epoch 41/100, Loss: 0.0596
[IL] Epoch 42/100, Loss: 0.0591
[IL] Epoch 43/100, Loss: 0.0630
[IL] Epoch 44/100, Loss: 0.0604
[IL] Epoch 45/100, Loss: 0.0609
[IL] Epoch 46/100, Loss: 0.0607
[IL] Epoch 47/100, Loss: 0.0592
[IL] Epoch 48/100, Loss: 0.0599
[IL] Epoch 49/100, Loss: 0.0610
[IL] Epoch 50/100, Loss: 0.0608
[IL] Epoch 51/100, Loss: 0.0580
[IL] Epoch 52/100, Loss: 0.0569
[IL] Epoch 53/100, Loss: 0.0581
[IL] Epoch 54/100, Loss: 0.0586
[IL] Epoch 55/100, Loss: 0.0612
[IL] Epoch 56/100, Loss: 0.0604
[IL] Epoch 57/100, Loss: 0.0554
[IL] Epoch 58/100, Loss: 0.0599
[IL] Epoch 59/100, Loss: 0.0583
[IL] Epoch 60/100, Loss: 0.0584
[IL] Epoch 61/100, Loss: 0.0588
[IL] Epoch 62/100, Loss: 0.0600
[IL] Epoch 63/100, Loss: 0.0565
[IL] Epoch 64/100, Loss: 0.0556
[IL] Epoch 65/100, Loss: 0.0572
[IL] Epoch 66/100, Loss: 0.0565
[IL] Epoch 67/100, Loss: 0.0600
[IL] Epoch 68/100, Loss: 0.0582
[IL] Epoch 69/100, Loss: 0.0551
[IL] Epoch 70/100, Loss: 0.0578
[IL] Epoch 71/100, Loss: 0.0564
[IL] Epoch 72/100, Loss: 0.0571
[IL] Epoch 73/100, Loss: 0.0563
[IL] Epoch 74/100, Loss: 0.0570
[IL] Epoch 75/100, Loss: 0.0588
[IL] Epoch 76/100, Loss: 0.0559
[IL] Epoch 77/100, Loss: 0.0562
[IL] Epoch 78/100, Loss: 0.0576
[IL] Epoch 79/100, Loss: 0.0534
[IL] Epoch 80/100, Loss: 0.0602
[IL] Epoch 81/100, Loss: 0.0574
[IL] Epoch 82/100, Loss: 0.0549
[IL] Epoch 83/100, Loss: 0.0555
[IL] Epoch 84/100, Loss: 0.0541
[IL] Epoch 85/100, Loss: 0.0575
[IL] Epoch 86/100, Loss: 0.0546
[IL] Epoch 87/100, Loss: 0.0580
[IL] Epoch 88/100, Loss: 0.0552
[IL] Epoch 89/100, Loss: 0.0536
[IL] Epoch 90/100, Loss: 0.0563
[IL] Epoch 91/100, Loss: 0.0543
[IL] Epoch 92/100, Loss: 0.0536
[IL] Epoch 93/100, Loss: 0.0573
[IL] Epoch 94/100, Loss: 0.0536
[IL] Epoch 95/100, Loss: 0.0537
[IL] Epoch 96/100, Loss: 0.0545
[IL] Epoch 97/100, Loss: 0.0577
[IL] Epoch 98/100, Loss: 0.0558
[IL] Epoch 99/100, Loss: 0.0558
test_mean_score: 0.05
[IL] Eval - Success Rate: 0.050
[Checkpoint] Saved to /nfs_global/S/yangrongzheng/RL100/3D-Diffusion-Policy/3D-Diffusion-Policy/checkpoints/offline_iter_1.ckpt

================================================================================
               OFFLINE RL ITERATION 3/5
================================================================================


[RL100Trainer] Line 6 — Training Transition Model T_θ (Iteration 2)

[TransitionModel] Encoding dataset for transition model training...
[TransitionModel] Dataset: 3730 samples, input_dim=260, target_dim=257
[TransitionModel] Epoch    0 | train=9964.69434 | val=5250.67412 | no-improve=0/5
[TransitionModel] Epoch   20 | train=2856.34969 | val=3843.08120 | no-improve=0/5
[TransitionModel] Epoch   40 | train=1686.51120 | val=3719.49502 | no-improve=4/5
[TransitionModel] Epoch   41 | train=1633.05830 | val=3790.27710 | no-improve=5/5
[TransitionModel] Training complete. Elites=[0, 5, 2, 3, 6], val_loss=3576.63540

[RL100Trainer] Phase 2a: Training IQL Critics (Iteration 2)
[IQL] Epoch 0/150, V Loss: 8.6456, Q Loss: 11122036.5333
[IQL] Epoch 1/150, V Loss: 13.1915, Q Loss: 11068447.8000
[IQL] Epoch 2/150, V Loss: 15.3918, Q Loss: 11197279.6667
[IQL] Epoch 3/150, V Loss: 15.4677, Q Loss: 11041110.7333
[IQL] Epoch 4/150, V Loss: 15.0697, Q Loss: 11125370.6667
[IQL] Epoch 5/150, V Loss: 14.4971, Q Loss: 11068115.2667
[IQL] Epoch 6/150, V Loss: 14.5487, Q Loss: 11154733.3333
[IQL] Epoch 7/150, V Loss: 14.8027, Q Loss: 11143850.6000
[IQL] Epoch 8/150, V Loss: 14.8041, Q Loss: 11170217.2667
[IQL] Epoch 9/150, V Loss: 14.5717, Q Loss: 11199824.6333
[IQL] Epoch 10/150, V Loss: 14.9878, Q Loss: 11100841.4000
[IQL] Epoch 11/150, V Loss: 14.7520, Q Loss: 11042588.0000
[IQL] Epoch 12/150, V Loss: 14.3103, Q Loss: 11057467.8000
[IQL] Epoch 13/150, V Loss: 14.4524, Q Loss: 11006683.3333
[IQL] Epoch 14/150, V Loss: 14.6505, Q Loss: 11131037.4667
[IQL] Epoch 15/150, V Loss: 14.5074, Q Loss: 11078142.6000
[IQL] Epoch 16/150, V Loss: 14.5254, Q Loss: 11121624.2333
[IQL] Epoch 17/150, V Loss: 14.8118, Q Loss: 11006749.8667
[IQL] Epoch 18/150, V Loss: 14.2023, Q Loss: 11114838.1667
[IQL] Epoch 19/150, V Loss: 13.9114, Q Loss: 11121432.2667
[IQL] Epoch 20/150, V Loss: 14.4570, Q Loss: 11113723.3333
[IQL] Epoch 21/150, V Loss: 14.3018, Q Loss: 11012798.3000
[IQL] Epoch 22/150, V Loss: 14.3445, Q Loss: 11084843.8000
[IQL] Epoch 23/150, V Loss: 14.5400, Q Loss: 11011259.8667
[IQL] Epoch 24/150, V Loss: 14.2848, Q Loss: 11102094.3333
[IQL] Epoch 25/150, V Loss: 14.4596, Q Loss: 10984126.3333
[IQL] Epoch 26/150, V Loss: 13.9800, Q Loss: 11253364.4000
[IQL] Epoch 27/150, V Loss: 14.3556, Q Loss: 10994762.2000
[IQL] Epoch 28/150, V Loss: 14.5238, Q Loss: 11012830.0000
[IQL] Epoch 29/150, V Loss: 14.2844, Q Loss: 11087233.7000
[IQL] Epoch 30/150, V Loss: 14.3956, Q Loss: 11032348.5667
[IQL] Epoch 31/150, V Loss: 14.2740, Q Loss: 11054803.0667
[IQL] Epoch 32/150, V Loss: 14.1931, Q Loss: 10945651.0000
[IQL] Epoch 33/150, V Loss: 14.1593, Q Loss: 11064600.0000
[IQL] Epoch 34/150, V Loss: 14.0339, Q Loss: 11037084.6000
[IQL] Epoch 35/150, V Loss: 14.1413, Q Loss: 10942802.1000
[IQL] Epoch 36/150, V Loss: 14.1404, Q Loss: 11054953.4667
[IQL] Epoch 37/150, V Loss: 14.2484, Q Loss: 11047793.8000
[IQL] Epoch 38/150, V Loss: 14.0700, Q Loss: 10949864.9333
[IQL] Epoch 39/150, V Loss: 13.9326, Q Loss: 11010609.4667
[IQL] Epoch 40/150, V Loss: 13.7577, Q Loss: 11120641.7667
[IQL] Epoch 41/150, V Loss: 14.1196, Q Loss: 11054899.8000
[IQL] Epoch 42/150, V Loss: 14.2734, Q Loss: 11104531.6000
[IQL] Epoch 43/150, V Loss: 14.2772, Q Loss: 10890707.8333
[IQL] Epoch 44/150, V Loss: 14.1482, Q Loss: 10947319.0333
[IQL] Epoch 45/150, V Loss: 13.9282, Q Loss: 11018232.4667
[IQL] Epoch 46/150, V Loss: 14.0529, Q Loss: 10996465.9667
[IQL] Epoch 47/150, V Loss: 13.8251, Q Loss: 11068404.0000
[IQL] Epoch 48/150, V Loss: 14.0866, Q Loss: 10997649.0667
[IQL] Epoch 49/150, V Loss: 13.9899, Q Loss: 11010974.0667
[IQL] Epoch 50/150, V Loss: 13.8618, Q Loss: 10995342.4000
[IQL] Epoch 51/150, V Loss: 13.8586, Q Loss: 11020295.4000
[IQL] Epoch 52/150, V Loss: 14.0350, Q Loss: 11021172.9000
[IQL] Epoch 53/150, V Loss: 13.9667, Q Loss: 11032172.6000
[IQL] Epoch 54/150, V Loss: 14.0492, Q Loss: 11020606.5333
[IQL] Epoch 55/150, V Loss: 14.0576, Q Loss: 11003937.8667
[IQL] Epoch 56/150, V Loss: 14.0928, Q Loss: 10995256.8667
[IQL] Epoch 57/150, V Loss: 13.9437, Q Loss: 10941261.4000
[IQL] Epoch 58/150, V Loss: 13.8524, Q Loss: 10997891.1333
[IQL] Epoch 59/150, V Loss: 13.6965, Q Loss: 10967274.3333
[IQL] Epoch 60/150, V Loss: 13.6882, Q Loss: 11016706.9333
[IQL] Epoch 61/150, V Loss: 13.9517, Q Loss: 10925294.8667
[IQL] Epoch 62/150, V Loss: 13.9703, Q Loss: 10966885.5333
[IQL] Epoch 63/150, V Loss: 13.4706, Q Loss: 11048622.6000
[IQL] Epoch 64/150, V Loss: 13.9308, Q Loss: 10991369.0667
[IQL] Epoch 65/150, V Loss: 14.0157, Q Loss: 11153423.1000
[IQL] Epoch 66/150, V Loss: 13.9861, Q Loss: 10845057.4667
[IQL] Epoch 67/150, V Loss: 13.8341, Q Loss: 10947767.6667
[IQL] Epoch 68/150, V Loss: 13.6055, Q Loss: 10898083.5333
[IQL] Epoch 69/150, V Loss: 13.4905, Q Loss: 10981345.4667
[IQL] Epoch 70/150, V Loss: 13.6830, Q Loss: 10972395.1000
[IQL] Epoch 71/150, V Loss: 13.6803, Q Loss: 10971944.1333
[IQL] Epoch 72/150, V Loss: 13.7783, Q Loss: 10982570.3333
[IQL] Epoch 73/150, V Loss: 13.6937, Q Loss: 10925299.4000
[IQL] Epoch 74/150, V Loss: 13.5248, Q Loss: 10975775.4667
[IQL] Epoch 75/150, V Loss: 13.5884, Q Loss: 10955385.6667
[IQL] Epoch 76/150, V Loss: 13.7695, Q Loss: 10944124.2667
[IQL] Epoch 77/150, V Loss: 13.9039, Q Loss: 10919254.9667
[IQL] Epoch 78/150, V Loss: 13.6053, Q Loss: 10870970.6000
[IQL] Epoch 79/150, V Loss: 13.3638, Q Loss: 10979657.4000
[IQL] Epoch 80/150, V Loss: 13.4434, Q Loss: 10905332.5333
[IQL] Epoch 81/150, V Loss: 13.7131, Q Loss: 10838491.1667
[IQL] Epoch 82/150, V Loss: 13.4882, Q Loss: 11019340.0000
[IQL] Epoch 83/150, V Loss: 13.4569, Q Loss: 10948919.0333
[IQL] Epoch 84/150, V Loss: 13.7669, Q Loss: 10923684.4667
[IQL] Epoch 85/150, V Loss: 13.5372, Q Loss: 11044767.5333
[IQL] Epoch 86/150, V Loss: 13.3850, Q Loss: 10932088.2000
[IQL] Epoch 87/150, V Loss: 13.6656, Q Loss: 10993889.2000
[IQL] Epoch 88/150, V Loss: 13.6392, Q Loss: 10986150.1333
[IQL] Epoch 89/150, V Loss: 13.6258, Q Loss: 10853252.7667
[IQL] Epoch 90/150, V Loss: 13.5163, Q Loss: 10967731.5333
[IQL] Epoch 91/150, V Loss: 13.1956, Q Loss: 10963795.2667
[IQL] Epoch 92/150, V Loss: 13.5508, Q Loss: 10917078.1333
[IQL] Epoch 93/150, V Loss: 13.7399, Q Loss: 10914932.3333
[IQL] Epoch 94/150, V Loss: 13.3651, Q Loss: 10983645.9333
[IQL] Epoch 95/150, V Loss: 13.3564, Q Loss: 10927005.0000
[IQL] Epoch 96/150, V Loss: 13.4866, Q Loss: 11072093.3333
[IQL] Epoch 97/150, V Loss: 13.3584, Q Loss: 10864960.0667
[IQL] Epoch 98/150, V Loss: 13.2693, Q Loss: 11021404.1667
[IQL] Epoch 99/150, V Loss: 13.6082, Q Loss: 10890543.9333
[IQL] Epoch 100/150, V Loss: 13.6418, Q Loss: 10944248.6667
[IQL] Epoch 101/150, V Loss: 13.4996, Q Loss: 10883032.3667
[IQL] Epoch 102/150, V Loss: 13.4448, Q Loss: 10801112.5333
[IQL] Epoch 103/150, V Loss: 13.1078, Q Loss: 10847670.2667
[IQL] Epoch 104/150, V Loss: 13.0868, Q Loss: 10975627.9333
[IQL] Epoch 105/150, V Loss: 13.2599, Q Loss: 10910581.9333
[IQL] Epoch 106/150, V Loss: 13.4040, Q Loss: 10914330.0000
[IQL] Epoch 107/150, V Loss: 13.2095, Q Loss: 10952736.3333
[IQL] Epoch 108/150, V Loss: 13.3621, Q Loss: 11004885.5000
[IQL] Epoch 109/150, V Loss: 13.4077, Q Loss: 10901950.4000
[IQL] Epoch 110/150, V Loss: 13.3470, Q Loss: 10821718.1667
[IQL] Epoch 111/150, V Loss: 13.1763, Q Loss: 10846953.6667
[IQL] Epoch 112/150, V Loss: 13.0775, Q Loss: 10784501.2000
[IQL] Epoch 113/150, V Loss: 13.1143, Q Loss: 10862822.4000
[IQL] Epoch 114/150, V Loss: 12.9111, Q Loss: 10844153.2000
[IQL] Epoch 115/150, V Loss: 13.1210, Q Loss: 10816258.6000
[IQL] Epoch 116/150, V Loss: 13.2517, Q Loss: 10827446.0333
[IQL] Epoch 117/150, V Loss: 13.2286, Q Loss: 10851400.8000
[IQL] Epoch 118/150, V Loss: 13.1693, Q Loss: 10818399.0667
[IQL] Epoch 119/150, V Loss: 12.9184, Q Loss: 10865960.9333
[IQL] Epoch 120/150, V Loss: 12.7800, Q Loss: 11000174.9000
[IQL] Epoch 121/150, V Loss: 13.2564, Q Loss: 10904828.6000
[IQL] Epoch 122/150, V Loss: 13.1065, Q Loss: 10769038.4000
[IQL] Epoch 123/150, V Loss: 13.1091, Q Loss: 10807334.8000
[IQL] Epoch 124/150, V Loss: 13.2022, Q Loss: 10819485.4000
[IQL] Epoch 125/150, V Loss: 12.9486, Q Loss: 10854588.6667
[IQL] Epoch 126/150, V Loss: 12.8492, Q Loss: 10866358.5667
[IQL] Epoch 127/150, V Loss: 12.8621, Q Loss: 10950663.3333
[IQL] Epoch 128/150, V Loss: 12.9450, Q Loss: 10855133.1667
[IQL] Epoch 129/150, V Loss: 13.0609, Q Loss: 10927698.2000
[IQL] Epoch 130/150, V Loss: 13.1077, Q Loss: 10955437.4000
[IQL] Epoch 131/150, V Loss: 13.3197, Q Loss: 10828954.2667
[IQL] Epoch 132/150, V Loss: 13.0721, Q Loss: 10830727.7333
[IQL] Epoch 133/150, V Loss: 13.1218, Q Loss: 10787020.4667
[IQL] Epoch 134/150, V Loss: 12.8321, Q Loss: 10832158.1333
[IQL] Epoch 135/150, V Loss: 12.5476, Q Loss: 10829306.4000
[IQL] Epoch 136/150, V Loss: 12.7587, Q Loss: 10836221.7000
[IQL] Epoch 137/150, V Loss: 13.1018, Q Loss: 10728660.0000
[IQL] Epoch 138/150, V Loss: 12.8320, Q Loss: 10861727.8000
[IQL] Epoch 139/150, V Loss: 12.6696, Q Loss: 10832055.8667
[IQL] Epoch 140/150, V Loss: 12.7778, Q Loss: 10850939.3333
[IQL] Epoch 141/150, V Loss: 13.0521, Q Loss: 10892305.4000
[IQL] Epoch 142/150, V Loss: 13.1314, Q Loss: 10762587.6667
[IQL] Epoch 143/150, V Loss: 12.6724, Q Loss: 10802787.8667
[IQL] Epoch 144/150, V Loss: 12.5984, Q Loss: 10835912.8000
[IQL] Epoch 145/150, V Loss: 12.6978, Q Loss: 10878124.2667
[IQL] Epoch 146/150, V Loss: 12.8941, Q Loss: 10843219.1333
[IQL] Epoch 147/150, V Loss: 12.9556, Q Loss: 10852593.0000
[IQL] Epoch 148/150, V Loss: 12.8634, Q Loss: 10821859.8667
[IQL] Epoch 149/150, V Loss: 12.9025, Q Loss: 10780952.7000

[RL100Trainer] Phase 2b: Offline RL Optimization (Iteration 2)
[OPE] Behavior policy value J_old = 1220.9726
[Offline RL] Epoch 0/100, PPO Loss: -0.0261, CD Loss: 0.2392
[Offline RL] Epoch 1/100, PPO Loss: -0.0245, CD Loss: 0.1576
[Offline RL] Epoch 2/100, PPO Loss: -0.0219, CD Loss: 0.1328
[Offline RL] Epoch 3/100, PPO Loss: -0.0263, CD Loss: 0.1149
[Offline RL] Epoch 4/100, PPO Loss: -0.0245, CD Loss: 0.1158
[Offline RL] Epoch 5/100, PPO Loss: -0.0246, CD Loss: 0.1272
[Offline RL] Epoch 6/100, PPO Loss: -0.0246, CD Loss: 0.1149
[Offline RL] Epoch 7/100, PPO Loss: -0.0240, CD Loss: 0.1372
[Offline RL] Epoch 8/100, PPO Loss: -0.0228, CD Loss: 0.1244
[Offline RL] Epoch 9/100, PPO Loss: -0.0235, CD Loss: 0.1232
[Offline RL] Epoch 10/100, PPO Loss: -0.0224, CD Loss: 0.1330
[Offline RL] Epoch 11/100, PPO Loss: -0.0198, CD Loss: 0.1195
[Offline RL] Epoch 12/100, PPO Loss: -0.0188, CD Loss: 0.1084
[Offline RL] Epoch 13/100, PPO Loss: -0.0209, CD Loss: 0.1251
