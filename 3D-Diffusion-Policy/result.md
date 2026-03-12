Job start at 2026-03-10 23:48:18
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
ext-zone00.nas02.future.cn:/nfs_global            404T  390T   14T  97% /nfs_global
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
          /home  14448M  16384M  20480M            168k       0       0        

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
  use_recon_vib: true
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
  reward_scale: 10.0
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
  critic_epochs: 500
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
[DP3Encoder] use_recon_vib: True
[DP3Encoder] beta_recon: 0.0001, beta_kl: 0.0001
[PointNetEncoderXYZ] use_layernorm: True
[PointNetEncoderXYZ] use_final_norm: layernorm
[PointNetEncoderXYZ] use_vib: True
[PointNetEncoderXYZ] VIB enabled with reconstruction decoder
[DP3Encoder] State reconstruction decoder initialized
[DP3Encoder] output dim: 128
[DiffusionUnetHybridPointcloudPolicy] use_pc_color: False
[DiffusionUnetHybridPointcloudPolicy] pointnet_type: pointnet
[2026-03-10 23:48:45,573][diffusion_policy_3d.model.diffusion.conditional_unet1d][INFO] - number of parameters: 2.550744e+08
----------------------------------
Class name: RL100Policy
  Number of parameters: 255.5873M
   _dummy_variable: 0.0000M (0.00%)
   obs_encoder: 0.5129M (0.20%)
   model: 255.0744M (99.80%)
   mask_generator: 0.0000M (0.00%)
----------------------------------
[RL100Trainer] Initializing IQL Critics...
[RL100Trainer] Initializing Consistency Model...
[2026-03-10 23:48:47,703][diffusion_policy_3d.model.diffusion.conditional_unet1d][INFO] - number of parameters: 2.550744e+08
[RL100Trainer] Initializing Transition Model T_θ(s'|s,a)...
[Setup] RL100Trainer initialized

[Training] Starting RL-100 pipeline...

================================================================================
                    RL-100 TRAINING PIPELINE
================================================================================


============================================================
[RL100Trainer] Phase 1: Imitation Learning
============================================================

[IL] Epoch 0/1000, Loss: 1.3755
[IL] Epoch 1/1000, Loss: 1.0124
[IL] Epoch 2/1000, Loss: 0.9780
[IL] Epoch 3/1000, Loss: 0.9401
[IL] Epoch 4/1000, Loss: 0.7420
[IL] Epoch 5/1000, Loss: 0.4956
[IL] Epoch 6/1000, Loss: 0.3347
[IL] Epoch 7/1000, Loss: 0.2560
[IL] Epoch 8/1000, Loss: 0.2057
[IL] Epoch 9/1000, Loss: 0.1860
[IL] Epoch 10/1000, Loss: 0.1778
[IL] Epoch 11/1000, Loss: 0.1537
[IL] Epoch 12/1000, Loss: 0.1328
[IL] Epoch 13/1000, Loss: 0.1285
[IL] Epoch 14/1000, Loss: 0.1173
[IL] Epoch 15/1000, Loss: 0.1147
[IL] Epoch 16/1000, Loss: 0.1109
[IL] Epoch 17/1000, Loss: 0.1065
[IL] Epoch 18/1000, Loss: 0.1047
[IL] Epoch 19/1000, Loss: 0.0988
[IL] Epoch 20/1000, Loss: 0.1012
[IL] Epoch 21/1000, Loss: 0.0969
[IL] Epoch 22/1000, Loss: 0.0934
[IL] Epoch 23/1000, Loss: 0.0907
[IL] Epoch 24/1000, Loss: 0.0836
[IL] Epoch 25/1000, Loss: 0.0856
[IL] Epoch 26/1000, Loss: 0.0814
[IL] Epoch 27/1000, Loss: 0.0828
[IL] Epoch 28/1000, Loss: 0.0775
[IL] Epoch 29/1000, Loss: 0.0742
[IL] Epoch 30/1000, Loss: 0.0731
[IL] Epoch 31/1000, Loss: 0.0728
[IL] Epoch 32/1000, Loss: 0.0727
[IL] Epoch 33/1000, Loss: 0.0679
[IL] Epoch 34/1000, Loss: 0.0704
[IL] Epoch 35/1000, Loss: 0.0678
[IL] Epoch 36/1000, Loss: 0.0709
[IL] Epoch 37/1000, Loss: 0.0658
[IL] Epoch 38/1000, Loss: 0.0682
[IL] Epoch 39/1000, Loss: 0.0669
[IL] Epoch 40/1000, Loss: 0.0684
[IL] Epoch 41/1000, Loss: 0.0660
[IL] Epoch 42/1000, Loss: 0.0622
[IL] Epoch 43/1000, Loss: 0.0587
[IL] Epoch 44/1000, Loss: 0.0626
[IL] Epoch 45/1000, Loss: 0.0628
[IL] Epoch 46/1000, Loss: 0.0607
[IL] Epoch 47/1000, Loss: 0.0610
[IL] Epoch 48/1000, Loss: 0.0592
[IL] Epoch 49/1000, Loss: 0.0610
[IL] Epoch 50/1000, Loss: 0.0546
[IL] Epoch 51/1000, Loss: 0.0548
[IL] Epoch 52/1000, Loss: 0.0542
[IL] Epoch 53/1000, Loss: 0.0549
[IL] Epoch 54/1000, Loss: 0.0519
[IL] Epoch 55/1000, Loss: 0.0518
[IL] Epoch 56/1000, Loss: 0.0535
[IL] Epoch 57/1000, Loss: 0.0515
[IL] Epoch 58/1000, Loss: 0.0531
[IL] Epoch 59/1000, Loss: 0.0498
[IL] Epoch 60/1000, Loss: 0.0516
[IL] Epoch 61/1000, Loss: 0.0497
[IL] Epoch 62/1000, Loss: 0.0480
[IL] Epoch 63/1000, Loss: 0.0527
[IL] Epoch 64/1000, Loss: 0.0487
[IL] Epoch 65/1000, Loss: 0.0481
[IL] Epoch 66/1000, Loss: 0.0479
[IL] Epoch 67/1000, Loss: 0.0481
[IL] Epoch 68/1000, Loss: 0.0486
[IL] Epoch 69/1000, Loss: 0.0499
[IL] Epoch 70/1000, Loss: 0.0481
[IL] Epoch 71/1000, Loss: 0.0461
[IL] Epoch 72/1000, Loss: 0.0459
[IL] Epoch 73/1000, Loss: 0.0464
[IL] Epoch 74/1000, Loss: 0.0455
[IL] Epoch 75/1000, Loss: 0.0478
[IL] Epoch 76/1000, Loss: 0.0469
[IL] Epoch 77/1000, Loss: 0.0459
[IL] Epoch 78/1000, Loss: 0.0472
[IL] Epoch 79/1000, Loss: 0.0467
[IL] Epoch 80/1000, Loss: 0.0439
[IL] Epoch 81/1000, Loss: 0.0466
[IL] Epoch 82/1000, Loss: 0.0437
[IL] Epoch 83/1000, Loss: 0.0453
[IL] Epoch 84/1000, Loss: 0.0405
[IL] Epoch 85/1000, Loss: 0.0407
[IL] Epoch 86/1000, Loss: 0.0433
[IL] Epoch 87/1000, Loss: 0.0404
[IL] Epoch 88/1000, Loss: 0.0420
[IL] Epoch 89/1000, Loss: 0.0420
[IL] Epoch 90/1000, Loss: 0.0404
[IL] Epoch 91/1000, Loss: 0.0406
[IL] Epoch 92/1000, Loss: 0.0415
[IL] Epoch 93/1000, Loss: 0.0397
[IL] Epoch 94/1000, Loss: 0.0409
[IL] Epoch 95/1000, Loss: 0.0416
[IL] Epoch 96/1000, Loss: 0.0408
[IL] Epoch 97/1000, Loss: 0.0415
[IL] Epoch 98/1000, Loss: 0.0418
[IL] Epoch 99/1000, Loss: 0.0392
test_mean_score: 0.05
[IL] Eval - Success Rate: 0.050
[IL] Epoch 100/1000, Loss: 0.0369
[IL] Epoch 101/1000, Loss: 0.0398
[IL] Epoch 102/1000, Loss: 0.0404
[IL] Epoch 103/1000, Loss: 0.0406
[IL] Epoch 104/1000, Loss: 0.0392
[IL] Epoch 105/1000, Loss: 0.0383
[IL] Epoch 106/1000, Loss: 0.0374
[IL] Epoch 107/1000, Loss: 0.0376
[IL] Epoch 108/1000, Loss: 0.0378
[IL] Epoch 109/1000, Loss: 0.0372
[IL] Epoch 110/1000, Loss: 0.0362
[IL] Epoch 111/1000, Loss: 0.0394
[IL] Epoch 112/1000, Loss: 0.0364
[IL] Epoch 113/1000, Loss: 0.0382
[IL] Epoch 114/1000, Loss: 0.0380
[IL] Epoch 115/1000, Loss: 0.0386
[IL] Epoch 116/1000, Loss: 0.0374
[IL] Epoch 117/1000, Loss: 0.0372
[IL] Epoch 118/1000, Loss: 0.0352
[IL] Epoch 119/1000, Loss: 0.0366
[IL] Epoch 120/1000, Loss: 0.0366
[IL] Epoch 121/1000, Loss: 0.0357
[IL] Epoch 122/1000, Loss: 0.0347
[IL] Epoch 123/1000, Loss: 0.0365
[IL] Epoch 124/1000, Loss: 0.0340
[IL] Epoch 125/1000, Loss: 0.0355
[IL] Epoch 126/1000, Loss: 0.0362
[IL] Epoch 127/1000, Loss: 0.0336
[IL] Epoch 128/1000, Loss: 0.0342
[IL] Epoch 129/1000, Loss: 0.0345
[IL] Epoch 130/1000, Loss: 0.0343
[IL] Epoch 131/1000, Loss: 0.0354
[IL] Epoch 132/1000, Loss: 0.0342
[IL] Epoch 133/1000, Loss: 0.0335
[IL] Epoch 134/1000, Loss: 0.0355
[IL] Epoch 135/1000, Loss: 0.0355
[IL] Epoch 136/1000, Loss: 0.0341
[IL] Epoch 137/1000, Loss: 0.0336
[IL] Epoch 138/1000, Loss: 0.0338
[IL] Epoch 139/1000, Loss: 0.0310
[IL] Epoch 140/1000, Loss: 0.0323
[IL] Epoch 141/1000, Loss: 0.0326
[IL] Epoch 142/1000, Loss: 0.0329
[IL] Epoch 143/1000, Loss: 0.0342
[IL] Epoch 144/1000, Loss: 0.0329
[IL] Epoch 145/1000, Loss: 0.0335
[IL] Epoch 146/1000, Loss: 0.0329
[IL] Epoch 147/1000, Loss: 0.0327
[IL] Epoch 148/1000, Loss: 0.0318
[IL] Epoch 149/1000, Loss: 0.0339
[IL] Epoch 150/1000, Loss: 0.0318
[IL] Epoch 151/1000, Loss: 0.0310
[IL] Epoch 152/1000, Loss: 0.0310
[IL] Epoch 153/1000, Loss: 0.0307
[IL] Epoch 154/1000, Loss: 0.0334
[IL] Epoch 155/1000, Loss: 0.0339
[IL] Epoch 156/1000, Loss: 0.0317
[IL] Epoch 157/1000, Loss: 0.0299
[IL] Epoch 158/1000, Loss: 0.0312
[IL] Epoch 159/1000, Loss: 0.0323
[IL] Epoch 160/1000, Loss: 0.0300
[IL] Epoch 161/1000, Loss: 0.0309
[IL] Epoch 162/1000, Loss: 0.0302
[IL] Epoch 163/1000, Loss: 0.0325
[IL] Epoch 164/1000, Loss: 0.0312
[IL] Epoch 165/1000, Loss: 0.0309
[IL] Epoch 166/1000, Loss: 0.0297
[IL] Epoch 167/1000, Loss: 0.0297
[IL] Epoch 168/1000, Loss: 0.0303
[IL] Epoch 169/1000, Loss: 0.0307
[IL] Epoch 170/1000, Loss: 0.0312
[IL] Epoch 171/1000, Loss: 0.0313
[IL] Epoch 172/1000, Loss: 0.0315
[IL] Epoch 173/1000, Loss: 0.0310
[IL] Epoch 174/1000, Loss: 0.0307
[IL] Epoch 175/1000, Loss: 0.0289
[IL] Epoch 176/1000, Loss: 0.0297
[IL] Epoch 177/1000, Loss: 0.0294
[IL] Epoch 178/1000, Loss: 0.0302
[IL] Epoch 179/1000, Loss: 0.0303
[IL] Epoch 180/1000, Loss: 0.0295
[IL] Epoch 181/1000, Loss: 0.0293
[IL] Epoch 182/1000, Loss: 0.0299
[IL] Epoch 183/1000, Loss: 0.0279
[IL] Epoch 184/1000, Loss: 0.0283
[IL] Epoch 185/1000, Loss: 0.0299
[IL] Epoch 186/1000, Loss: 0.0280
[IL] Epoch 187/1000, Loss: 0.0293
[IL] Epoch 188/1000, Loss: 0.0307
[IL] Epoch 189/1000, Loss: 0.0293
[IL] Epoch 190/1000, Loss: 0.0287
[IL] Epoch 191/1000, Loss: 0.0276
[IL] Epoch 192/1000, Loss: 0.0282
[IL] Epoch 193/1000, Loss: 0.0279
[IL] Epoch 194/1000, Loss: 0.0286
[IL] Epoch 195/1000, Loss: 0.0306
[IL] Epoch 196/1000, Loss: 0.0274
[IL] Epoch 197/1000, Loss: 0.0277
[IL] Epoch 198/1000, Loss: 0.0267
[IL] Epoch 199/1000, Loss: 0.0285
test_mean_score: 0.1
[IL] Eval - Success Rate: 0.100
[IL] Epoch 200/1000, Loss: 0.0281
[IL] Epoch 201/1000, Loss: 0.0273
[IL] Epoch 202/1000, Loss: 0.0286
[IL] Epoch 203/1000, Loss: 0.0287
[IL] Epoch 204/1000, Loss: 0.0257
[IL] Epoch 205/1000, Loss: 0.0265
[IL] Epoch 206/1000, Loss: 0.0263
[IL] Epoch 207/1000, Loss: 0.0275
[IL] Epoch 208/1000, Loss: 0.0269
[IL] Epoch 209/1000, Loss: 0.0261
[IL] Epoch 210/1000, Loss: 0.0275
[IL] Epoch 211/1000, Loss: 0.0272
[IL] Epoch 212/1000, Loss: 0.0271
[IL] Epoch 213/1000, Loss: 0.0249
[IL] Epoch 214/1000, Loss: 0.0265
[IL] Epoch 215/1000, Loss: 0.0265
[IL] Epoch 216/1000, Loss: 0.0247
[IL] Epoch 217/1000, Loss: 0.0255
[IL] Epoch 218/1000, Loss: 0.0251
[IL] Epoch 219/1000, Loss: 0.0249
[IL] Epoch 220/1000, Loss: 0.0243
[IL] Epoch 221/1000, Loss: 0.0250
[IL] Epoch 222/1000, Loss: 0.0244
[IL] Epoch 223/1000, Loss: 0.0252
[IL] Epoch 224/1000, Loss: 0.0224
[IL] Epoch 225/1000, Loss: 0.0259
[IL] Epoch 226/1000, Loss: 0.0280
[IL] Epoch 227/1000, Loss: 0.0258
[IL] Epoch 228/1000, Loss: 0.0258
[IL] Epoch 229/1000, Loss: 0.0265
[IL] Epoch 230/1000, Loss: 0.0251
[IL] Epoch 231/1000, Loss: 0.0254
[IL] Epoch 232/1000, Loss: 0.0239
[IL] Epoch 233/1000, Loss: 0.0244
[IL] Epoch 234/1000, Loss: 0.0228
[IL] Epoch 235/1000, Loss: 0.0255
[IL] Epoch 236/1000, Loss: 0.0236
[IL] Epoch 237/1000, Loss: 0.0237
[IL] Epoch 238/1000, Loss: 0.0230
[IL] Epoch 239/1000, Loss: 0.0247
[IL] Epoch 240/1000, Loss: 0.0238
[IL] Epoch 241/1000, Loss: 0.0242
[IL] Epoch 242/1000, Loss: 0.0242
[IL] Epoch 243/1000, Loss: 0.0250
[IL] Epoch 244/1000, Loss: 0.0247
[IL] Epoch 245/1000, Loss: 0.0240
[IL] Epoch 246/1000, Loss: 0.0238
[IL] Epoch 247/1000, Loss: 0.0247
[IL] Epoch 248/1000, Loss: 0.0232
[IL] Epoch 249/1000, Loss: 0.0236
[IL] Epoch 250/1000, Loss: 0.0225
[IL] Epoch 251/1000, Loss: 0.0228
[IL] Epoch 252/1000, Loss: 0.0233
[IL] Epoch 253/1000, Loss: 0.0223
[IL] Epoch 254/1000, Loss: 0.0240
[IL] Epoch 255/1000, Loss: 0.0231
[IL] Epoch 256/1000, Loss: 0.0229
[IL] Epoch 257/1000, Loss: 0.0237
[IL] Epoch 258/1000, Loss: 0.0226
[IL] Epoch 259/1000, Loss: 0.0231
[IL] Epoch 260/1000, Loss: 0.0212
[IL] Epoch 261/1000, Loss: 0.0209
[IL] Epoch 262/1000, Loss: 0.0222
[IL] Epoch 263/1000, Loss: 0.0219
[IL] Epoch 264/1000, Loss: 0.0240
[IL] Epoch 265/1000, Loss: 0.0230
[IL] Epoch 266/1000, Loss: 0.0236
[IL] Epoch 267/1000, Loss: 0.0238
[IL] Epoch 268/1000, Loss: 0.0221
[IL] Epoch 269/1000, Loss: 0.0219
[IL] Epoch 270/1000, Loss: 0.0221
[IL] Epoch 271/1000, Loss: 0.0209
[IL] Epoch 272/1000, Loss: 0.0222
[IL] Epoch 273/1000, Loss: 0.0220
[IL] Epoch 274/1000, Loss: 0.0227
[IL] Epoch 275/1000, Loss: 0.0219
[IL] Epoch 276/1000, Loss: 0.0216
[IL] Epoch 277/1000, Loss: 0.0216
[IL] Epoch 278/1000, Loss: 0.0201
[IL] Epoch 279/1000, Loss: 0.0218
[IL] Epoch 280/1000, Loss: 0.0203
[IL] Epoch 281/1000, Loss: 0.0205
[IL] Epoch 282/1000, Loss: 0.0228
[IL] Epoch 283/1000, Loss: 0.0205
[IL] Epoch 284/1000, Loss: 0.0209
[IL] Epoch 285/1000, Loss: 0.0212
[IL] Epoch 286/1000, Loss: 0.0225
[IL] Epoch 287/1000, Loss: 0.0207
[IL] Epoch 288/1000, Loss: 0.0221
[IL] Epoch 289/1000, Loss: 0.0219
[IL] Epoch 290/1000, Loss: 0.0226
[IL] Epoch 291/1000, Loss: 0.0209
[IL] Epoch 292/1000, Loss: 0.0216
[IL] Epoch 293/1000, Loss: 0.0215
[IL] Epoch 294/1000, Loss: 0.0213
[IL] Epoch 295/1000, Loss: 0.0213
[IL] Epoch 296/1000, Loss: 0.0213
[IL] Epoch 297/1000, Loss: 0.0199
[IL] Epoch 298/1000, Loss: 0.0206
[IL] Epoch 299/1000, Loss: 0.0214
test_mean_score: 0.25
[IL] Eval - Success Rate: 0.250
[IL] Epoch 300/1000, Loss: 0.0207
[IL] Epoch 301/1000, Loss: 0.0206
[IL] Epoch 302/1000, Loss: 0.0212
[IL] Epoch 303/1000, Loss: 0.0198
[IL] Epoch 304/1000, Loss: 0.0216
[IL] Epoch 305/1000, Loss: 0.0209
[IL] Epoch 306/1000, Loss: 0.0221
[IL] Epoch 307/1000, Loss: 0.0196
[IL] Epoch 308/1000, Loss: 0.0199
[IL] Epoch 309/1000, Loss: 0.0188
[IL] Epoch 310/1000, Loss: 0.0200
[IL] Epoch 311/1000, Loss: 0.0200
[IL] Epoch 312/1000, Loss: 0.0184
[IL] Epoch 313/1000, Loss: 0.0192
[IL] Epoch 314/1000, Loss: 0.0201
[IL] Epoch 315/1000, Loss: 0.0196
[IL] Epoch 316/1000, Loss: 0.0194
[IL] Epoch 317/1000, Loss: 0.0194
[IL] Epoch 318/1000, Loss: 0.0197
[IL] Epoch 319/1000, Loss: 0.0198
[IL] Epoch 320/1000, Loss: 0.0200
[IL] Epoch 321/1000, Loss: 0.0205
[IL] Epoch 322/1000, Loss: 0.0202
[IL] Epoch 323/1000, Loss: 0.0205
[IL] Epoch 324/1000, Loss: 0.0185
[IL] Epoch 325/1000, Loss: 0.0195
[IL] Epoch 326/1000, Loss: 0.0196
[IL] Epoch 327/1000, Loss: 0.0178
[IL] Epoch 328/1000, Loss: 0.0191
[IL] Epoch 329/1000, Loss: 0.0199
[IL] Epoch 330/1000, Loss: 0.0200
[IL] Epoch 331/1000, Loss: 0.0176
[IL] Epoch 332/1000, Loss: 0.0198
[IL] Epoch 333/1000, Loss: 0.0181
[IL] Epoch 334/1000, Loss: 0.0194
[IL] Epoch 335/1000, Loss: 0.0177
[IL] Epoch 336/1000, Loss: 0.0181
[IL] Epoch 337/1000, Loss: 0.0187
[IL] Epoch 338/1000, Loss: 0.0198
[IL] Epoch 339/1000, Loss: 0.0183
[IL] Epoch 340/1000, Loss: 0.0191
[IL] Epoch 341/1000, Loss: 0.0181
[IL] Epoch 342/1000, Loss: 0.0181
[IL] Epoch 343/1000, Loss: 0.0198
[IL] Epoch 344/1000, Loss: 0.0194
[IL] Epoch 345/1000, Loss: 0.0191
[IL] Epoch 346/1000, Loss: 0.0184
[IL] Epoch 347/1000, Loss: 0.0182
[IL] Epoch 348/1000, Loss: 0.0188
[IL] Epoch 349/1000, Loss: 0.0182
[IL] Epoch 350/1000, Loss: 0.0200
[IL] Epoch 351/1000, Loss: 0.0203
[IL] Epoch 352/1000, Loss: 0.0193
[IL] Epoch 353/1000, Loss: 0.0181
[IL] Epoch 354/1000, Loss: 0.0186
[IL] Epoch 355/1000, Loss: 0.0176
[IL] Epoch 356/1000, Loss: 0.0187
[IL] Epoch 357/1000, Loss: 0.0192
[IL] Epoch 358/1000, Loss: 0.0190
[IL] Epoch 359/1000, Loss: 0.0187
[IL] Epoch 360/1000, Loss: 0.0174
[IL] Epoch 361/1000, Loss: 0.0183
[IL] Epoch 362/1000, Loss: 0.0171
[IL] Epoch 363/1000, Loss: 0.0182
[IL] Epoch 364/1000, Loss: 0.0183
[IL] Epoch 365/1000, Loss: 0.0184
[IL] Epoch 366/1000, Loss: 0.0173
[IL] Epoch 367/1000, Loss: 0.0188
[IL] Epoch 368/1000, Loss: 0.0187
[IL] Epoch 369/1000, Loss: 0.0188
[IL] Epoch 370/1000, Loss: 0.0178
[IL] Epoch 371/1000, Loss: 0.0179
[IL] Epoch 372/1000, Loss: 0.0172
[IL] Epoch 373/1000, Loss: 0.0183
[IL] Epoch 374/1000, Loss: 0.0164
[IL] Epoch 375/1000, Loss: 0.0170
[IL] Epoch 376/1000, Loss: 0.0173
[IL] Epoch 377/1000, Loss: 0.0183
[IL] Epoch 378/1000, Loss: 0.0179
[IL] Epoch 379/1000, Loss: 0.0173
[IL] Epoch 380/1000, Loss: 0.0179
[IL] Epoch 381/1000, Loss: 0.0177
[IL] Epoch 382/1000, Loss: 0.0159
[IL] Epoch 383/1000, Loss: 0.0178
[IL] Epoch 384/1000, Loss: 0.0160
[IL] Epoch 385/1000, Loss: 0.0162
[IL] Epoch 386/1000, Loss: 0.0165
[IL] Epoch 387/1000, Loss: 0.0163
[IL] Epoch 388/1000, Loss: 0.0171
[IL] Epoch 389/1000, Loss: 0.0169
[IL] Epoch 390/1000, Loss: 0.0173
[IL] Epoch 391/1000, Loss: 0.0160
[IL] Epoch 392/1000, Loss: 0.0167
[IL] Epoch 393/1000, Loss: 0.0170
[IL] Epoch 394/1000, Loss: 0.0167
[IL] Epoch 395/1000, Loss: 0.0164
[IL] Epoch 396/1000, Loss: 0.0159
[IL] Epoch 397/1000, Loss: 0.0169
[IL] Epoch 398/1000, Loss: 0.0177
[IL] Epoch 399/1000, Loss: 0.0162
test_mean_score: 0.35
[IL] Eval - Success Rate: 0.350
[IL] Epoch 400/1000, Loss: 0.0167
[IL] Epoch 401/1000, Loss: 0.0165
[IL] Epoch 402/1000, Loss: 0.0160
[IL] Epoch 403/1000, Loss: 0.0163
[IL] Epoch 404/1000, Loss: 0.0163
[IL] Epoch 405/1000, Loss: 0.0179
[IL] Epoch 406/1000, Loss: 0.0161
[IL] Epoch 407/1000, Loss: 0.0155
[IL] Epoch 408/1000, Loss: 0.0154
[IL] Epoch 409/1000, Loss: 0.0147
[IL] Epoch 410/1000, Loss: 0.0159
[IL] Epoch 411/1000, Loss: 0.0169
[IL] Epoch 412/1000, Loss: 0.0182
[IL] Epoch 413/1000, Loss: 0.0174
[IL] Epoch 414/1000, Loss: 0.0178
[IL] Epoch 415/1000, Loss: 0.0177
[IL] Epoch 416/1000, Loss: 0.0170
[IL] Epoch 417/1000, Loss: 0.0176
[IL] Epoch 418/1000, Loss: 0.0164
[IL] Epoch 419/1000, Loss: 0.0160
[IL] Epoch 420/1000, Loss: 0.0166
[IL] Epoch 421/1000, Loss: 0.0168
[IL] Epoch 422/1000, Loss: 0.0156
[IL] Epoch 423/1000, Loss: 0.0160
[IL] Epoch 424/1000, Loss: 0.0159
[IL] Epoch 425/1000, Loss: 0.0161
[IL] Epoch 426/1000, Loss: 0.0154
[IL] Epoch 427/1000, Loss: 0.0171
[IL] Epoch 428/1000, Loss: 0.0159
[IL] Epoch 429/1000, Loss: 0.0173
[IL] Epoch 430/1000, Loss: 0.0153
[IL] Epoch 431/1000, Loss: 0.0154
[IL] Epoch 432/1000, Loss: 0.0158
[IL] Epoch 433/1000, Loss: 0.0157
[IL] Epoch 434/1000, Loss: 0.0157
[IL] Epoch 435/1000, Loss: 0.0165
[IL] Epoch 436/1000, Loss: 0.0153
[IL] Epoch 437/1000, Loss: 0.0157
[IL] Epoch 438/1000, Loss: 0.0152
[IL] Epoch 439/1000, Loss: 0.0150
[IL] Epoch 440/1000, Loss: 0.0152
[IL] Epoch 441/1000, Loss: 0.0153
[IL] Epoch 442/1000, Loss: 0.0154
[IL] Epoch 443/1000, Loss: 0.0155
[IL] Epoch 444/1000, Loss: 0.0150
[IL] Epoch 445/1000, Loss: 0.0155
[IL] Epoch 446/1000, Loss: 0.0153
[IL] Epoch 447/1000, Loss: 0.0152
[IL] Epoch 448/1000, Loss: 0.0161
[IL] Epoch 449/1000, Loss: 0.0150
[IL] Epoch 450/1000, Loss: 0.0149
[IL] Epoch 451/1000, Loss: 0.0151
[IL] Epoch 452/1000, Loss: 0.0151
[IL] Epoch 453/1000, Loss: 0.0150
[IL] Epoch 454/1000, Loss: 0.0150
[IL] Epoch 455/1000, Loss: 0.0160
[IL] Epoch 456/1000, Loss: 0.0146
[IL] Epoch 457/1000, Loss: 0.0151
[IL] Epoch 458/1000, Loss: 0.0165
[IL] Epoch 459/1000, Loss: 0.0154
[IL] Epoch 460/1000, Loss: 0.0158
[IL] Epoch 461/1000, Loss: 0.0164
[IL] Epoch 462/1000, Loss: 0.0149
[IL] Epoch 463/1000, Loss: 0.0140
[IL] Epoch 464/1000, Loss: 0.0143
[IL] Epoch 465/1000, Loss: 0.0149
[IL] Epoch 466/1000, Loss: 0.0142
[IL] Epoch 467/1000, Loss: 0.0145
[IL] Epoch 468/1000, Loss: 0.0158
[IL] Epoch 469/1000, Loss: 0.0150
[IL] Epoch 470/1000, Loss: 0.0145
[IL] Epoch 471/1000, Loss: 0.0152
[IL] Epoch 472/1000, Loss: 0.0149
[IL] Epoch 473/1000, Loss: 0.0153
[IL] Epoch 474/1000, Loss: 0.0152
[IL] Epoch 475/1000, Loss: 0.0143
[IL] Epoch 476/1000, Loss: 0.0156
[IL] Epoch 477/1000, Loss: 0.0151
[IL] Epoch 478/1000, Loss: 0.0148
[IL] Epoch 479/1000, Loss: 0.0161
[IL] Epoch 480/1000, Loss: 0.0157
[IL] Epoch 481/1000, Loss: 0.0154
[IL] Epoch 482/1000, Loss: 0.0156
[IL] Epoch 483/1000, Loss: 0.0145
[IL] Epoch 484/1000, Loss: 0.0143
[IL] Epoch 485/1000, Loss: 0.0157
[IL] Epoch 486/1000, Loss: 0.0152
[IL] Epoch 487/1000, Loss: 0.0150
[IL] Epoch 488/1000, Loss: 0.0147
[IL] Epoch 489/1000, Loss: 0.0146
[IL] Epoch 490/1000, Loss: 0.0150
[IL] Epoch 491/1000, Loss: 0.0156
[IL] Epoch 492/1000, Loss: 0.0141
[IL] Epoch 493/1000, Loss: 0.0150
[IL] Epoch 494/1000, Loss: 0.0148
[IL] Epoch 495/1000, Loss: 0.0157
[IL] Epoch 496/1000, Loss: 0.0157
[IL] Epoch 497/1000, Loss: 0.0147
[IL] Epoch 498/1000, Loss: 0.0139
[IL] Epoch 499/1000, Loss: 0.0149
test_mean_score: 0.35
[IL] Eval - Success Rate: 0.350
[IL] Epoch 500/1000, Loss: 0.0145
[IL] Epoch 501/1000, Loss: 0.0141
[IL] Epoch 502/1000, Loss: 0.0147
[IL] Epoch 503/1000, Loss: 0.0148
[IL] Epoch 504/1000, Loss: 0.0147
[IL] Epoch 505/1000, Loss: 0.0145
[IL] Epoch 506/1000, Loss: 0.0158
[IL] Epoch 507/1000, Loss: 0.0147
[IL] Epoch 508/1000, Loss: 0.0154
[IL] Epoch 509/1000, Loss: 0.0156
[IL] Epoch 510/1000, Loss: 0.0141
[IL] Epoch 511/1000, Loss: 0.0135
[IL] Epoch 512/1000, Loss: 0.0142
[IL] Epoch 513/1000, Loss: 0.0132
[IL] Epoch 514/1000, Loss: 0.0145
[IL] Epoch 515/1000, Loss: 0.0146
[IL] Epoch 516/1000, Loss: 0.0135
[IL] Epoch 517/1000, Loss: 0.0129
[IL] Epoch 518/1000, Loss: 0.0139
[IL] Epoch 519/1000, Loss: 0.0126
[IL] Epoch 520/1000, Loss: 0.0129
[IL] Epoch 521/1000, Loss: 0.0139
[IL] Epoch 522/1000, Loss: 0.0135
[IL] Epoch 523/1000, Loss: 0.0137
[IL] Epoch 524/1000, Loss: 0.0135
[IL] Epoch 525/1000, Loss: 0.0127
[IL] Epoch 526/1000, Loss: 0.0132
[IL] Epoch 527/1000, Loss: 0.0142
[IL] Epoch 528/1000, Loss: 0.0142
[IL] Epoch 529/1000, Loss: 0.0136
[IL] Epoch 530/1000, Loss: 0.0133
[IL] Epoch 531/1000, Loss: 0.0131
[IL] Epoch 532/1000, Loss: 0.0133
[IL] Epoch 533/1000, Loss: 0.0143
[IL] Epoch 534/1000, Loss: 0.0145
[IL] Epoch 535/1000, Loss: 0.0137
[IL] Epoch 536/1000, Loss: 0.0135
[IL] Epoch 537/1000, Loss: 0.0137
[IL] Epoch 538/1000, Loss: 0.0139
[IL] Epoch 539/1000, Loss: 0.0131
[IL] Epoch 540/1000, Loss: 0.0132
[IL] Epoch 541/1000, Loss: 0.0129
[IL] Epoch 542/1000, Loss: 0.0147
[IL] Epoch 543/1000, Loss: 0.0139
[IL] Epoch 544/1000, Loss: 0.0146
[IL] Epoch 545/1000, Loss: 0.0138
[IL] Epoch 546/1000, Loss: 0.0139
[IL] Epoch 547/1000, Loss: 0.0138
[IL] Epoch 548/1000, Loss: 0.0142
[IL] Epoch 549/1000, Loss: 0.0135
[IL] Epoch 550/1000, Loss: 0.0137
[IL] Epoch 551/1000, Loss: 0.0134
[IL] Epoch 552/1000, Loss: 0.0134
[IL] Epoch 553/1000, Loss: 0.0134
[IL] Epoch 554/1000, Loss: 0.0143
[IL] Epoch 555/1000, Loss: 0.0131
[IL] Epoch 556/1000, Loss: 0.0137
[IL] Epoch 557/1000, Loss: 0.0137
[IL] Epoch 558/1000, Loss: 0.0133
[IL] Epoch 559/1000, Loss: 0.0126
[IL] Epoch 560/1000, Loss: 0.0119
[IL] Epoch 561/1000, Loss: 0.0140
[IL] Epoch 562/1000, Loss: 0.0135
[IL] Epoch 563/1000, Loss: 0.0145
[IL] Epoch 564/1000, Loss: 0.0141
[IL] Epoch 565/1000, Loss: 0.0143
[IL] Epoch 566/1000, Loss: 0.0128
[IL] Epoch 567/1000, Loss: 0.0127
[IL] Epoch 568/1000, Loss: 0.0141
[IL] Epoch 569/1000, Loss: 0.0134
[IL] Epoch 570/1000, Loss: 0.0125
[IL] Epoch 571/1000, Loss: 0.0121
[IL] Epoch 572/1000, Loss: 0.0123
[IL] Epoch 573/1000, Loss: 0.0118
[IL] Epoch 574/1000, Loss: 0.0119
[IL] Epoch 575/1000, Loss: 0.0125
[IL] Epoch 576/1000, Loss: 0.0121
[IL] Epoch 577/1000, Loss: 0.0125
[IL] Epoch 578/1000, Loss: 0.0131
[IL] Epoch 579/1000, Loss: 0.0120
[IL] Epoch 580/1000, Loss: 0.0126
[IL] Epoch 581/1000, Loss: 0.0127
[IL] Epoch 582/1000, Loss: 0.0132
[IL] Epoch 583/1000, Loss: 0.0132
[IL] Epoch 584/1000, Loss: 0.0124
[IL] Epoch 585/1000, Loss: 0.0121
[IL] Epoch 586/1000, Loss: 0.0120
[IL] Epoch 587/1000, Loss: 0.0123
[IL] Epoch 588/1000, Loss: 0.0124
[IL] Epoch 589/1000, Loss: 0.0134
[IL] Epoch 590/1000, Loss: 0.0132
[IL] Epoch 591/1000, Loss: 0.0132
[IL] Epoch 592/1000, Loss: 0.0128
[IL] Epoch 593/1000, Loss: 0.0123
[IL] Epoch 594/1000, Loss: 0.0123
[IL] Epoch 595/1000, Loss: 0.0128
[IL] Epoch 596/1000, Loss: 0.0135
[IL] Epoch 597/1000, Loss: 0.0130
[IL] Epoch 598/1000, Loss: 0.0128
[IL] Epoch 599/1000, Loss: 0.0129
test_mean_score: 0.55
[IL] Eval - Success Rate: 0.550
[IL] Epoch 600/1000, Loss: 0.0127
[IL] Epoch 601/1000, Loss: 0.0123
[IL] Epoch 602/1000, Loss: 0.0127
[IL] Epoch 603/1000, Loss: 0.0129
[IL] Epoch 604/1000, Loss: 0.0129
[IL] Epoch 605/1000, Loss: 0.0128
[IL] Epoch 606/1000, Loss: 0.0128
[IL] Epoch 607/1000, Loss: 0.0115
[IL] Epoch 608/1000, Loss: 0.0126
[IL] Epoch 609/1000, Loss: 0.0135
[IL] Epoch 610/1000, Loss: 0.0129
[IL] Epoch 611/1000, Loss: 0.0125
[IL] Epoch 612/1000, Loss: 0.0122
[IL] Epoch 613/1000, Loss: 0.0125
[IL] Epoch 614/1000, Loss: 0.0127
[IL] Epoch 615/1000, Loss: 0.0128
[IL] Epoch 616/1000, Loss: 0.0126
[IL] Epoch 617/1000, Loss: 0.0146
[IL] Epoch 618/1000, Loss: 0.0129
[IL] Epoch 619/1000, Loss: 0.0138
[IL] Epoch 620/1000, Loss: 0.0129
[IL] Epoch 621/1000, Loss: 0.0135
[IL] Epoch 622/1000, Loss: 0.0129
[IL] Epoch 623/1000, Loss: 0.0125
[IL] Epoch 624/1000, Loss: 0.0122
[IL] Epoch 625/1000, Loss: 0.0122
[IL] Epoch 626/1000, Loss: 0.0122
[IL] Epoch 627/1000, Loss: 0.0123
[IL] Epoch 628/1000, Loss: 0.0121
[IL] Epoch 629/1000, Loss: 0.0127
[IL] Epoch 630/1000, Loss: 0.0124
[IL] Epoch 631/1000, Loss: 0.0126
[IL] Epoch 632/1000, Loss: 0.0119
[IL] Epoch 633/1000, Loss: 0.0111
[IL] Epoch 634/1000, Loss: 0.0124
[IL] Epoch 635/1000, Loss: 0.0120
[IL] Epoch 636/1000, Loss: 0.0112
[IL] Epoch 637/1000, Loss: 0.0113
[IL] Epoch 638/1000, Loss: 0.0108
[IL] Epoch 639/1000, Loss: 0.0120
[IL] Epoch 640/1000, Loss: 0.0117
[IL] Epoch 641/1000, Loss: 0.0112
[IL] Epoch 642/1000, Loss: 0.0128
[IL] Epoch 643/1000, Loss: 0.0132
[IL] Epoch 644/1000, Loss: 0.0125
[IL] Epoch 645/1000, Loss: 0.0117
[IL] Epoch 646/1000, Loss: 0.0128
[IL] Epoch 647/1000, Loss: 0.0126
[IL] Epoch 648/1000, Loss: 0.0113
[IL] Epoch 649/1000, Loss: 0.0121
[IL] Epoch 650/1000, Loss: 0.0115
[IL] Epoch 651/1000, Loss: 0.0116
[IL] Epoch 652/1000, Loss: 0.0113
[IL] Epoch 653/1000, Loss: 0.0120
[IL] Epoch 654/1000, Loss: 0.0106
[IL] Epoch 655/1000, Loss: 0.0118
[IL] Epoch 656/1000, Loss: 0.0118
[IL] Epoch 657/1000, Loss: 0.0122
[IL] Epoch 658/1000, Loss: 0.0121
[IL] Epoch 659/1000, Loss: 0.0128
[IL] Epoch 660/1000, Loss: 0.0133
[IL] Epoch 661/1000, Loss: 0.0129
[IL] Epoch 662/1000, Loss: 0.0124
[IL] Epoch 663/1000, Loss: 0.0118
[IL] Epoch 664/1000, Loss: 0.0119
[IL] Epoch 665/1000, Loss: 0.0112
[IL] Epoch 666/1000, Loss: 0.0120
[IL] Epoch 667/1000, Loss: 0.0122
[IL] Epoch 668/1000, Loss: 0.0123
[IL] Epoch 669/1000, Loss: 0.0115
[IL] Epoch 670/1000, Loss: 0.0123
[IL] Epoch 671/1000, Loss: 0.0115
[IL] Epoch 672/1000, Loss: 0.0110
[IL] Epoch 673/1000, Loss: 0.0123
[IL] Epoch 674/1000, Loss: 0.0122
[IL] Epoch 675/1000, Loss: 0.0112
[IL] Epoch 676/1000, Loss: 0.0109
[IL] Epoch 677/1000, Loss: 0.0114
[IL] Epoch 678/1000, Loss: 0.0120
[IL] Epoch 679/1000, Loss: 0.0117
[IL] Epoch 680/1000, Loss: 0.0122
[IL] Epoch 681/1000, Loss: 0.0122
[IL] Epoch 682/1000, Loss: 0.0122
[IL] Epoch 683/1000, Loss: 0.0129
[IL] Epoch 684/1000, Loss: 0.0113
[IL] Epoch 685/1000, Loss: 0.0119
[IL] Epoch 686/1000, Loss: 0.0128
[IL] Epoch 687/1000, Loss: 0.0118
[IL] Epoch 688/1000, Loss: 0.0124
[IL] Epoch 689/1000, Loss: 0.0121
[IL] Epoch 690/1000, Loss: 0.0118
[IL] Epoch 691/1000, Loss: 0.0116
[IL] Epoch 692/1000, Loss: 0.0127
[IL] Epoch 693/1000, Loss: 0.0127
[IL] Epoch 694/1000, Loss: 0.0114
[IL] Epoch 695/1000, Loss: 0.0103
[IL] Epoch 696/1000, Loss: 0.0120
[IL] Epoch 697/1000, Loss: 0.0108
[IL] Epoch 698/1000, Loss: 0.0129
[IL] Epoch 699/1000, Loss: 0.0124
test_mean_score: 0.5
[IL] Eval - Success Rate: 0.500
[IL] Epoch 700/1000, Loss: 0.0127
[IL] Epoch 701/1000, Loss: 0.0125
[IL] Epoch 702/1000, Loss: 0.0114
[IL] Epoch 703/1000, Loss: 0.0115
[IL] Epoch 704/1000, Loss: 0.0117
[IL] Epoch 705/1000, Loss: 0.0111
[IL] Epoch 706/1000, Loss: 0.0114
[IL] Epoch 707/1000, Loss: 0.0113
[IL] Epoch 708/1000, Loss: 0.0109
[IL] Epoch 709/1000, Loss: 0.0103
[IL] Epoch 710/1000, Loss: 0.0098
[IL] Epoch 711/1000, Loss: 0.0107
[IL] Epoch 712/1000, Loss: 0.0107
[IL] Epoch 713/1000, Loss: 0.0113
[IL] Epoch 714/1000, Loss: 0.0112
[IL] Epoch 715/1000, Loss: 0.0118
[IL] Epoch 716/1000, Loss: 0.0116
[IL] Epoch 717/1000, Loss: 0.0113
[IL] Epoch 718/1000, Loss: 0.0116
[IL] Epoch 719/1000, Loss: 0.0105
[IL] Epoch 720/1000, Loss: 0.0101
[IL] Epoch 721/1000, Loss: 0.0107
[IL] Epoch 722/1000, Loss: 0.0104
[IL] Epoch 723/1000, Loss: 0.0111
[IL] Epoch 724/1000, Loss: 0.0109
[IL] Epoch 725/1000, Loss: 0.0120
[IL] Epoch 726/1000, Loss: 0.0123
[IL] Epoch 727/1000, Loss: 0.0123
[IL] Epoch 728/1000, Loss: 0.0116
[IL] Epoch 729/1000, Loss: 0.0120
[IL] Epoch 730/1000, Loss: 0.0112
[IL] Epoch 731/1000, Loss: 0.0115
[IL] Epoch 732/1000, Loss: 0.0112
[IL] Epoch 733/1000, Loss: 0.0118
[IL] Epoch 734/1000, Loss: 0.0112
[IL] Epoch 735/1000, Loss: 0.0108
[IL] Epoch 736/1000, Loss: 0.0107
[IL] Epoch 737/1000, Loss: 0.0106
[IL] Epoch 738/1000, Loss: 0.0118
[IL] Epoch 739/1000, Loss: 0.0112
[IL] Epoch 740/1000, Loss: 0.0106
[IL] Epoch 741/1000, Loss: 0.0100
[IL] Epoch 742/1000, Loss: 0.0099
[IL] Epoch 743/1000, Loss: 0.0109
[IL] Epoch 744/1000, Loss: 0.0103
[IL] Epoch 745/1000, Loss: 0.0094
[IL] Epoch 746/1000, Loss: 0.0105
[IL] Epoch 747/1000, Loss: 0.0093
[IL] Epoch 748/1000, Loss: 0.0098
[IL] Epoch 749/1000, Loss: 0.0107
[IL] Epoch 750/1000, Loss: 0.0113
[IL] Epoch 751/1000, Loss: 0.0118
[IL] Epoch 752/1000, Loss: 0.0117
[IL] Epoch 753/1000, Loss: 0.0113
[IL] Epoch 754/1000, Loss: 0.0109
[IL] Epoch 755/1000, Loss: 0.0106
[IL] Epoch 756/1000, Loss: 0.0102
[IL] Epoch 757/1000, Loss: 0.0116
[IL] Epoch 758/1000, Loss: 0.0109
[IL] Epoch 759/1000, Loss: 0.0120
[IL] Epoch 760/1000, Loss: 0.0107
[IL] Epoch 761/1000, Loss: 0.0115
[IL] Epoch 762/1000, Loss: 0.0113
[IL] Epoch 763/1000, Loss: 0.0111
[IL] Epoch 764/1000, Loss: 0.0102
[IL] Epoch 765/1000, Loss: 0.0116
[IL] Epoch 766/1000, Loss: 0.0111
[IL] Epoch 767/1000, Loss: 0.0108
[IL] Epoch 768/1000, Loss: 0.0105
[IL] Epoch 769/1000, Loss: 0.0113
[IL] Epoch 770/1000, Loss: 0.0110
[IL] Epoch 771/1000, Loss: 0.0111
[IL] Epoch 772/1000, Loss: 0.0117
[IL] Epoch 773/1000, Loss: 0.0113
[IL] Epoch 774/1000, Loss: 0.0108
[IL] Epoch 775/1000, Loss: 0.0112
[IL] Epoch 776/1000, Loss: 0.0105
[IL] Epoch 777/1000, Loss: 0.0110
[IL] Epoch 778/1000, Loss: 0.0112
[IL] Epoch 779/1000, Loss: 0.0109
[IL] Epoch 780/1000, Loss: 0.0112
[IL] Epoch 781/1000, Loss: 0.0107
[IL] Epoch 782/1000, Loss: 0.0100
[IL] Epoch 783/1000, Loss: 0.0109
[IL] Epoch 784/1000, Loss: 0.0097
[IL] Epoch 785/1000, Loss: 0.0101
[IL] Epoch 786/1000, Loss: 0.0105
[IL] Epoch 787/1000, Loss: 0.0099
[IL] Epoch 788/1000, Loss: 0.0107
[IL] Epoch 789/1000, Loss: 0.0100
[IL] Epoch 790/1000, Loss: 0.0096
[IL] Epoch 791/1000, Loss: 0.0103
[IL] Epoch 792/1000, Loss: 0.0098
[IL] Epoch 793/1000, Loss: 0.0100
[IL] Epoch 794/1000, Loss: 0.0109
[IL] Epoch 795/1000, Loss: 0.0107
[IL] Epoch 796/1000, Loss: 0.0106
[IL] Epoch 797/1000, Loss: 0.0112
[IL] Epoch 798/1000, Loss: 0.0104
[IL] Epoch 799/1000, Loss: 0.0108
test_mean_score: 0.45
[IL] Eval - Success Rate: 0.450
[IL] Epoch 800/1000, Loss: 0.0108
[IL] Epoch 801/1000, Loss: 0.0106
[IL] Epoch 802/1000, Loss: 0.0103
[IL] Epoch 803/1000, Loss: 0.0111
[IL] Epoch 804/1000, Loss: 0.0113
[IL] Epoch 805/1000, Loss: 0.0110
[IL] Epoch 806/1000, Loss: 0.0112
[IL] Epoch 807/1000, Loss: 0.0115
[IL] Epoch 808/1000, Loss: 0.0107
[IL] Epoch 809/1000, Loss: 0.0098
[IL] Epoch 810/1000, Loss: 0.0095
[IL] Epoch 811/1000, Loss: 0.0097
[IL] Epoch 812/1000, Loss: 0.0107
[IL] Epoch 813/1000, Loss: 0.0094
[IL] Epoch 814/1000, Loss: 0.0093
[IL] Epoch 815/1000, Loss: 0.0095
[IL] Epoch 816/1000, Loss: 0.0102
[IL] Epoch 817/1000, Loss: 0.0101
[IL] Epoch 818/1000, Loss: 0.0098
[IL] Epoch 819/1000, Loss: 0.0092
[IL] Epoch 820/1000, Loss: 0.0104
[IL] Epoch 821/1000, Loss: 0.0101
[IL] Epoch 822/1000, Loss: 0.0111
[IL] Epoch 823/1000, Loss: 0.0106
[IL] Epoch 824/1000, Loss: 0.0109
[IL] Epoch 825/1000, Loss: 0.0107
[IL] Epoch 826/1000, Loss: 0.0102
[IL] Epoch 827/1000, Loss: 0.0109
[IL] Epoch 828/1000, Loss: 0.0106
[IL] Epoch 829/1000, Loss: 0.0105
[IL] Epoch 830/1000, Loss: 0.0106
[IL] Epoch 831/1000, Loss: 0.0112
[IL] Epoch 832/1000, Loss: 0.0118
[IL] Epoch 833/1000, Loss: 0.0115
[IL] Epoch 834/1000, Loss: 0.0105
[IL] Epoch 835/1000, Loss: 0.0099
[IL] Epoch 836/1000, Loss: 0.0095
[IL] Epoch 837/1000, Loss: 0.0104
[IL] Epoch 838/1000, Loss: 0.0106
[IL] Epoch 839/1000, Loss: 0.0120
[IL] Epoch 840/1000, Loss: 0.0109
[IL] Epoch 841/1000, Loss: 0.0105
[IL] Epoch 842/1000, Loss: 0.0101
[IL] Epoch 843/1000, Loss: 0.0097
[IL] Epoch 844/1000, Loss: 0.0104
[IL] Epoch 845/1000, Loss: 0.0098
[IL] Epoch 846/1000, Loss: 0.0095
[IL] Epoch 847/1000, Loss: 0.0090
[IL] Epoch 848/1000, Loss: 0.0101
[IL] Epoch 849/1000, Loss: 0.0085
[IL] Epoch 850/1000, Loss: 0.0096
[IL] Epoch 851/1000, Loss: 0.0094
[IL] Epoch 852/1000, Loss: 0.0093
[IL] Epoch 853/1000, Loss: 0.0098
[IL] Epoch 854/1000, Loss: 0.0100
[IL] Epoch 855/1000, Loss: 0.0099
[IL] Epoch 856/1000, Loss: 0.0101
[IL] Epoch 857/1000, Loss: 0.0098
[IL] Epoch 858/1000, Loss: 0.0103
[IL] Epoch 859/1000, Loss: 0.0100
[IL] Epoch 860/1000, Loss: 0.0094
[IL] Epoch 861/1000, Loss: 0.0107
[IL] Epoch 862/1000, Loss: 0.0096
[IL] Epoch 863/1000, Loss: 0.0100
[IL] Epoch 864/1000, Loss: 0.0094
[IL] Epoch 865/1000, Loss: 0.0093
[IL] Epoch 866/1000, Loss: 0.0098
[IL] Epoch 867/1000, Loss: 0.0099
[IL] Epoch 868/1000, Loss: 0.0099
[IL] Epoch 869/1000, Loss: 0.0100
[IL] Epoch 870/1000, Loss: 0.0094
[IL] Epoch 871/1000, Loss: 0.0095
[IL] Epoch 872/1000, Loss: 0.0095
[IL] Epoch 873/1000, Loss: 0.0095
[IL] Epoch 874/1000, Loss: 0.0091
[IL] Epoch 875/1000, Loss: 0.0092
[IL] Epoch 876/1000, Loss: 0.0093
[IL] Epoch 877/1000, Loss: 0.0099
[IL] Epoch 878/1000, Loss: 0.0093
[IL] Epoch 879/1000, Loss: 0.0096
[IL] Epoch 880/1000, Loss: 0.0102
[IL] Epoch 881/1000, Loss: 0.0103
[IL] Epoch 882/1000, Loss: 0.0106
[IL] Epoch 883/1000, Loss: 0.0098
[IL] Epoch 884/1000, Loss: 0.0101
[IL] Epoch 885/1000, Loss: 0.0103
[IL] Epoch 886/1000, Loss: 0.0104
[IL] Epoch 887/1000, Loss: 0.0093
[IL] Epoch 888/1000, Loss: 0.0095
[IL] Epoch 889/1000, Loss: 0.0093
[IL] Epoch 890/1000, Loss: 0.0107
[IL] Epoch 891/1000, Loss: 0.0096
[IL] Epoch 892/1000, Loss: 0.0094
[IL] Epoch 893/1000, Loss: 0.0103
[IL] Epoch 894/1000, Loss: 0.0101
[IL] Epoch 895/1000, Loss: 0.0115
[IL] Epoch 896/1000, Loss: 0.0109
[IL] Epoch 897/1000, Loss: 0.0111
[IL] Epoch 898/1000, Loss: 0.0104
[IL] Epoch 899/1000, Loss: 0.0102
test_mean_score: 0.35
[IL] Eval - Success Rate: 0.350
[IL] Epoch 900/1000, Loss: 0.0101
[IL] Epoch 901/1000, Loss: 0.0093
[IL] Epoch 902/1000, Loss: 0.0091
[IL] Epoch 903/1000, Loss: 0.0096
[IL] Epoch 904/1000, Loss: 0.0083
[IL] Epoch 905/1000, Loss: 0.0095
[IL] Epoch 906/1000, Loss: 0.0095
[IL] Epoch 907/1000, Loss: 0.0095
[IL] Epoch 908/1000, Loss: 0.0099
[IL] Epoch 909/1000, Loss: 0.0093
[IL] Epoch 910/1000, Loss: 0.0117
[IL] Epoch 911/1000, Loss: 0.0108
[IL] Epoch 912/1000, Loss: 0.0106
[IL] Epoch 913/1000, Loss: 0.0107
[IL] Epoch 914/1000, Loss: 0.0103
[IL] Epoch 915/1000, Loss: 0.0098
[IL] Epoch 916/1000, Loss: 0.0103
[IL] Epoch 917/1000, Loss: 0.0102
[IL] Epoch 918/1000, Loss: 0.0111
[IL] Epoch 919/1000, Loss: 0.0104
[IL] Epoch 920/1000, Loss: 0.0108
[IL] Epoch 921/1000, Loss: 0.0099
[IL] Epoch 922/1000, Loss: 0.0096
[IL] Epoch 923/1000, Loss: 0.0105
[IL] Epoch 924/1000, Loss: 0.0100
[IL] Epoch 925/1000, Loss: 0.0103
[IL] Epoch 926/1000, Loss: 0.0100
[IL] Epoch 927/1000, Loss: 0.0095
[IL] Epoch 928/1000, Loss: 0.0100
[IL] Epoch 929/1000, Loss: 0.0092
[IL] Epoch 930/1000, Loss: 0.0086
[IL] Epoch 931/1000, Loss: 0.0101
[IL] Epoch 932/1000, Loss: 0.0105
[IL] Epoch 933/1000, Loss: 0.0093
[IL] Epoch 934/1000, Loss: 0.0098
[IL] Epoch 935/1000, Loss: 0.0090
[IL] Epoch 936/1000, Loss: 0.0094
[IL] Epoch 937/1000, Loss: 0.0100
[IL] Epoch 938/1000, Loss: 0.0089
[IL] Epoch 939/1000, Loss: 0.0084
[IL] Epoch 940/1000, Loss: 0.0095
[IL] Epoch 941/1000, Loss: 0.0091
[IL] Epoch 942/1000, Loss: 0.0097
[IL] Epoch 943/1000, Loss: 0.0094
[IL] Epoch 944/1000, Loss: 0.0104
[IL] Epoch 945/1000, Loss: 0.0095
[IL] Epoch 946/1000, Loss: 0.0093
[IL] Epoch 947/1000, Loss: 0.0093
[IL] Epoch 948/1000, Loss: 0.0087
[IL] Epoch 949/1000, Loss: 0.0092
[IL] Epoch 950/1000, Loss: 0.0090
[IL] Epoch 951/1000, Loss: 0.0095
[IL] Epoch 952/1000, Loss: 0.0101
[IL] Epoch 953/1000, Loss: 0.0086
[IL] Epoch 954/1000, Loss: 0.0102
[IL] Epoch 955/1000, Loss: 0.0095
[IL] Epoch 956/1000, Loss: 0.0085
[IL] Epoch 957/1000, Loss: 0.0092
[IL] Epoch 958/1000, Loss: 0.0088
[IL] Epoch 959/1000, Loss: 0.0091
[IL] Epoch 960/1000, Loss: 0.0095
[IL] Epoch 961/1000, Loss: 0.0096
[IL] Epoch 962/1000, Loss: 0.0096
[IL] Epoch 963/1000, Loss: 0.0085
[IL] Epoch 964/1000, Loss: 0.0092
[IL] Epoch 965/1000, Loss: 0.0097
[IL] Epoch 966/1000, Loss: 0.0099
[IL] Epoch 967/1000, Loss: 0.0086
[IL] Epoch 968/1000, Loss: 0.0088
[IL] Epoch 969/1000, Loss: 0.0082
[IL] Epoch 970/1000, Loss: 0.0092
[IL] Epoch 971/1000, Loss: 0.0089
[IL] Epoch 972/1000, Loss: 0.0088
[IL] Epoch 973/1000, Loss: 0.0098
[IL] Epoch 974/1000, Loss: 0.0089
[IL] Epoch 975/1000, Loss: 0.0092
[IL] Epoch 976/1000, Loss: 0.0102
[IL] Epoch 977/1000, Loss: 0.0105
[IL] Epoch 978/1000, Loss: 0.0109
[IL] Epoch 979/1000, Loss: 0.0087
[IL] Epoch 980/1000, Loss: 0.0095
[IL] Epoch 981/1000, Loss: 0.0091
[IL] Epoch 982/1000, Loss: 0.0087
[IL] Epoch 983/1000, Loss: 0.0091
[IL] Epoch 984/1000, Loss: 0.0093
[IL] Epoch 985/1000, Loss: 0.0090
[IL] Epoch 986/1000, Loss: 0.0086
[IL] Epoch 987/1000, Loss: 0.0088
[IL] Epoch 988/1000, Loss: 0.0098
[IL] Epoch 989/1000, Loss: 0.0095
[IL] Epoch 990/1000, Loss: 0.0091
[IL] Epoch 991/1000, Loss: 0.0092
[IL] Epoch 992/1000, Loss: 0.0088
[IL] Epoch 993/1000, Loss: 0.0078
[IL] Epoch 994/1000, Loss: 0.0087
[IL] Epoch 995/1000, Loss: 0.0087
[IL] Epoch 996/1000, Loss: 0.0082
[IL] Epoch 997/1000, Loss: 0.0087
[IL] Epoch 998/1000, Loss: 0.0085
[IL] Epoch 999/1000, Loss: 0.0089
test_mean_score: 0.35
[IL] Eval - Success Rate: 0.350
[Checkpoint] Saved to /nfs_global/S/yangrongzheng/RL100/3D-Diffusion-Policy/3D-Diffusion-Policy/checkpoints/after_il.ckpt

================================================================================
               OFFLINE RL ITERATION 1/5
================================================================================


[RL100Trainer] Line 6 — Training Transition Model T_θ (Iteration 0)

[TransitionModel] Encoding dataset for transition model training...
[TransitionModel] Dataset: 1737 samples, input_dim=260, target_dim=257
[TransitionModel] Epoch    0 | train=166.49058 | val=13.05136 | no-improve=0/5
[TransitionModel] Epoch   20 | train=12.44753 | val=3.77356 | no-improve=0/5
[TransitionModel] Epoch   40 | train=-6.72556 | val=1.07508 | no-improve=0/5
[TransitionModel] Epoch   60 | train=-12.45615 | val=0.66170 | no-improve=0/5
[TransitionModel] Epoch   80 | train=-16.30973 | val=0.54784 | no-improve=0/5
[TransitionModel] Epoch  100 | train=-21.61101 | val=0.43988 | no-improve=1/5
[TransitionModel] Epoch  120 | train=-23.99700 | val=0.33705 | no-improve=1/5
[TransitionModel] Epoch  140 | train=-24.79973 | val=0.27653 | no-improve=1/5
[TransitionModel] Epoch  160 | train=-27.35350 | val=0.19825 | no-improve=0/5
[TransitionModel] Epoch  180 | train=-28.43796 | val=0.15580 | no-improve=0/5
[TransitionModel] Training complete. Elites=[6, 2, 4, 5, 3], val_loss=0.11977

[RL100Trainer] Phase 2a: Training IQL Critics (Iteration 0)
[IQL] Epoch 0/500, V Loss: 1.8348, Q Loss: 35.5203
[IQL] Epoch 1/500, V Loss: 0.9544, Q Loss: 7.8978
[IQL] Epoch 2/500, V Loss: 0.2578, Q Loss: 4.6478
[IQL] Epoch 3/500, V Loss: 0.2972, Q Loss: 3.8922
[IQL] Epoch 4/500, V Loss: 0.1184, Q Loss: 3.3236
[IQL] Epoch 5/500, V Loss: 0.1734, Q Loss: 2.9977
[IQL] Epoch 6/500, V Loss: 0.2050, Q Loss: 2.8501
[IQL] Epoch 7/500, V Loss: 0.2257, Q Loss: 2.7269
[IQL] Epoch 8/500, V Loss: 0.2512, Q Loss: 2.5910
[IQL] Epoch 9/500, V Loss: 0.2469, Q Loss: 2.4449
[IQL] Epoch 10/500, V Loss: 0.2296, Q Loss: 2.2556
[IQL] Epoch 11/500, V Loss: 0.2361, Q Loss: 2.0605
[IQL] Epoch 12/500, V Loss: 0.2187, Q Loss: 1.8055
[IQL] Epoch 13/500, V Loss: 0.2100, Q Loss: 1.5649
[IQL] Epoch 14/500, V Loss: 0.2515, Q Loss: 1.3254
[IQL] Epoch 15/500, V Loss: 0.2594, Q Loss: 1.1290
[IQL] Epoch 16/500, V Loss: 0.2721, Q Loss: 0.9084
[IQL] Epoch 17/500, V Loss: 0.2692, Q Loss: 0.7422
[IQL] Epoch 18/500, V Loss: 0.2597, Q Loss: 0.6347
[IQL] Epoch 19/500, V Loss: 0.2417, Q Loss: 0.5484
[IQL] Epoch 20/500, V Loss: 0.2126, Q Loss: 0.5514
[IQL] Epoch 21/500, V Loss: 0.1839, Q Loss: 0.5016
[IQL] Epoch 22/500, V Loss: 0.1735, Q Loss: 0.4708
[IQL] Epoch 23/500, V Loss: 0.1777, Q Loss: 0.4723
[IQL] Epoch 24/500, V Loss: 0.1477, Q Loss: 0.4302
[IQL] Epoch 25/500, V Loss: 0.1683, Q Loss: 0.4434
[IQL] Epoch 26/500, V Loss: 0.1163, Q Loss: 0.3778
[IQL] Epoch 27/500, V Loss: 0.1335, Q Loss: 0.3658
[IQL] Epoch 28/500, V Loss: 0.1370, Q Loss: 0.3375
[IQL] Epoch 29/500, V Loss: 0.1423, Q Loss: 0.3244
[IQL] Epoch 30/500, V Loss: 0.1154, Q Loss: 0.3176
[IQL] Epoch 31/500, V Loss: 0.1323, Q Loss: 0.3087
[IQL] Epoch 32/500, V Loss: 0.1070, Q Loss: 0.2978
[IQL] Epoch 33/500, V Loss: 0.1182, Q Loss: 0.2982
[IQL] Epoch 34/500, V Loss: 0.1086, Q Loss: 0.3007
[IQL] Epoch 35/500, V Loss: 0.1022, Q Loss: 0.2828
[IQL] Epoch 36/500, V Loss: 0.1059, Q Loss: 0.2863
[IQL] Epoch 37/500, V Loss: 0.1073, Q Loss: 0.3067
[IQL] Epoch 38/500, V Loss: 0.1049, Q Loss: 0.3023
[IQL] Epoch 39/500, V Loss: 0.0975, Q Loss: 0.2940
[IQL] Epoch 40/500, V Loss: 0.1059, Q Loss: 0.3059
[IQL] Epoch 41/500, V Loss: 0.0947, Q Loss: 0.3358
[IQL] Epoch 42/500, V Loss: 0.1372, Q Loss: 0.3979
[IQL] Epoch 43/500, V Loss: 0.1057, Q Loss: 0.3845
[IQL] Epoch 44/500, V Loss: 0.1164, Q Loss: 0.3893
[IQL] Epoch 45/500, V Loss: 0.1173, Q Loss: 0.4004
[IQL] Epoch 46/500, V Loss: 0.1386, Q Loss: 0.3855
[IQL] Epoch 47/500, V Loss: 0.1346, Q Loss: 0.3731
[IQL] Epoch 48/500, V Loss: 0.0934, Q Loss: 0.3720
[IQL] Epoch 49/500, V Loss: 0.0901, Q Loss: 0.3822
[IQL] Epoch 50/500, V Loss: 0.0778, Q Loss: 0.3824
[IQL] Epoch 51/500, V Loss: 0.0736, Q Loss: 0.3778
[IQL] Epoch 52/500, V Loss: 0.0721, Q Loss: 0.3933
[IQL] Epoch 53/500, V Loss: 0.1027, Q Loss: 0.4255
[IQL] Epoch 54/500, V Loss: 0.0985, Q Loss: 0.4063
[IQL] Epoch 55/500, V Loss: 0.0878, Q Loss: 0.4075
[IQL] Epoch 56/500, V Loss: 0.0776, Q Loss: 0.4065
[IQL] Epoch 57/500, V Loss: 0.0544, Q Loss: 0.4067
[IQL] Epoch 58/500, V Loss: 0.0630, Q Loss: 0.4423
[IQL] Epoch 59/500, V Loss: 0.0747, Q Loss: 0.4647
[IQL] Epoch 60/500, V Loss: 0.0728, Q Loss: 0.4597
[IQL] Epoch 61/500, V Loss: 0.0781, Q Loss: 0.4880
[IQL] Epoch 62/500, V Loss: 0.1167, Q Loss: 0.5312
[IQL] Epoch 63/500, V Loss: 0.1493, Q Loss: 0.4834
[IQL] Epoch 64/500, V Loss: 0.1211, Q Loss: 0.4905
[IQL] Epoch 65/500, V Loss: 0.1259, Q Loss: 0.5248
[IQL] Epoch 66/500, V Loss: 0.0910, Q Loss: 0.5134
[IQL] Epoch 67/500, V Loss: 0.0903, Q Loss: 0.5499
[IQL] Epoch 68/500, V Loss: 0.0691, Q Loss: 0.5026
[IQL] Epoch 69/500, V Loss: 0.0710, Q Loss: 0.4948
[IQL] Epoch 70/500, V Loss: 0.0716, Q Loss: 0.4932
[IQL] Epoch 71/500, V Loss: 0.0848, Q Loss: 0.5802
[IQL] Epoch 72/500, V Loss: 0.0972, Q Loss: 0.5948
[IQL] Epoch 73/500, V Loss: 0.1030, Q Loss: 0.6014
[IQL] Epoch 74/500, V Loss: 0.1377, Q Loss: 0.6435
[IQL] Epoch 75/500, V Loss: 0.1138, Q Loss: 0.6226
[IQL] Epoch 76/500, V Loss: 0.1037, Q Loss: 0.6234
[IQL] Epoch 77/500, V Loss: 0.1115, Q Loss: 0.5934
[IQL] Epoch 78/500, V Loss: 0.1030, Q Loss: 0.6150
[IQL] Epoch 79/500, V Loss: 0.0974, Q Loss: 0.6237
[IQL] Epoch 80/500, V Loss: 0.1173, Q Loss: 0.5985
[IQL] Epoch 81/500, V Loss: 0.0918, Q Loss: 0.6083
[IQL] Epoch 82/500, V Loss: 0.0914, Q Loss: 0.6326
[IQL] Epoch 83/500, V Loss: 0.1330, Q Loss: 0.5957
[IQL] Epoch 84/500, V Loss: 0.0845, Q Loss: 0.6035
[IQL] Epoch 85/500, V Loss: 0.1025, Q Loss: 0.6137
[IQL] Epoch 86/500, V Loss: 0.1118, Q Loss: 0.6601
[IQL] Epoch 87/500, V Loss: 0.1215, Q Loss: 0.6519
[IQL] Epoch 88/500, V Loss: 0.1032, Q Loss: 0.6872
[IQL] Epoch 89/500, V Loss: 0.1267, Q Loss: 0.6572
[IQL] Epoch 90/500, V Loss: 0.1394, Q Loss: 0.6858
[IQL] Epoch 91/500, V Loss: 0.0984, Q Loss: 0.6654
[IQL] Epoch 92/500, V Loss: 0.0907, Q Loss: 0.6637
[IQL] Epoch 93/500, V Loss: 0.1097, Q Loss: 0.6578
[IQL] Epoch 94/500, V Loss: 0.0977, Q Loss: 0.6476
[IQL] Epoch 95/500, V Loss: 0.1014, Q Loss: 0.6695
[IQL] Epoch 96/500, V Loss: 0.0972, Q Loss: 0.6528
[IQL] Epoch 97/500, V Loss: 0.1016, Q Loss: 0.7432
[IQL] Epoch 98/500, V Loss: 0.1224, Q Loss: 0.7240
[IQL] Epoch 99/500, V Loss: 0.1244, Q Loss: 0.7146
[IQL] Epoch 100/500, V Loss: 0.1090, Q Loss: 0.7620
[IQL] Epoch 101/500, V Loss: 0.1251, Q Loss: 0.7684
[IQL] Epoch 102/500, V Loss: 0.1132, Q Loss: 0.7432
[IQL] Epoch 103/500, V Loss: 0.1300, Q Loss: 0.7933
[IQL] Epoch 104/500, V Loss: 0.1296, Q Loss: 0.7603
[IQL] Epoch 105/500, V Loss: 0.1321, Q Loss: 0.7548
[IQL] Epoch 106/500, V Loss: 0.1237, Q Loss: 0.7173
[IQL] Epoch 107/500, V Loss: 0.1098, Q Loss: 0.7601
[IQL] Epoch 108/500, V Loss: 0.1394, Q Loss: 0.7548
[IQL] Epoch 109/500, V Loss: 0.1242, Q Loss: 0.7552
[IQL] Epoch 110/500, V Loss: 0.1197, Q Loss: 0.7588
[IQL] Epoch 111/500, V Loss: 0.1147, Q Loss: 0.8054
[IQL] Epoch 112/500, V Loss: 0.1562, Q Loss: 0.7955
[IQL] Epoch 113/500, V Loss: 0.1661, Q Loss: 0.8407
[IQL] Epoch 114/500, V Loss: 0.1791, Q Loss: 0.8454
[IQL] Epoch 115/500, V Loss: 0.1649, Q Loss: 0.8499
[IQL] Epoch 116/500, V Loss: 0.1144, Q Loss: 0.9043
[IQL] Epoch 117/500, V Loss: 0.1372, Q Loss: 0.8706
[IQL] Epoch 118/500, V Loss: 0.1224, Q Loss: 0.7711
[IQL] Epoch 119/500, V Loss: 0.1607, Q Loss: 0.8379
[IQL] Epoch 120/500, V Loss: 0.1252, Q Loss: 0.8568
[IQL] Epoch 121/500, V Loss: 0.1007, Q Loss: 0.8171
[IQL] Epoch 122/500, V Loss: 0.1477, Q Loss: 0.8429
[IQL] Epoch 123/500, V Loss: 0.1845, Q Loss: 0.8756
[IQL] Epoch 124/500, V Loss: 0.1482, Q Loss: 0.8394
[IQL] Epoch 125/500, V Loss: 0.0986, Q Loss: 0.9079
[IQL] Epoch 126/500, V Loss: 0.0846, Q Loss: 0.8847
[IQL] Epoch 127/500, V Loss: 0.1186, Q Loss: 0.8068
[IQL] Epoch 128/500, V Loss: 0.1380, Q Loss: 0.8394
[IQL] Epoch 129/500, V Loss: 0.1406, Q Loss: 0.8521
[IQL] Epoch 130/500, V Loss: 0.1887, Q Loss: 0.8623
[IQL] Epoch 131/500, V Loss: 0.1596, Q Loss: 0.8729
[IQL] Epoch 132/500, V Loss: 0.1058, Q Loss: 0.9171
[IQL] Epoch 133/500, V Loss: 0.1549, Q Loss: 0.9286
[IQL] Epoch 134/500, V Loss: 0.2003, Q Loss: 0.8696
[IQL] Epoch 135/500, V Loss: 0.1528, Q Loss: 0.9351
[IQL] Epoch 136/500, V Loss: 0.2252, Q Loss: 1.0101
[IQL] Epoch 137/500, V Loss: 0.2534, Q Loss: 0.8933
[IQL] Epoch 138/500, V Loss: 0.2452, Q Loss: 0.9605
[IQL] Epoch 139/500, V Loss: 0.2367, Q Loss: 0.9506
[IQL] Epoch 140/500, V Loss: 0.1856, Q Loss: 0.9277
[IQL] Epoch 141/500, V Loss: 0.1858, Q Loss: 1.0242
[IQL] Epoch 142/500, V Loss: 0.3400, Q Loss: 1.0497
[IQL] Epoch 143/500, V Loss: 0.2069, Q Loss: 0.8875
[IQL] Epoch 144/500, V Loss: 0.1243, Q Loss: 0.9879
[IQL] Epoch 145/500, V Loss: 0.1122, Q Loss: 0.8823
[IQL] Epoch 146/500, V Loss: 0.1224, Q Loss: 0.9293
[IQL] Epoch 147/500, V Loss: 0.1401, Q Loss: 0.9249
[IQL] Epoch 148/500, V Loss: 0.1913, Q Loss: 1.0231
[IQL] Epoch 149/500, V Loss: 0.1821, Q Loss: 0.8938
[IQL] Epoch 150/500, V Loss: 0.2097, Q Loss: 0.8691
[IQL] Epoch 151/500, V Loss: 0.1423, Q Loss: 0.8919
[IQL] Epoch 152/500, V Loss: 0.1033, Q Loss: 0.9385
[IQL] Epoch 153/500, V Loss: 0.1169, Q Loss: 0.8804
[IQL] Epoch 154/500, V Loss: 0.1611, Q Loss: 0.9523
[IQL] Epoch 155/500, V Loss: 0.1616, Q Loss: 0.9925
[IQL] Epoch 156/500, V Loss: 0.1981, Q Loss: 0.9894
[IQL] Epoch 157/500, V Loss: 0.2017, Q Loss: 0.8995
[IQL] Epoch 158/500, V Loss: 0.1513, Q Loss: 0.9302
[IQL] Epoch 159/500, V Loss: 0.1747, Q Loss: 0.9544
[IQL] Epoch 160/500, V Loss: 0.1661, Q Loss: 0.8949
[IQL] Epoch 161/500, V Loss: 0.1471, Q Loss: 0.9214
[IQL] Epoch 162/500, V Loss: 0.2467, Q Loss: 1.1871
[IQL] Epoch 163/500, V Loss: 0.2440, Q Loss: 1.0868
[IQL] Epoch 164/500, V Loss: 0.2105, Q Loss: 1.1017
[IQL] Epoch 165/500, V Loss: 0.2054, Q Loss: 1.0327
[IQL] Epoch 166/500, V Loss: 0.1545, Q Loss: 1.0069
[IQL] Epoch 167/500, V Loss: 0.1351, Q Loss: 0.8966
[IQL] Epoch 168/500, V Loss: 0.1540, Q Loss: 0.9614
[IQL] Epoch 169/500, V Loss: 0.2027, Q Loss: 0.9362
[IQL] Epoch 170/500, V Loss: 0.1667, Q Loss: 0.9384
[IQL] Epoch 171/500, V Loss: 0.1271, Q Loss: 0.9244
[IQL] Epoch 172/500, V Loss: 0.1415, Q Loss: 0.9307
[IQL] Epoch 173/500, V Loss: 0.1531, Q Loss: 1.0226
[IQL] Epoch 174/500, V Loss: 0.2361, Q Loss: 1.0666
[IQL] Epoch 175/500, V Loss: 0.2848, Q Loss: 0.9359
[IQL] Epoch 176/500, V Loss: 0.2190, Q Loss: 0.8910
[IQL] Epoch 177/500, V Loss: 0.1973, Q Loss: 1.0344
[IQL] Epoch 178/500, V Loss: 0.2109, Q Loss: 0.9819
[IQL] Epoch 179/500, V Loss: 0.1599, Q Loss: 1.0064
[IQL] Epoch 180/500, V Loss: 0.2215, Q Loss: 0.9370
[IQL] Epoch 181/500, V Loss: 0.2104, Q Loss: 1.0384
[IQL] Epoch 182/500, V Loss: 0.2113, Q Loss: 0.9788
[IQL] Epoch 183/500, V Loss: 0.1382, Q Loss: 0.8941
[IQL] Epoch 184/500, V Loss: 0.1064, Q Loss: 0.9955
[IQL] Epoch 185/500, V Loss: 0.1742, Q Loss: 1.0459
[IQL] Epoch 186/500, V Loss: 0.1637, Q Loss: 0.9367
[IQL] Epoch 187/500, V Loss: 0.1315, Q Loss: 0.9702
[IQL] Epoch 188/500, V Loss: 0.1169, Q Loss: 1.0487
[IQL] Epoch 189/500, V Loss: 0.1238, Q Loss: 0.9102
[IQL] Epoch 190/500, V Loss: 0.1280, Q Loss: 0.9564
[IQL] Epoch 191/500, V Loss: 0.1248, Q Loss: 1.0330
[IQL] Epoch 192/500, V Loss: 0.2284, Q Loss: 1.0121
[IQL] Epoch 193/500, V Loss: 0.2178, Q Loss: 0.9941
[IQL] Epoch 194/500, V Loss: 0.1444, Q Loss: 0.9098
[IQL] Epoch 195/500, V Loss: 0.1797, Q Loss: 0.9261
[IQL] Epoch 196/500, V Loss: 0.1913, Q Loss: 0.8548
[IQL] Epoch 197/500, V Loss: 0.1497, Q Loss: 0.9046
[IQL] Epoch 198/500, V Loss: 0.1604, Q Loss: 1.0258
[IQL] Epoch 199/500, V Loss: 0.1986, Q Loss: 0.9403
[IQL] Epoch 200/500, V Loss: 0.2477, Q Loss: 0.9957
[IQL] Epoch 201/500, V Loss: 0.1931, Q Loss: 1.1010
[IQL] Epoch 202/500, V Loss: 0.2808, Q Loss: 1.1438
[IQL] Epoch 203/500, V Loss: 0.2272, Q Loss: 0.9157
[IQL] Epoch 204/500, V Loss: 0.1972, Q Loss: 1.0026
[IQL] Epoch 205/500, V Loss: 0.1792, Q Loss: 1.0608
[IQL] Epoch 206/500, V Loss: 0.2560, Q Loss: 0.8998
[IQL] Epoch 207/500, V Loss: 0.1647, Q Loss: 0.9674
[IQL] Epoch 208/500, V Loss: 0.1592, Q Loss: 0.9100
[IQL] Epoch 209/500, V Loss: 0.1565, Q Loss: 1.0177
[IQL] Epoch 210/500, V Loss: 0.2575, Q Loss: 0.9477
[IQL] Epoch 211/500, V Loss: 0.2791, Q Loss: 0.9930
[IQL] Epoch 212/500, V Loss: 0.3268, Q Loss: 1.0197
[IQL] Epoch 213/500, V Loss: 0.1724, Q Loss: 0.9815
[IQL] Epoch 214/500, V Loss: 0.1179, Q Loss: 0.9040
[IQL] Epoch 215/500, V Loss: 0.1397, Q Loss: 1.0782
[IQL] Epoch 216/500, V Loss: 0.1515, Q Loss: 1.0761
[IQL] Epoch 217/500, V Loss: 0.2368, Q Loss: 1.1369
[IQL] Epoch 218/500, V Loss: 0.2528, Q Loss: 1.0115
[IQL] Epoch 219/500, V Loss: 0.2990, Q Loss: 1.1208
[IQL] Epoch 220/500, V Loss: 0.1492, Q Loss: 1.0131
[IQL] Epoch 221/500, V Loss: 0.2709, Q Loss: 1.0355
[IQL] Epoch 222/500, V Loss: 0.2674, Q Loss: 0.9514
[IQL] Epoch 223/500, V Loss: 0.1938, Q Loss: 0.9299
[IQL] Epoch 224/500, V Loss: 0.2658, Q Loss: 1.0696
[IQL] Epoch 225/500, V Loss: 0.2403, Q Loss: 1.1418
[IQL] Epoch 226/500, V Loss: 0.2436, Q Loss: 1.0510
[IQL] Epoch 227/500, V Loss: 0.2057, Q Loss: 1.0205
[IQL] Epoch 228/500, V Loss: 0.2299, Q Loss: 0.9690
[IQL] Epoch 229/500, V Loss: 0.1977, Q Loss: 0.9560
[IQL] Epoch 230/500, V Loss: 0.2006, Q Loss: 0.9388
[IQL] Epoch 231/500, V Loss: 0.1768, Q Loss: 0.8597
[IQL] Epoch 232/500, V Loss: 0.1664, Q Loss: 0.9004
[IQL] Epoch 233/500, V Loss: 0.1894, Q Loss: 0.8806
[IQL] Epoch 234/500, V Loss: 0.2231, Q Loss: 0.9267
[IQL] Epoch 235/500, V Loss: 0.2386, Q Loss: 1.1473
[IQL] Epoch 236/500, V Loss: 0.2467, Q Loss: 0.9212
[IQL] Epoch 237/500, V Loss: 0.2463, Q Loss: 0.8964
[IQL] Epoch 238/500, V Loss: 0.1536, Q Loss: 1.0553
[IQL] Epoch 239/500, V Loss: 0.1660, Q Loss: 0.9531
[IQL] Epoch 240/500, V Loss: 0.1744, Q Loss: 0.9077
[IQL] Epoch 241/500, V Loss: 0.1675, Q Loss: 0.9156
[IQL] Epoch 242/500, V Loss: 0.2408, Q Loss: 1.1113
[IQL] Epoch 243/500, V Loss: 0.3020, Q Loss: 1.1076
[IQL] Epoch 244/500, V Loss: 0.2255, Q Loss: 1.0956
[IQL] Epoch 245/500, V Loss: 0.1994, Q Loss: 0.9171
[IQL] Epoch 246/500, V Loss: 0.1283, Q Loss: 0.9485
[IQL] Epoch 247/500, V Loss: 0.1480, Q Loss: 1.0087
[IQL] Epoch 248/500, V Loss: 0.2323, Q Loss: 0.9730
[IQL] Epoch 249/500, V Loss: 0.2182, Q Loss: 1.1920
[IQL] Epoch 250/500, V Loss: 0.1926, Q Loss: 1.3102
[IQL] Epoch 251/500, V Loss: 0.2971, Q Loss: 1.2340
[IQL] Epoch 252/500, V Loss: 0.5092, Q Loss: 1.3850
[IQL] Epoch 253/500, V Loss: 0.2051, Q Loss: 1.1924
[IQL] Epoch 254/500, V Loss: 0.2325, Q Loss: 1.0659
[IQL] Epoch 255/500, V Loss: 0.1940, Q Loss: 1.0112
[IQL] Epoch 256/500, V Loss: 0.1837, Q Loss: 0.9155
[IQL] Epoch 257/500, V Loss: 0.1480, Q Loss: 0.9134
[IQL] Epoch 258/500, V Loss: 0.1500, Q Loss: 0.9235
[IQL] Epoch 259/500, V Loss: 0.2220, Q Loss: 1.1354
[IQL] Epoch 260/500, V Loss: 0.2552, Q Loss: 0.9838
[IQL] Epoch 261/500, V Loss: 0.3907, Q Loss: 1.4390
[IQL] Epoch 262/500, V Loss: 0.2964, Q Loss: 1.1706
[IQL] Epoch 263/500, V Loss: 0.2971, Q Loss: 1.0176
[IQL] Epoch 264/500, V Loss: 0.2611, Q Loss: 1.1250
[IQL] Epoch 265/500, V Loss: 0.2163, Q Loss: 1.0239
[IQL] Epoch 266/500, V Loss: 0.2285, Q Loss: 0.9203
[IQL] Epoch 267/500, V Loss: 0.2674, Q Loss: 0.9429
[IQL] Epoch 268/500, V Loss: 0.2598, Q Loss: 0.9874
[IQL] Epoch 269/500, V Loss: 0.2187, Q Loss: 0.9778
[IQL] Epoch 270/500, V Loss: 0.2093, Q Loss: 0.8988
[IQL] Epoch 271/500, V Loss: 0.1724, Q Loss: 0.9897
[IQL] Epoch 272/500, V Loss: 0.2294, Q Loss: 1.0018
[IQL] Epoch 273/500, V Loss: 0.1779, Q Loss: 0.9284
[IQL] Epoch 274/500, V Loss: 0.1763, Q Loss: 0.9358
[IQL] Epoch 275/500, V Loss: 0.1911, Q Loss: 0.8421
[IQL] Epoch 276/500, V Loss: 0.2421, Q Loss: 1.0903
[IQL] Epoch 277/500, V Loss: 0.1895, Q Loss: 0.9614
[IQL] Epoch 278/500, V Loss: 0.1699, Q Loss: 0.8904
[IQL] Epoch 279/500, V Loss: 0.2478, Q Loss: 0.9373
[IQL] Epoch 280/500, V Loss: 0.1930, Q Loss: 0.9782
[IQL] Epoch 281/500, V Loss: 0.2326, Q Loss: 0.9037
[IQL] Epoch 282/500, V Loss: 0.1667, Q Loss: 0.8944
[IQL] Epoch 283/500, V Loss: 0.2128, Q Loss: 1.0158
[IQL] Epoch 284/500, V Loss: 0.2042, Q Loss: 1.0526
[IQL] Epoch 285/500, V Loss: 0.1885, Q Loss: 0.8308
[IQL] Epoch 286/500, V Loss: 0.2132, Q Loss: 1.0113
[IQL] Epoch 287/500, V Loss: 0.2067, Q Loss: 0.8377
[IQL] Epoch 288/500, V Loss: 0.1806, Q Loss: 0.9433
[IQL] Epoch 289/500, V Loss: 0.2493, Q Loss: 0.8576
[IQL] Epoch 290/500, V Loss: 0.2075, Q Loss: 1.0835
[IQL] Epoch 291/500, V Loss: 0.3455, Q Loss: 1.0226
[IQL] Epoch 292/500, V Loss: 0.2865, Q Loss: 1.0389
[IQL] Epoch 293/500, V Loss: 0.2034, Q Loss: 1.0427
[IQL] Epoch 294/500, V Loss: 0.2340, Q Loss: 1.0132
[IQL] Epoch 295/500, V Loss: 0.1982, Q Loss: 0.8580
[IQL] Epoch 296/500, V Loss: 0.2146, Q Loss: 0.8531
[IQL] Epoch 297/500, V Loss: 0.1680, Q Loss: 1.0171
[IQL] Epoch 298/500, V Loss: 0.2713, Q Loss: 0.8997
[IQL] Epoch 299/500, V Loss: 0.2496, Q Loss: 0.9405
[IQL] Epoch 300/500, V Loss: 0.1824, Q Loss: 1.0410
[IQL] Epoch 301/500, V Loss: 0.2141, Q Loss: 1.0123
[IQL] Epoch 302/500, V Loss: 0.2426, Q Loss: 0.9818
[IQL] Epoch 303/500, V Loss: 0.2834, Q Loss: 1.0502
[IQL] Epoch 304/500, V Loss: 0.2419, Q Loss: 1.0731
[IQL] Epoch 305/500, V Loss: 0.1691, Q Loss: 1.0054
[IQL] Epoch 306/500, V Loss: 0.2308, Q Loss: 1.0279
[IQL] Epoch 307/500, V Loss: 0.2346, Q Loss: 0.9109
[IQL] Epoch 308/500, V Loss: 0.1817, Q Loss: 0.8123
[IQL] Epoch 309/500, V Loss: 0.2020, Q Loss: 0.8937
[IQL] Epoch 310/500, V Loss: 0.2988, Q Loss: 0.8778
[IQL] Epoch 311/500, V Loss: 0.1542, Q Loss: 1.0193
[IQL] Epoch 312/500, V Loss: 0.2057, Q Loss: 0.9078
[IQL] Epoch 313/500, V Loss: 0.1910, Q Loss: 0.8625
[IQL] Epoch 314/500, V Loss: 0.1839, Q Loss: 0.9928
[IQL] Epoch 315/500, V Loss: 0.2521, Q Loss: 0.9644
[IQL] Epoch 316/500, V Loss: 0.2479, Q Loss: 0.9450
[IQL] Epoch 317/500, V Loss: 0.1698, Q Loss: 1.0422
[IQL] Epoch 318/500, V Loss: 0.1646, Q Loss: 1.0851
[IQL] Epoch 319/500, V Loss: 0.1836, Q Loss: 0.8485
[IQL] Epoch 320/500, V Loss: 0.2164, Q Loss: 0.9403
[IQL] Epoch 321/500, V Loss: 0.2747, Q Loss: 1.4375
[IQL] Epoch 322/500, V Loss: 0.3695, Q Loss: 1.2158
[IQL] Epoch 323/500, V Loss: 0.3258, Q Loss: 0.9803
[IQL] Epoch 324/500, V Loss: 0.2466, Q Loss: 1.1631
[IQL] Epoch 325/500, V Loss: 0.2636, Q Loss: 0.9788
[IQL] Epoch 326/500, V Loss: 0.2367, Q Loss: 0.9241
[IQL] Epoch 327/500, V Loss: 0.1503, Q Loss: 0.8909
[IQL] Epoch 328/500, V Loss: 0.1836, Q Loss: 1.0226
[IQL] Epoch 329/500, V Loss: 0.1645, Q Loss: 1.1172
[IQL] Epoch 330/500, V Loss: 0.1709, Q Loss: 1.0244
[IQL] Epoch 331/500, V Loss: 0.3187, Q Loss: 1.0471
[IQL] Epoch 332/500, V Loss: 0.2209, Q Loss: 0.9560
[IQL] Epoch 333/500, V Loss: 0.1785, Q Loss: 0.8008
[IQL] Epoch 334/500, V Loss: 0.1805, Q Loss: 1.0030
[IQL] Epoch 335/500, V Loss: 0.2261, Q Loss: 1.1522
[IQL] Epoch 336/500, V Loss: 0.1951, Q Loss: 1.2565
[IQL] Epoch 337/500, V Loss: 0.1726, Q Loss: 1.0185
[IQL] Epoch 338/500, V Loss: 0.1576, Q Loss: 0.9817
[IQL] Epoch 339/500, V Loss: 0.1724, Q Loss: 1.0565
[IQL] Epoch 340/500, V Loss: 0.2264, Q Loss: 1.2103
[IQL] Epoch 341/500, V Loss: 0.2299, Q Loss: 1.0923
[IQL] Epoch 342/500, V Loss: 0.2239, Q Loss: 1.0986
[IQL] Epoch 343/500, V Loss: 0.2012, Q Loss: 1.2530
[IQL] Epoch 344/500, V Loss: 0.2936, Q Loss: 1.2247
[IQL] Epoch 345/500, V Loss: 0.2393, Q Loss: 0.9744
[IQL] Epoch 346/500, V Loss: 0.1803, Q Loss: 0.9164
[IQL] Epoch 347/500, V Loss: 0.2556, Q Loss: 1.0343
[IQL] Epoch 348/500, V Loss: 0.1949, Q Loss: 0.9146
[IQL] Epoch 349/500, V Loss: 0.3232, Q Loss: 1.1908
[IQL] Epoch 350/500, V Loss: 0.4081, Q Loss: 1.0162
[IQL] Epoch 351/500, V Loss: 0.2521, Q Loss: 1.0453
[IQL] Epoch 352/500, V Loss: 0.1656, Q Loss: 1.0353
[IQL] Epoch 353/500, V Loss: 0.2861, Q Loss: 1.1221
[IQL] Epoch 354/500, V Loss: 0.1810, Q Loss: 1.0194
[IQL] Epoch 355/500, V Loss: 0.2212, Q Loss: 0.9949
[IQL] Epoch 356/500, V Loss: 0.2107, Q Loss: 0.9713
[IQL] Epoch 357/500, V Loss: 0.1557, Q Loss: 1.0555
[IQL] Epoch 358/500, V Loss: 0.2465, Q Loss: 1.1318
[IQL] Epoch 359/500, V Loss: 0.2436, Q Loss: 1.0690
[IQL] Epoch 360/500, V Loss: 0.2919, Q Loss: 0.9710
[IQL] Epoch 361/500, V Loss: 0.2001, Q Loss: 1.0780
[IQL] Epoch 362/500, V Loss: 0.2010, Q Loss: 0.8581
[IQL] Epoch 363/500, V Loss: 0.2407, Q Loss: 1.1329
[IQL] Epoch 364/500, V Loss: 0.2094, Q Loss: 0.9465
[IQL] Epoch 365/500, V Loss: 0.1905, Q Loss: 1.0458
[IQL] Epoch 366/500, V Loss: 0.2392, Q Loss: 1.0991
[IQL] Epoch 367/500, V Loss: 0.3536, Q Loss: 0.9278
[IQL] Epoch 368/500, V Loss: 0.1882, Q Loss: 1.0682
[IQL] Epoch 369/500, V Loss: 0.2873, Q Loss: 1.0366
[IQL] Epoch 370/500, V Loss: 0.2398, Q Loss: 1.1053
[IQL] Epoch 371/500, V Loss: 0.2842, Q Loss: 1.0992
[IQL] Epoch 372/500, V Loss: 0.2559, Q Loss: 1.0111
[IQL] Epoch 373/500, V Loss: 0.2249, Q Loss: 1.0653
[IQL] Epoch 374/500, V Loss: 0.2461, Q Loss: 0.9224
[IQL] Epoch 375/500, V Loss: 0.1948, Q Loss: 1.0305
[IQL] Epoch 376/500, V Loss: 0.2560, Q Loss: 1.0512
[IQL] Epoch 377/500, V Loss: 0.2958, Q Loss: 0.9619
[IQL] Epoch 378/500, V Loss: 0.3225, Q Loss: 1.0597
[IQL] Epoch 379/500, V Loss: 0.3197, Q Loss: 0.9386
[IQL] Epoch 380/500, V Loss: 0.2221, Q Loss: 1.0193
[IQL] Epoch 381/500, V Loss: 0.1863, Q Loss: 0.8745
[IQL] Epoch 382/500, V Loss: 0.2682, Q Loss: 0.9304
[IQL] Epoch 383/500, V Loss: 0.2549, Q Loss: 1.2454
[IQL] Epoch 384/500, V Loss: 0.4318, Q Loss: 1.4841
[IQL] Epoch 385/500, V Loss: 0.2825, Q Loss: 1.1064
[IQL] Epoch 386/500, V Loss: 0.2272, Q Loss: 1.3063
[IQL] Epoch 387/500, V Loss: 0.2281, Q Loss: 1.0172
[IQL] Epoch 388/500, V Loss: 0.1972, Q Loss: 1.0180
[IQL] Epoch 389/500, V Loss: 0.1642, Q Loss: 1.0630
[IQL] Epoch 390/500, V Loss: 0.1328, Q Loss: 0.9421
[IQL] Epoch 391/500, V Loss: 0.1939, Q Loss: 0.9858
[IQL] Epoch 392/500, V Loss: 0.1549, Q Loss: 0.9905
[IQL] Epoch 393/500, V Loss: 0.2474, Q Loss: 0.9853
[IQL] Epoch 394/500, V Loss: 0.2286, Q Loss: 1.0852
[IQL] Epoch 395/500, V Loss: 0.2142, Q Loss: 0.9663
[IQL] Epoch 396/500, V Loss: 0.1793, Q Loss: 1.1508
[IQL] Epoch 397/500, V Loss: 0.3739, Q Loss: 1.3410
[IQL] Epoch 398/500, V Loss: 0.3011, Q Loss: 0.9480
[IQL] Epoch 399/500, V Loss: 0.1926, Q Loss: 1.0973
[IQL] Epoch 400/500, V Loss: 0.2448, Q Loss: 0.9836
[IQL] Epoch 401/500, V Loss: 0.2316, Q Loss: 1.1609
[IQL] Epoch 402/500, V Loss: 0.2351, Q Loss: 1.2443
[IQL] Epoch 403/500, V Loss: 0.2483, Q Loss: 1.2306
[IQL] Epoch 404/500, V Loss: 0.2179, Q Loss: 1.1072
[IQL] Epoch 405/500, V Loss: 0.1850, Q Loss: 1.1116
[IQL] Epoch 406/500, V Loss: 0.2219, Q Loss: 1.2502
[IQL] Epoch 407/500, V Loss: 0.2295, Q Loss: 1.2094
[IQL] Epoch 408/500, V Loss: 0.2348, Q Loss: 1.0155
[IQL] Epoch 409/500, V Loss: 0.3418, Q Loss: 1.0817
[IQL] Epoch 410/500, V Loss: 0.2142, Q Loss: 1.0709
[IQL] Epoch 411/500, V Loss: 0.1957, Q Loss: 1.0035
[IQL] Epoch 412/500, V Loss: 0.2830, Q Loss: 1.0469
[IQL] Epoch 413/500, V Loss: 0.2003, Q Loss: 1.0533
[IQL] Epoch 414/500, V Loss: 0.2121, Q Loss: 1.0031
[IQL] Epoch 415/500, V Loss: 0.3246, Q Loss: 1.1939
[IQL] Epoch 416/500, V Loss: 0.1966, Q Loss: 1.2906
[IQL] Epoch 417/500, V Loss: 0.2878, Q Loss: 1.3202
[IQL] Epoch 418/500, V Loss: 0.2775, Q Loss: 1.1385
[IQL] Epoch 419/500, V Loss: 0.1937, Q Loss: 1.1576
[IQL] Epoch 420/500, V Loss: 0.2140, Q Loss: 1.1462
[IQL] Epoch 421/500, V Loss: 0.2549, Q Loss: 1.3048
[IQL] Epoch 422/500, V Loss: 0.2424, Q Loss: 1.0644
[IQL] Epoch 423/500, V Loss: 0.2911, Q Loss: 1.3286
[IQL] Epoch 424/500, V Loss: 0.3274, Q Loss: 1.1387
[IQL] Epoch 425/500, V Loss: 0.3128, Q Loss: 1.0297
[IQL] Epoch 426/500, V Loss: 0.2351, Q Loss: 1.1335
[IQL] Epoch 427/500, V Loss: 0.2912, Q Loss: 1.0591
[IQL] Epoch 428/500, V Loss: 0.2658, Q Loss: 1.0817
[IQL] Epoch 429/500, V Loss: 0.2459, Q Loss: 1.1349
[IQL] Epoch 430/500, V Loss: 0.3139, Q Loss: 1.2567
[IQL] Epoch 431/500, V Loss: 0.3535, Q Loss: 1.2247
[IQL] Epoch 432/500, V Loss: 0.3265, Q Loss: 1.1135
[IQL] Epoch 433/500, V Loss: 0.2668, Q Loss: 1.1663
[IQL] Epoch 434/500, V Loss: 0.3518, Q Loss: 1.1164
[IQL] Epoch 435/500, V Loss: 0.2407, Q Loss: 1.1624
[IQL] Epoch 436/500, V Loss: 0.3138, Q Loss: 1.0248
[IQL] Epoch 437/500, V Loss: 0.2136, Q Loss: 0.9214
[IQL] Epoch 438/500, V Loss: 0.2507, Q Loss: 1.1107
[IQL] Epoch 439/500, V Loss: 0.2960, Q Loss: 1.1564
[IQL] Epoch 440/500, V Loss: 0.1407, Q Loss: 1.3150
[IQL] Epoch 441/500, V Loss: 0.2886, Q Loss: 1.0986
[IQL] Epoch 442/500, V Loss: 0.2617, Q Loss: 0.9577
[IQL] Epoch 443/500, V Loss: 0.2045, Q Loss: 1.2221
[IQL] Epoch 444/500, V Loss: 0.4030, Q Loss: 1.1019
[IQL] Epoch 445/500, V Loss: 0.2572, Q Loss: 1.1152
[IQL] Epoch 446/500, V Loss: 0.2179, Q Loss: 1.2808
[IQL] Epoch 447/500, V Loss: 0.2646, Q Loss: 1.1905
[IQL] Epoch 448/500, V Loss: 0.2516, Q Loss: 1.0529
[IQL] Epoch 449/500, V Loss: 0.2480, Q Loss: 1.1642
[IQL] Epoch 450/500, V Loss: 0.1735, Q Loss: 1.4189
[IQL] Epoch 451/500, V Loss: 0.3346, Q Loss: 1.4423
[IQL] Epoch 452/500, V Loss: 0.2428, Q Loss: 1.2599
[IQL] Epoch 453/500, V Loss: 0.2808, Q Loss: 1.1511
[IQL] Epoch 454/500, V Loss: 0.2534, Q Loss: 1.0219
[IQL] Epoch 455/500, V Loss: 0.2773, Q Loss: 1.0706
[IQL] Epoch 456/500, V Loss: 0.3034, Q Loss: 1.0274
[IQL] Epoch 457/500, V Loss: 0.3182, Q Loss: 1.1201
[IQL] Epoch 458/500, V Loss: 0.2974, Q Loss: 0.9722
[IQL] Epoch 459/500, V Loss: 0.1977, Q Loss: 1.1197
[IQL] Epoch 460/500, V Loss: 0.2254, Q Loss: 1.1429
[IQL] Epoch 461/500, V Loss: 0.2539, Q Loss: 1.1071
[IQL] Epoch 462/500, V Loss: 0.2995, Q Loss: 1.2030
[IQL] Epoch 463/500, V Loss: 0.3848, Q Loss: 1.3157
[IQL] Epoch 464/500, V Loss: 0.2610, Q Loss: 1.1420
[IQL] Epoch 465/500, V Loss: 0.3539, Q Loss: 1.0205
[IQL] Epoch 466/500, V Loss: 0.3035, Q Loss: 1.1324
[IQL] Epoch 467/500, V Loss: 0.2987, Q Loss: 1.1919
[IQL] Epoch 468/500, V Loss: 0.2457, Q Loss: 1.0671
[IQL] Epoch 469/500, V Loss: 0.1629, Q Loss: 1.3025
[IQL] Epoch 470/500, V Loss: 0.2507, Q Loss: 1.1365
[IQL] Epoch 471/500, V Loss: 0.2474, Q Loss: 1.0453
[IQL] Epoch 472/500, V Loss: 0.2588, Q Loss: 1.1395
[IQL] Epoch 473/500, V Loss: 0.2717, Q Loss: 0.9464
[IQL] Epoch 474/500, V Loss: 0.2210, Q Loss: 1.1574
[IQL] Epoch 475/500, V Loss: 0.3337, Q Loss: 1.0096
[IQL] Epoch 476/500, V Loss: 0.2721, Q Loss: 1.2282
[IQL] Epoch 477/500, V Loss: 0.2738, Q Loss: 1.1715
[IQL] Epoch 478/500, V Loss: 0.3556, Q Loss: 1.1123
[IQL] Epoch 479/500, V Loss: 0.2690, Q Loss: 1.4096
[IQL] Epoch 480/500, V Loss: 0.3398, Q Loss: 1.2675
[IQL] Epoch 481/500, V Loss: 0.3818, Q Loss: 1.1265
[IQL] Epoch 482/500, V Loss: 0.2483, Q Loss: 1.1658
[IQL] Epoch 483/500, V Loss: 0.3198, Q Loss: 1.1920
[IQL] Epoch 484/500, V Loss: 0.2499, Q Loss: 1.1138
[IQL] Epoch 485/500, V Loss: 0.2557, Q Loss: 1.1051
[IQL] Epoch 486/500, V Loss: 0.2425, Q Loss: 1.1755
[IQL] Epoch 487/500, V Loss: 0.2458, Q Loss: 0.9741
[IQL] Epoch 488/500, V Loss: 0.3071, Q Loss: 0.9297
[IQL] Epoch 489/500, V Loss: 0.1959, Q Loss: 1.2074
[IQL] Epoch 490/500, V Loss: 0.3585, Q Loss: 1.2854
[IQL] Epoch 491/500, V Loss: 0.2497, Q Loss: 1.2545
[IQL] Epoch 492/500, V Loss: 0.1988, Q Loss: 1.1628
[IQL] Epoch 493/500, V Loss: 0.2418, Q Loss: 1.2048
[IQL] Epoch 494/500, V Loss: 0.3424, Q Loss: 1.1908
[IQL] Epoch 495/500, V Loss: 0.3185, Q Loss: 1.1165
[IQL] Epoch 496/500, V Loss: 0.3047, Q Loss: 0.9305
[IQL] Epoch 497/500, V Loss: 0.3951, Q Loss: 1.7395
[IQL] Epoch 498/500, V Loss: 0.6103, Q Loss: 0.9459
[IQL] Epoch 499/500, V Loss: 0.2163, Q Loss: 1.5338
[RL100] VIB betas set to factor=0.1: beta_recon=0.000010, beta_kl=0.000010

[RL100Trainer] Phase 2b: Offline RL Optimization (Iteration 0)
[OPE] Behavior policy value J_old = 61.5332
[RL PPO] Reducing policy LR: 1.00e-04 → 1.00e-05
[Offline RL] Epoch 0/100, PPO Loss: -0.0270, CD Loss: 1.0967
[Offline RL] Epoch 1/100, PPO Loss: -0.0261, CD Loss: 0.1466
[Offline RL] Epoch 2/100, PPO Loss: -0.0241, CD Loss: 0.3066
[Offline RL] Epoch 3/100, PPO Loss: -0.0241, CD Loss: 0.0898
[Offline RL] Epoch 4/100, PPO Loss: -0.0256, CD Loss: 0.1072
[Offline RL] Epoch 5/100, PPO Loss: -0.0265, CD Loss: 0.1478
[Offline RL] Epoch 6/100, PPO Loss: -0.0255, CD Loss: 0.1037
[Offline RL] Epoch 7/100, PPO Loss: -0.0254, CD Loss: 0.0697
[Offline RL] Epoch 8/100, PPO Loss: -0.0250, CD Loss: 0.0779
[Offline RL] Epoch 9/100, PPO Loss: -0.0257, CD Loss: 0.0939
[Offline RL] Epoch 10/100, PPO Loss: -0.0234, CD Loss: 0.0862
[Offline RL] Epoch 11/100, PPO Loss: -0.0240, CD Loss: 0.0672
[Offline RL] Epoch 12/100, PPO Loss: -0.0227, CD Loss: 0.0541
[Offline RL] Epoch 13/100, PPO Loss: -0.0219, CD Loss: 0.0514
[Offline RL] Epoch 14/100, PPO Loss: -0.0212, CD Loss: 0.0581
[Offline RL] Epoch 15/100, PPO Loss: -0.0210, CD Loss: 0.0643
[Offline RL] Epoch 16/100, PPO Loss: -0.0223, CD Loss: 0.0564
[Offline RL] Epoch 17/100, PPO Loss: -0.0215, CD Loss: 0.0541
[Offline RL] Epoch 18/100, PPO Loss: -0.0253, CD Loss: 0.0460
[Offline RL] Epoch 19/100, PPO Loss: -0.0233, CD Loss: 0.0462
[Offline RL] Epoch 20/100, PPO Loss: -0.0225, CD Loss: 0.0506
[Offline RL] Epoch 21/100, PPO Loss: -0.0239, CD Loss: 0.0550
[Offline RL] Epoch 22/100, PPO Loss: -0.0209, CD Loss: 0.0533
[Offline RL] Epoch 23/100, PPO Loss: -0.0224, CD Loss: 0.0520
[Offline RL] Epoch 24/100, PPO Loss: -0.0209, CD Loss: 0.0528
[Offline RL] Epoch 25/100, PPO Loss: -0.0204, CD Loss: 0.0577
[Offline RL] Epoch 26/100, PPO Loss: -0.0205, CD Loss: 0.0741
[Offline RL] Epoch 27/100, PPO Loss: -0.0197, CD Loss: 0.0626
[Offline RL] Epoch 28/100, PPO Loss: -0.0199, CD Loss: 0.0625
[Offline RL] Epoch 29/100, PPO Loss: -0.0223, CD Loss: 0.0652
[Offline RL] Epoch 30/100, PPO Loss: -0.0199, CD Loss: 0.0586
[Offline RL] Epoch 31/100, PPO Loss: -0.0222, CD Loss: 0.0601
[Offline RL] Epoch 32/100, PPO Loss: -0.0223, CD Loss: 0.0617
[Offline RL] Epoch 33/100, PPO Loss: -0.0208, CD Loss: 0.0667
[Offline RL] Epoch 34/100, PPO Loss: -0.0212, CD Loss: 0.0751
[Offline RL] Epoch 35/100, PPO Loss: -0.0193, CD Loss: 0.0767
[Offline RL] Epoch 36/100, PPO Loss: -0.0205, CD Loss: 0.0768
[Offline RL] Epoch 37/100, PPO Loss: -0.0196, CD Loss: 0.0683
[Offline RL] Epoch 38/100, PPO Loss: -0.0205, CD Loss: 0.0622
[Offline RL] Epoch 39/100, PPO Loss: -0.0216, CD Loss: 0.0652
[Offline RL] Epoch 40/100, PPO Loss: -0.0197, CD Loss: 0.0690
[Offline RL] Epoch 41/100, PPO Loss: -0.0201, CD Loss: 0.0647
[Offline RL] Epoch 42/100, PPO Loss: -0.0201, CD Loss: 0.0677
[Offline RL] Epoch 43/100, PPO Loss: -0.0202, CD Loss: 0.0640
[Offline RL] Epoch 44/100, PPO Loss: -0.0194, CD Loss: 0.0655
[Offline RL] Epoch 45/100, PPO Loss: -0.0190, CD Loss: 0.0644
[Offline RL] Epoch 46/100, PPO Loss: -0.0173, CD Loss: 0.0664
[Offline RL] Epoch 47/100, PPO Loss: -0.0175, CD Loss: 0.0605
[Offline RL] Epoch 48/100, PPO Loss: -0.0182, CD Loss: 0.0639
[Offline RL] Epoch 49/100, PPO Loss: -0.0168, CD Loss: 0.0673
[Offline RL] Epoch 50/100, PPO Loss: -0.0175, CD Loss: 0.0700
[Offline RL] Epoch 51/100, PPO Loss: -0.0181, CD Loss: 0.0731
[Offline RL] Epoch 52/100, PPO Loss: -0.0190, CD Loss: 0.0735
[Offline RL] Epoch 53/100, PPO Loss: -0.0198, CD Loss: 0.0708
[Offline RL] Epoch 54/100, PPO Loss: -0.0196, CD Loss: 0.0683
[Offline RL] Epoch 55/100, PPO Loss: -0.0203, CD Loss: 0.0657
[Offline RL] Epoch 56/100, PPO Loss: -0.0211, CD Loss: 0.0668
[Offline RL] Epoch 57/100, PPO Loss: -0.0230, CD Loss: 0.0691
[Offline RL] Epoch 58/100, PPO Loss: -0.0229, CD Loss: 0.0722
[Offline RL] Epoch 59/100, PPO Loss: -0.0213, CD Loss: 0.0727
[Offline RL] Epoch 60/100, PPO Loss: -0.0195, CD Loss: 0.0744
[Offline RL] Epoch 61/100, PPO Loss: -0.0213, CD Loss: 0.0696
[Offline RL] Epoch 62/100, PPO Loss: -0.0187, CD Loss: 0.0725
[Offline RL] Epoch 63/100, PPO Loss: -0.0201, CD Loss: 0.0743
[Offline RL] Epoch 64/100, PPO Loss: -0.0174, CD Loss: 0.0796
[Offline RL] Epoch 65/100, PPO Loss: -0.0205, CD Loss: 0.0851
[Offline RL] Epoch 66/100, PPO Loss: -0.0200, CD Loss: 0.0809
[Offline RL] Epoch 67/100, PPO Loss: -0.0201, CD Loss: 0.0831
[Offline RL] Epoch 68/100, PPO Loss: -0.0214, CD Loss: 0.0834
[Offline RL] Epoch 69/100, PPO Loss: -0.0194, CD Loss: 0.0803
[Offline RL] Epoch 70/100, PPO Loss: -0.0225, CD Loss: 0.0844
[Offline RL] Epoch 71/100, PPO Loss: -0.0191, CD Loss: 0.0875
[Offline RL] Epoch 72/100, PPO Loss: -0.0192, CD Loss: 0.0850
[Offline RL] Epoch 73/100, PPO Loss: -0.0218, CD Loss: 0.0837
[Offline RL] Epoch 74/100, PPO Loss: -0.0193, CD Loss: 0.0817
[Offline RL] Epoch 75/100, PPO Loss: -0.0210, CD Loss: 0.0798
[Offline RL] Epoch 76/100, PPO Loss: -0.0190, CD Loss: 0.0747
[Offline RL] Epoch 77/100, PPO Loss: -0.0190, CD Loss: 0.0812
[Offline RL] Epoch 78/100, PPO Loss: -0.0221, CD Loss: 0.0823
[Offline RL] Epoch 79/100, PPO Loss: -0.0181, CD Loss: 0.0781
[Offline RL] Epoch 80/100, PPO Loss: -0.0189, CD Loss: 0.0802
[Offline RL] Epoch 81/100, PPO Loss: -0.0204, CD Loss: 0.0840
[Offline RL] Epoch 82/100, PPO Loss: -0.0226, CD Loss: 0.0913
[Offline RL] Epoch 83/100, PPO Loss: -0.0202, CD Loss: 0.0960
[Offline RL] Epoch 84/100, PPO Loss: -0.0190, CD Loss: 0.0975
[Offline RL] Epoch 85/100, PPO Loss: -0.0194, CD Loss: 0.0942
[Offline RL] Epoch 86/100, PPO Loss: -0.0197, CD Loss: 0.0856
[Offline RL] Epoch 87/100, PPO Loss: -0.0206, CD Loss: 0.0848
[Offline RL] Epoch 88/100, PPO Loss: -0.0201, CD Loss: 0.0816
[Offline RL] Epoch 89/100, PPO Loss: -0.0228, CD Loss: 0.0844
[Offline RL] Epoch 90/100, PPO Loss: -0.0244, CD Loss: 0.0796
[Offline RL] Epoch 91/100, PPO Loss: -0.0218, CD Loss: 0.0864
[Offline RL] Epoch 92/100, PPO Loss: -0.0237, CD Loss: 0.0863
[Offline RL] Epoch 93/100, PPO Loss: -0.0237, CD Loss: 0.0849
[Offline RL] Epoch 94/100, PPO Loss: -0.0246, CD Loss: 0.0821
[Offline RL] Epoch 95/100, PPO Loss: -0.0222, CD Loss: 0.0820
[Offline RL] Epoch 96/100, PPO Loss: -0.0213, CD Loss: 0.0789
[Offline RL] Epoch 97/100, PPO Loss: -0.0213, CD Loss: 0.0833
[Offline RL] Epoch 98/100, PPO Loss: -0.0233, CD Loss: 0.0852
[Offline RL] Epoch 99/100, PPO Loss: -0.0218, CD Loss: 0.0767
[OPE] Policy REJECTED: J_new=61.4407 ≤ J_old=61.5332 + δ=3.0767. Rolling back to behavior policy.

[RL100Trainer] Phase 2c: Collecting New Data (Iteration 0)
[Collect] 50 episodes, success=0.440, steps=1250
[Data Collection] Success Rate: 0.440, Reward: 11589.64, Episodes: 50, Steps: 1250
[Dataset] Merged 50 episodes (1250 steps) → total 3250 steps, 60 episodes
[RL100] VIB betas set to factor=1.0: beta_recon=0.000100, beta_kl=0.000100

[RL100Trainer] Retraining IL on merged dataset...

============================================================
[RL100Trainer] Phase 1: Imitation Learning
============================================================

[IL] Epoch 0/100, Loss: 0.2554
[IL] Epoch 1/100, Loss: 0.1511
[IL] Epoch 2/100, Loss: 0.1418
[IL] Epoch 3/100, Loss: 0.1225
[IL] Epoch 4/100, Loss: 0.1150
[IL] Epoch 5/100, Loss: 0.1041
[IL] Epoch 6/100, Loss: 0.1079
[IL] Epoch 7/100, Loss: 0.1043
[IL] Epoch 8/100, Loss: 0.0932
[IL] Epoch 9/100, Loss: 0.0929
[IL] Epoch 10/100, Loss: 0.0859
[IL] Epoch 11/100, Loss: 0.0971
[IL] Epoch 12/100, Loss: 0.0974
[IL] Epoch 13/100, Loss: 0.0802
[IL] Epoch 14/100, Loss: 0.0845
[IL] Epoch 15/100, Loss: 0.0861
[IL] Epoch 16/100, Loss: 0.0779
[IL] Epoch 17/100, Loss: 0.0755
[IL] Epoch 18/100, Loss: 0.0781
[IL] Epoch 19/100, Loss: 0.0748
[IL] Epoch 20/100, Loss: 0.0836
[IL] Epoch 21/100, Loss: 0.0768
[IL] Epoch 22/100, Loss: 0.0693
[IL] Epoch 23/100, Loss: 0.0756
[IL] Epoch 24/100, Loss: 0.0680
[IL] Epoch 25/100, Loss: 0.0735
[IL] Epoch 26/100, Loss: 0.0798
[IL] Epoch 27/100, Loss: 0.0719
[IL] Epoch 28/100, Loss: 0.0771
[IL] Epoch 29/100, Loss: 0.0656
[IL] Epoch 30/100, Loss: 0.0730
[IL] Epoch 31/100, Loss: 0.0683
[IL] Epoch 32/100, Loss: 0.0663
[IL] Epoch 33/100, Loss: 0.0672
[IL] Epoch 34/100, Loss: 0.0663
[IL] Epoch 35/100, Loss: 0.0658
[IL] Epoch 36/100, Loss: 0.0692
[IL] Epoch 37/100, Loss: 0.0675
[IL] Epoch 38/100, Loss: 0.0640
[IL] Epoch 39/100, Loss: 0.0697
[IL] Epoch 40/100, Loss: 0.0680
[IL] Epoch 41/100, Loss: 0.0669
[IL] Epoch 42/100, Loss: 0.0648
[IL] Epoch 43/100, Loss: 0.0635
[IL] Epoch 44/100, Loss: 0.0672
[IL] Epoch 45/100, Loss: 0.0629
[IL] Epoch 46/100, Loss: 0.0646
[IL] Epoch 47/100, Loss: 0.0655
[IL] Epoch 48/100, Loss: 0.0694
[IL] Epoch 49/100, Loss: 0.0666
[IL] Epoch 50/100, Loss: 0.0619
[IL] Epoch 51/100, Loss: 0.0605
[IL] Epoch 52/100, Loss: 0.0606
[IL] Epoch 53/100, Loss: 0.0695
[IL] Epoch 54/100, Loss: 0.0560
[IL] Epoch 55/100, Loss: 0.0695
[IL] Epoch 56/100, Loss: 0.0651
[IL] Epoch 57/100, Loss: 0.0578
[IL] Epoch 58/100, Loss: 0.0628
[IL] Epoch 59/100, Loss: 0.0615
[IL] Epoch 60/100, Loss: 0.0618
[IL] Epoch 61/100, Loss: 0.0582
[IL] Epoch 62/100, Loss: 0.0582
[IL] Epoch 63/100, Loss: 0.0592
[IL] Epoch 64/100, Loss: 0.0615
[IL] Epoch 65/100, Loss: 0.0596
[IL] Epoch 66/100, Loss: 0.0581
[IL] Epoch 67/100, Loss: 0.0625
[IL] Epoch 68/100, Loss: 0.0574
[IL] Epoch 69/100, Loss: 0.0555
[IL] Epoch 70/100, Loss: 0.0536
[IL] Epoch 71/100, Loss: 0.0606
[IL] Epoch 72/100, Loss: 0.0571
[IL] Epoch 73/100, Loss: 0.0584
[IL] Epoch 74/100, Loss: 0.0631
[IL] Epoch 75/100, Loss: 0.0599
[IL] Epoch 76/100, Loss: 0.0539
[IL] Epoch 77/100, Loss: 0.0563
[IL] Epoch 78/100, Loss: 0.0597
[IL] Epoch 79/100, Loss: 0.0594
[IL] Epoch 80/100, Loss: 0.0535
[IL] Epoch 81/100, Loss: 0.0573
[IL] Epoch 82/100, Loss: 0.0561
[IL] Epoch 83/100, Loss: 0.0572
[IL] Epoch 84/100, Loss: 0.0526
[IL] Epoch 85/100, Loss: 0.0527
[IL] Epoch 86/100, Loss: 0.0529
[IL] Epoch 87/100, Loss: 0.0588
[IL] Epoch 88/100, Loss: 0.0584
[IL] Epoch 89/100, Loss: 0.0575
[IL] Epoch 90/100, Loss: 0.0518
[IL] Epoch 91/100, Loss: 0.0563
[IL] Epoch 92/100, Loss: 0.0580
[IL] Epoch 93/100, Loss: 0.0559
[IL] Epoch 94/100, Loss: 0.0518
[IL] Epoch 95/100, Loss: 0.0512
[IL] Epoch 96/100, Loss: 0.0532
[IL] Epoch 97/100, Loss: 0.0530
[IL] Epoch 98/100, Loss: 0.0522
[IL] Epoch 99/100, Loss: 0.0576
test_mean_score: 0.15
[IL] Eval - Success Rate: 0.150
[Checkpoint] Saved to /nfs_global/S/yangrongzheng/RL100/3D-Diffusion-Policy/3D-Diffusion-Policy/checkpoints/offline_iter_0.ckpt

================================================================================
               OFFLINE RL ITERATION 2/5
================================================================================


[RL100Trainer] Line 6 — Training Transition Model T_θ (Iteration 1)

[TransitionModel] Encoding dataset for transition model training...
[TransitionModel] Dataset: 2830 samples, input_dim=260, target_dim=257
[TransitionModel] Epoch    0 | train=65544.23481 | val=23752.09258 | no-improve=0/5
[TransitionModel] Epoch   20 | train=9261.83811 | val=5436.60498 | no-improve=0/5
[TransitionModel] Epoch   40 | train=3781.38471 | val=3742.42129 | no-improve=0/5
[TransitionModel] Epoch   60 | train=2294.09045 | val=3349.53032 | no-improve=1/5
[TransitionModel] Epoch   80 | train=1274.03084 | val=2972.96133 | no-improve=0/5
[TransitionModel] Epoch  100 | train=914.91874 | val=2795.53667 | no-improve=0/5
[TransitionModel] Epoch  120 | train=672.76810 | val=2723.05542 | no-improve=2/5
[TransitionModel] Epoch  136 | train=514.59619 | val=2746.83130 | no-improve=5/5
[TransitionModel] Training complete. Elites=[5, 3, 4, 6, 2], val_loss=2608.78096

[RL100Trainer] Phase 2a: Training IQL Critics (Iteration 1)
[IQL] Epoch 0/500, V Loss: 12.0568, Q Loss: 93264.0540
[IQL] Epoch 1/500, V Loss: 7.1762, Q Loss: 95276.1637
[IQL] Epoch 2/500, V Loss: 2.8257, Q Loss: 95402.0020
[IQL] Epoch 3/500, V Loss: 5.0042, Q Loss: 99836.4010
[IQL] Epoch 4/500, V Loss: 7.7318, Q Loss: 89935.7178
[IQL] Epoch 5/500, V Loss: 10.6720, Q Loss: 90417.8132
[IQL] Epoch 6/500, V Loss: 13.7387, Q Loss: 94313.5658
[IQL] Epoch 7/500, V Loss: 16.9374, Q Loss: 94253.0299
[IQL] Epoch 8/500, V Loss: 20.3116, Q Loss: 98049.4323
[IQL] Epoch 9/500, V Loss: 23.7788, Q Loss: 91517.9590
[IQL] Epoch 10/500, V Loss: 27.3548, Q Loss: 84452.8721
[IQL] Epoch 11/500, V Loss: 30.9120, Q Loss: 94207.7155
[IQL] Epoch 12/500, V Loss: 34.5967, Q Loss: 82616.1511
[IQL] Epoch 13/500, V Loss: 36.0722, Q Loss: 87625.2357
[IQL] Epoch 14/500, V Loss: 37.8833, Q Loss: 88046.7666
[IQL] Epoch 15/500, V Loss: 40.7826, Q Loss: 89228.7767
[IQL] Epoch 16/500, V Loss: 44.1530, Q Loss: 93834.9798
[IQL] Epoch 17/500, V Loss: 47.6188, Q Loss: 92007.3522
[IQL] Epoch 18/500, V Loss: 50.9478, Q Loss: 82728.0947
[IQL] Epoch 19/500, V Loss: 51.1050, Q Loss: 89053.0495
[IQL] Epoch 20/500, V Loss: 51.6826, Q Loss: 84275.9072
[IQL] Epoch 21/500, V Loss: 52.5084, Q Loss: 90261.8783
[IQL] Epoch 22/500, V Loss: 54.1033, Q Loss: 105063.3158
[IQL] Epoch 23/500, V Loss: 53.0499, Q Loss: 89641.9954
[IQL] Epoch 24/500, V Loss: 57.9412, Q Loss: 86185.2116
[IQL] Epoch 25/500, V Loss: 60.7715, Q Loss: 88627.4990
[IQL] Epoch 26/500, V Loss: 86.7075, Q Loss: 84328.7562
[IQL] Epoch 27/500, V Loss: 93.6755, Q Loss: 79644.9746
[IQL] Epoch 28/500, V Loss: 129.2795, Q Loss: 80939.1846
[IQL] Epoch 29/500, V Loss: 124.2761, Q Loss: 79564.6315
[IQL] Epoch 30/500, V Loss: 122.6238, Q Loss: 84983.4801
[IQL] Epoch 31/500, V Loss: 125.9639, Q Loss: 86983.1146
[IQL] Epoch 32/500, V Loss: 133.1589, Q Loss: 80459.2552
[IQL] Epoch 33/500, V Loss: 112.9100, Q Loss: 88048.7168
[IQL] Epoch 34/500, V Loss: 97.3394, Q Loss: 89285.6624
[IQL] Epoch 35/500, V Loss: 87.4525, Q Loss: 87184.3177
[IQL] Epoch 36/500, V Loss: 94.9146, Q Loss: 84729.9303
[IQL] Epoch 37/500, V Loss: 92.8391, Q Loss: 84419.3268
[IQL] Epoch 38/500, V Loss: 92.0315, Q Loss: 79620.6003
[IQL] Epoch 39/500, V Loss: 93.3114, Q Loss: 87721.1790
[IQL] Epoch 40/500, V Loss: 89.0829, Q Loss: 79094.3154
[IQL] Epoch 41/500, V Loss: 104.9240, Q Loss: 79708.8376
[IQL] Epoch 42/500, V Loss: 109.6648, Q Loss: 84363.3171
[IQL] Epoch 43/500, V Loss: 100.9340, Q Loss: 77011.4119
[IQL] Epoch 44/500, V Loss: 124.3917, Q Loss: 85168.1523
[IQL] Epoch 45/500, V Loss: 106.2873, Q Loss: 80500.1624
[IQL] Epoch 46/500, V Loss: 106.0484, Q Loss: 78999.8747
[IQL] Epoch 47/500, V Loss: 132.0675, Q Loss: 87702.3477
[IQL] Epoch 48/500, V Loss: 103.7501, Q Loss: 79369.5342
[IQL] Epoch 49/500, V Loss: 109.4249, Q Loss: 81490.9362
[IQL] Epoch 50/500, V Loss: 117.3712, Q Loss: 77261.3014
[IQL] Epoch 51/500, V Loss: 147.8503, Q Loss: 81352.5221
[IQL] Epoch 52/500, V Loss: 116.9003, Q Loss: 86442.0553
[IQL] Epoch 53/500, V Loss: 121.5825, Q Loss: 75804.6236
[IQL] Epoch 54/500, V Loss: 131.8138, Q Loss: 77481.4744
[IQL] Epoch 55/500, V Loss: 142.0272, Q Loss: 77222.6753
[IQL] Epoch 56/500, V Loss: 141.3465, Q Loss: 80811.6771
[IQL] Epoch 57/500, V Loss: 150.4675, Q Loss: 92228.1413
[IQL] Epoch 58/500, V Loss: 158.4668, Q Loss: 82779.7288
[IQL] Epoch 59/500, V Loss: 145.9339, Q Loss: 82677.0879
[IQL] Epoch 60/500, V Loss: 155.6191, Q Loss: 80326.4759
[IQL] Epoch 61/500, V Loss: 154.7831, Q Loss: 79329.5479
[IQL] Epoch 62/500, V Loss: 150.2188, Q Loss: 75742.6624
[IQL] Epoch 63/500, V Loss: 173.6975, Q Loss: 77825.1712
[IQL] Epoch 64/500, V Loss: 169.8687, Q Loss: 89872.2438
[IQL] Epoch 65/500, V Loss: 144.7198, Q Loss: 75107.3319
[IQL] Epoch 66/500, V Loss: 161.9633, Q Loss: 73542.4013
[IQL] Epoch 67/500, V Loss: 180.5674, Q Loss: 82316.1374
[IQL] Epoch 68/500, V Loss: 154.3244, Q Loss: 81068.6585
[IQL] Epoch 69/500, V Loss: 156.5054, Q Loss: 82830.5579
[IQL] Epoch 70/500, V Loss: 168.1558, Q Loss: 78443.5785
[IQL] Epoch 71/500, V Loss: 172.3283, Q Loss: 79934.5609
[IQL] Epoch 72/500, V Loss: 173.1002, Q Loss: 78075.6061
[IQL] Epoch 73/500, V Loss: 198.8872, Q Loss: 82178.1045
[IQL] Epoch 74/500, V Loss: 193.8367, Q Loss: 79872.6950
[IQL] Epoch 75/500, V Loss: 192.6663, Q Loss: 88517.0072
[IQL] Epoch 76/500, V Loss: 182.4814, Q Loss: 74915.9733
[IQL] Epoch 77/500, V Loss: 214.5545, Q Loss: 71961.0403
[IQL] Epoch 78/500, V Loss: 213.6851, Q Loss: 90030.5358
[IQL] Epoch 79/500, V Loss: 195.3893, Q Loss: 71424.1390
[IQL] Epoch 80/500, V Loss: 239.8523, Q Loss: 83301.6849
[IQL] Epoch 81/500, V Loss: 219.8534, Q Loss: 74535.8766
[IQL] Epoch 82/500, V Loss: 233.6096, Q Loss: 73986.2048
[IQL] Epoch 83/500, V Loss: 220.8574, Q Loss: 77717.2871
[IQL] Epoch 84/500, V Loss: 231.2020, Q Loss: 73827.3600
[IQL] Epoch 85/500, V Loss: 244.7120, Q Loss: 87218.8529
[IQL] Epoch 86/500, V Loss: 237.9757, Q Loss: 76855.9967
[IQL] Epoch 87/500, V Loss: 242.5510, Q Loss: 71988.1045
[IQL] Epoch 88/500, V Loss: 240.6153, Q Loss: 72539.9707
[IQL] Epoch 89/500, V Loss: 278.6626, Q Loss: 76543.5068
[IQL] Epoch 90/500, V Loss: 265.5360, Q Loss: 69967.3641
[IQL] Epoch 91/500, V Loss: 260.1155, Q Loss: 72162.8910
[IQL] Epoch 92/500, V Loss: 270.6866, Q Loss: 72444.6481
[IQL] Epoch 93/500, V Loss: 268.0470, Q Loss: 68935.7092
[IQL] Epoch 94/500, V Loss: 291.1853, Q Loss: 75203.6947
[IQL] Epoch 95/500, V Loss: 280.5269, Q Loss: 73485.6702
[IQL] Epoch 96/500, V Loss: 319.0832, Q Loss: 68924.0744
[IQL] Epoch 97/500, V Loss: 296.6383, Q Loss: 76250.4062
[IQL] Epoch 98/500, V Loss: 306.3955, Q Loss: 71626.0944
[IQL] Epoch 99/500, V Loss: 321.4961, Q Loss: 72004.4766
[IQL] Epoch 100/500, V Loss: 330.8741, Q Loss: 71783.2998
[IQL] Epoch 101/500, V Loss: 318.9121, Q Loss: 77958.5918
[IQL] Epoch 102/500, V Loss: 351.4598, Q Loss: 81400.4388
[IQL] Epoch 103/500, V Loss: 327.5420, Q Loss: 68747.1702
[IQL] Epoch 104/500, V Loss: 378.3176, Q Loss: 75533.8301
[IQL] Epoch 105/500, V Loss: 374.6761, Q Loss: 71325.8919
[IQL] Epoch 106/500, V Loss: 340.0422, Q Loss: 72860.6380
[IQL] Epoch 107/500, V Loss: 356.0355, Q Loss: 76352.7689
[IQL] Epoch 108/500, V Loss: 362.9315, Q Loss: 75537.3867
[IQL] Epoch 109/500, V Loss: 346.0777, Q Loss: 70165.6029
[IQL] Epoch 110/500, V Loss: 365.0563, Q Loss: 68587.2301
[IQL] Epoch 111/500, V Loss: 361.8959, Q Loss: 67188.9382
[IQL] Epoch 112/500, V Loss: 405.8500, Q Loss: 70146.1393
[IQL] Epoch 113/500, V Loss: 387.5919, Q Loss: 65146.2947
[IQL] Epoch 114/500, V Loss: 390.4389, Q Loss: 68823.9596
[IQL] Epoch 115/500, V Loss: 388.9128, Q Loss: 67521.9359
[IQL] Epoch 116/500, V Loss: 376.1163, Q Loss: 71597.8096
[IQL] Epoch 117/500, V Loss: 399.5409, Q Loss: 67093.3044
[IQL] Epoch 118/500, V Loss: 390.7924, Q Loss: 70483.9128
[IQL] Epoch 119/500, V Loss: 397.2093, Q Loss: 66488.6956
[IQL] Epoch 120/500, V Loss: 420.8129, Q Loss: 67537.7018
[IQL] Epoch 121/500, V Loss: 459.4660, Q Loss: 76920.9867
[IQL] Epoch 122/500, V Loss: 414.2145, Q Loss: 72799.4333
[IQL] Epoch 123/500, V Loss: 444.7504, Q Loss: 74771.8854
[IQL] Epoch 124/500, V Loss: 474.9581, Q Loss: 65351.3976
[IQL] Epoch 125/500, V Loss: 416.1139, Q Loss: 63184.2372
[IQL] Epoch 126/500, V Loss: 477.0095, Q Loss: 64284.6723
[IQL] Epoch 127/500, V Loss: 437.6672, Q Loss: 67071.0166
[IQL] Epoch 128/500, V Loss: 479.9485, Q Loss: 66248.7249
[IQL] Epoch 129/500, V Loss: 452.9838, Q Loss: 66129.6003
[IQL] Epoch 130/500, V Loss: 476.4403, Q Loss: 63390.0771
[IQL] Epoch 131/500, V Loss: 512.6485, Q Loss: 69202.4629
[IQL] Epoch 132/500, V Loss: 561.6195, Q Loss: 73325.1100
[IQL] Epoch 133/500, V Loss: 501.5957, Q Loss: 65033.5809
[IQL] Epoch 134/500, V Loss: 499.8052, Q Loss: 66346.8167
[IQL] Epoch 135/500, V Loss: 503.8870, Q Loss: 65381.1484
[IQL] Epoch 136/500, V Loss: 487.7129, Q Loss: 63625.2627
[IQL] Epoch 137/500, V Loss: 477.9027, Q Loss: 65088.8490
[IQL] Epoch 138/500, V Loss: 518.4066, Q Loss: 79060.3050
[IQL] Epoch 139/500, V Loss: 510.8217, Q Loss: 71587.8932
[IQL] Epoch 140/500, V Loss: 497.4022, Q Loss: 64128.5340
[IQL] Epoch 141/500, V Loss: 553.6494, Q Loss: 68158.9430
[IQL] Epoch 142/500, V Loss: 497.5056, Q Loss: 64491.1390
[IQL] Epoch 143/500, V Loss: 520.2093, Q Loss: 65010.2438
[IQL] Epoch 144/500, V Loss: 552.3808, Q Loss: 67909.1667
[IQL] Epoch 145/500, V Loss: 529.0938, Q Loss: 64226.6462
[IQL] Epoch 146/500, V Loss: 565.1727, Q Loss: 75541.3467
[IQL] Epoch 147/500, V Loss: 528.5337, Q Loss: 65298.2210
[IQL] Epoch 148/500, V Loss: 632.1694, Q Loss: 68927.2682
[IQL] Epoch 149/500, V Loss: 618.1454, Q Loss: 68995.2591
[IQL] Epoch 150/500, V Loss: 602.0155, Q Loss: 61316.0835
[IQL] Epoch 151/500, V Loss: 581.7534, Q Loss: 61224.0160
[IQL] Epoch 152/500, V Loss: 583.8482, Q Loss: 62298.2454
[IQL] Epoch 153/500, V Loss: 564.9773, Q Loss: 63036.0348
[IQL] Epoch 154/500, V Loss: 612.5962, Q Loss: 66372.2223
[IQL] Epoch 155/500, V Loss: 624.5848, Q Loss: 66010.7881
[IQL] Epoch 156/500, V Loss: 683.0743, Q Loss: 71697.7207
[IQL] Epoch 157/500, V Loss: 604.6656, Q Loss: 62101.1061
[IQL] Epoch 158/500, V Loss: 622.2904, Q Loss: 59717.8820
[IQL] Epoch 159/500, V Loss: 683.0123, Q Loss: 66904.9639
[IQL] Epoch 160/500, V Loss: 599.4007, Q Loss: 62508.5098
[IQL] Epoch 161/500, V Loss: 652.1671, Q Loss: 69285.0811
[IQL] Epoch 162/500, V Loss: 666.0598, Q Loss: 67454.5365
[IQL] Epoch 163/500, V Loss: 649.7763, Q Loss: 58513.4757
[IQL] Epoch 164/500, V Loss: 705.1468, Q Loss: 63474.7480
[IQL] Epoch 165/500, V Loss: 701.3179, Q Loss: 61954.3232
[IQL] Epoch 166/500, V Loss: 753.9819, Q Loss: 58871.0015
[IQL] Epoch 167/500, V Loss: 676.2752, Q Loss: 61206.8776
[IQL] Epoch 168/500, V Loss: 700.7557, Q Loss: 61809.6019
[IQL] Epoch 169/500, V Loss: 715.6009, Q Loss: 60914.7458
[IQL] Epoch 170/500, V Loss: 746.8637, Q Loss: 57421.1632
[IQL] Epoch 171/500, V Loss: 745.7251, Q Loss: 65239.3206
[IQL] Epoch 172/500, V Loss: 774.1656, Q Loss: 63760.8988
[IQL] Epoch 173/500, V Loss: 767.6779, Q Loss: 59391.2972
[IQL] Epoch 174/500, V Loss: 825.3236, Q Loss: 58508.9580
[IQL] Epoch 175/500, V Loss: 764.1920, Q Loss: 60189.3691
[IQL] Epoch 176/500, V Loss: 857.6827, Q Loss: 76115.0085
[IQL] Epoch 177/500, V Loss: 806.1775, Q Loss: 63532.5059
[IQL] Epoch 178/500, V Loss: 839.7396, Q Loss: 60940.3154
[IQL] Epoch 179/500, V Loss: 759.8539, Q Loss: 60858.4967
[IQL] Epoch 180/500, V Loss: 783.8387, Q Loss: 63604.6322
[IQL] Epoch 181/500, V Loss: 805.3850, Q Loss: 58865.1589
[IQL] Epoch 182/500, V Loss: 824.8220, Q Loss: 65784.8942
[IQL] Epoch 183/500, V Loss: 778.0935, Q Loss: 60964.8590
[IQL] Epoch 184/500, V Loss: 736.8901, Q Loss: 56169.1099
[IQL] Epoch 185/500, V Loss: 822.8629, Q Loss: 55668.6911
[IQL] Epoch 186/500, V Loss: 836.5912, Q Loss: 62302.3226
[IQL] Epoch 187/500, V Loss: 791.1873, Q Loss: 55152.6613
[IQL] Epoch 188/500, V Loss: 845.7891, Q Loss: 56295.2694
[IQL] Epoch 189/500, V Loss: 879.9095, Q Loss: 64994.9124
[IQL] Epoch 190/500, V Loss: 887.2990, Q Loss: 61350.6305
[IQL] Epoch 191/500, V Loss: 812.5295, Q Loss: 59195.9769
[IQL] Epoch 192/500, V Loss: 738.3815, Q Loss: 58464.7855
[IQL] Epoch 193/500, V Loss: 868.1340, Q Loss: 56933.1367
[IQL] Epoch 194/500, V Loss: 793.5032, Q Loss: 54724.6797
[IQL] Epoch 195/500, V Loss: 764.1573, Q Loss: 54850.5275
[IQL] Epoch 196/500, V Loss: 824.0400, Q Loss: 58300.4782
[IQL] Epoch 197/500, V Loss: 842.4716, Q Loss: 60184.8854
[IQL] Epoch 198/500, V Loss: 787.8803, Q Loss: 57326.7080
[IQL] Epoch 199/500, V Loss: 824.5469, Q Loss: 63143.9619
[IQL] Epoch 200/500, V Loss: 830.7898, Q Loss: 55225.2689
[IQL] Epoch 201/500, V Loss: 897.8543, Q Loss: 57241.0439
[IQL] Epoch 202/500, V Loss: 823.9383, Q Loss: 58149.0726
[IQL] Epoch 203/500, V Loss: 875.5054, Q Loss: 55173.8895
[IQL] Epoch 204/500, V Loss: 890.3369, Q Loss: 57236.3372
[IQL] Epoch 205/500, V Loss: 891.5814, Q Loss: 58610.9333
[IQL] Epoch 206/500, V Loss: 894.6420, Q Loss: 55214.2357
[IQL] Epoch 207/500, V Loss: 890.1675, Q Loss: 56740.4704
[IQL] Epoch 208/500, V Loss: 935.9135, Q Loss: 65183.9342
[IQL] Epoch 209/500, V Loss: 894.6057, Q Loss: 52176.6083
[IQL] Epoch 210/500, V Loss: 909.5316, Q Loss: 55044.3076
[IQL] Epoch 211/500, V Loss: 940.0981, Q Loss: 60708.3262
[IQL] Epoch 212/500, V Loss: 953.3320, Q Loss: 54250.0083
[IQL] Epoch 213/500, V Loss: 889.1096, Q Loss: 59110.0817
[IQL] Epoch 214/500, V Loss: 895.7071, Q Loss: 52901.5270
[IQL] Epoch 215/500, V Loss: 950.2354, Q Loss: 59930.6562
[IQL] Epoch 216/500, V Loss: 1058.9887, Q Loss: 63953.3903
[IQL] Epoch 217/500, V Loss: 916.3006, Q Loss: 57292.9775
[IQL] Epoch 218/500, V Loss: 999.0444, Q Loss: 51909.0535
[IQL] Epoch 219/500, V Loss: 915.8559, Q Loss: 54677.2246
[IQL] Epoch 220/500, V Loss: 933.7619, Q Loss: 62897.5088
[IQL] Epoch 221/500, V Loss: 1006.8222, Q Loss: 52740.0667
[IQL] Epoch 222/500, V Loss: 940.6295, Q Loss: 51626.8416
[IQL] Epoch 223/500, V Loss: 994.1157, Q Loss: 55675.5833
[IQL] Epoch 224/500, V Loss: 1021.0772, Q Loss: 51815.8164
[IQL] Epoch 225/500, V Loss: 949.2518, Q Loss: 58495.3617
[IQL] Epoch 226/500, V Loss: 938.5777, Q Loss: 52405.0316
[IQL] Epoch 227/500, V Loss: 978.5117, Q Loss: 55655.3125
[IQL] Epoch 228/500, V Loss: 899.4239, Q Loss: 53642.0514
[IQL] Epoch 229/500, V Loss: 1003.2444, Q Loss: 60079.0464
[IQL] Epoch 230/500, V Loss: 967.3952, Q Loss: 52083.0117
[IQL] Epoch 231/500, V Loss: 899.7890, Q Loss: 55877.0827
[IQL] Epoch 232/500, V Loss: 960.6739, Q Loss: 57950.6940
[IQL] Epoch 233/500, V Loss: 893.7934, Q Loss: 51695.7498
[IQL] Epoch 234/500, V Loss: 917.9002, Q Loss: 53792.9017
[IQL] Epoch 235/500, V Loss: 948.6247, Q Loss: 56123.9857
[IQL] Epoch 236/500, V Loss: 881.3605, Q Loss: 53695.5944
[IQL] Epoch 237/500, V Loss: 868.8762, Q Loss: 51801.8154
[IQL] Epoch 238/500, V Loss: 939.4306, Q Loss: 51599.8773
[IQL] Epoch 239/500, V Loss: 883.9154, Q Loss: 52038.7477
[IQL] Epoch 240/500, V Loss: 836.3814, Q Loss: 51000.0286
[IQL] Epoch 241/500, V Loss: 891.3493, Q Loss: 49495.6924
[IQL] Epoch 242/500, V Loss: 1011.8654, Q Loss: 50004.8708
[IQL] Epoch 243/500, V Loss: 903.4678, Q Loss: 55106.8835
[IQL] Epoch 244/500, V Loss: 871.8494, Q Loss: 55204.3294
[IQL] Epoch 245/500, V Loss: 874.0676, Q Loss: 50710.9368
[IQL] Epoch 246/500, V Loss: 848.2498, Q Loss: 53887.2373
[IQL] Epoch 247/500, V Loss: 878.1744, Q Loss: 54400.3962
[IQL] Epoch 248/500, V Loss: 905.8735, Q Loss: 56893.5762
[IQL] Epoch 249/500, V Loss: 834.3765, Q Loss: 52894.3392
[IQL] Epoch 250/500, V Loss: 916.3656, Q Loss: 49430.2895
[IQL] Epoch 251/500, V Loss: 880.2883, Q Loss: 52616.1452
[IQL] Epoch 252/500, V Loss: 971.1402, Q Loss: 50332.1260
[IQL] Epoch 253/500, V Loss: 999.1913, Q Loss: 53720.8278
[IQL] Epoch 254/500, V Loss: 994.1885, Q Loss: 51375.2891
[IQL] Epoch 255/500, V Loss: 1015.5596, Q Loss: 58928.9609
[IQL] Epoch 256/500, V Loss: 935.0460, Q Loss: 55698.3841
[IQL] Epoch 257/500, V Loss: 803.3083, Q Loss: 48432.0903
[IQL] Epoch 258/500, V Loss: 784.7021, Q Loss: 49120.3421
[IQL] Epoch 259/500, V Loss: 1082.8723, Q Loss: 55555.4650
[IQL] Epoch 260/500, V Loss: 950.9039, Q Loss: 49329.8403
[IQL] Epoch 261/500, V Loss: 1102.2276, Q Loss: 58232.4336
[IQL] Epoch 262/500, V Loss: 927.5771, Q Loss: 56011.1354
[IQL] Epoch 263/500, V Loss: 1011.9478, Q Loss: 51583.7559
[IQL] Epoch 264/500, V Loss: 833.0453, Q Loss: 48631.1509
[IQL] Epoch 265/500, V Loss: 926.7197, Q Loss: 50379.9328
[IQL] Epoch 266/500, V Loss: 843.3276, Q Loss: 50916.6318
[IQL] Epoch 267/500, V Loss: 976.9210, Q Loss: 57737.5902
[IQL] Epoch 268/500, V Loss: 993.7762, Q Loss: 49297.7900
[IQL] Epoch 269/500, V Loss: 1008.2937, Q Loss: 50662.4590
[IQL] Epoch 270/500, V Loss: 887.5249, Q Loss: 48608.1792
[IQL] Epoch 271/500, V Loss: 1112.4262, Q Loss: 58631.1377
[IQL] Epoch 272/500, V Loss: 971.4567, Q Loss: 48860.5959
[IQL] Epoch 273/500, V Loss: 900.7199, Q Loss: 51184.3675
[IQL] Epoch 274/500, V Loss: 921.0749, Q Loss: 54455.7728
[IQL] Epoch 275/500, V Loss: 923.8638, Q Loss: 48304.2209
[IQL] Epoch 276/500, V Loss: 972.8434, Q Loss: 49950.3890
[IQL] Epoch 277/500, V Loss: 933.8285, Q Loss: 54923.4137
[IQL] Epoch 278/500, V Loss: 968.9253, Q Loss: 50592.8421
[IQL] Epoch 279/500, V Loss: 1056.6996, Q Loss: 51007.9580
[IQL] Epoch 280/500, V Loss: 951.0046, Q Loss: 50805.0824
[IQL] Epoch 281/500, V Loss: 890.7442, Q Loss: 48633.6826
[IQL] Epoch 282/500, V Loss: 939.3955, Q Loss: 52424.5615
[IQL] Epoch 283/500, V Loss: 842.2579, Q Loss: 47801.2930
[IQL] Epoch 284/500, V Loss: 883.9489, Q Loss: 46921.1560
[IQL] Epoch 285/500, V Loss: 861.2662, Q Loss: 48005.2469
[IQL] Epoch 286/500, V Loss: 911.6840, Q Loss: 51121.4619
[IQL] Epoch 287/500, V Loss: 970.5526, Q Loss: 46712.1823
[IQL] Epoch 288/500, V Loss: 895.1127, Q Loss: 48328.1331
[IQL] Epoch 289/500, V Loss: 991.3531, Q Loss: 55867.7832
[IQL] Epoch 290/500, V Loss: 929.1669, Q Loss: 52865.6986
[IQL] Epoch 291/500, V Loss: 947.5272, Q Loss: 49499.7337
[IQL] Epoch 292/500, V Loss: 1074.5601, Q Loss: 59141.0081
[IQL] Epoch 293/500, V Loss: 1068.9770, Q Loss: 55631.1875
[IQL] Epoch 294/500, V Loss: 890.1281, Q Loss: 48225.5859
[IQL] Epoch 295/500, V Loss: 863.2115, Q Loss: 60271.7246
[IQL] Epoch 296/500, V Loss: 952.6893, Q Loss: 46223.1764
[IQL] Epoch 297/500, V Loss: 927.5291, Q Loss: 47236.9609
[IQL] Epoch 298/500, V Loss: 1187.8897, Q Loss: 50134.8197
[IQL] Epoch 299/500, V Loss: 962.2980, Q Loss: 46112.3669
[IQL] Epoch 300/500, V Loss: 1074.9285, Q Loss: 51502.1686
[IQL] Epoch 301/500, V Loss: 954.8248, Q Loss: 52778.7511
[IQL] Epoch 302/500, V Loss: 896.1838, Q Loss: 50788.2669
[IQL] Epoch 303/500, V Loss: 855.2939, Q Loss: 48499.9359
[IQL] Epoch 304/500, V Loss: 1015.4605, Q Loss: 48779.2025
[IQL] Epoch 305/500, V Loss: 1017.4437, Q Loss: 52919.5381
[IQL] Epoch 306/500, V Loss: 1083.4085, Q Loss: 52351.2402
[IQL] Epoch 307/500, V Loss: 939.9170, Q Loss: 46492.0559
[IQL] Epoch 308/500, V Loss: 878.3411, Q Loss: 46941.9969
[IQL] Epoch 309/500, V Loss: 952.0838, Q Loss: 47266.7126
[IQL] Epoch 310/500, V Loss: 948.2934, Q Loss: 47867.0475
[IQL] Epoch 311/500, V Loss: 946.0880, Q Loss: 45718.2451
[IQL] Epoch 312/500, V Loss: 1011.9241, Q Loss: 45375.0019
[IQL] Epoch 313/500, V Loss: 1059.1729, Q Loss: 45714.0915
[IQL] Epoch 314/500, V Loss: 935.5360, Q Loss: 48077.7715
[IQL] Epoch 315/500, V Loss: 1001.5966, Q Loss: 54179.1878
[IQL] Epoch 316/500, V Loss: 988.4339, Q Loss: 56005.0879
[IQL] Epoch 317/500, V Loss: 925.3910, Q Loss: 45709.1328
[IQL] Epoch 318/500, V Loss: 928.0812, Q Loss: 46128.8838
[IQL] Epoch 319/500, V Loss: 1155.0929, Q Loss: 47955.9176
[IQL] Epoch 320/500, V Loss: 941.4390, Q Loss: 45400.3055
[IQL] Epoch 321/500, V Loss: 888.9389, Q Loss: 44465.6673
[IQL] Epoch 322/500, V Loss: 954.1565, Q Loss: 45196.0623
[IQL] Epoch 323/500, V Loss: 1005.8897, Q Loss: 47647.1004
[IQL] Epoch 324/500, V Loss: 931.4432, Q Loss: 47194.1527
[IQL] Epoch 325/500, V Loss: 976.1216, Q Loss: 49120.3874
[IQL] Epoch 326/500, V Loss: 944.2683, Q Loss: 50078.2407
[IQL] Epoch 327/500, V Loss: 915.9857, Q Loss: 45316.1211
[IQL] Epoch 328/500, V Loss: 999.0354, Q Loss: 47385.9727
[IQL] Epoch 329/500, V Loss: 934.9368, Q Loss: 50924.7926
[IQL] Epoch 330/500, V Loss: 876.4492, Q Loss: 45866.0290
[IQL] Epoch 331/500, V Loss: 1227.7239, Q Loss: 45189.0549
[IQL] Epoch 332/500, V Loss: 1087.2041, Q Loss: 50700.0365
[IQL] Epoch 333/500, V Loss: 860.5216, Q Loss: 45801.7699
[IQL] Epoch 334/500, V Loss: 953.0660, Q Loss: 47996.5358
[IQL] Epoch 335/500, V Loss: 971.6787, Q Loss: 45905.4486
[IQL] Epoch 336/500, V Loss: 1184.3498, Q Loss: 48745.6702
[IQL] Epoch 337/500, V Loss: 864.8297, Q Loss: 44322.6923
[IQL] Epoch 338/500, V Loss: 918.7591, Q Loss: 49952.8838
[IQL] Epoch 339/500, V Loss: 1446.6043, Q Loss: 45408.3035
[IQL] Epoch 340/500, V Loss: 918.5627, Q Loss: 43989.6632
[IQL] Epoch 341/500, V Loss: 916.6185, Q Loss: 47732.8577
[IQL] Epoch 342/500, V Loss: 983.1015, Q Loss: 47185.6672
[IQL] Epoch 343/500, V Loss: 988.0050, Q Loss: 44105.7481
[IQL] Epoch 344/500, V Loss: 1172.2495, Q Loss: 51282.1807
[IQL] Epoch 345/500, V Loss: 934.9573, Q Loss: 48112.7308
[IQL] Epoch 346/500, V Loss: 909.8952, Q Loss: 44496.6939
[IQL] Epoch 347/500, V Loss: 939.1622, Q Loss: 44961.2845
[IQL] Epoch 348/500, V Loss: 880.2265, Q Loss: 48195.6243
[IQL] Epoch 349/500, V Loss: 1046.3191, Q Loss: 46870.6058
[IQL] Epoch 350/500, V Loss: 950.2387, Q Loss: 47764.8698
[IQL] Epoch 351/500, V Loss: 850.0628, Q Loss: 48222.1204
[IQL] Epoch 352/500, V Loss: 1047.6709, Q Loss: 48714.0921
[IQL] Epoch 353/500, V Loss: 808.8107, Q Loss: 46965.9759
[IQL] Epoch 354/500, V Loss: 909.0243, Q Loss: 46647.1696
[IQL] Epoch 355/500, V Loss: 915.7922, Q Loss: 50490.5417
[IQL] Epoch 356/500, V Loss: 856.7185, Q Loss: 44208.1017
[IQL] Epoch 357/500, V Loss: 807.5123, Q Loss: 45375.4312
[IQL] Epoch 358/500, V Loss: 983.9324, Q Loss: 48573.1748
[IQL] Epoch 359/500, V Loss: 930.2636, Q Loss: 47360.7738
[IQL] Epoch 360/500, V Loss: 1018.3011, Q Loss: 54225.0700
[IQL] Epoch 361/500, V Loss: 956.8396, Q Loss: 45243.7516
[IQL] Epoch 362/500, V Loss: 887.0786, Q Loss: 51238.2386
[IQL] Epoch 363/500, V Loss: 883.5097, Q Loss: 46657.3262
[IQL] Epoch 364/500, V Loss: 991.5943, Q Loss: 47641.4639
[IQL] Epoch 365/500, V Loss: 934.2106, Q Loss: 47919.0845
[IQL] Epoch 366/500, V Loss: 976.9339, Q Loss: 45919.7524
[IQL] Epoch 367/500, V Loss: 938.6586, Q Loss: 47887.7979
[IQL] Epoch 368/500, V Loss: 1113.3706, Q Loss: 46001.8415
[IQL] Epoch 369/500, V Loss: 996.7498, Q Loss: 43812.2694
[IQL] Epoch 370/500, V Loss: 1025.5217, Q Loss: 47999.4227
[IQL] Epoch 371/500, V Loss: 1243.2827, Q Loss: 53105.0882
[IQL] Epoch 372/500, V Loss: 1235.4607, Q Loss: 45791.1198
[IQL] Epoch 373/500, V Loss: 1493.0619, Q Loss: 58559.4167
[IQL] Epoch 374/500, V Loss: 1028.3529, Q Loss: 46180.6229
[IQL] Epoch 375/500, V Loss: 920.6569, Q Loss: 45134.8729
[IQL] Epoch 376/500, V Loss: 932.5255, Q Loss: 55938.7764
[IQL] Epoch 377/500, V Loss: 1081.4192, Q Loss: 45504.2848
[IQL] Epoch 378/500, V Loss: 991.1683, Q Loss: 47803.5296
[IQL] Epoch 379/500, V Loss: 988.4741, Q Loss: 43696.2250
[IQL] Epoch 380/500, V Loss: 975.5874, Q Loss: 44011.4061
[IQL] Epoch 381/500, V Loss: 1156.7172, Q Loss: 48378.2064
[IQL] Epoch 382/500, V Loss: 987.4608, Q Loss: 55800.1634
[IQL] Epoch 383/500, V Loss: 1116.6196, Q Loss: 51101.0433
[IQL] Epoch 384/500, V Loss: 1055.7336, Q Loss: 50867.7878
[IQL] Epoch 385/500, V Loss: 919.5894, Q Loss: 46090.9220
[IQL] Epoch 386/500, V Loss: 1212.9744, Q Loss: 47074.2194
[IQL] Epoch 387/500, V Loss: 1001.9735, Q Loss: 47034.4113
[IQL] Epoch 388/500, V Loss: 1016.5422, Q Loss: 49323.3612
[IQL] Epoch 389/500, V Loss: 1106.8588, Q Loss: 48205.8620
[IQL] Epoch 390/500, V Loss: 1251.8594, Q Loss: 43969.3647
[IQL] Epoch 391/500, V Loss: 1118.3806, Q Loss: 44486.7170
[IQL] Epoch 392/500, V Loss: 836.7398, Q Loss: 42990.6289
[IQL] Epoch 393/500, V Loss: 1083.5172, Q Loss: 46613.0954
[IQL] Epoch 394/500, V Loss: 1027.9727, Q Loss: 53010.9811
[IQL] Epoch 395/500, V Loss: 993.6448, Q Loss: 45281.5029
[IQL] Epoch 396/500, V Loss: 896.3324, Q Loss: 44614.5472
[IQL] Epoch 397/500, V Loss: 1024.8973, Q Loss: 51972.7298
[IQL] Epoch 398/500, V Loss: 1088.4975, Q Loss: 43649.0470
[IQL] Epoch 399/500, V Loss: 953.4432, Q Loss: 43733.6702
[IQL] Epoch 400/500, V Loss: 1339.8540, Q Loss: 43657.6079
[IQL] Epoch 401/500, V Loss: 1074.8575, Q Loss: 45190.4450
[IQL] Epoch 402/500, V Loss: 1033.2685, Q Loss: 46516.6624
[IQL] Epoch 403/500, V Loss: 1234.4676, Q Loss: 46671.8275
[IQL] Epoch 404/500, V Loss: 962.3437, Q Loss: 48876.1257
[IQL] Epoch 405/500, V Loss: 1030.2986, Q Loss: 44737.9390
[IQL] Epoch 406/500, V Loss: 990.8973, Q Loss: 44319.6989
[IQL] Epoch 407/500, V Loss: 1087.4644, Q Loss: 49587.8255
[IQL] Epoch 408/500, V Loss: 1257.9957, Q Loss: 43445.8357
[IQL] Epoch 409/500, V Loss: 1326.1730, Q Loss: 43365.3078
[IQL] Epoch 410/500, V Loss: 1202.7762, Q Loss: 43814.0080
[IQL] Epoch 411/500, V Loss: 984.6726, Q Loss: 48089.3229
[IQL] Epoch 412/500, V Loss: 1059.3899, Q Loss: 48034.7507
[IQL] Epoch 413/500, V Loss: 1242.7464, Q Loss: 49295.5187
[IQL] Epoch 414/500, V Loss: 1100.1565, Q Loss: 43042.6204
[IQL] Epoch 415/500, V Loss: 1313.0607, Q Loss: 44311.6777
[IQL] Epoch 416/500, V Loss: 1295.2824, Q Loss: 43692.1580
[IQL] Epoch 417/500, V Loss: 1106.9592, Q Loss: 51875.9854
[IQL] Epoch 418/500, V Loss: 1126.1071, Q Loss: 45021.6885
[IQL] Epoch 419/500, V Loss: 946.8932, Q Loss: 43630.8257
[IQL] Epoch 420/500, V Loss: 1056.7661, Q Loss: 45771.7025
[IQL] Epoch 421/500, V Loss: 1302.1671, Q Loss: 45850.5199
[IQL] Epoch 422/500, V Loss: 1378.2180, Q Loss: 46198.8537
[IQL] Epoch 423/500, V Loss: 1086.8554, Q Loss: 43796.2845
[IQL] Epoch 424/500, V Loss: 987.3897, Q Loss: 43080.2263
[IQL] Epoch 425/500, V Loss: 974.1131, Q Loss: 43813.7832
[IQL] Epoch 426/500, V Loss: 998.0552, Q Loss: 46100.0758
[IQL] Epoch 427/500, V Loss: 1142.9848, Q Loss: 48364.4163
[IQL] Epoch 428/500, V Loss: 1101.9418, Q Loss: 47002.8167
[IQL] Epoch 429/500, V Loss: 1073.9916, Q Loss: 43153.5178
[IQL] Epoch 430/500, V Loss: 1098.6652, Q Loss: 51425.8063
[IQL] Epoch 431/500, V Loss: 1011.0199, Q Loss: 45678.2448
[IQL] Epoch 432/500, V Loss: 1135.0824, Q Loss: 47695.7456
[IQL] Epoch 433/500, V Loss: 1502.4508, Q Loss: 44207.9588
[IQL] Epoch 434/500, V Loss: 1379.4192, Q Loss: 46180.1380
[IQL] Epoch 435/500, V Loss: 1203.8325, Q Loss: 54583.3021
[IQL] Epoch 436/500, V Loss: 950.2960, Q Loss: 43009.2500
[IQL] Epoch 437/500, V Loss: 1274.2512, Q Loss: 50176.7119
[IQL] Epoch 438/500, V Loss: 1138.0083, Q Loss: 47956.1302
[IQL] Epoch 439/500, V Loss: 1250.3444, Q Loss: 42705.3470
[IQL] Epoch 440/500, V Loss: 1306.6085, Q Loss: 47623.4141
[IQL] Epoch 441/500, V Loss: 1281.0495, Q Loss: 43647.3030
[IQL] Epoch 442/500, V Loss: 1440.2387, Q Loss: 42787.3318
[IQL] Epoch 443/500, V Loss: 1107.7698, Q Loss: 52084.7054
[IQL] Epoch 444/500, V Loss: 1177.3428, Q Loss: 42953.4892
[IQL] Epoch 445/500, V Loss: 1048.5516, Q Loss: 44831.3219
[IQL] Epoch 446/500, V Loss: 1208.4397, Q Loss: 45269.8854
[IQL] Epoch 447/500, V Loss: 1138.8862, Q Loss: 46303.7549
[IQL] Epoch 448/500, V Loss: 1319.7287, Q Loss: 44715.1532
[IQL] Epoch 449/500, V Loss: 1157.8009, Q Loss: 46172.6344
[IQL] Epoch 450/500, V Loss: 1041.5136, Q Loss: 46129.4189
[IQL] Epoch 451/500, V Loss: 1885.5696, Q Loss: 52643.2087
[IQL] Epoch 452/500, V Loss: 1066.5934, Q Loss: 43182.0931
[IQL] Epoch 453/500, V Loss: 1113.2309, Q Loss: 45646.0482
[IQL] Epoch 454/500, V Loss: 1219.3392, Q Loss: 46126.2038
[IQL] Epoch 455/500, V Loss: 1087.7917, Q Loss: 45451.7835
[IQL] Epoch 456/500, V Loss: 1119.6063, Q Loss: 50926.0327
[IQL] Epoch 457/500, V Loss: 3332.4216, Q Loss: 44523.5680
[IQL] Epoch 458/500, V Loss: 1075.9019, Q Loss: 47292.6702
[IQL] Epoch 459/500, V Loss: 1684.5279, Q Loss: 54560.9648
[IQL] Epoch 460/500, V Loss: 1030.2049, Q Loss: 46453.9891
[IQL] Epoch 461/500, V Loss: 1186.4881, Q Loss: 49813.6374
[IQL] Epoch 462/500, V Loss: 1668.1939, Q Loss: 44556.8708
[IQL] Epoch 463/500, V Loss: 1280.1689, Q Loss: 48267.4020
[IQL] Epoch 464/500, V Loss: 1535.1307, Q Loss: 43536.7135
[IQL] Epoch 465/500, V Loss: 1191.6178, Q Loss: 44435.4170
[IQL] Epoch 466/500, V Loss: 1669.2984, Q Loss: 47960.4557
[IQL] Epoch 467/500, V Loss: 1361.4863, Q Loss: 48939.4131
[IQL] Epoch 468/500, V Loss: 1241.4536, Q Loss: 46692.0872
[IQL] Epoch 469/500, V Loss: 1205.9469, Q Loss: 46205.4199
[IQL] Epoch 470/500, V Loss: 1211.0548, Q Loss: 49850.0967
[IQL] Epoch 471/500, V Loss: 1571.9474, Q Loss: 42360.3892
[IQL] Epoch 472/500, V Loss: 1459.5458, Q Loss: 43594.0871
[IQL] Epoch 473/500, V Loss: 1267.4568, Q Loss: 41942.6285
[IQL] Epoch 474/500, V Loss: 1201.1760, Q Loss: 49231.8900
[IQL] Epoch 475/500, V Loss: 1238.2861, Q Loss: 42470.5280
[IQL] Epoch 476/500, V Loss: 1158.1597, Q Loss: 44234.9938
[IQL] Epoch 477/500, V Loss: 1281.4083, Q Loss: 42824.9518
[IQL] Epoch 478/500, V Loss: 1206.1023, Q Loss: 49068.4012
[IQL] Epoch 479/500, V Loss: 1358.3347, Q Loss: 42147.9023
[IQL] Epoch 480/500, V Loss: 1325.2034, Q Loss: 43497.3167
[IQL] Epoch 481/500, V Loss: 1367.8779, Q Loss: 42314.5286
[IQL] Epoch 482/500, V Loss: 1506.1162, Q Loss: 45155.5000
[IQL] Epoch 483/500, V Loss: 1198.2963, Q Loss: 47850.4821
[IQL] Epoch 484/500, V Loss: 1647.8600, Q Loss: 40692.7162
[IQL] Epoch 485/500, V Loss: 1416.5311, Q Loss: 45577.6149
[IQL] Epoch 486/500, V Loss: 1267.6461, Q Loss: 42039.0215
[IQL] Epoch 487/500, V Loss: 1606.8764, Q Loss: 42145.7404
[IQL] Epoch 488/500, V Loss: 1523.4873, Q Loss: 40757.6549
[IQL] Epoch 489/500, V Loss: 1401.1354, Q Loss: 43744.1003
[IQL] Epoch 490/500, V Loss: 1251.7715, Q Loss: 48183.8994
[IQL] Epoch 491/500, V Loss: 1537.5751, Q Loss: 42339.8903
[IQL] Epoch 492/500, V Loss: 1379.2765, Q Loss: 41820.2189
[IQL] Epoch 493/500, V Loss: 1238.6848, Q Loss: 43612.5208
[IQL] Epoch 494/500, V Loss: 1523.3037, Q Loss: 42116.9661
[IQL] Epoch 495/500, V Loss: 1387.6342, Q Loss: 44024.1460
[IQL] Epoch 496/500, V Loss: 1196.4794, Q Loss: 43678.7546
[IQL] Epoch 497/500, V Loss: 1389.3194, Q Loss: 51521.1025
[IQL] Epoch 498/500, V Loss: 2160.9194, Q Loss: 46359.9987
[IQL] Epoch 499/500, V Loss: 2012.3171, Q Loss: 42953.0290
[RL100] VIB betas set to factor=0.1: beta_recon=0.000010, beta_kl=0.000010

[RL100Trainer] Phase 2b: Offline RL Optimization (Iteration 1)
[OPE] Behavior policy value J_old = 244.3572
[Offline RL] Epoch 0/100, PPO Loss: -0.0237, CD Loss: 0.1494
[Offline RL] Epoch 1/100, PPO Loss: -0.0220, CD Loss: 0.1230
[Offline RL] Epoch 2/100, PPO Loss: -0.0182, CD Loss: 0.1019
[Offline RL] Epoch 3/100, PPO Loss: -0.0200, CD Loss: 0.0979
[Offline RL] Epoch 4/100, PPO Loss: -0.0225, CD Loss: 0.0819
[Offline RL] Epoch 5/100, PPO Loss: -0.0228, CD Loss: 0.0850
[Offline RL] Epoch 6/100, PPO Loss: -0.0229, CD Loss: 0.0738
[Offline RL] Epoch 7/100, PPO Loss: -0.0220, CD Loss: 0.0796
[Offline RL] Epoch 8/100, PPO Loss: -0.0236, CD Loss: 0.0734
[Offline RL] Epoch 9/100, PPO Loss: -0.0218, CD Loss: 0.0757
[Offline RL] Epoch 10/100, PPO Loss: -0.0205, CD Loss: 0.0703
[Offline RL] Epoch 11/100, PPO Loss: -0.0229, CD Loss: 0.0728
[Offline RL] Epoch 12/100, PPO Loss: -0.0211, CD Loss: 0.0691
[Offline RL] Epoch 13/100, PPO Loss: -0.0223, CD Loss: 0.0750
[Offline RL] Epoch 14/100, PPO Loss: -0.0221, CD Loss: 0.0799
[Offline RL] Epoch 15/100, PPO Loss: -0.0206, CD Loss: 0.0798
[Offline RL] Epoch 16/100, PPO Loss: -0.0205, CD Loss: 0.0819
[Offline RL] Epoch 17/100, PPO Loss: -0.0221, CD Loss: 0.0756
[Offline RL] Epoch 18/100, PPO Loss: -0.0213, CD Loss: 0.0680
[Offline RL] Epoch 19/100, PPO Loss: -0.0258, CD Loss: 0.0645
[Offline RL] Epoch 20/100, PPO Loss: -0.0211, CD Loss: 0.0646
[Offline RL] Epoch 21/100, PPO Loss: -0.0256, CD Loss: 0.0627
[Offline RL] Epoch 22/100, PPO Loss: -0.0216, CD Loss: 0.0696
[Offline RL] Epoch 23/100, PPO Loss: -0.0234, CD Loss: 0.0692
[Offline RL] Epoch 24/100, PPO Loss: -0.0233, CD Loss: 0.0813
[Offline RL] Epoch 25/100, PPO Loss: -0.0224, CD Loss: 0.0726
[Offline RL] Epoch 26/100, PPO Loss: -0.0245, CD Loss: 0.0745
[Offline RL] Epoch 27/100, PPO Loss: -0.0241, CD Loss: 0.0801
[Offline RL] Epoch 28/100, PPO Loss: -0.0254, CD Loss: 0.0764
[Offline RL] Epoch 29/100, PPO Loss: -0.0281, CD Loss: 0.0818
[Offline RL] Epoch 30/100, PPO Loss: -0.0281, CD Loss: 0.0819
[Offline RL] Epoch 31/100, PPO Loss: -0.0283, CD Loss: 0.0777
[Offline RL] Epoch 32/100, PPO Loss: -0.0286, CD Loss: 0.0758
[Offline RL] Epoch 33/100, PPO Loss: -0.0277, CD Loss: 0.0736
[Offline RL] Epoch 34/100, PPO Loss: -0.0276, CD Loss: 0.0721
[Offline RL] Epoch 35/100, PPO Loss: -0.0260, CD Loss: 0.0720
[Offline RL] Epoch 36/100, PPO Loss: -0.0258, CD Loss: 0.0717
[Offline RL] Epoch 37/100, PPO Loss: -0.0257, CD Loss: 0.0726
[Offline RL] Epoch 38/100, PPO Loss: -0.0237, CD Loss: 0.0734
[Offline RL] Epoch 39/100, PPO Loss: -0.0261, CD Loss: 0.0728
[Offline RL] Epoch 40/100, PPO Loss: -0.0237, CD Loss: 0.0651
[Offline RL] Epoch 41/100, PPO Loss: -0.0259, CD Loss: 0.0700
[Offline RL] Epoch 42/100, PPO Loss: -0.0254, CD Loss: 0.0758
[Offline RL] Epoch 43/100, PPO Loss: -0.0243, CD Loss: 0.0774
[Offline RL] Epoch 44/100, PPO Loss: -0.0283, CD Loss: 0.0813
[Offline RL] Epoch 45/100, PPO Loss: -0.0249, CD Loss: 0.0850
[Offline RL] Epoch 46/100, PPO Loss: -0.0239, CD Loss: 0.0818
[Offline RL] Epoch 47/100, PPO Loss: -0.0278, CD Loss: 0.0850
[Offline RL] Epoch 48/100, PPO Loss: -0.0266, CD Loss: 0.0826
[Offline RL] Epoch 49/100, PPO Loss: -0.0273, CD Loss: 0.0959
[Offline RL] Epoch 50/100, PPO Loss: -0.0271, CD Loss: 0.0857
[Offline RL] Epoch 51/100, PPO Loss: -0.0259, CD Loss: 0.0917
[Offline RL] Epoch 52/100, PPO Loss: -0.0279, CD Loss: 0.1010
[Offline RL] Epoch 53/100, PPO Loss: -0.0291, CD Loss: 0.0934
[Offline RL] Epoch 54/100, PPO Loss: -0.0288, CD Loss: 0.0997
[Offline RL] Epoch 55/100, PPO Loss: -0.0318, CD Loss: 0.1074
[Offline RL] Epoch 56/100, PPO Loss: -0.0318, CD Loss: 0.1034
[Offline RL] Epoch 57/100, PPO Loss: -0.0246, CD Loss: 0.0970
[Offline RL] Epoch 58/100, PPO Loss: -0.0291, CD Loss: 0.0938
[Offline RL] Epoch 59/100, PPO Loss: -0.0301, CD Loss: 0.0893
[Offline RL] Epoch 60/100, PPO Loss: -0.0264, CD Loss: 0.0826
[Offline RL] Epoch 61/100, PPO Loss: -0.0270, CD Loss: 0.0752
[Offline RL] Epoch 62/100, PPO Loss: -0.0270, CD Loss: 0.0699
[Offline RL] Epoch 63/100, PPO Loss: -0.0272, CD Loss: 0.0692
[Offline RL] Epoch 64/100, PPO Loss: -0.0260, CD Loss: 0.0701
[Offline RL] Epoch 65/100, PPO Loss: -0.0282, CD Loss: 0.0781
[Offline RL] Epoch 66/100, PPO Loss: -0.0291, CD Loss: 0.0839
[Offline RL] Epoch 67/100, PPO Loss: -0.0296, CD Loss: 0.0905
[Offline RL] Epoch 68/100, PPO Loss: -0.0298, CD Loss: 0.0991
[Offline RL] Epoch 69/100, PPO Loss: -0.0310, CD Loss: 0.1002
[Offline RL] Epoch 70/100, PPO Loss: -0.0271, CD Loss: 0.1090
[Offline RL] Epoch 71/100, PPO Loss: -0.0293, CD Loss: 0.0943
[Offline RL] Epoch 72/100, PPO Loss: -0.0260, CD Loss: 0.1091
[Offline RL] Epoch 73/100, PPO Loss: -0.0271, CD Loss: 0.1068
[Offline RL] Epoch 74/100, PPO Loss: -0.0281, CD Loss: 0.1036
[Offline RL] Epoch 75/100, PPO Loss: -0.0290, CD Loss: 0.1040
[Offline RL] Epoch 76/100, PPO Loss: -0.0271, CD Loss: 0.1040
[Offline RL] Epoch 77/100, PPO Loss: -0.0292, CD Loss: 0.1098
[Offline RL] Epoch 78/100, PPO Loss: -0.0285, CD Loss: 0.1137
[Offline RL] Epoch 79/100, PPO Loss: -0.0309, CD Loss: 0.1064
[Offline RL] Epoch 80/100, PPO Loss: -0.0261, CD Loss: 0.1108
[Offline RL] Epoch 81/100, PPO Loss: -0.0258, CD Loss: 0.1076
[Offline RL] Epoch 82/100, PPO Loss: -0.0273, CD Loss: 0.1065
[Offline RL] Epoch 83/100, PPO Loss: -0.0286, CD Loss: 0.1034
[Offline RL] Epoch 84/100, PPO Loss: -0.0271, CD Loss: 0.1055
[Offline RL] Epoch 85/100, PPO Loss: -0.0292, CD Loss: 0.1070
[Offline RL] Epoch 86/100, PPO Loss: -0.0294, CD Loss: 0.1001
[Offline RL] Epoch 87/100, PPO Loss: -0.0312, CD Loss: 0.0948
[Offline RL] Epoch 88/100, PPO Loss: -0.0289, CD Loss: 0.0977
[Offline RL] Epoch 89/100, PPO Loss: -0.0272, CD Loss: 0.0943
[Offline RL] Epoch 90/100, PPO Loss: -0.0281, CD Loss: 0.1020
[Offline RL] Epoch 91/100, PPO Loss: -0.0301, CD Loss: 0.1025
[Offline RL] Epoch 92/100, PPO Loss: -0.0293, CD Loss: 0.1109
[Offline RL] Epoch 93/100, PPO Loss: -0.0258, CD Loss: 0.1043
[Offline RL] Epoch 94/100, PPO Loss: -0.0282, CD Loss: 0.0999
[Offline RL] Epoch 95/100, PPO Loss: -0.0252, CD Loss: 0.0919
[Offline RL] Epoch 96/100, PPO Loss: -0.0248, CD Loss: 0.0983
[Offline RL] Epoch 97/100, PPO Loss: -0.0268, CD Loss: 0.0941
[Offline RL] Epoch 98/100, PPO Loss: -0.0275, CD Loss: 0.1019
[Offline RL] Epoch 99/100, PPO Loss: -0.0260, CD Loss: 0.0963
[OPE] Policy ACCEPTED: J_new=329.1080 > J_old=244.3572 + δ=12.2179

[RL100Trainer] Phase 2c: Collecting New Data (Iteration 1)
[Collect] 50 episodes, success=0.000, steps=1250
[Data Collection] Success Rate: 0.000, Reward: 1921.74, Episodes: 50, Steps: 1250
[Dataset] Merged 50 episodes (1250 steps) → total 4500 steps, 110 episodes
[RL100] VIB betas set to factor=1.0: beta_recon=0.000100, beta_kl=0.000100

[RL100Trainer] Retraining IL on merged dataset...

============================================================
[RL100Trainer] Phase 1: Imitation Learning
============================================================

[IL] Epoch 0/100, Loss: 1.3491
[IL] Epoch 1/100, Loss: 0.5823
[IL] Epoch 2/100, Loss: 0.4249
[IL] Epoch 3/100, Loss: 0.3328
[IL] Epoch 4/100, Loss: 0.2681
[IL] Epoch 5/100, Loss: 0.2218
[IL] Epoch 6/100, Loss: 0.1928
[IL] Epoch 7/100, Loss: 0.1676
[IL] Epoch 8/100, Loss: 0.1493
[IL] Epoch 9/100, Loss: 0.1421
[IL] Epoch 10/100, Loss: 0.1298
[IL] Epoch 11/100, Loss: 0.1202
[IL] Epoch 12/100, Loss: 0.1224
[IL] Epoch 13/100, Loss: 0.1197
[IL] Epoch 14/100, Loss: 0.1127
[IL] Epoch 15/100, Loss: 0.1096
[IL] Epoch 16/100, Loss: 0.1077
[IL] Epoch 17/100, Loss: 0.1036
[IL] Epoch 18/100, Loss: 0.1054
[IL] Epoch 19/100, Loss: 0.0973
[IL] Epoch 20/100, Loss: 0.1011
[IL] Epoch 21/100, Loss: 0.1020
[IL] Epoch 22/100, Loss: 0.1004
[IL] Epoch 23/100, Loss: 0.0962
[IL] Epoch 24/100, Loss: 0.0959
[IL] Epoch 25/100, Loss: 0.0944
[IL] Epoch 26/100, Loss: 0.0957
[IL] Epoch 27/100, Loss: 0.0902
[IL] Epoch 28/100, Loss: 0.0893
[IL] Epoch 29/100, Loss: 0.0937
[IL] Epoch 30/100, Loss: 0.0909
[IL] Epoch 31/100, Loss: 0.0924
[IL] Epoch 32/100, Loss: 0.0934
[IL] Epoch 33/100, Loss: 0.0878
[IL] Epoch 34/100, Loss: 0.0858
[IL] Epoch 35/100, Loss: 0.0866
[IL] Epoch 36/100, Loss: 0.0878
[IL] Epoch 37/100, Loss: 0.0900
[IL] Epoch 38/100, Loss: 0.0852
[IL] Epoch 39/100, Loss: 0.0891
[IL] Epoch 40/100, Loss: 0.0886
[IL] Epoch 41/100, Loss: 0.0845
[IL] Epoch 42/100, Loss: 0.0910
[IL] Epoch 43/100, Loss: 0.0868
[IL] Epoch 44/100, Loss: 0.0883
[IL] Epoch 45/100, Loss: 0.0880
[IL] Epoch 46/100, Loss: 0.0860
[IL] Epoch 47/100, Loss: 0.0848
[IL] Epoch 48/100, Loss: 0.0870
[IL] Epoch 49/100, Loss: 0.0876
[IL] Epoch 50/100, Loss: 0.0814
[IL] Epoch 51/100, Loss: 0.0865
[IL] Epoch 52/100, Loss: 0.0804
[IL] Epoch 53/100, Loss: 0.0790
[IL] Epoch 54/100, Loss: 0.0807
[IL] Epoch 55/100, Loss: 0.0786
[IL] Epoch 56/100, Loss: 0.0894
[IL] Epoch 57/100, Loss: 0.0892
[IL] Epoch 58/100, Loss: 0.0810
[IL] Epoch 59/100, Loss: 0.0827
[IL] Epoch 60/100, Loss: 0.0790
[IL] Epoch 61/100, Loss: 0.0816
[IL] Epoch 62/100, Loss: 0.0792
[IL] Epoch 63/100, Loss: 0.0804
[IL] Epoch 64/100, Loss: 0.0779
[IL] Epoch 65/100, Loss: 0.0806
[IL] Epoch 66/100, Loss: 0.0773
[IL] Epoch 67/100, Loss: 0.0810
[IL] Epoch 68/100, Loss: 0.0793
[IL] Epoch 69/100, Loss: 0.0753
[IL] Epoch 70/100, Loss: 0.0758
[IL] Epoch 71/100, Loss: 0.0872
[IL] Epoch 72/100, Loss: 0.0799
[IL] Epoch 73/100, Loss: 0.0782
[IL] Epoch 74/100, Loss: 0.0782
[IL] Epoch 75/100, Loss: 0.0710
[IL] Epoch 76/100, Loss: 0.0725
[IL] Epoch 77/100, Loss: 0.0805
[IL] Epoch 78/100, Loss: 0.0781
[IL] Epoch 79/100, Loss: 0.0725
[IL] Epoch 80/100, Loss: 0.0816
[IL] Epoch 81/100, Loss: 0.0752
[IL] Epoch 82/100, Loss: 0.0786
[IL] Epoch 83/100, Loss: 0.0774
[IL] Epoch 84/100, Loss: 0.0758
[IL] Epoch 85/100, Loss: 0.0773
[IL] Epoch 86/100, Loss: 0.0689
[IL] Epoch 87/100, Loss: 0.0775
[IL] Epoch 88/100, Loss: 0.0775
[IL] Epoch 89/100, Loss: 0.0739
[IL] Epoch 90/100, Loss: 0.0782
[IL] Epoch 91/100, Loss: 0.0770
[IL] Epoch 92/100, Loss: 0.0741
[IL] Epoch 93/100, Loss: 0.0736
[IL] Epoch 94/100, Loss: 0.0755
[IL] Epoch 95/100, Loss: 0.0731
[IL] Epoch 96/100, Loss: 0.0756
[IL] Epoch 97/100, Loss: 0.0762
[IL] Epoch 98/100, Loss: 0.0739
[IL] Epoch 99/100, Loss: 0.0729
test_mean_score: 0.15
[IL] Eval - Success Rate: 0.150
[Checkpoint] Saved to /nfs_global/S/yangrongzheng/RL100/3D-Diffusion-Policy/3D-Diffusion-Policy/checkpoints/offline_iter_1.ckpt

================================================================================
               OFFLINE RL ITERATION 3/5
================================================================================


[RL100Trainer] Line 6 — Training Transition Model T_θ (Iteration 2)

[TransitionModel] Encoding dataset for transition model training...
[TransitionModel] Dataset: 3730 samples, input_dim=260, target_dim=257
[TransitionModel] Epoch    0 | train=14410.25936 | val=4819.70332 | no-improve=0/5
[TransitionModel] Epoch   20 | train=2176.48579 | val=1561.50144 | no-improve=0/5
[TransitionModel] Epoch   40 | train=1369.03919 | val=1388.76035 | no-improve=0/5
[TransitionModel] Epoch   60 | train=1012.72836 | val=1244.45134 | no-improve=1/5
[TransitionModel] Epoch   80 | train=753.96441 | val=1209.60747 | no-improve=1/5
[TransitionModel] Epoch   96 | train=602.76311 | val=1152.43484 | no-improve=5/5
[TransitionModel] Training complete. Elites=[5, 3, 2, 4, 6], val_loss=1112.52603

[RL100Trainer] Phase 2a: Training IQL Critics (Iteration 2)
[IQL] Epoch 0/500, V Loss: 13271.1926, Q Loss: 150964.7760
[IQL] Epoch 1/500, V Loss: 6763.6303, Q Loss: 101983.8557
[IQL] Epoch 2/500, V Loss: 7519.1248, Q Loss: 80975.8307
[IQL] Epoch 3/500, V Loss: 6758.5209, Q Loss: 69536.8401
[IQL] Epoch 4/500, V Loss: 4748.9755, Q Loss: 62216.1703
[IQL] Epoch 5/500, V Loss: 3983.2045, Q Loss: 57085.1268
[IQL] Epoch 6/500, V Loss: 3649.1464, Q Loss: 52434.2102
[IQL] Epoch 7/500, V Loss: 3579.1343, Q Loss: 49407.6729
[IQL] Epoch 8/500, V Loss: 3550.5385, Q Loss: 46161.2620
[IQL] Epoch 9/500, V Loss: 4104.8514, Q Loss: 43763.2349
[IQL] Epoch 10/500, V Loss: 4249.2553, Q Loss: 43537.8458
[IQL] Epoch 11/500, V Loss: 3963.4432, Q Loss: 41509.8357
[IQL] Epoch 12/500, V Loss: 3532.9585, Q Loss: 41208.6448
[IQL] Epoch 13/500, V Loss: 3834.5532, Q Loss: 39726.5632
[IQL] Epoch 14/500, V Loss: 3717.1404, Q Loss: 40048.5064
[IQL] Epoch 15/500, V Loss: 3430.0348, Q Loss: 39480.9427
[IQL] Epoch 16/500, V Loss: 3285.9076, Q Loss: 39429.6982
[IQL] Epoch 17/500, V Loss: 3810.3736, Q Loss: 39134.5478
[IQL] Epoch 18/500, V Loss: 3090.8268, Q Loss: 40337.7159
[IQL] Epoch 19/500, V Loss: 3303.2500, Q Loss: 40582.1596
[IQL] Epoch 20/500, V Loss: 3034.0496, Q Loss: 39661.3995
[IQL] Epoch 21/500, V Loss: 2594.8007, Q Loss: 38336.5155
[IQL] Epoch 22/500, V Loss: 3511.2767, Q Loss: 39699.5792
[IQL] Epoch 23/500, V Loss: 2933.2266, Q Loss: 38068.8307
[IQL] Epoch 24/500, V Loss: 2693.4048, Q Loss: 38455.1129
[IQL] Epoch 25/500, V Loss: 2406.6045, Q Loss: 39320.8628
[IQL] Epoch 26/500, V Loss: 2460.0339, Q Loss: 40454.5396
[IQL] Epoch 27/500, V Loss: 2898.8583, Q Loss: 38728.2217
[IQL] Epoch 28/500, V Loss: 2289.5336, Q Loss: 39338.8066
[IQL] Epoch 29/500, V Loss: 2643.7258, Q Loss: 39562.0487
[IQL] Epoch 30/500, V Loss: 3496.8865, Q Loss: 41689.4716
[IQL] Epoch 31/500, V Loss: 2914.4716, Q Loss: 40505.0507
[IQL] Epoch 32/500, V Loss: 2503.4674, Q Loss: 40719.0517
[IQL] Epoch 33/500, V Loss: 2480.2258, Q Loss: 38916.8154
[IQL] Epoch 34/500, V Loss: 2463.6687, Q Loss: 38131.7604
[IQL] Epoch 35/500, V Loss: 2384.8444, Q Loss: 39115.1453
[IQL] Epoch 36/500, V Loss: 2076.0981, Q Loss: 39597.4288
[IQL] Epoch 37/500, V Loss: 2962.4213, Q Loss: 39436.4052
[IQL] Epoch 38/500, V Loss: 3148.0300, Q Loss: 39633.5654
[IQL] Epoch 39/500, V Loss: 3171.7805, Q Loss: 39954.4993
[IQL] Epoch 40/500, V Loss: 2000.8729, Q Loss: 39536.5344
[IQL] Epoch 41/500, V Loss: 2408.5316, Q Loss: 40281.8352
[IQL] Epoch 42/500, V Loss: 2770.0744, Q Loss: 39578.8733
[IQL] Epoch 43/500, V Loss: 1822.5108, Q Loss: 38996.2913
[IQL] Epoch 44/500, V Loss: 2399.0165, Q Loss: 38339.8799
[IQL] Epoch 45/500, V Loss: 2405.4932, Q Loss: 37840.7672
[IQL] Epoch 46/500, V Loss: 2478.8837, Q Loss: 39835.3180
[IQL] Epoch 47/500, V Loss: 2009.3746, Q Loss: 37938.2712
[IQL] Epoch 48/500, V Loss: 1993.9556, Q Loss: 38448.7642
[IQL] Epoch 49/500, V Loss: 1995.6764, Q Loss: 37208.3104
[IQL] Epoch 50/500, V Loss: 2049.6685, Q Loss: 37943.7727
[IQL] Epoch 51/500, V Loss: 1827.3024, Q Loss: 38549.1013
[IQL] Epoch 52/500, V Loss: 2597.5880, Q Loss: 37867.4663
[IQL] Epoch 53/500, V Loss: 2212.8361, Q Loss: 37377.6263
[IQL] Epoch 54/500, V Loss: 2054.2543, Q Loss: 38153.9357
[IQL] Epoch 55/500, V Loss: 2348.2021, Q Loss: 38948.8577
[IQL] Epoch 56/500, V Loss: 2247.6483, Q Loss: 39790.5581
[IQL] Epoch 57/500, V Loss: 2404.9081, Q Loss: 39216.9839
[IQL] Epoch 58/500, V Loss: 2451.0884, Q Loss: 36280.5408
[IQL] Epoch 59/500, V Loss: 2352.7922, Q Loss: 37317.3159
[IQL] Epoch 60/500, V Loss: 2143.0222, Q Loss: 37070.9447
[IQL] Epoch 61/500, V Loss: 1980.4556, Q Loss: 37097.3124
[IQL] Epoch 62/500, V Loss: 1871.9943, Q Loss: 37409.7548
[IQL] Epoch 63/500, V Loss: 2288.0506, Q Loss: 36270.9784
[IQL] Epoch 64/500, V Loss: 2066.2162, Q Loss: 35987.0669
[IQL] Epoch 65/500, V Loss: 2121.8331, Q Loss: 36563.0557
[IQL] Epoch 66/500, V Loss: 1902.5675, Q Loss: 36665.4628
[IQL] Epoch 67/500, V Loss: 2847.0250, Q Loss: 35818.6967
[IQL] Epoch 68/500, V Loss: 2413.5590, Q Loss: 35787.4151
[IQL] Epoch 69/500, V Loss: 2317.0711, Q Loss: 35088.5163
[IQL] Epoch 70/500, V Loss: 2354.9332, Q Loss: 35381.7507
[IQL] Epoch 71/500, V Loss: 2297.3892, Q Loss: 34041.7633
[IQL] Epoch 72/500, V Loss: 2547.1222, Q Loss: 35279.9719
[IQL] Epoch 73/500, V Loss: 2580.9581, Q Loss: 35547.7783
[IQL] Epoch 74/500, V Loss: 2529.5226, Q Loss: 35416.4888
[IQL] Epoch 75/500, V Loss: 2335.1396, Q Loss: 34236.4210
[IQL] Epoch 76/500, V Loss: 2516.4716, Q Loss: 36287.7090
[IQL] Epoch 77/500, V Loss: 2219.4880, Q Loss: 38559.5108
[IQL] Epoch 78/500, V Loss: 2829.2276, Q Loss: 35181.5961
[IQL] Epoch 79/500, V Loss: 2034.7152, Q Loss: 35871.9824
[IQL] Epoch 80/500, V Loss: 2412.8612, Q Loss: 35126.6155
[IQL] Epoch 81/500, V Loss: 2551.3860, Q Loss: 34099.6233
[IQL] Epoch 82/500, V Loss: 1963.8603, Q Loss: 34154.5146
[IQL] Epoch 83/500, V Loss: 2028.5959, Q Loss: 33840.0965
[IQL] Epoch 84/500, V Loss: 2128.9606, Q Loss: 33617.0884
[IQL] Epoch 85/500, V Loss: 2067.5235, Q Loss: 34200.1568
[IQL] Epoch 86/500, V Loss: 1949.2599, Q Loss: 34950.8009
[IQL] Epoch 87/500, V Loss: 2481.7117, Q Loss: 33856.6023
[IQL] Epoch 88/500, V Loss: 3304.4614, Q Loss: 35401.3130
[IQL] Epoch 89/500, V Loss: 2342.5408, Q Loss: 33905.6512
[IQL] Epoch 90/500, V Loss: 2049.5567, Q Loss: 34102.8025
[IQL] Epoch 91/500, V Loss: 2039.6640, Q Loss: 33475.9809
[IQL] Epoch 92/500, V Loss: 2094.9617, Q Loss: 32549.9809
[IQL] Epoch 93/500, V Loss: 2363.5155, Q Loss: 33077.4076
[IQL] Epoch 94/500, V Loss: 2254.8036, Q Loss: 33546.4456
[IQL] Epoch 95/500, V Loss: 2221.0226, Q Loss: 32872.9453
[IQL] Epoch 96/500, V Loss: 2206.9176, Q Loss: 33059.3616
[IQL] Epoch 97/500, V Loss: 2228.6710, Q Loss: 33134.4576
[IQL] Epoch 98/500, V Loss: 2193.1259, Q Loss: 32906.1826
[IQL] Epoch 99/500, V Loss: 2157.2657, Q Loss: 32430.8107
[IQL] Epoch 100/500, V Loss: 1969.8067, Q Loss: 32167.1898
[IQL] Epoch 101/500, V Loss: 2348.7287, Q Loss: 32084.4531
[IQL] Epoch 102/500, V Loss: 1989.7711, Q Loss: 32400.8462
[IQL] Epoch 103/500, V Loss: 2254.5734, Q Loss: 32658.2280
[IQL] Epoch 104/500, V Loss: 2396.6674, Q Loss: 32107.5704
[IQL] Epoch 105/500, V Loss: 2550.6003, Q Loss: 32437.9427
[IQL] Epoch 106/500, V Loss: 2665.7680, Q Loss: 32721.9768
[IQL] Epoch 107/500, V Loss: 2280.1568, Q Loss: 32836.3083
[IQL] Epoch 108/500, V Loss: 2388.1952, Q Loss: 31950.2117
[IQL] Epoch 109/500, V Loss: 2440.0899, Q Loss: 32451.8632
[IQL] Epoch 110/500, V Loss: 2215.6761, Q Loss: 32353.7638
[IQL] Epoch 111/500, V Loss: 2362.9235, Q Loss: 31698.4439
[IQL] Epoch 112/500, V Loss: 2087.0709, Q Loss: 32255.3181
[IQL] Epoch 113/500, V Loss: 2340.9957, Q Loss: 32641.8775
[IQL] Epoch 114/500, V Loss: 2713.1894, Q Loss: 33382.4085
[IQL] Epoch 115/500, V Loss: 2015.1032, Q Loss: 32553.7986
[IQL] Epoch 116/500, V Loss: 2581.7126, Q Loss: 33552.9267
[IQL] Epoch 117/500, V Loss: 2360.9363, Q Loss: 32721.0895
[IQL] Epoch 118/500, V Loss: 2221.5815, Q Loss: 32318.0406
[IQL] Epoch 119/500, V Loss: 2352.9190, Q Loss: 31926.0659
[IQL] Epoch 120/500, V Loss: 2677.8988, Q Loss: 32645.5533
[IQL] Epoch 121/500, V Loss: 2131.1105, Q Loss: 31718.7104
[IQL] Epoch 122/500, V Loss: 2403.9618, Q Loss: 32426.2214
[IQL] Epoch 123/500, V Loss: 2802.8982, Q Loss: 32996.2225
[IQL] Epoch 124/500, V Loss: 1992.4304, Q Loss: 31594.6382
[IQL] Epoch 125/500, V Loss: 2158.5537, Q Loss: 31346.6717
[IQL] Epoch 126/500, V Loss: 2282.6804, Q Loss: 31654.8669
[IQL] Epoch 127/500, V Loss: 2405.0257, Q Loss: 32147.4785
[IQL] Epoch 128/500, V Loss: 2344.1434, Q Loss: 32468.7378
[IQL] Epoch 129/500, V Loss: 2141.6745, Q Loss: 31942.3982
[IQL] Epoch 130/500, V Loss: 2014.6506, Q Loss: 31803.0085
[IQL] Epoch 131/500, V Loss: 2325.2872, Q Loss: 31499.9562
[IQL] Epoch 132/500, V Loss: 2064.3111, Q Loss: 30566.0257
[IQL] Epoch 133/500, V Loss: 2059.3993, Q Loss: 31198.6126
[IQL] Epoch 134/500, V Loss: 2255.9652, Q Loss: 31007.1465
[IQL] Epoch 135/500, V Loss: 2310.0347, Q Loss: 32445.5285
[IQL] Epoch 136/500, V Loss: 2175.0240, Q Loss: 31819.5663
[IQL] Epoch 137/500, V Loss: 1961.7465, Q Loss: 32243.7471
[IQL] Epoch 138/500, V Loss: 2416.6831, Q Loss: 30398.5342
[IQL] Epoch 139/500, V Loss: 2229.3044, Q Loss: 31280.4710
[IQL] Epoch 140/500, V Loss: 2134.5983, Q Loss: 31158.6061
[IQL] Epoch 141/500, V Loss: 2576.9497, Q Loss: 30729.3266
[IQL] Epoch 142/500, V Loss: 2444.7938, Q Loss: 31229.7461
[IQL] Epoch 143/500, V Loss: 2049.7138, Q Loss: 30688.6833
[IQL] Epoch 144/500, V Loss: 3056.2202, Q Loss: 32804.5637
[IQL] Epoch 145/500, V Loss: 2677.8189, Q Loss: 31338.4560
[IQL] Epoch 146/500, V Loss: 2444.8950, Q Loss: 31267.3061
[IQL] Epoch 147/500, V Loss: 2347.0680, Q Loss: 31185.8195
[IQL] Epoch 148/500, V Loss: 2182.5321, Q Loss: 30209.4522
[IQL] Epoch 149/500, V Loss: 2123.9627, Q Loss: 30500.1064
[IQL] Epoch 150/500, V Loss: 2240.9025, Q Loss: 31828.7585
[IQL] Epoch 151/500, V Loss: 2206.1573, Q Loss: 31817.5147
[IQL] Epoch 152/500, V Loss: 2623.3994, Q Loss: 31028.5260
[IQL] Epoch 153/500, V Loss: 2988.1273, Q Loss: 32086.4043
[IQL] Epoch 154/500, V Loss: 2521.2739, Q Loss: 32308.9342
[IQL] Epoch 155/500, V Loss: 2511.4164, Q Loss: 31917.6536
[IQL] Epoch 156/500, V Loss: 2217.7877, Q Loss: 30595.2893
[IQL] Epoch 157/500, V Loss: 2548.6245, Q Loss: 32349.8146
[IQL] Epoch 158/500, V Loss: 2346.6625, Q Loss: 31375.7401
[IQL] Epoch 159/500, V Loss: 2196.9089, Q Loss: 31453.6715
[IQL] Epoch 160/500, V Loss: 2555.3056, Q Loss: 30946.2496
[IQL] Epoch 161/500, V Loss: 2013.7858, Q Loss: 31321.8543
[IQL] Epoch 162/500, V Loss: 2376.3498, Q Loss: 31456.9479
[IQL] Epoch 163/500, V Loss: 2291.6906, Q Loss: 30819.2408
[IQL] Epoch 164/500, V Loss: 2347.9994, Q Loss: 31810.5465
[IQL] Epoch 165/500, V Loss: 2526.2610, Q Loss: 31629.7095
[IQL] Epoch 166/500, V Loss: 2355.3642, Q Loss: 31142.5965
[IQL] Epoch 167/500, V Loss: 2692.6150, Q Loss: 32392.0734
[IQL] Epoch 168/500, V Loss: 2333.6780, Q Loss: 32090.1853
[IQL] Epoch 169/500, V Loss: 2208.9943, Q Loss: 30885.5316
[IQL] Epoch 170/500, V Loss: 2415.7245, Q Loss: 29930.0395
[IQL] Epoch 171/500, V Loss: 2325.8125, Q Loss: 31091.2513
[IQL] Epoch 172/500, V Loss: 3041.7277, Q Loss: 32404.4727
[IQL] Epoch 173/500, V Loss: 1938.4699, Q Loss: 30474.5721
[IQL] Epoch 174/500, V Loss: 2287.1820, Q Loss: 30714.8988
[IQL] Epoch 175/500, V Loss: 2328.1630, Q Loss: 30889.1013
[IQL] Epoch 176/500, V Loss: 2366.7233, Q Loss: 31407.8816
[IQL] Epoch 177/500, V Loss: 2433.4948, Q Loss: 32013.1402
[IQL] Epoch 178/500, V Loss: 2563.0725, Q Loss: 31263.9385
[IQL] Epoch 179/500, V Loss: 2376.8246, Q Loss: 30709.6952
[IQL] Epoch 180/500, V Loss: 2349.8051, Q Loss: 31427.7777
[IQL] Epoch 181/500, V Loss: 2402.3065, Q Loss: 31276.6096
[IQL] Epoch 182/500, V Loss: 2215.5932, Q Loss: 30581.8431
[IQL] Epoch 183/500, V Loss: 2305.7950, Q Loss: 30788.8983
[IQL] Epoch 184/500, V Loss: 2199.2319, Q Loss: 30721.0590
[IQL] Epoch 185/500, V Loss: 2429.1600, Q Loss: 30747.8779
[IQL] Epoch 186/500, V Loss: 2573.9741, Q Loss: 32446.8923
[IQL] Epoch 187/500, V Loss: 2588.5502, Q Loss: 30846.0383
[IQL] Epoch 188/500, V Loss: 2551.1715, Q Loss: 30861.0855
[IQL] Epoch 189/500, V Loss: 2735.8319, Q Loss: 32502.0674
[IQL] Epoch 190/500, V Loss: 2419.8874, Q Loss: 31181.3810
[IQL] Epoch 191/500, V Loss: 2337.1577, Q Loss: 31262.1102
[IQL] Epoch 192/500, V Loss: 2632.6803, Q Loss: 31044.7092
[IQL] Epoch 193/500, V Loss: 2359.2708, Q Loss: 30518.2210
[IQL] Epoch 194/500, V Loss: 2221.0916, Q Loss: 30387.7983
[IQL] Epoch 195/500, V Loss: 2482.0449, Q Loss: 29647.7223
[IQL] Epoch 196/500, V Loss: 2607.6865, Q Loss: 30405.1422
[IQL] Epoch 197/500, V Loss: 2879.8087, Q Loss: 30838.0501
[IQL] Epoch 198/500, V Loss: 2840.8330, Q Loss: 29711.1400
[IQL] Epoch 199/500, V Loss: 2885.6604, Q Loss: 30878.7432
[IQL] Epoch 200/500, V Loss: 2494.3253, Q Loss: 30456.8746
[IQL] Epoch 201/500, V Loss: 2640.4222, Q Loss: 30790.3428
[IQL] Epoch 202/500, V Loss: 2280.6975, Q Loss: 31105.8094
[IQL] Epoch 203/500, V Loss: 2935.1517, Q Loss: 30866.5303
[IQL] Epoch 204/500, V Loss: 2567.7091, Q Loss: 30466.3099
[IQL] Epoch 205/500, V Loss: 2603.9790, Q Loss: 29855.1297
[IQL] Epoch 206/500, V Loss: 2540.1350, Q Loss: 30714.2956
[IQL] Epoch 207/500, V Loss: 2693.6866, Q Loss: 30526.3957
[IQL] Epoch 208/500, V Loss: 2789.4024, Q Loss: 30339.2096
[IQL] Epoch 209/500, V Loss: 2617.5692, Q Loss: 31150.6527
[IQL] Epoch 210/500, V Loss: 2257.8967, Q Loss: 29586.3936
[IQL] Epoch 211/500, V Loss: 2659.5600, Q Loss: 29625.0461
[IQL] Epoch 212/500, V Loss: 2252.2284, Q Loss: 30448.2100
[IQL] Epoch 213/500, V Loss: 2644.2094, Q Loss: 31958.6934
[IQL] Epoch 214/500, V Loss: 2975.3329, Q Loss: 29819.4038
[IQL] Epoch 215/500, V Loss: 3114.3018, Q Loss: 32429.3296
[IQL] Epoch 216/500, V Loss: 2564.7993, Q Loss: 31475.9743
[IQL] Epoch 217/500, V Loss: 2331.4863, Q Loss: 30848.3887
[IQL] Epoch 218/500, V Loss: 2262.1169, Q Loss: 31178.5039
[IQL] Epoch 219/500, V Loss: 2518.1192, Q Loss: 29311.1458
[IQL] Epoch 220/500, V Loss: 2745.4570, Q Loss: 30248.8923
[IQL] Epoch 221/500, V Loss: 2491.3897, Q Loss: 30226.8121
[IQL] Epoch 222/500, V Loss: 2672.5319, Q Loss: 30375.2077
[IQL] Epoch 223/500, V Loss: 2835.3841, Q Loss: 29297.3233
[IQL] Epoch 224/500, V Loss: 2459.3812, Q Loss: 30199.9672
[IQL] Epoch 225/500, V Loss: 2689.8564, Q Loss: 30493.6672
[IQL] Epoch 226/500, V Loss: 3182.1743, Q Loss: 30558.5355
[IQL] Epoch 227/500, V Loss: 2700.9683, Q Loss: 30193.3409
[IQL] Epoch 228/500, V Loss: 2685.8440, Q Loss: 30230.3232
[IQL] Epoch 229/500, V Loss: 3029.9578, Q Loss: 29772.6857
[IQL] Epoch 230/500, V Loss: 2894.7227, Q Loss: 32734.4345
[IQL] Epoch 231/500, V Loss: 2840.6815, Q Loss: 30396.3163
[IQL] Epoch 232/500, V Loss: 2930.5126, Q Loss: 30340.8635
[IQL] Epoch 233/500, V Loss: 3006.6845, Q Loss: 30903.1229
[IQL] Epoch 234/500, V Loss: 2387.8394, Q Loss: 29509.3150
[IQL] Epoch 235/500, V Loss: 2667.2380, Q Loss: 29945.2138
[IQL] Epoch 236/500, V Loss: 2646.2326, Q Loss: 29429.1617
[IQL] Epoch 237/500, V Loss: 2809.9281, Q Loss: 29699.0943
[IQL] Epoch 238/500, V Loss: 2658.4020, Q Loss: 31123.7228
[IQL] Epoch 239/500, V Loss: 3311.7711, Q Loss: 31112.1141
[IQL] Epoch 240/500, V Loss: 2690.2578, Q Loss: 31082.3240
[IQL] Epoch 241/500, V Loss: 2682.5182, Q Loss: 30635.2505
[IQL] Epoch 242/500, V Loss: 2801.7721, Q Loss: 29535.1753
[IQL] Epoch 243/500, V Loss: 2805.6924, Q Loss: 29821.4013
[IQL] Epoch 244/500, V Loss: 2989.2394, Q Loss: 29690.4887
[IQL] Epoch 245/500, V Loss: 2707.0156, Q Loss: 31384.6590
[IQL] Epoch 246/500, V Loss: 2788.0575, Q Loss: 29727.6085
[IQL] Epoch 247/500, V Loss: 3262.2279, Q Loss: 31212.7363
[IQL] Epoch 248/500, V Loss: 2917.4535, Q Loss: 30420.4160
[IQL] Epoch 249/500, V Loss: 3094.6016, Q Loss: 31551.4021
[IQL] Epoch 250/500, V Loss: 3099.9329, Q Loss: 30692.9471
[IQL] Epoch 251/500, V Loss: 3570.7470, Q Loss: 30090.7661
[IQL] Epoch 252/500, V Loss: 2670.5214, Q Loss: 30655.5544
[IQL] Epoch 253/500, V Loss: 2760.6502, Q Loss: 30109.8870
[IQL] Epoch 254/500, V Loss: 2926.2704, Q Loss: 29515.6311
[IQL] Epoch 255/500, V Loss: 2712.0112, Q Loss: 29691.4992
[IQL] Epoch 256/500, V Loss: 3169.9234, Q Loss: 29393.6177
[IQL] Epoch 257/500, V Loss: 3054.9933, Q Loss: 28817.9966
[IQL] Epoch 258/500, V Loss: 3208.8909, Q Loss: 30479.1866
[IQL] Epoch 259/500, V Loss: 3081.0106, Q Loss: 30004.5693
[IQL] Epoch 260/500, V Loss: 3645.4879, Q Loss: 30899.3918
[IQL] Epoch 261/500, V Loss: 2838.5984, Q Loss: 29987.4260
[IQL] Epoch 262/500, V Loss: 2845.6513, Q Loss: 28944.5719
[IQL] Epoch 263/500, V Loss: 3136.8780, Q Loss: 29965.3738
[IQL] Epoch 264/500, V Loss: 3452.4027, Q Loss: 28304.4868
[IQL] Epoch 265/500, V Loss: 2878.1386, Q Loss: 29633.3414
[IQL] Epoch 266/500, V Loss: 3192.6759, Q Loss: 30172.0557
[IQL] Epoch 267/500, V Loss: 3753.1315, Q Loss: 28232.3992
[IQL] Epoch 268/500, V Loss: 3442.1665, Q Loss: 28877.2585
[IQL] Epoch 269/500, V Loss: 2935.0739, Q Loss: 29265.3065
[IQL] Epoch 270/500, V Loss: 3123.4631, Q Loss: 29326.4251
[IQL] Epoch 271/500, V Loss: 2893.2352, Q Loss: 28869.7357
[IQL] Epoch 272/500, V Loss: 3320.9380, Q Loss: 29408.7638
[IQL] Epoch 273/500, V Loss: 3120.6179, Q Loss: 30179.0734
[IQL] Epoch 274/500, V Loss: 2891.0960, Q Loss: 28850.6833
[IQL] Epoch 275/500, V Loss: 3831.3402, Q Loss: 29351.2029
[IQL] Epoch 276/500, V Loss: 3274.2141, Q Loss: 30474.5663
[IQL] Epoch 277/500, V Loss: 3295.4468, Q Loss: 29252.9702
[IQL] Epoch 278/500, V Loss: 3113.6452, Q Loss: 30573.6038
[IQL] Epoch 279/500, V Loss: 3759.4488, Q Loss: 31572.8807
[IQL] Epoch 280/500, V Loss: 3568.8889, Q Loss: 29336.3233
[IQL] Epoch 281/500, V Loss: 3066.3311, Q Loss: 29327.6079
[IQL] Epoch 282/500, V Loss: 3070.9682, Q Loss: 30360.3809
[IQL] Epoch 283/500, V Loss: 2771.2890, Q Loss: 29346.1009
[IQL] Epoch 284/500, V Loss: 4021.8284, Q Loss: 32877.3810
[IQL] Epoch 285/500, V Loss: 4225.5199, Q Loss: 29566.6456
[IQL] Epoch 286/500, V Loss: 3207.7690, Q Loss: 30271.3220
[IQL] Epoch 287/500, V Loss: 3567.7840, Q Loss: 30042.4469
[IQL] Epoch 288/500, V Loss: 3606.6751, Q Loss: 30376.5797
[IQL] Epoch 289/500, V Loss: 3922.0412, Q Loss: 28184.3256
[IQL] Epoch 290/500, V Loss: 3031.7512, Q Loss: 29270.1201
[IQL] Epoch 291/500, V Loss: 3702.5342, Q Loss: 29493.5504
[IQL] Epoch 292/500, V Loss: 3789.0099, Q Loss: 31585.7376
[IQL] Epoch 293/500, V Loss: 3326.7282, Q Loss: 31295.9643
[IQL] Epoch 294/500, V Loss: 3375.6684, Q Loss: 28924.0196
[IQL] Epoch 295/500, V Loss: 3225.9588, Q Loss: 29809.6576
[IQL] Epoch 296/500, V Loss: 3248.7372, Q Loss: 30764.4118
[IQL] Epoch 297/500, V Loss: 3023.6824, Q Loss: 29756.0121
[IQL] Epoch 298/500, V Loss: 2957.3042, Q Loss: 29421.2738
[IQL] Epoch 299/500, V Loss: 3255.0114, Q Loss: 30104.8745
[IQL] Epoch 300/500, V Loss: 3336.4835, Q Loss: 29147.7103
[IQL] Epoch 301/500, V Loss: 3679.4322, Q Loss: 30440.0549
[IQL] Epoch 302/500, V Loss: 3471.2265, Q Loss: 32338.5603
[IQL] Epoch 303/500, V Loss: 3477.7503, Q Loss: 29233.1228
[IQL] Epoch 304/500, V Loss: 4364.9583, Q Loss: 29606.4529
[IQL] Epoch 305/500, V Loss: 3711.4849, Q Loss: 30037.3076
[IQL] Epoch 306/500, V Loss: 3235.5715, Q Loss: 30905.5464
[IQL] Epoch 307/500, V Loss: 3444.7771, Q Loss: 30803.6400
[IQL] Epoch 308/500, V Loss: 2924.1519, Q Loss: 30589.1725
[IQL] Epoch 309/500, V Loss: 3298.0812, Q Loss: 29926.8164
[IQL] Epoch 310/500, V Loss: 3964.5157, Q Loss: 30264.3626
[IQL] Epoch 311/500, V Loss: 3614.5623, Q Loss: 30564.1191
[IQL] Epoch 312/500, V Loss: 4349.7848, Q Loss: 29821.8038
[IQL] Epoch 313/500, V Loss: 3646.4003, Q Loss: 29831.0893
[IQL] Epoch 314/500, V Loss: 3272.7589, Q Loss: 28758.8405
[IQL] Epoch 315/500, V Loss: 3509.4418, Q Loss: 28073.6632
[IQL] Epoch 316/500, V Loss: 4146.0441, Q Loss: 29643.8775
[IQL] Epoch 317/500, V Loss: 3852.1717, Q Loss: 28475.6643
[IQL] Epoch 318/500, V Loss: 3601.0646, Q Loss: 29524.6714
[IQL] Epoch 319/500, V Loss: 3517.8401, Q Loss: 29967.4596
[IQL] Epoch 320/500, V Loss: 4093.6760, Q Loss: 30156.7393
[IQL] Epoch 321/500, V Loss: 3647.2560, Q Loss: 28720.1411
[IQL] Epoch 322/500, V Loss: 3922.4523, Q Loss: 28901.3146
[IQL] Epoch 323/500, V Loss: 3812.2371, Q Loss: 28775.8722
[IQL] Epoch 324/500, V Loss: 4022.2307, Q Loss: 28615.8316
[IQL] Epoch 325/500, V Loss: 3666.7336, Q Loss: 28993.7206
[IQL] Epoch 326/500, V Loss: 3366.2858, Q Loss: 28723.3076
[IQL] Epoch 327/500, V Loss: 4342.8347, Q Loss: 28118.7557
[IQL] Epoch 328/500, V Loss: 3853.2662, Q Loss: 28731.9081
[IQL] Epoch 329/500, V Loss: 3654.1897, Q Loss: 28282.7421
[IQL] Epoch 330/500, V Loss: 4065.2583, Q Loss: 29223.9496
[IQL] Epoch 331/500, V Loss: 3924.4332, Q Loss: 28765.0651
[IQL] Epoch 332/500, V Loss: 3943.9110, Q Loss: 29693.5448
[IQL] Epoch 333/500, V Loss: 4192.0978, Q Loss: 30378.1716
[IQL] Epoch 334/500, V Loss: 3309.2009, Q Loss: 30451.7424
[IQL] Epoch 335/500, V Loss: 3767.4502, Q Loss: 29542.1040
[IQL] Epoch 336/500, V Loss: 3635.0255, Q Loss: 29104.8583
[IQL] Epoch 337/500, V Loss: 3757.9578, Q Loss: 28960.9562
[IQL] Epoch 338/500, V Loss: 3949.2557, Q Loss: 29446.2164
[IQL] Epoch 339/500, V Loss: 3458.9269, Q Loss: 28299.9207
[IQL] Epoch 340/500, V Loss: 3763.9068, Q Loss: 29398.9942
[IQL] Epoch 341/500, V Loss: 3741.8323, Q Loss: 31131.8370
[IQL] Epoch 342/500, V Loss: 3920.1921, Q Loss: 30307.9816
[IQL] Epoch 343/500, V Loss: 3685.0657, Q Loss: 28349.9268
[IQL] Epoch 344/500, V Loss: 3383.3253, Q Loss: 29603.4660
[IQL] Epoch 345/500, V Loss: 3502.6692, Q Loss: 29052.6771
[IQL] Epoch 346/500, V Loss: 3629.3618, Q Loss: 29840.8458
[IQL] Epoch 347/500, V Loss: 3583.0617, Q Loss: 29260.4701
[IQL] Epoch 348/500, V Loss: 3747.3568, Q Loss: 29916.7283
[IQL] Epoch 349/500, V Loss: 4665.5839, Q Loss: 29943.9503
[IQL] Epoch 350/500, V Loss: 4837.2710, Q Loss: 28875.2029
[IQL] Epoch 351/500, V Loss: 4008.7275, Q Loss: 30091.7035
[IQL] Epoch 352/500, V Loss: 4072.3317, Q Loss: 30611.8773
[IQL] Epoch 353/500, V Loss: 4071.8134, Q Loss: 29370.4056
[IQL] Epoch 354/500, V Loss: 4049.5315, Q Loss: 31107.7061
[IQL] Epoch 355/500, V Loss: 4669.9246, Q Loss: 30553.9310
[IQL] Epoch 356/500, V Loss: 4532.6260, Q Loss: 32735.7228
[IQL] Epoch 357/500, V Loss: 4130.1191, Q Loss: 28443.1805
[IQL] Epoch 358/500, V Loss: 4084.4111, Q Loss: 27980.6017
[IQL] Epoch 359/500, V Loss: 3992.5085, Q Loss: 28335.3947
[IQL] Epoch 360/500, V Loss: 4263.7666, Q Loss: 29358.7074
[IQL] Epoch 361/500, V Loss: 5101.3975, Q Loss: 30034.4553
[IQL] Epoch 362/500, V Loss: 4576.6200, Q Loss: 30409.6839
[IQL] Epoch 363/500, V Loss: 4013.5634, Q Loss: 30064.8980
[IQL] Epoch 364/500, V Loss: 5428.7817, Q Loss: 29922.3536
[IQL] Epoch 365/500, V Loss: 3897.9932, Q Loss: 28663.9383
[IQL] Epoch 366/500, V Loss: 4680.2100, Q Loss: 29009.7915
[IQL] Epoch 367/500, V Loss: 4007.4527, Q Loss: 30627.6156
[IQL] Epoch 368/500, V Loss: 3951.8042, Q Loss: 28155.3992
[IQL] Epoch 369/500, V Loss: 4086.7511, Q Loss: 27042.9348
[IQL] Epoch 370/500, V Loss: 4481.2015, Q Loss: 29822.6243
[IQL] Epoch 371/500, V Loss: 4002.7280, Q Loss: 29520.9771
[IQL] Epoch 372/500, V Loss: 4313.0821, Q Loss: 29280.7540
[IQL] Epoch 373/500, V Loss: 3997.1888, Q Loss: 29724.7607
[IQL] Epoch 374/500, V Loss: 4593.6642, Q Loss: 29618.7591
[IQL] Epoch 375/500, V Loss: 4942.6382, Q Loss: 29498.1121
[IQL] Epoch 376/500, V Loss: 4304.4339, Q Loss: 28837.0312
[IQL] Epoch 377/500, V Loss: 4379.7993, Q Loss: 29040.6194
[IQL] Epoch 378/500, V Loss: 4820.4191, Q Loss: 30746.4987
[IQL] Epoch 379/500, V Loss: 5230.0516, Q Loss: 29336.8284
[IQL] Epoch 380/500, V Loss: 4436.9475, Q Loss: 29843.2098
[IQL] Epoch 381/500, V Loss: 3935.7472, Q Loss: 29197.2663
[IQL] Epoch 382/500, V Loss: 4538.1496, Q Loss: 28706.0249
[IQL] Epoch 383/500, V Loss: 4465.4021, Q Loss: 28883.1224
[IQL] Epoch 384/500, V Loss: 4159.2741, Q Loss: 30408.8608
[IQL] Epoch 385/500, V Loss: 4246.3829, Q Loss: 29467.4948
[IQL] Epoch 386/500, V Loss: 4131.8052, Q Loss: 27173.8296
[IQL] Epoch 387/500, V Loss: 4553.6656, Q Loss: 28625.0026
[IQL] Epoch 388/500, V Loss: 4050.7280, Q Loss: 27457.0540
[IQL] Epoch 389/500, V Loss: 4509.1219, Q Loss: 28442.1993
[IQL] Epoch 390/500, V Loss: 4458.7154, Q Loss: 29031.5376
[IQL] Epoch 391/500, V Loss: 5036.2026, Q Loss: 29695.2436
[IQL] Epoch 392/500, V Loss: 4651.6285, Q Loss: 28734.5349
[IQL] Epoch 393/500, V Loss: 5139.3761, Q Loss: 27628.9849
[IQL] Epoch 394/500, V Loss: 5437.3801, Q Loss: 28816.8087
[IQL] Epoch 395/500, V Loss: 4388.7791, Q Loss: 28084.4813
[IQL] Epoch 396/500, V Loss: 4630.3451, Q Loss: 27400.9060
[IQL] Epoch 397/500, V Loss: 4466.3695, Q Loss: 28073.0367
[IQL] Epoch 398/500, V Loss: 3811.1564, Q Loss: 28205.6393
[IQL] Epoch 399/500, V Loss: 5623.3988, Q Loss: 29447.1159
[IQL] Epoch 400/500, V Loss: 4645.7991, Q Loss: 28201.5661
[IQL] Epoch 401/500, V Loss: 4978.6703, Q Loss: 29156.6188
[IQL] Epoch 402/500, V Loss: 4369.4058, Q Loss: 30285.0725
[IQL] Epoch 403/500, V Loss: 4863.8368, Q Loss: 29215.1673
[IQL] Epoch 404/500, V Loss: 5034.9756, Q Loss: 27539.0077
[IQL] Epoch 405/500, V Loss: 4722.7828, Q Loss: 26724.8225
[IQL] Epoch 406/500, V Loss: 4509.5945, Q Loss: 30328.1638
[IQL] Epoch 407/500, V Loss: 4850.9271, Q Loss: 29369.2581
[IQL] Epoch 408/500, V Loss: 4913.4302, Q Loss: 28971.2895
[IQL] Epoch 409/500, V Loss: 4326.7968, Q Loss: 28331.1368
[IQL] Epoch 410/500, V Loss: 4059.8462, Q Loss: 28989.0013
[IQL] Epoch 411/500, V Loss: 4748.1437, Q Loss: 27696.5121
[IQL] Epoch 412/500, V Loss: 4438.7847, Q Loss: 27933.7229
[IQL] Epoch 413/500, V Loss: 4583.6293, Q Loss: 30024.5753
[IQL] Epoch 414/500, V Loss: 4537.1329, Q Loss: 32008.2534
[IQL] Epoch 415/500, V Loss: 4640.0220, Q Loss: 29612.2402
[IQL] Epoch 416/500, V Loss: 4371.1255, Q Loss: 28009.4970
[IQL] Epoch 417/500, V Loss: 4538.6313, Q Loss: 26948.3891
[IQL] Epoch 418/500, V Loss: 4612.1865, Q Loss: 27825.1805
[IQL] Epoch 419/500, V Loss: 4631.8550, Q Loss: 28973.2033
[IQL] Epoch 420/500, V Loss: 5074.7085, Q Loss: 27936.2665
[IQL] Epoch 421/500, V Loss: 5084.2053, Q Loss: 27793.1872
[IQL] Epoch 422/500, V Loss: 4857.0761, Q Loss: 29481.7124
[IQL] Epoch 423/500, V Loss: 4643.0172, Q Loss: 28533.7740
[IQL] Epoch 424/500, V Loss: 5565.8562, Q Loss: 28600.5310
[IQL] Epoch 425/500, V Loss: 5226.8163, Q Loss: 27519.8023
[IQL] Epoch 426/500, V Loss: 4143.9316, Q Loss: 27361.7223
[IQL] Epoch 427/500, V Loss: 4755.1614, Q Loss: 27643.4404
[IQL] Epoch 428/500, V Loss: 4928.6541, Q Loss: 27464.3125
[IQL] Epoch 429/500, V Loss: 4992.0873, Q Loss: 26423.2880
[IQL] Epoch 430/500, V Loss: 4524.3356, Q Loss: 27818.0617
[IQL] Epoch 431/500, V Loss: 4937.3919, Q Loss: 27926.7790
[IQL] Epoch 432/500, V Loss: 4965.6244, Q Loss: 27912.6753
[IQL] Epoch 433/500, V Loss: 5769.4669, Q Loss: 26972.2628
[IQL] Epoch 434/500, V Loss: 5211.8763, Q Loss: 29148.5044
[IQL] Epoch 435/500, V Loss: 5651.2832, Q Loss: 29187.1500
[IQL] Epoch 436/500, V Loss: 6048.6424, Q Loss: 29692.6143
[IQL] Epoch 437/500, V Loss: 4962.0052, Q Loss: 28055.4594
[IQL] Epoch 438/500, V Loss: 4729.3322, Q Loss: 27413.0443
[IQL] Epoch 439/500, V Loss: 4791.8743, Q Loss: 25267.0806
[IQL] Epoch 440/500, V Loss: 5306.0679, Q Loss: 26550.3151
[IQL] Epoch 441/500, V Loss: 4794.7391, Q Loss: 24538.9794
[IQL] Epoch 442/500, V Loss: 4727.2092, Q Loss: 26612.0493
[IQL] Epoch 443/500, V Loss: 4493.9459, Q Loss: 26351.9466
[IQL] Epoch 444/500, V Loss: 4915.4254, Q Loss: 25014.8297
[IQL] Epoch 445/500, V Loss: 4633.4573, Q Loss: 25404.3326
[IQL] Epoch 446/500, V Loss: 5125.9846, Q Loss: 26419.8240
[IQL] Epoch 447/500, V Loss: 4765.5748, Q Loss: 24784.5907
[IQL] Epoch 448/500, V Loss: 4776.6929, Q Loss: 24971.7962
[IQL] Epoch 449/500, V Loss: 4979.4043, Q Loss: 23890.9970
[IQL] Epoch 450/500, V Loss: 4644.8135, Q Loss: 24733.6658
[IQL] Epoch 451/500, V Loss: 4860.6474, Q Loss: 26186.2750
[IQL] Epoch 452/500, V Loss: 6248.0157, Q Loss: 25003.9565
[IQL] Epoch 453/500, V Loss: 5411.0425, Q Loss: 25527.6978
[IQL] Epoch 454/500, V Loss: 5373.5628, Q Loss: 26169.6037
[IQL] Epoch 455/500, V Loss: 5613.7064, Q Loss: 25224.1060
[IQL] Epoch 456/500, V Loss: 4750.1564, Q Loss: 24314.2294
[IQL] Epoch 457/500, V Loss: 5272.4594, Q Loss: 26071.6595
[IQL] Epoch 458/500, V Loss: 4440.3566, Q Loss: 26156.7964
[IQL] Epoch 459/500, V Loss: 4781.6663, Q Loss: 24769.0091
[IQL] Epoch 460/500, V Loss: 5277.8051, Q Loss: 25057.9557
[IQL] Epoch 461/500, V Loss: 4766.2115, Q Loss: 26477.5695
[IQL] Epoch 462/500, V Loss: 6223.9378, Q Loss: 26024.5643
[IQL] Epoch 463/500, V Loss: 5221.9340, Q Loss: 24364.7224
[IQL] Epoch 464/500, V Loss: 5265.8221, Q Loss: 26473.0488
[IQL] Epoch 465/500, V Loss: 5320.4118, Q Loss: 27034.9155
[IQL] Epoch 466/500, V Loss: 5795.6415, Q Loss: 24884.8879
[IQL] Epoch 467/500, V Loss: 4667.9461, Q Loss: 24691.6471
[IQL] Epoch 468/500, V Loss: 4864.1719, Q Loss: 25024.7464
[IQL] Epoch 469/500, V Loss: 4825.0418, Q Loss: 25232.3845
[IQL] Epoch 470/500, V Loss: 4844.8194, Q Loss: 25524.5307
[IQL] Epoch 471/500, V Loss: 5663.9148, Q Loss: 26064.2299
[IQL] Epoch 472/500, V Loss: 5897.4236, Q Loss: 28880.1598
[IQL] Epoch 473/500, V Loss: 5100.9544, Q Loss: 25331.9650
[IQL] Epoch 474/500, V Loss: 5009.4145, Q Loss: 24696.0681
[IQL] Epoch 475/500, V Loss: 5538.3296, Q Loss: 24353.0475
[IQL] Epoch 476/500, V Loss: 5333.4968, Q Loss: 24910.0284
[IQL] Epoch 477/500, V Loss: 5732.4280, Q Loss: 26888.0770
[IQL] Epoch 478/500, V Loss: 5520.0286, Q Loss: 25882.2712
[IQL] Epoch 479/500, V Loss: 5411.1231, Q Loss: 24704.6655
[IQL] Epoch 480/500, V Loss: 4765.2504, Q Loss: 26635.1784
[IQL] Epoch 481/500, V Loss: 5501.0834, Q Loss: 25398.9702
[IQL] Epoch 482/500, V Loss: 6403.9275, Q Loss: 27297.4481
[IQL] Epoch 483/500, V Loss: 5386.3534, Q Loss: 26884.2936
[IQL] Epoch 484/500, V Loss: 5655.5710, Q Loss: 26349.8116
[IQL] Epoch 485/500, V Loss: 6678.1459, Q Loss: 28019.3007
[IQL] Epoch 486/500, V Loss: 5729.6268, Q Loss: 28883.1331
[IQL] Epoch 487/500, V Loss: 5250.9406, Q Loss: 26813.0893
[IQL] Epoch 488/500, V Loss: 5180.6360, Q Loss: 26848.6464
[IQL] Epoch 489/500, V Loss: 5251.0906, Q Loss: 26871.6330
[IQL] Epoch 490/500, V Loss: 5854.0912, Q Loss: 26957.0621
[IQL] Epoch 491/500, V Loss: 5199.7946, Q Loss: 27472.9521
[IQL] Epoch 492/500, V Loss: 5008.0891, Q Loss: 28062.3892
[IQL] Epoch 493/500, V Loss: 5174.8606, Q Loss: 27135.8202
[IQL] Epoch 494/500, V Loss: 5473.7002, Q Loss: 25941.3904
[IQL] Epoch 495/500, V Loss: 5568.3243, Q Loss: 24569.3717
[IQL] Epoch 496/500, V Loss: 5684.0702, Q Loss: 25411.1323
[IQL] Epoch 497/500, V Loss: 6570.1356, Q Loss: 24910.6812
[IQL] Epoch 498/500, V Loss: 5069.1750, Q Loss: 23701.9437
[IQL] Epoch 499/500, V Loss: 4960.8744, Q Loss: 24090.9562
[RL100] VIB betas set to factor=0.1: beta_recon=0.000010, beta_kl=0.000010

[RL100Trainer] Phase 2b: Offline RL Optimization (Iteration 2)
[OPE] Behavior policy value J_old = 844.6563
[Offline RL] Epoch 0/100, PPO Loss: -0.0178, CD Loss: 0.2378
[Offline RL] Epoch 1/100, PPO Loss: -0.0156, CD Loss: 0.1307
[Offline RL] Epoch 2/100, PPO Loss: -0.0170, CD Loss: 0.0998
[Offline RL] Epoch 3/100, PPO Loss: -0.0187, CD Loss: 0.0832
[Offline RL] Epoch 4/100, PPO Loss: -0.0177, CD Loss: 0.0842
[Offline RL] Epoch 5/100, PPO Loss: -0.0175, CD Loss: 0.0902
[Offline RL] Epoch 6/100, PPO Loss: -0.0180, CD Loss: 0.0720
[Offline RL] Epoch 7/100, PPO Loss: -0.0173, CD Loss: 0.0712
[Offline RL] Epoch 8/100, PPO Loss: -0.0162, CD Loss: 0.0676
[Offline RL] Epoch 9/100, PPO Loss: -0.0179, CD Loss: 0.0619
[Offline RL] Epoch 10/100, PPO Loss: -0.0174, CD Loss: 0.0669
[Offline RL] Epoch 11/100, PPO Loss: -0.0163, CD Loss: 0.0623
[Offline RL] Epoch 12/100, PPO Loss: -0.0156, CD Loss: 0.0611
[Offline RL] Epoch 13/100, PPO Loss: -0.0158, CD Loss: 0.0601
[Offline RL] Epoch 14/100, PPO Loss: -0.0151, CD Loss: 0.0665
[Offline RL] Epoch 15/100, PPO Loss: -0.0157, CD Loss: 0.0711
[Offline RL] Epoch 16/100, PPO Loss: -0.0158, CD Loss: 0.0791
[Offline RL] Epoch 17/100, PPO Loss: -0.0163, CD Loss: 0.0839
[Offline RL] Epoch 18/100, PPO Loss: -0.0163, CD Loss: 0.0822
[Offline RL] Epoch 19/100, PPO Loss: -0.0156, CD Loss: 0.0886
[Offline RL] Epoch 20/100, PPO Loss: -0.0166, CD Loss: 0.0909
[Offline RL] Epoch 21/100, PPO Loss: -0.0186, CD Loss: 0.0873
[Offline RL] Epoch 22/100, PPO Loss: -0.0191, CD Loss: 0.0843
[Offline RL] Epoch 23/100, PPO Loss: -0.0189, CD Loss: 0.0914
[Offline RL] Epoch 24/100, PPO Loss: -0.0187, CD Loss: 0.0969
[Offline RL] Epoch 25/100, PPO Loss: -0.0178, CD Loss: 0.0964
[Offline RL] Epoch 26/100, PPO Loss: -0.0184, CD Loss: 0.0954
[Offline RL] Epoch 27/100, PPO Loss: -0.0180, CD Loss: 0.1025
[Offline RL] Epoch 28/100, PPO Loss: -0.0195, CD Loss: 0.1100
[Offline RL] Epoch 29/100, PPO Loss: -0.0187, CD Loss: 0.1077
[Offline RL] Epoch 30/100, PPO Loss: -0.0203, CD Loss: 0.1020
[Offline RL] Epoch 31/100, PPO Loss: -0.0212, CD Loss: 0.0946
[Offline RL] Epoch 32/100, PPO Loss: -0.0218, CD Loss: 0.0971
[Offline RL] Epoch 33/100, PPO Loss: -0.0210, CD Loss: 0.0999
[Offline RL] Epoch 34/100, PPO Loss: -0.0214, CD Loss: 0.1057
[Offline RL] Epoch 35/100, PPO Loss: -0.0206, CD Loss: 0.1154
[Offline RL] Epoch 36/100, PPO Loss: -0.0197, CD Loss: 0.1186
[Offline RL] Epoch 37/100, PPO Loss: -0.0213, CD Loss: 0.1045
[Offline RL] Epoch 38/100, PPO Loss: -0.0202, CD Loss: 0.1076
[Offline RL] Epoch 39/100, PPO Loss: -0.0177, CD Loss: 0.1040
[Offline RL] Epoch 40/100, PPO Loss: -0.0181, CD Loss: 0.0953
[Offline RL] Epoch 41/100, PPO Loss: -0.0188, CD Loss: 0.0919
[Offline RL] Epoch 42/100, PPO Loss: -0.0186, CD Loss: 0.1022
[Offline RL] Epoch 43/100, PPO Loss: -0.0198, CD Loss: 0.1063
[Offline RL] Epoch 44/100, PPO Loss: -0.0183, CD Loss: 0.1095
[Offline RL] Epoch 45/100, PPO Loss: -0.0186, CD Loss: 0.1105
[Offline RL] Epoch 46/100, PPO Loss: -0.0172, CD Loss: 0.1080
[Offline RL] Epoch 47/100, PPO Loss: -0.0170, CD Loss: 0.1015
[Offline RL] Epoch 48/100, PPO Loss: -0.0155, CD Loss: 0.0921
[Offline RL] Epoch 49/100, PPO Loss: -0.0164, CD Loss: 0.1082
[Offline RL] Epoch 50/100, PPO Loss: -0.0160, CD Loss: 0.1100
[Offline RL] Epoch 51/100, PPO Loss: -0.0154, CD Loss: 0.1135
[Offline RL] Epoch 52/100, PPO Loss: -0.0156, CD Loss: 0.1097
[Offline RL] Epoch 53/100, PPO Loss: -0.0156, CD Loss: 0.1056
[Offline RL] Epoch 54/100, PPO Loss: -0.0165, CD Loss: 0.0956
[Offline RL] Epoch 55/100, PPO Loss: -0.0164, CD Loss: 0.1249
[Offline RL] Epoch 56/100, PPO Loss: -0.0180, CD Loss: 0.1214
[Offline RL] Epoch 57/100, PPO Loss: -0.0166, CD Loss: 0.1334
[Offline RL] Epoch 58/100, PPO Loss: -0.0179, CD Loss: 0.1391
[Offline RL] Epoch 59/100, PPO Loss: -0.0178, CD Loss: 0.1303
[Offline RL] Epoch 60/100, PPO Loss: -0.0172, CD Loss: 0.1379
[Offline RL] Epoch 61/100, PPO Loss: -0.0172, CD Loss: 0.1338
[Offline RL] Epoch 62/100, PPO Loss: -0.0163, CD Loss: 0.1330
[Offline RL] Epoch 63/100, PPO Loss: -0.0155, CD Loss: 0.1285
[Offline RL] Epoch 64/100, PPO Loss: -0.0150, CD Loss: 0.1302
[Offline RL] Epoch 65/100, PPO Loss: -0.0143, CD Loss: 0.1380
[Offline RL] Epoch 66/100, PPO Loss: -0.0155, CD Loss: 0.1365
[Offline RL] Epoch 67/100, PPO Loss: -0.0152, CD Loss: 0.1365
[Offline RL] Epoch 68/100, PPO Loss: -0.0142, CD Loss: 0.1426
[Offline RL] Epoch 69/100, PPO Loss: -0.0158, CD Loss: 0.1495
[Offline RL] Epoch 70/100, PPO Loss: -0.0164, CD Loss: 0.1444
[Offline RL] Epoch 71/100, PPO Loss: -0.0174, CD Loss: 0.1458
[Offline RL] Epoch 72/100, PPO Loss: -0.0152, CD Loss: 0.1511
[Offline RL] Epoch 73/100, PPO Loss: -0.0154, CD Loss: 0.1503
[Offline RL] Epoch 74/100, PPO Loss: -0.0149, CD Loss: 0.1516
[Offline RL] Epoch 75/100, PPO Loss: -0.0164, CD Loss: 0.1539
[Offline RL] Epoch 76/100, PPO Loss: -0.0166, CD Loss: 0.1586
[Offline RL] Epoch 77/100, PPO Loss: -0.0166, CD Loss: 0.1561
[Offline RL] Epoch 78/100, PPO Loss: -0.0159, CD Loss: 0.1573
[Offline RL] Epoch 79/100, PPO Loss: -0.0168, CD Loss: 0.1582
[Offline RL] Epoch 80/100, PPO Loss: -0.0172, CD Loss: 0.1611
[Offline RL] Epoch 81/100, PPO Loss: -0.0173, CD Loss: 0.1578
[Offline RL] Epoch 82/100, PPO Loss: -0.0162, CD Loss: 0.1608
[Offline RL] Epoch 83/100, PPO Loss: -0.0180, CD Loss: 0.1572
[Offline RL] Epoch 84/100, PPO Loss: -0.0160, CD Loss: 0.1607
[Offline RL] Epoch 85/100, PPO Loss: -0.0165, CD Loss: 0.1648
[Offline RL] Epoch 86/100, PPO Loss: -0.0195, CD Loss: 0.1583
[Offline RL] Epoch 87/100, PPO Loss: -0.0166, CD Loss: 0.1574
[Offline RL] Epoch 88/100, PPO Loss: -0.0190, CD Loss: 0.1574
[Offline RL] Epoch 89/100, PPO Loss: -0.0189, CD Loss: 0.1613
[Offline RL] Epoch 90/100, PPO Loss: -0.0199, CD Loss: 0.1734
[Offline RL] Epoch 91/100, PPO Loss: -0.0194, CD Loss: 0.1768
[Offline RL] Epoch 92/100, PPO Loss: -0.0197, CD Loss: 0.1752
[Offline RL] Epoch 93/100, PPO Loss: -0.0188, CD Loss: 0.1773
[Offline RL] Epoch 94/100, PPO Loss: -0.0198, CD Loss: 0.1771
[Offline RL] Epoch 95/100, PPO Loss: -0.0209, CD Loss: 0.1763
[Offline RL] Epoch 96/100, PPO Loss: -0.0205, CD Loss: 0.1813
[Offline RL] Epoch 97/100, PPO Loss: -0.0220, CD Loss: 0.1735
[Offline RL] Epoch 98/100, PPO Loss: -0.0204, CD Loss: 0.1773
[Offline RL] Epoch 99/100, PPO Loss: -0.0219, CD Loss: 0.1791
[OPE] Policy REJECTED: J_new=737.5352 ≤ J_old=844.6563 + δ=42.2328. Rolling back to behavior policy.

[RL100Trainer] Phase 2c: Collecting New Data (Iteration 2)
[Collect] 50 episodes, success=0.080, steps=1250
[Data Collection] Success Rate: 0.080, Reward: 6439.09, Episodes: 50, Steps: 1250
[Dataset] Merged 50 episodes (1250 steps) → total 5750 steps, 160 episodes
[RL100] VIB betas set to factor=1.0: beta_recon=0.000100, beta_kl=0.000100

[RL100Trainer] Retraining IL on merged dataset...

============================================================
[RL100Trainer] Phase 1: Imitation Learning
============================================================

[IL] Epoch 0/100, Loss: 0.1062
[IL] Epoch 1/100, Loss: 0.0981
[IL] Epoch 2/100, Loss: 0.0976
[IL] Epoch 3/100, Loss: 0.0963
[IL] Epoch 4/100, Loss: 0.0971
[IL] Epoch 5/100, Loss: 0.0950
[IL] Epoch 6/100, Loss: 0.0936
[IL] Epoch 7/100, Loss: 0.0929
[IL] Epoch 8/100, Loss: 0.0965
[IL] Epoch 9/100, Loss: 0.0951
[IL] Epoch 10/100, Loss: 0.0935
[IL] Epoch 11/100, Loss: 0.0942
[IL] Epoch 12/100, Loss: 0.0953
[IL] Epoch 13/100, Loss: 0.0944
[IL] Epoch 14/100, Loss: 0.0946
[IL] Epoch 15/100, Loss: 0.0974
[IL] Epoch 16/100, Loss: 0.0909
[IL] Epoch 17/100, Loss: 0.0952
[IL] Epoch 18/100, Loss: 0.0898
[IL] Epoch 19/100, Loss: 0.0952
[IL] Epoch 20/100, Loss: 0.0921
[IL] Epoch 21/100, Loss: 0.0904
[IL] Epoch 22/100, Loss: 0.0945
[IL] Epoch 23/100, Loss: 0.0942
[IL] Epoch 24/100, Loss: 0.0929
[IL] Epoch 25/100, Loss: 0.0918
[IL] Epoch 26/100, Loss: 0.0925
[IL] Epoch 27/100, Loss: 0.0949
[IL] Epoch 28/100, Loss: 0.0895
[IL] Epoch 29/100, Loss: 0.0966
[IL] Epoch 30/100, Loss: 0.0882
[IL] Epoch 31/100, Loss: 0.0898
[IL] Epoch 32/100, Loss: 0.0923
[IL] Epoch 33/100, Loss: 0.0872
[IL] Epoch 34/100, Loss: 0.0932
[IL] Epoch 35/100, Loss: 0.0900
[IL] Epoch 36/100, Loss: 0.0886
[IL] Epoch 37/100, Loss: 0.0937
[IL] Epoch 38/100, Loss: 0.0967
[IL] Epoch 39/100, Loss: 0.0936
[IL] Epoch 40/100, Loss: 0.0898
[IL] Epoch 41/100, Loss: 0.0909
[IL] Epoch 42/100, Loss: 0.0922
[IL] Epoch 43/100, Loss: 0.0920
[IL] Epoch 44/100, Loss: 0.0897
[IL] Epoch 45/100, Loss: 0.0946
[IL] Epoch 46/100, Loss: 0.0859
[IL] Epoch 47/100, Loss: 0.0911
[IL] Epoch 48/100, Loss: 0.0925
[IL] Epoch 49/100, Loss: 0.0875
[IL] Epoch 50/100, Loss: 0.0919
[IL] Epoch 51/100, Loss: 0.0911
[IL] Epoch 52/100, Loss: 0.0853
[IL] Epoch 53/100, Loss: 0.0934
[IL] Epoch 54/100, Loss: 0.0886
[IL] Epoch 55/100, Loss: 0.0946
[IL] Epoch 56/100, Loss: 0.0855
[IL] Epoch 57/100, Loss: 0.0926
[IL] Epoch 58/100, Loss: 0.0924
[IL] Epoch 59/100, Loss: 0.0900
[IL] Epoch 60/100, Loss: 0.0880
[IL] Epoch 61/100, Loss: 0.0948
[IL] Epoch 62/100, Loss: 0.0914
[IL] Epoch 63/100, Loss: 0.0918
[IL] Epoch 64/100, Loss: 0.0884
[IL] Epoch 65/100, Loss: 0.0901
[IL] Epoch 66/100, Loss: 0.0892
[IL] Epoch 67/100, Loss: 0.0886
[IL] Epoch 68/100, Loss: 0.0880
[IL] Epoch 69/100, Loss: 0.0855
[IL] Epoch 70/100, Loss: 0.0920
[IL] Epoch 71/100, Loss: 0.0827
[IL] Epoch 72/100, Loss: 0.0862
[IL] Epoch 73/100, Loss: 0.0910
[IL] Epoch 74/100, Loss: 0.0887
[IL] Epoch 75/100, Loss: 0.0843
[IL] Epoch 76/100, Loss: 0.0839
[IL] Epoch 77/100, Loss: 0.0879
[IL] Epoch 78/100, Loss: 0.0890
[IL] Epoch 79/100, Loss: 0.0857
[IL] Epoch 80/100, Loss: 0.0846
[IL] Epoch 81/100, Loss: 0.0857
[IL] Epoch 82/100, Loss: 0.0909
[IL] Epoch 83/100, Loss: 0.0864
[IL] Epoch 84/100, Loss: 0.0889
[IL] Epoch 85/100, Loss: 0.0875
[IL] Epoch 86/100, Loss: 0.0897
[IL] Epoch 87/100, Loss: 0.0859
[IL] Epoch 88/100, Loss: 0.0912
[IL] Epoch 89/100, Loss: 0.0895
[IL] Epoch 90/100, Loss: 0.0854
[IL] Epoch 91/100, Loss: 0.0887
[IL] Epoch 92/100, Loss: 0.0862
[IL] Epoch 93/100, Loss: 0.0869
[IL] Epoch 94/100, Loss: 0.0851
[IL] Epoch 95/100, Loss: 0.0843
[IL] Epoch 96/100, Loss: 0.0836
[IL] Epoch 97/100, Loss: 0.0905
[IL] Epoch 98/100, Loss: 0.0862
[IL] Epoch 99/100, Loss: 0.0877
test_mean_score: 0.35
[IL] Eval - Success Rate: 0.350
[Checkpoint] Saved to /nfs_global/S/yangrongzheng/RL100/3D-Diffusion-Policy/3D-Diffusion-Policy/checkpoints/offline_iter_2.ckpt

================================================================================
               OFFLINE RL ITERATION 4/5
================================================================================


[RL100Trainer] Line 6 — Training Transition Model T_θ (Iteration 3)

[TransitionModel] Encoding dataset for transition model training...
[TransitionModel] Dataset: 4630 samples, input_dim=260, target_dim=257
[TransitionModel] Epoch    0 | train=6633.90811 | val=4071.53120 | no-improve=0/5
[TransitionModel] Epoch   20 | train=3222.21204 | val=1923.32463 | no-improve=0/5
[TransitionModel] Epoch   40 | train=965.54787 | val=1792.49209 | no-improve=0/5
[TransitionModel] Epoch   60 | train=653.01963 | val=1667.62576 | no-improve=0/5
[TransitionModel] Epoch   80 | train=469.77449 | val=1617.05366 | no-improve=2/5
[TransitionModel] Epoch   83 | train=447.18313 | val=1641.96487 | no-improve=5/5
[TransitionModel] Training complete. Elites=[5, 6, 3, 4, 1], val_loss=1593.11982

[RL100Trainer] Phase 2a: Training IQL Critics (Iteration 3)
[IQL] Epoch 0/500, V Loss: 65097.0736, Q Loss: 463704.0411
[IQL] Epoch 1/500, V Loss: 18310.6134, Q Loss: 229597.0633
[IQL] Epoch 2/500, V Loss: 17950.1797, Q Loss: 172804.7558
[IQL] Epoch 3/500, V Loss: 14140.6347, Q Loss: 141680.6949
[IQL] Epoch 4/500, V Loss: 11053.9731, Q Loss: 115792.8314
[IQL] Epoch 5/500, V Loss: 9142.3894, Q Loss: 101741.6143
[IQL] Epoch 6/500, V Loss: 8878.3844, Q Loss: 85693.3923
[IQL] Epoch 7/500, V Loss: 8399.5999, Q Loss: 75596.7946
[IQL] Epoch 8/500, V Loss: 7585.0589, Q Loss: 69377.5884
[IQL] Epoch 9/500, V Loss: 7774.4475, Q Loss: 64626.3616
[IQL] Epoch 10/500, V Loss: 8152.2162, Q Loss: 60689.3697
[IQL] Epoch 11/500, V Loss: 7486.2473, Q Loss: 54817.2416
[IQL] Epoch 12/500, V Loss: 7461.6357, Q Loss: 51601.9570
[IQL] Epoch 13/500, V Loss: 6483.9096, Q Loss: 48145.9221
[IQL] Epoch 14/500, V Loss: 6707.1926, Q Loss: 47898.1850
[IQL] Epoch 15/500, V Loss: 6990.4870, Q Loss: 43334.3831
[IQL] Epoch 16/500, V Loss: 6411.9195, Q Loss: 42419.9260
[IQL] Epoch 17/500, V Loss: 6501.1837, Q Loss: 40368.6683
[IQL] Epoch 18/500, V Loss: 6291.5982, Q Loss: 39109.9573
[IQL] Epoch 19/500, V Loss: 5635.8293, Q Loss: 36023.3809
[IQL] Epoch 20/500, V Loss: 6334.6041, Q Loss: 37926.0258
[IQL] Epoch 21/500, V Loss: 6799.5339, Q Loss: 34281.7580
[IQL] Epoch 22/500, V Loss: 5724.1160, Q Loss: 35208.8526
[IQL] Epoch 23/500, V Loss: 5711.7863, Q Loss: 33103.8336
[IQL] Epoch 24/500, V Loss: 6750.7455, Q Loss: 36068.1495
[IQL] Epoch 25/500, V Loss: 5161.5839, Q Loss: 40553.7975
[IQL] Epoch 26/500, V Loss: 5866.4375, Q Loss: 33292.2855
[IQL] Epoch 27/500, V Loss: 5872.8908, Q Loss: 32583.7851
[IQL] Epoch 28/500, V Loss: 6620.0756, Q Loss: 37012.7931
[IQL] Epoch 29/500, V Loss: 5278.4541, Q Loss: 32563.8046
[IQL] Epoch 30/500, V Loss: 5298.9054, Q Loss: 31905.7015
[IQL] Epoch 31/500, V Loss: 5404.2607, Q Loss: 30830.6731
[IQL] Epoch 32/500, V Loss: 5187.3412, Q Loss: 33902.8408
[IQL] Epoch 33/500, V Loss: 5396.2031, Q Loss: 31577.2551
[IQL] Epoch 34/500, V Loss: 5880.6612, Q Loss: 31451.2783
[IQL] Epoch 35/500, V Loss: 5192.9526, Q Loss: 33035.0745
[IQL] Epoch 36/500, V Loss: 5904.0855, Q Loss: 30801.3836
[IQL] Epoch 37/500, V Loss: 5716.8803, Q Loss: 31878.5337
[IQL] Epoch 38/500, V Loss: 6189.6946, Q Loss: 31817.2095
[IQL] Epoch 39/500, V Loss: 5670.1416, Q Loss: 31293.2156
[IQL] Epoch 40/500, V Loss: 7364.9398, Q Loss: 30498.6390
[IQL] Epoch 41/500, V Loss: 5927.7807, Q Loss: 30782.6718
[IQL] Epoch 42/500, V Loss: 6713.5695, Q Loss: 30494.3866
[IQL] Epoch 43/500, V Loss: 5897.1910, Q Loss: 30926.1742
[IQL] Epoch 44/500, V Loss: 5488.3346, Q Loss: 31256.9600
[IQL] Epoch 45/500, V Loss: 5957.9018, Q Loss: 28093.3445
[IQL] Epoch 46/500, V Loss: 6073.2020, Q Loss: 29552.2174
[IQL] Epoch 47/500, V Loss: 6089.6608, Q Loss: 29541.8962
[IQL] Epoch 48/500, V Loss: 5952.1880, Q Loss: 29439.8334
[IQL] Epoch 49/500, V Loss: 5485.3271, Q Loss: 28918.5975
[IQL] Epoch 50/500, V Loss: 6087.4970, Q Loss: 31976.8405
[IQL] Epoch 51/500, V Loss: 5618.0237, Q Loss: 28711.3506
[IQL] Epoch 52/500, V Loss: 6000.8585, Q Loss: 29910.1928
[IQL] Epoch 53/500, V Loss: 6398.6439, Q Loss: 29030.8397
[IQL] Epoch 54/500, V Loss: 6271.9767, Q Loss: 31953.6459
[IQL] Epoch 55/500, V Loss: 6395.3709, Q Loss: 27167.0017
[IQL] Epoch 56/500, V Loss: 6118.4496, Q Loss: 29124.5214
[IQL] Epoch 57/500, V Loss: 5895.5609, Q Loss: 28085.9564
[IQL] Epoch 58/500, V Loss: 5793.5924, Q Loss: 28535.5178
[IQL] Epoch 59/500, V Loss: 6008.9470, Q Loss: 32284.1436
[IQL] Epoch 60/500, V Loss: 6344.8933, Q Loss: 29612.3463
[IQL] Epoch 61/500, V Loss: 6621.4841, Q Loss: 29249.6901
[IQL] Epoch 62/500, V Loss: 6109.1720, Q Loss: 29949.9307
[IQL] Epoch 63/500, V Loss: 6649.7319, Q Loss: 29078.5849
[IQL] Epoch 64/500, V Loss: 6453.8803, Q Loss: 28502.2134
[IQL] Epoch 65/500, V Loss: 6521.0353, Q Loss: 33926.1585
[IQL] Epoch 66/500, V Loss: 5976.1276, Q Loss: 28651.3130
[IQL] Epoch 67/500, V Loss: 6208.8184, Q Loss: 27543.2230
[IQL] Epoch 68/500, V Loss: 6569.6247, Q Loss: 30083.0163
[IQL] Epoch 69/500, V Loss: 6411.6240, Q Loss: 29885.6511
[IQL] Epoch 70/500, V Loss: 6011.8183, Q Loss: 29470.4474
[IQL] Epoch 71/500, V Loss: 7342.1339, Q Loss: 30301.5502
[IQL] Epoch 72/500, V Loss: 6446.4597, Q Loss: 29855.6477
[IQL] Epoch 73/500, V Loss: 6276.1910, Q Loss: 29566.2121
[IQL] Epoch 74/500, V Loss: 6602.4802, Q Loss: 29366.0233
[IQL] Epoch 75/500, V Loss: 7774.9561, Q Loss: 30735.8769
[IQL] Epoch 76/500, V Loss: 7157.1434, Q Loss: 30060.3517
[IQL] Epoch 77/500, V Loss: 7364.0972, Q Loss: 29004.2705
[IQL] Epoch 78/500, V Loss: 6542.7612, Q Loss: 27982.5987
[IQL] Epoch 79/500, V Loss: 6703.8913, Q Loss: 28764.0985
[IQL] Epoch 80/500, V Loss: 6568.8411, Q Loss: 29384.6945
[IQL] Epoch 81/500, V Loss: 6452.5251, Q Loss: 27122.9499
[IQL] Epoch 82/500, V Loss: 7030.6706, Q Loss: 28318.4895
[IQL] Epoch 83/500, V Loss: 7713.6000, Q Loss: 29946.1674
[IQL] Epoch 84/500, V Loss: 7789.2294, Q Loss: 28637.1521
[IQL] Epoch 85/500, V Loss: 6854.3811, Q Loss: 29351.0267
[IQL] Epoch 86/500, V Loss: 6928.7751, Q Loss: 29243.2677
[IQL] Epoch 87/500, V Loss: 7841.2207, Q Loss: 29965.7878
[IQL] Epoch 88/500, V Loss: 7317.2331, Q Loss: 30378.0438
[IQL] Epoch 89/500, V Loss: 7110.4626, Q Loss: 29867.5067
[IQL] Epoch 90/500, V Loss: 7083.9579, Q Loss: 30828.0739
[IQL] Epoch 91/500, V Loss: 7265.7132, Q Loss: 28635.8048
[IQL] Epoch 92/500, V Loss: 6812.7079, Q Loss: 31654.4037
[IQL] Epoch 93/500, V Loss: 7233.7250, Q Loss: 29149.2785
[IQL] Epoch 94/500, V Loss: 7389.4469, Q Loss: 29008.7281
[IQL] Epoch 95/500, V Loss: 6381.9410, Q Loss: 28537.3431
[IQL] Epoch 96/500, V Loss: 8248.9504, Q Loss: 29348.9790
[IQL] Epoch 97/500, V Loss: 7346.1730, Q Loss: 27908.4725
[IQL] Epoch 98/500, V Loss: 7677.9635, Q Loss: 28493.0837
[IQL] Epoch 99/500, V Loss: 8221.4739, Q Loss: 30300.4040
[IQL] Epoch 100/500, V Loss: 7435.5189, Q Loss: 28018.1071
[IQL] Epoch 101/500, V Loss: 7449.2160, Q Loss: 28430.3642
[IQL] Epoch 102/500, V Loss: 8521.3132, Q Loss: 27682.4592
[IQL] Epoch 103/500, V Loss: 7624.6160, Q Loss: 29283.2131
[IQL] Epoch 104/500, V Loss: 7033.6446, Q Loss: 29274.1454
[IQL] Epoch 105/500, V Loss: 7795.5245, Q Loss: 27750.5174
[IQL] Epoch 106/500, V Loss: 7389.0445, Q Loss: 28079.6927
[IQL] Epoch 107/500, V Loss: 8032.7354, Q Loss: 29632.9684
[IQL] Epoch 108/500, V Loss: 8093.5568, Q Loss: 27930.2424
[IQL] Epoch 109/500, V Loss: 8080.7726, Q Loss: 28282.0826
[IQL] Epoch 110/500, V Loss: 8668.8412, Q Loss: 29349.0673
[IQL] Epoch 111/500, V Loss: 7891.0494, Q Loss: 28683.9245
[IQL] Epoch 112/500, V Loss: 7853.5767, Q Loss: 27152.1251
[IQL] Epoch 113/500, V Loss: 7764.8752, Q Loss: 28101.3307
[IQL] Epoch 114/500, V Loss: 8138.5397, Q Loss: 38954.7059
[IQL] Epoch 115/500, V Loss: 7369.2178, Q Loss: 29825.7779
[IQL] Epoch 116/500, V Loss: 7717.9321, Q Loss: 28004.2779
[IQL] Epoch 117/500, V Loss: 7690.2670, Q Loss: 29821.4584
[IQL] Epoch 118/500, V Loss: 8740.3465, Q Loss: 29489.2364
[IQL] Epoch 119/500, V Loss: 7867.7413, Q Loss: 28515.3427
[IQL] Epoch 120/500, V Loss: 8139.4540, Q Loss: 28810.2577
[IQL] Epoch 121/500, V Loss: 7977.1626, Q Loss: 29233.3396
[IQL] Epoch 122/500, V Loss: 9115.4723, Q Loss: 29121.1295
[IQL] Epoch 123/500, V Loss: 8896.6430, Q Loss: 29374.2516
[IQL] Epoch 124/500, V Loss: 8204.5815, Q Loss: 26465.7383
[IQL] Epoch 125/500, V Loss: 8491.6786, Q Loss: 27734.5350
[IQL] Epoch 126/500, V Loss: 8335.9406, Q Loss: 27671.0914
[IQL] Epoch 127/500, V Loss: 8218.3955, Q Loss: 28994.7238
[IQL] Epoch 128/500, V Loss: 8745.7451, Q Loss: 31362.7520
[IQL] Epoch 129/500, V Loss: 8506.7283, Q Loss: 28169.6253
[IQL] Epoch 130/500, V Loss: 9942.0738, Q Loss: 32133.7834
[IQL] Epoch 131/500, V Loss: 8740.6478, Q Loss: 29158.8898
[IQL] Epoch 132/500, V Loss: 9242.7636, Q Loss: 30534.7029
[IQL] Epoch 133/500, V Loss: 8990.3887, Q Loss: 29856.9776
[IQL] Epoch 134/500, V Loss: 8394.2746, Q Loss: 29483.5363
[IQL] Epoch 135/500, V Loss: 9804.4859, Q Loss: 31149.0787
[IQL] Epoch 136/500, V Loss: 8894.9030, Q Loss: 28516.7563
[IQL] Epoch 137/500, V Loss: 8413.0291, Q Loss: 27843.2666
[IQL] Epoch 138/500, V Loss: 10115.9516, Q Loss: 29371.0215
[IQL] Epoch 139/500, V Loss: 8400.2525, Q Loss: 30604.9214
[IQL] Epoch 140/500, V Loss: 9178.1457, Q Loss: 31713.3504
[IQL] Epoch 141/500, V Loss: 10369.6550, Q Loss: 27811.4895
[IQL] Epoch 142/500, V Loss: 10533.2894, Q Loss: 30591.0651
[IQL] Epoch 143/500, V Loss: 9039.6622, Q Loss: 27522.2799
[IQL] Epoch 144/500, V Loss: 9060.1810, Q Loss: 26670.4970
[IQL] Epoch 145/500, V Loss: 9668.3367, Q Loss: 31168.6360
[IQL] Epoch 146/500, V Loss: 9162.4787, Q Loss: 30398.7737
[IQL] Epoch 147/500, V Loss: 9419.4220, Q Loss: 34898.8936
[IQL] Epoch 148/500, V Loss: 9614.9836, Q Loss: 29363.7120
[IQL] Epoch 149/500, V Loss: 10162.8699, Q Loss: 30964.0996
[IQL] Epoch 150/500, V Loss: 10449.4057, Q Loss: 30908.2767
[IQL] Epoch 151/500, V Loss: 9737.2953, Q Loss: 28374.2573
[IQL] Epoch 152/500, V Loss: 9392.2213, Q Loss: 29413.4068
[IQL] Epoch 153/500, V Loss: 9367.2365, Q Loss: 28560.2374
[IQL] Epoch 154/500, V Loss: 9995.4638, Q Loss: 29161.6167
[IQL] Epoch 155/500, V Loss: 9395.7498, Q Loss: 29958.0092
[IQL] Epoch 156/500, V Loss: 9617.9130, Q Loss: 29366.1909
[IQL] Epoch 157/500, V Loss: 9977.8909, Q Loss: 28551.8952
[IQL] Epoch 158/500, V Loss: 9356.7737, Q Loss: 27774.6693
[IQL] Epoch 159/500, V Loss: 9456.2328, Q Loss: 29824.3229
[IQL] Epoch 160/500, V Loss: 9797.8925, Q Loss: 28475.5241
[IQL] Epoch 161/500, V Loss: 10726.2193, Q Loss: 29325.2429
[IQL] Epoch 162/500, V Loss: 10941.5531, Q Loss: 28557.1333
[IQL] Epoch 163/500, V Loss: 10540.3977, Q Loss: 29083.3235
[IQL] Epoch 164/500, V Loss: 10223.6631, Q Loss: 28334.5756
[IQL] Epoch 165/500, V Loss: 9765.5665, Q Loss: 27510.1333
[IQL] Epoch 166/500, V Loss: 11612.4348, Q Loss: 31416.9284
[IQL] Epoch 167/500, V Loss: 10239.2967, Q Loss: 27838.9642
[IQL] Epoch 168/500, V Loss: 10182.1636, Q Loss: 26918.6624
[IQL] Epoch 169/500, V Loss: 10939.6934, Q Loss: 28404.9191
[IQL] Epoch 170/500, V Loss: 10694.6213, Q Loss: 28514.5335
[IQL] Epoch 171/500, V Loss: 10461.2674, Q Loss: 29413.3813
[IQL] Epoch 172/500, V Loss: 10062.7182, Q Loss: 28129.9277
[IQL] Epoch 173/500, V Loss: 10068.7932, Q Loss: 29384.7431
[IQL] Epoch 174/500, V Loss: 10486.0877, Q Loss: 29312.7264
[IQL] Epoch 175/500, V Loss: 9998.4342, Q Loss: 27370.2043
[IQL] Epoch 176/500, V Loss: 10893.3894, Q Loss: 33503.2222
[IQL] Epoch 177/500, V Loss: 9781.8211, Q Loss: 27974.9999
[IQL] Epoch 178/500, V Loss: 9389.0441, Q Loss: 28563.7790
[IQL] Epoch 179/500, V Loss: 9831.7007, Q Loss: 28426.0879
[IQL] Epoch 180/500, V Loss: 10626.7155, Q Loss: 29373.1672
[IQL] Epoch 181/500, V Loss: 11413.2572, Q Loss: 32580.6035
[IQL] Epoch 182/500, V Loss: 11063.7539, Q Loss: 31768.1199
[IQL] Epoch 183/500, V Loss: 11373.7623, Q Loss: 32768.2883
[IQL] Epoch 184/500, V Loss: 9463.6126, Q Loss: 28545.1766
[IQL] Epoch 185/500, V Loss: 11274.0600, Q Loss: 29240.7002
[IQL] Epoch 186/500, V Loss: 10094.2453, Q Loss: 29502.8576
[IQL] Epoch 187/500, V Loss: 10139.1148, Q Loss: 28250.8142
[IQL] Epoch 188/500, V Loss: 10431.4785, Q Loss: 31905.8260
[IQL] Epoch 189/500, V Loss: 9300.8704, Q Loss: 28845.6807
[IQL] Epoch 190/500, V Loss: 10568.1791, Q Loss: 28259.2519
[IQL] Epoch 191/500, V Loss: 10809.9888, Q Loss: 31364.2786
[IQL] Epoch 192/500, V Loss: 10292.1595, Q Loss: 28903.3733
[IQL] Epoch 193/500, V Loss: 10484.8211, Q Loss: 30057.7735
[IQL] Epoch 194/500, V Loss: 10672.1805, Q Loss: 28450.0674
[IQL] Epoch 195/500, V Loss: 10627.0945, Q Loss: 28372.2499
[IQL] Epoch 196/500, V Loss: 10757.2662, Q Loss: 29036.4616
[IQL] Epoch 197/500, V Loss: 11278.8291, Q Loss: 29060.5933
[IQL] Epoch 198/500, V Loss: 11232.4011, Q Loss: 29262.2169
[IQL] Epoch 199/500, V Loss: 11289.7361, Q Loss: 29633.0537
[IQL] Epoch 200/500, V Loss: 11044.6322, Q Loss: 33048.2630
[IQL] Epoch 201/500, V Loss: 10718.0341, Q Loss: 29306.8898
[IQL] Epoch 202/500, V Loss: 10692.0584, Q Loss: 28750.4247
[IQL] Epoch 203/500, V Loss: 10552.0124, Q Loss: 29012.3668
[IQL] Epoch 204/500, V Loss: 10611.8521, Q Loss: 29336.7186
[IQL] Epoch 205/500, V Loss: 10513.6879, Q Loss: 29293.1774
[IQL] Epoch 206/500, V Loss: 10995.5583, Q Loss: 29931.1817
[IQL] Epoch 207/500, V Loss: 12101.7707, Q Loss: 32169.1839
[IQL] Epoch 208/500, V Loss: 10481.7719, Q Loss: 32946.9673
[IQL] Epoch 209/500, V Loss: 11392.6698, Q Loss: 29347.4139
[IQL] Epoch 210/500, V Loss: 10346.3840, Q Loss: 31309.6285
[IQL] Epoch 211/500, V Loss: 10571.2526, Q Loss: 29317.8565
[IQL] Epoch 212/500, V Loss: 10617.0730, Q Loss: 29251.9789
[IQL] Epoch 213/500, V Loss: 10175.9350, Q Loss: 28416.3044
[IQL] Epoch 214/500, V Loss: 10831.3086, Q Loss: 26497.4187
[IQL] Epoch 215/500, V Loss: 11404.2543, Q Loss: 29476.1889
[IQL] Epoch 216/500, V Loss: 10924.8066, Q Loss: 30172.9661
[IQL] Epoch 217/500, V Loss: 11275.0219, Q Loss: 33402.5970
[IQL] Epoch 218/500, V Loss: 11361.8224, Q Loss: 28381.7047
[IQL] Epoch 219/500, V Loss: 9548.1337, Q Loss: 28241.6086
[IQL] Epoch 220/500, V Loss: 11557.6626, Q Loss: 27911.7338
[IQL] Epoch 221/500, V Loss: 14959.9708, Q Loss: 31719.1582
[IQL] Epoch 222/500, V Loss: 10826.7791, Q Loss: 29595.4366
[IQL] Epoch 223/500, V Loss: 12491.7671, Q Loss: 29731.2367
[IQL] Epoch 224/500, V Loss: 11094.3141, Q Loss: 29597.1607
[IQL] Epoch 225/500, V Loss: 11834.2281, Q Loss: 30633.4038
[IQL] Epoch 226/500, V Loss: 14113.8577, Q Loss: 31114.1398
[IQL] Epoch 227/500, V Loss: 12739.3010, Q Loss: 31824.7950
[IQL] Epoch 228/500, V Loss: 12347.2753, Q Loss: 28600.1074
[IQL] Epoch 229/500, V Loss: 11424.8252, Q Loss: 29180.6670
[IQL] Epoch 230/500, V Loss: 11381.5905, Q Loss: 28131.5041
[IQL] Epoch 231/500, V Loss: 12008.3812, Q Loss: 28426.7751
[IQL] Epoch 232/500, V Loss: 10583.9917, Q Loss: 28845.1839
[IQL] Epoch 233/500, V Loss: 10864.3000, Q Loss: 27319.8781
[IQL] Epoch 234/500, V Loss: 10910.9231, Q Loss: 29302.0671
[IQL] Epoch 235/500, V Loss: 11869.8384, Q Loss: 28391.2437
[IQL] Epoch 236/500, V Loss: 11302.6646, Q Loss: 28560.6730
[IQL] Epoch 237/500, V Loss: 11184.5608, Q Loss: 32744.4255
[IQL] Epoch 238/500, V Loss: 10771.5502, Q Loss: 34064.4191
[IQL] Epoch 239/500, V Loss: 12538.4999, Q Loss: 29664.0460
[IQL] Epoch 240/500, V Loss: 11002.1607, Q Loss: 30664.0217
[IQL] Epoch 241/500, V Loss: 11378.6067, Q Loss: 31910.9000
[IQL] Epoch 242/500, V Loss: 11485.4072, Q Loss: 29210.8981
[IQL] Epoch 243/500, V Loss: 10980.6453, Q Loss: 28262.1136
[IQL] Epoch 244/500, V Loss: 11527.0511, Q Loss: 29043.2580
[IQL] Epoch 245/500, V Loss: 11930.5969, Q Loss: 30574.4427
[IQL] Epoch 246/500, V Loss: 11433.4868, Q Loss: 31316.3757
[IQL] Epoch 247/500, V Loss: 11377.3213, Q Loss: 29123.7299
[IQL] Epoch 248/500, V Loss: 12117.2170, Q Loss: 32385.5586
[IQL] Epoch 249/500, V Loss: 12728.0833, Q Loss: 33263.0710
[IQL] Epoch 250/500, V Loss: 11734.1242, Q Loss: 29480.8972
[IQL] Epoch 251/500, V Loss: 10781.6653, Q Loss: 29935.8083
[IQL] Epoch 252/500, V Loss: 12146.6852, Q Loss: 30697.8034
[IQL] Epoch 253/500, V Loss: 11388.7216, Q Loss: 30947.6050
[IQL] Epoch 254/500, V Loss: 11133.3262, Q Loss: 27020.0235
[IQL] Epoch 255/500, V Loss: 10819.4936, Q Loss: 28607.2260
[IQL] Epoch 256/500, V Loss: 12002.5666, Q Loss: 32600.1658
[IQL] Epoch 257/500, V Loss: 11724.6285, Q Loss: 29088.2008
[IQL] Epoch 258/500, V Loss: 11230.6157, Q Loss: 30292.7398
[IQL] Epoch 259/500, V Loss: 12397.5520, Q Loss: 35604.0711
[IQL] Epoch 260/500, V Loss: 12218.4604, Q Loss: 29593.7681
[IQL] Epoch 261/500, V Loss: 10889.4134, Q Loss: 29976.5544
[IQL] Epoch 262/500, V Loss: 11644.5251, Q Loss: 32752.0100
[IQL] Epoch 263/500, V Loss: 12084.2257, Q Loss: 30499.8783
[IQL] Epoch 264/500, V Loss: 11435.7357, Q Loss: 28533.6730
[IQL] Epoch 265/500, V Loss: 11909.6306, Q Loss: 31616.9073
[IQL] Epoch 266/500, V Loss: 11962.9790, Q Loss: 29101.2030
[IQL] Epoch 267/500, V Loss: 11966.5073, Q Loss: 29774.1154
[IQL] Epoch 268/500, V Loss: 10824.3722, Q Loss: 29261.6389
[IQL] Epoch 269/500, V Loss: 11361.8047, Q Loss: 28574.3411
[IQL] Epoch 270/500, V Loss: 11347.8998, Q Loss: 29923.8478
[IQL] Epoch 271/500, V Loss: 12507.2546, Q Loss: 29031.1345
[IQL] Epoch 272/500, V Loss: 12789.1860, Q Loss: 28999.1003
[IQL] Epoch 273/500, V Loss: 11096.5790, Q Loss: 28668.1124
[IQL] Epoch 274/500, V Loss: 12109.7726, Q Loss: 30162.3978
[IQL] Epoch 275/500, V Loss: 12523.9441, Q Loss: 30521.3358
[IQL] Epoch 276/500, V Loss: 11364.3466, Q Loss: 29208.0603
[IQL] Epoch 277/500, V Loss: 11484.9036, Q Loss: 32083.8575
[IQL] Epoch 278/500, V Loss: 11292.6120, Q Loss: 30064.7216
[IQL] Epoch 279/500, V Loss: 11907.4691, Q Loss: 30785.9121
[IQL] Epoch 280/500, V Loss: 10733.5693, Q Loss: 28193.6570
[IQL] Epoch 281/500, V Loss: 10917.0207, Q Loss: 30840.4273
[IQL] Epoch 282/500, V Loss: 11758.0634, Q Loss: 33592.8010
[IQL] Epoch 283/500, V Loss: 11963.8144, Q Loss: 29106.3643
[IQL] Epoch 284/500, V Loss: 12029.4796, Q Loss: 29913.7850
[IQL] Epoch 285/500, V Loss: 11401.5469, Q Loss: 31676.4983
[IQL] Epoch 286/500, V Loss: 12258.0304, Q Loss: 29052.1300
[IQL] Epoch 287/500, V Loss: 13076.8408, Q Loss: 35880.3229
[IQL] Epoch 288/500, V Loss: 11990.0288, Q Loss: 31251.7170
[IQL] Epoch 289/500, V Loss: 13129.0411, Q Loss: 32678.2353
[IQL] Epoch 290/500, V Loss: 12048.3401, Q Loss: 30969.4572
[IQL] Epoch 291/500, V Loss: 13777.7648, Q Loss: 31715.6185
[IQL] Epoch 292/500, V Loss: 12627.6545, Q Loss: 34433.8136
[IQL] Epoch 293/500, V Loss: 12018.4397, Q Loss: 31162.6456
[IQL] Epoch 294/500, V Loss: 13607.9842, Q Loss: 32789.2767
[IQL] Epoch 295/500, V Loss: 11407.0375, Q Loss: 29939.9951
[IQL] Epoch 296/500, V Loss: 11381.8606, Q Loss: 33093.6270
[IQL] Epoch 297/500, V Loss: 12541.3268, Q Loss: 29403.5558
[IQL] Epoch 298/500, V Loss: 11220.4135, Q Loss: 32829.8798
[IQL] Epoch 299/500, V Loss: 10919.5492, Q Loss: 32865.3150
[IQL] Epoch 300/500, V Loss: 11610.0787, Q Loss: 31129.6212
[IQL] Epoch 301/500, V Loss: 11824.0802, Q Loss: 30223.4067
[IQL] Epoch 302/500, V Loss: 11669.1185, Q Loss: 31271.4205
[IQL] Epoch 303/500, V Loss: 11896.1207, Q Loss: 33336.9179
[IQL] Epoch 304/500, V Loss: 13428.6952, Q Loss: 35408.9027
[IQL] Epoch 305/500, V Loss: 11330.8350, Q Loss: 30191.7067
[IQL] Epoch 306/500, V Loss: 12007.0733, Q Loss: 31847.9349
[IQL] Epoch 307/500, V Loss: 12928.0995, Q Loss: 30759.7112
[IQL] Epoch 308/500, V Loss: 11704.2309, Q Loss: 34143.6901
[IQL] Epoch 309/500, V Loss: 14418.0422, Q Loss: 31066.1911
[IQL] Epoch 310/500, V Loss: 12419.3622, Q Loss: 30237.5274
[IQL] Epoch 311/500, V Loss: 14119.8170, Q Loss: 31608.0872
[IQL] Epoch 312/500, V Loss: 13003.0127, Q Loss: 32514.9412
[IQL] Epoch 313/500, V Loss: 13288.2638, Q Loss: 29196.6271
[IQL] Epoch 314/500, V Loss: 12895.2493, Q Loss: 30497.2013
[IQL] Epoch 315/500, V Loss: 13344.8881, Q Loss: 32443.0090
[IQL] Epoch 316/500, V Loss: 13078.2193, Q Loss: 29204.6997
[IQL] Epoch 317/500, V Loss: 12461.9884, Q Loss: 34291.7734
[IQL] Epoch 318/500, V Loss: 13577.2966, Q Loss: 32052.8464
[IQL] Epoch 319/500, V Loss: 11300.0770, Q Loss: 37473.6928
[IQL] Epoch 320/500, V Loss: 13763.2961, Q Loss: 33753.6474
[IQL] Epoch 321/500, V Loss: 11882.7685, Q Loss: 33315.1115
[IQL] Epoch 322/500, V Loss: 12504.2888, Q Loss: 34123.2311
[IQL] Epoch 323/500, V Loss: 12693.6889, Q Loss: 32048.9605
[IQL] Epoch 324/500, V Loss: 12017.6296, Q Loss: 31819.5589
[IQL] Epoch 325/500, V Loss: 12113.0928, Q Loss: 30086.9902
[IQL] Epoch 326/500, V Loss: 11655.5153, Q Loss: 34292.7032
[IQL] Epoch 327/500, V Loss: 13168.9575, Q Loss: 47211.5938
[IQL] Epoch 328/500, V Loss: 11602.5916, Q Loss: 28946.0382
[IQL] Epoch 329/500, V Loss: 12152.5548, Q Loss: 31244.5463
[IQL] Epoch 330/500, V Loss: 15212.9569, Q Loss: 32418.1871
[IQL] Epoch 331/500, V Loss: 12721.8997, Q Loss: 32528.0662
[IQL] Epoch 332/500, V Loss: 11125.5371, Q Loss: 31476.5972
[IQL] Epoch 333/500, V Loss: 12064.3274, Q Loss: 31204.2201
[IQL] Epoch 334/500, V Loss: 12301.4426, Q Loss: 31019.7571
[IQL] Epoch 335/500, V Loss: 12949.6794, Q Loss: 30536.0535
[IQL] Epoch 336/500, V Loss: 12652.3485, Q Loss: 29447.7040
[IQL] Epoch 337/500, V Loss: 14008.9255, Q Loss: 30163.5899
[IQL] Epoch 338/500, V Loss: 13343.4773, Q Loss: 29935.6885
[IQL] Epoch 339/500, V Loss: 11763.4594, Q Loss: 32211.6388
[IQL] Epoch 340/500, V Loss: 13554.6787, Q Loss: 32604.3472
[IQL] Epoch 341/500, V Loss: 13242.7917, Q Loss: 30506.2925
[IQL] Epoch 342/500, V Loss: 13834.7117, Q Loss: 30150.3786
[IQL] Epoch 343/500, V Loss: 12300.7130, Q Loss: 32250.9295
[IQL] Epoch 344/500, V Loss: 14624.1482, Q Loss: 32135.7719
[IQL] Epoch 345/500, V Loss: 11901.7470, Q Loss: 34060.1174
[IQL] Epoch 346/500, V Loss: 12023.2391, Q Loss: 30502.6674
[IQL] Epoch 347/500, V Loss: 12492.3956, Q Loss: 30380.2708
[IQL] Epoch 348/500, V Loss: 11444.4399, Q Loss: 29034.6213
[IQL] Epoch 349/500, V Loss: 11929.5043, Q Loss: 28346.8629
[IQL] Epoch 350/500, V Loss: 12636.9677, Q Loss: 30339.5664
[IQL] Epoch 351/500, V Loss: 11629.6277, Q Loss: 27664.4743
[IQL] Epoch 352/500, V Loss: 12194.8847, Q Loss: 30323.2103
[IQL] Epoch 353/500, V Loss: 12691.6935, Q Loss: 33726.8245
[IQL] Epoch 354/500, V Loss: 11874.5012, Q Loss: 33116.6743
[IQL] Epoch 355/500, V Loss: 13172.6783, Q Loss: 33720.3038
[IQL] Epoch 356/500, V Loss: 14249.2388, Q Loss: 37506.4662
[IQL] Epoch 357/500, V Loss: 12007.6597, Q Loss: 29900.3298
[IQL] Epoch 358/500, V Loss: 12859.7833, Q Loss: 30478.6192
[IQL] Epoch 359/500, V Loss: 12714.5031, Q Loss: 29868.8493
[IQL] Epoch 360/500, V Loss: 11524.6762, Q Loss: 30325.1747
[IQL] Epoch 361/500, V Loss: 12496.3926, Q Loss: 28992.4859
[IQL] Epoch 362/500, V Loss: 14207.0740, Q Loss: 29216.7551
[IQL] Epoch 363/500, V Loss: 12621.4479, Q Loss: 29582.3000
[IQL] Epoch 364/500, V Loss: 12376.2306, Q Loss: 30192.7632
[IQL] Epoch 365/500, V Loss: 13385.1153, Q Loss: 33643.4985
[IQL] Epoch 366/500, V Loss: 12520.7201, Q Loss: 29067.1664
[IQL] Epoch 367/500, V Loss: 12761.9708, Q Loss: 29634.6291
[IQL] Epoch 368/500, V Loss: 11286.3438, Q Loss: 32562.6658
[IQL] Epoch 369/500, V Loss: 12859.4672, Q Loss: 32975.5549
[IQL] Epoch 370/500, V Loss: 11832.4935, Q Loss: 30724.9292
[IQL] Epoch 371/500, V Loss: 13483.8795, Q Loss: 26162.5378
[IQL] Epoch 372/500, V Loss: 12724.2983, Q Loss: 29676.5574
[IQL] Epoch 373/500, V Loss: 13784.6107, Q Loss: 37741.4023
[IQL] Epoch 374/500, V Loss: 12409.9627, Q Loss: 27880.1291
[IQL] Epoch 375/500, V Loss: 12306.8383, Q Loss: 31987.5080
[IQL] Epoch 376/500, V Loss: 12959.4679, Q Loss: 29908.2142
[IQL] Epoch 377/500, V Loss: 14075.6838, Q Loss: 32300.3931
[IQL] Epoch 378/500, V Loss: 13490.6567, Q Loss: 27033.6093
[IQL] Epoch 379/500, V Loss: 12731.7343, Q Loss: 29244.0625
[IQL] Epoch 380/500, V Loss: 13677.3792, Q Loss: 30097.1849
[IQL] Epoch 381/500, V Loss: 12164.5325, Q Loss: 29171.9526
[IQL] Epoch 382/500, V Loss: 13084.4370, Q Loss: 28880.7137
[IQL] Epoch 383/500, V Loss: 12397.2212, Q Loss: 29597.7008
[IQL] Epoch 384/500, V Loss: 13129.7933, Q Loss: 28483.0857
[IQL] Epoch 385/500, V Loss: 13186.5207, Q Loss: 28268.0531
[IQL] Epoch 386/500, V Loss: 13308.1137, Q Loss: 27303.5472
[IQL] Epoch 387/500, V Loss: 11281.6068, Q Loss: 25384.7846
[IQL] Epoch 388/500, V Loss: 14237.8411, Q Loss: 28699.7491
[IQL] Epoch 389/500, V Loss: 12852.3457, Q Loss: 32734.3166
[IQL] Epoch 390/500, V Loss: 12153.7624, Q Loss: 33236.1083
[IQL] Epoch 391/500, V Loss: 13692.6769, Q Loss: 27922.2730
[IQL] Epoch 392/500, V Loss: 11606.1968, Q Loss: 33224.0112
[IQL] Epoch 393/500, V Loss: 15075.0599, Q Loss: 30786.1173
[IQL] Epoch 394/500, V Loss: 14276.5958, Q Loss: 33608.1274
[IQL] Epoch 395/500, V Loss: 12386.4914, Q Loss: 32377.1396
[IQL] Epoch 396/500, V Loss: 13814.8282, Q Loss: 32185.0903
[IQL] Epoch 397/500, V Loss: 12048.6986, Q Loss: 30581.7442
[IQL] Epoch 398/500, V Loss: 12939.2071, Q Loss: 29017.5728
[IQL] Epoch 399/500, V Loss: 12086.2680, Q Loss: 33508.0801
[IQL] Epoch 400/500, V Loss: 12224.3306, Q Loss: 30239.0320
[IQL] Epoch 401/500, V Loss: 13187.4425, Q Loss: 33535.0504
[IQL] Epoch 402/500, V Loss: 13726.3485, Q Loss: 31714.6598
[IQL] Epoch 403/500, V Loss: 12840.0761, Q Loss: 30527.4392
[IQL] Epoch 404/500, V Loss: 13281.9562, Q Loss: 32836.3464
[IQL] Epoch 405/500, V Loss: 13697.4177, Q Loss: 29838.4267
[IQL] Epoch 406/500, V Loss: 14085.3828, Q Loss: 29819.9929
[IQL] Epoch 407/500, V Loss: 11327.7199, Q Loss: 28729.9756
[IQL] Epoch 408/500, V Loss: 12848.3652, Q Loss: 30570.4127
[IQL] Epoch 409/500, V Loss: 12513.5678, Q Loss: 29737.1278
[IQL] Epoch 410/500, V Loss: 14749.9648, Q Loss: 41119.0130
[IQL] Epoch 411/500, V Loss: 11654.1810, Q Loss: 28946.7674
[IQL] Epoch 412/500, V Loss: 12272.0082, Q Loss: 28953.9434
[IQL] Epoch 413/500, V Loss: 11157.0440, Q Loss: 29433.8348
[IQL] Epoch 414/500, V Loss: 11710.1286, Q Loss: 27655.8031
[IQL] Epoch 415/500, V Loss: 13189.9409, Q Loss: 28136.4940
[IQL] Epoch 416/500, V Loss: 11891.0961, Q Loss: 27258.5197
[IQL] Epoch 417/500, V Loss: 13764.3392, Q Loss: 27442.9861
[IQL] Epoch 418/500, V Loss: 13167.9627, Q Loss: 31451.1405
[IQL] Epoch 419/500, V Loss: 14207.1903, Q Loss: 33031.4737
[IQL] Epoch 420/500, V Loss: 12860.6890, Q Loss: 32158.1093
[IQL] Epoch 421/500, V Loss: 15915.0308, Q Loss: 29550.5009
[IQL] Epoch 422/500, V Loss: 12910.2130, Q Loss: 27049.8693
[IQL] Epoch 423/500, V Loss: 11714.1259, Q Loss: 27773.3589
[IQL] Epoch 424/500, V Loss: 12805.0193, Q Loss: 36650.0670
[IQL] Epoch 425/500, V Loss: 14266.4644, Q Loss: 33304.6701
[IQL] Epoch 426/500, V Loss: 15617.0807, Q Loss: 30819.0443
[IQL] Epoch 427/500, V Loss: 13686.7998, Q Loss: 30456.6182
[IQL] Epoch 428/500, V Loss: 12518.7731, Q Loss: 28379.6240
[IQL] Epoch 429/500, V Loss: 13044.4284, Q Loss: 29513.4764
[IQL] Epoch 430/500, V Loss: 13735.3961, Q Loss: 30040.0184
[IQL] Epoch 431/500, V Loss: 10688.2879, Q Loss: 28087.9257
[IQL] Epoch 432/500, V Loss: 13830.7234, Q Loss: 28955.3365
[IQL] Epoch 433/500, V Loss: 14186.3758, Q Loss: 32302.9456
[IQL] Epoch 434/500, V Loss: 11549.3467, Q Loss: 33149.2559
[IQL] Epoch 435/500, V Loss: 12767.7794, Q Loss: 28998.7318
[IQL] Epoch 436/500, V Loss: 13983.7217, Q Loss: 30118.0825
[IQL] Epoch 437/500, V Loss: 12313.4463, Q Loss: 29638.1983
[IQL] Epoch 438/500, V Loss: 15232.1780, Q Loss: 30581.3381
[IQL] Epoch 439/500, V Loss: 12532.4004, Q Loss: 31530.5921
[IQL] Epoch 440/500, V Loss: 14868.7544, Q Loss: 30477.2995
[IQL] Epoch 441/500, V Loss: 13318.8732, Q Loss: 30498.3049
[IQL] Epoch 442/500, V Loss: 13427.9290, Q Loss: 28575.3177
[IQL] Epoch 443/500, V Loss: 13855.8763, Q Loss: 31651.3122
[IQL] Epoch 444/500, V Loss: 13087.8891, Q Loss: 29682.0897
[IQL] Epoch 445/500, V Loss: 12421.8113, Q Loss: 26981.4378
[IQL] Epoch 446/500, V Loss: 12405.6613, Q Loss: 28343.3011
[IQL] Epoch 447/500, V Loss: 11351.1875, Q Loss: 27313.4034
[IQL] Epoch 448/500, V Loss: 13890.4938, Q Loss: 30697.2098
[IQL] Epoch 449/500, V Loss: 13409.5120, Q Loss: 28308.7704
[IQL] Epoch 450/500, V Loss: 13468.6913, Q Loss: 31423.0805
[IQL] Epoch 451/500, V Loss: 13723.5374, Q Loss: 28456.9039
[IQL] Epoch 452/500, V Loss: 13453.5864, Q Loss: 45484.8726
[IQL] Epoch 453/500, V Loss: 11490.4249, Q Loss: 27828.5505
[IQL] Epoch 454/500, V Loss: 13299.7376, Q Loss: 27812.4291
[IQL] Epoch 455/500, V Loss: 12865.8279, Q Loss: 28616.7567
[IQL] Epoch 456/500, V Loss: 12119.9335, Q Loss: 26394.4858
[IQL] Epoch 457/500, V Loss: 11696.4474, Q Loss: 25480.1357
[IQL] Epoch 458/500, V Loss: 12793.8625, Q Loss: 25024.3853
[IQL] Epoch 459/500, V Loss: 15190.9895, Q Loss: 31439.5958
[IQL] Epoch 460/500, V Loss: 13101.4092, Q Loss: 30299.5455
[IQL] Epoch 461/500, V Loss: 13104.7305, Q Loss: 30159.7107
[IQL] Epoch 462/500, V Loss: 12696.4930, Q Loss: 32131.9734
[IQL] Epoch 463/500, V Loss: 13445.3500, Q Loss: 34419.7929
[IQL] Epoch 464/500, V Loss: 14221.8978, Q Loss: 36217.2987
[IQL] Epoch 465/500, V Loss: 11978.0073, Q Loss: 26454.1611
[IQL] Epoch 466/500, V Loss: 13764.1692, Q Loss: 32634.4442
[IQL] Epoch 467/500, V Loss: 13712.5299, Q Loss: 30268.0553
[IQL] Epoch 468/500, V Loss: 13982.8449, Q Loss: 28026.5520
[IQL] Epoch 469/500, V Loss: 12728.7461, Q Loss: 28518.5930
[IQL] Epoch 470/500, V Loss: 12456.7292, Q Loss: 27211.3468
[IQL] Epoch 471/500, V Loss: 12342.5656, Q Loss: 27016.7356
[IQL] Epoch 472/500, V Loss: 13263.6381, Q Loss: 28233.1751
[IQL] Epoch 473/500, V Loss: 11399.7703, Q Loss: 25987.9353
[IQL] Epoch 474/500, V Loss: 12644.0646, Q Loss: 30012.5502
[IQL] Epoch 475/500, V Loss: 13401.0314, Q Loss: 25299.4781
[IQL] Epoch 476/500, V Loss: 13559.5145, Q Loss: 27744.9781
[IQL] Epoch 477/500, V Loss: 13895.3325, Q Loss: 26327.2666
[IQL] Epoch 478/500, V Loss: 13775.8826, Q Loss: 29355.4258
[IQL] Epoch 479/500, V Loss: 16413.8608, Q Loss: 35061.1486
[IQL] Epoch 480/500, V Loss: 16165.6904, Q Loss: 31549.8206
[IQL] Epoch 481/500, V Loss: 13681.2121, Q Loss: 26331.9723
[IQL] Epoch 482/500, V Loss: 13820.1301, Q Loss: 30485.2034
[IQL] Epoch 483/500, V Loss: 12961.2092, Q Loss: 31382.0631
[IQL] Epoch 484/500, V Loss: 15083.7900, Q Loss: 32945.8494
[IQL] Epoch 485/500, V Loss: 12636.9534, Q Loss: 30824.5091
[IQL] Epoch 486/500, V Loss: 13885.9938, Q Loss: 29789.6822
[IQL] Epoch 487/500, V Loss: 15128.1289, Q Loss: 29166.0329
[IQL] Epoch 488/500, V Loss: 12746.1019, Q Loss: 27372.5938
[IQL] Epoch 489/500, V Loss: 12210.1716, Q Loss: 28762.3456
[IQL] Epoch 490/500, V Loss: 13793.7174, Q Loss: 27078.5485
[IQL] Epoch 491/500, V Loss: 14795.9550, Q Loss: 31546.0387
[IQL] Epoch 492/500, V Loss: 15066.6979, Q Loss: 31780.0262
[IQL] Epoch 493/500, V Loss: 12791.5590, Q Loss: 27907.1934
[IQL] Epoch 494/500, V Loss: 14183.0496, Q Loss: 32566.2138
[IQL] Epoch 495/500, V Loss: 11994.3009, Q Loss: 31161.1656
[IQL] Epoch 496/500, V Loss: 14394.8290, Q Loss: 31025.6230
[IQL] Epoch 497/500, V Loss: 13866.5927, Q Loss: 30624.9312
[IQL] Epoch 498/500, V Loss: 14157.7715, Q Loss: 28532.4001
[IQL] Epoch 499/500, V Loss: 13034.5984, Q Loss: 28339.0021
[RL100] VIB betas set to factor=0.1: beta_recon=0.000010, beta_kl=0.000010

[RL100Trainer] Phase 2b: Offline RL Optimization (Iteration 3)
[OPE] Behavior policy value J_old = 1327.9185
[Offline RL] Epoch 0/100, PPO Loss: -0.0249, CD Loss: 0.1970
[Offline RL] Epoch 1/100, PPO Loss: -0.0250, CD Loss: 0.1413
[Offline RL] Epoch 2/100, PPO Loss: -0.0226, CD Loss: 0.1183
[Offline RL] Epoch 3/100, PPO Loss: -0.0236, CD Loss: 0.0981
[Offline RL] Epoch 4/100, PPO Loss: -0.0256, CD Loss: 0.1195
[Offline RL] Epoch 5/100, PPO Loss: -0.0239, CD Loss: 0.1251
[Offline RL] Epoch 6/100, PPO Loss: -0.0240, CD Loss: 0.1263
[Offline RL] Epoch 7/100, PPO Loss: -0.0253, CD Loss: 0.1291
[Offline RL] Epoch 8/100, PPO Loss: -0.0257, CD Loss: 0.1123
[Offline RL] Epoch 9/100, PPO Loss: -0.0254, CD Loss: 0.1009
[Offline RL] Epoch 10/100, PPO Loss: -0.0258, CD Loss: 0.1007
[Offline RL] Epoch 11/100, PPO Loss: -0.0260, CD Loss: 0.1100
[Offline RL] Epoch 12/100, PPO Loss: -0.0262, CD Loss: 0.1164
[Offline RL] Epoch 13/100, PPO Loss: -0.0250, CD Loss: 0.1083
[Offline RL] Epoch 14/100, PPO Loss: -0.0247, CD Loss: 0.1151
[Offline RL] Epoch 15/100, PPO Loss: -0.0252, CD Loss: 0.1288
[Offline RL] Epoch 16/100, PPO Loss: -0.0236, CD Loss: 0.1404
[Offline RL] Epoch 17/100, PPO Loss: -0.0239, CD Loss: 0.1377
[Offline RL] Epoch 18/100, PPO Loss: -0.0255, CD Loss: 0.1467
[Offline RL] Epoch 19/100, PPO Loss: -0.0252, CD Loss: 0.1610
[Offline RL] Epoch 20/100, PPO Loss: -0.0237, CD Loss: 0.1606
[Offline RL] Epoch 21/100, PPO Loss: -0.0250, CD Loss: 0.1577
[Offline RL] Epoch 22/100, PPO Loss: -0.0242, CD Loss: 0.1513
[Offline RL] Epoch 23/100, PPO Loss: -0.0245, CD Loss: 0.1422
[Offline RL] Epoch 24/100, PPO Loss: -0.0245, CD Loss: 0.1488
[Offline RL] Epoch 25/100, PPO Loss: -0.0254, CD Loss: 0.1454
[Offline RL] Epoch 26/100, PPO Loss: -0.0245, CD Loss: 0.1471
[Offline RL] Epoch 27/100, PPO Loss: -0.0237, CD Loss: 0.1569
[Offline RL] Epoch 28/100, PPO Loss: -0.0224, CD Loss: 0.1549
[Offline RL] Epoch 29/100, PPO Loss: -0.0222, CD Loss: 0.1557
[Offline RL] Epoch 30/100, PPO Loss: -0.0226, CD Loss: 0.1552
[Offline RL] Epoch 31/100, PPO Loss: -0.0227, CD Loss: 0.1544
[Offline RL] Epoch 32/100, PPO Loss: -0.0219, CD Loss: 0.1552
[Offline RL] Epoch 33/100, PPO Loss: -0.0220, CD Loss: 0.1563
[Offline RL] Epoch 34/100, PPO Loss: -0.0230, CD Loss: 0.1644
[Offline RL] Epoch 35/100, PPO Loss: -0.0223, CD Loss: 0.1716
[Offline RL] Epoch 36/100, PPO Loss: -0.0207, CD Loss: 0.1692
[Offline RL] Epoch 37/100, PPO Loss: -0.0204, CD Loss: 0.1743
[Offline RL] Epoch 38/100, PPO Loss: -0.0216, CD Loss: 0.1876
[Offline RL] Epoch 39/100, PPO Loss: -0.0230, CD Loss: 0.1997
[Offline RL] Epoch 40/100, PPO Loss: -0.0240, CD Loss: 0.1962
[Offline RL] Epoch 41/100, PPO Loss: -0.0219, CD Loss: 0.1972
[Offline RL] Epoch 42/100, PPO Loss: -0.0241, CD Loss: 0.1991
[Offline RL] Epoch 43/100, PPO Loss: -0.0234, CD Loss: 0.2001
[Offline RL] Epoch 44/100, PPO Loss: -0.0233, CD Loss: 0.1939
[Offline RL] Epoch 45/100, PPO Loss: -0.0243, CD Loss: 0.1980
[Offline RL] Epoch 46/100, PPO Loss: -0.0232, CD Loss: 0.2000
[Offline RL] Epoch 47/100, PPO Loss: -0.0240, CD Loss: 0.2069
[Offline RL] Epoch 48/100, PPO Loss: -0.0244, CD Loss: 0.2017
[Offline RL] Epoch 49/100, PPO Loss: -0.0249, CD Loss: 0.1991
[Offline RL] Epoch 50/100, PPO Loss: -0.0258, CD Loss: 0.1950
[Offline RL] Epoch 51/100, PPO Loss: -0.0245, CD Loss: 0.1861
[Offline RL] Epoch 52/100, PPO Loss: -0.0249, CD Loss: 0.1855
[Offline RL] Epoch 53/100, PPO Loss: -0.0247, CD Loss: 0.1910
[Offline RL] Epoch 54/100, PPO Loss: -0.0244, CD Loss: 0.1888
[Offline RL] Epoch 55/100, PPO Loss: -0.0247, CD Loss: 0.1888
[Offline RL] Epoch 56/100, PPO Loss: -0.0250, CD Loss: 0.1899
[Offline RL] Epoch 57/100, PPO Loss: -0.0251, CD Loss: 0.1879
[Offline RL] Epoch 58/100, PPO Loss: -0.0250, CD Loss: 0.1888
[Offline RL] Epoch 59/100, PPO Loss: -0.0260, CD Loss: 0.1911
[Offline RL] Epoch 60/100, PPO Loss: -0.0267, CD Loss: 0.2004
[Offline RL] Epoch 61/100, PPO Loss: -0.0254, CD Loss: 0.2064
[Offline RL] Epoch 62/100, PPO Loss: -0.0242, CD Loss: 0.2057
[Offline RL] Epoch 63/100, PPO Loss: -0.0236, CD Loss: 0.2033
[Offline RL] Epoch 64/100, PPO Loss: -0.0227, CD Loss: 0.1916
[Offline RL] Epoch 65/100, PPO Loss: -0.0239, CD Loss: 0.1942
[Offline RL] Epoch 66/100, PPO Loss: -0.0224, CD Loss: 0.1919
[Offline RL] Epoch 67/100, PPO Loss: -0.0236, CD Loss: 0.1963
[Offline RL] Epoch 68/100, PPO Loss: -0.0241, CD Loss: 0.1925
[Offline RL] Epoch 69/100, PPO Loss: -0.0231, CD Loss: 0.1970
[Offline RL] Epoch 70/100, PPO Loss: -0.0238, CD Loss: 0.2043
[Offline RL] Epoch 71/100, PPO Loss: -0.0244, CD Loss: 0.2064
[Offline RL] Epoch 72/100, PPO Loss: -0.0246, CD Loss: 0.2078
[Offline RL] Epoch 73/100, PPO Loss: -0.0247, CD Loss: 0.1940
[Offline RL] Epoch 74/100, PPO Loss: -0.0243, CD Loss: 0.1998
[Offline RL] Epoch 75/100, PPO Loss: -0.0228, CD Loss: 0.2043
[Offline RL] Epoch 76/100, PPO Loss: -0.0244, CD Loss: 0.2112
[Offline RL] Epoch 77/100, PPO Loss: -0.0239, CD Loss: 0.2212
[Offline RL] Epoch 78/100, PPO Loss: -0.0244, CD Loss: 0.2323
[Offline RL] Epoch 79/100, PPO Loss: -0.0248, CD Loss: 0.2306
[Offline RL] Epoch 80/100, PPO Loss: -0.0251, CD Loss: 0.2389
[Offline RL] Epoch 81/100, PPO Loss: -0.0255, CD Loss: 0.2492
[Offline RL] Epoch 82/100, PPO Loss: -0.0257, CD Loss: 0.2511
[Offline RL] Epoch 83/100, PPO Loss: -0.0258, CD Loss: 0.2496
[Offline RL] Epoch 84/100, PPO Loss: -0.0244, CD Loss: 0.2478
[Offline RL] Epoch 85/100, PPO Loss: -0.0266, CD Loss: 0.2441
[Offline RL] Epoch 86/100, PPO Loss: -0.0259, CD Loss: 0.2496
[Offline RL] Epoch 87/100, PPO Loss: -0.0260, CD Loss: 0.2478
[Offline RL] Epoch 88/100, PPO Loss: -0.0267, CD Loss: 0.2390
[Offline RL] Epoch 89/100, PPO Loss: -0.0236, CD Loss: 0.2408
[Offline RL] Epoch 90/100, PPO Loss: -0.0255, CD Loss: 0.2426
[Offline RL] Epoch 91/100, PPO Loss: -0.0259, CD Loss: 0.2433
[Offline RL] Epoch 92/100, PPO Loss: -0.0255, CD Loss: 0.2379
[Offline RL] Epoch 93/100, PPO Loss: -0.0272, CD Loss: 0.2341
[Offline RL] Epoch 94/100, PPO Loss: -0.0256, CD Loss: 0.2379
[Offline RL] Epoch 95/100, PPO Loss: -0.0251, CD Loss: 0.2420
[Offline RL] Epoch 96/100, PPO Loss: -0.0233, CD Loss: 0.2478
[Offline RL] Epoch 97/100, PPO Loss: -0.0238, CD Loss: 0.2467
[Offline RL] Epoch 98/100, PPO Loss: -0.0258, CD Loss: 0.2481
[Offline RL] Epoch 99/100, PPO Loss: -0.0237, CD Loss: 0.2444
[OPE] Policy ACCEPTED: J_new=2097.6004 > J_old=1327.9185 + δ=66.3959

[RL100Trainer] Phase 2c: Collecting New Data (Iteration 3)
[Collect] 50 episodes, success=0.000, steps=1250
[Data Collection] Success Rate: 0.000, Reward: 2546.90, Episodes: 50, Steps: 1250
[Dataset] Merged 50 episodes (1250 steps) → total 7000 steps, 210 episodes
[RL100] VIB betas set to factor=1.0: beta_recon=0.000100, beta_kl=0.000100

[RL100Trainer] Retraining IL on merged dataset...

============================================================
[RL100Trainer] Phase 1: Imitation Learning
============================================================

[IL] Epoch 0/100, Loss: 2.5484
[IL] Epoch 1/100, Loss: 0.8178
[IL] Epoch 2/100, Loss: 0.6920
[IL] Epoch 3/100, Loss: 0.5741
[IL] Epoch 4/100, Loss: 0.4581
[IL] Epoch 5/100, Loss: 0.3486
[IL] Epoch 6/100, Loss: 0.2822
[IL] Epoch 7/100, Loss: 0.2306
[IL] Epoch 8/100, Loss: 0.2009
[IL] Epoch 9/100, Loss: 0.1869
[IL] Epoch 10/100, Loss: 0.1807
[IL] Epoch 11/100, Loss: 0.1709
[IL] Epoch 12/100, Loss: 0.1687
[IL] Epoch 13/100, Loss: 0.1622
[IL] Epoch 14/100, Loss: 0.1558
[IL] Epoch 15/100, Loss: 0.1567
[IL] Epoch 16/100, Loss: 0.1530
[IL] Epoch 17/100, Loss: 0.1497
[IL] Epoch 18/100, Loss: 0.1493
[IL] Epoch 19/100, Loss: 0.1428
[IL] Epoch 20/100, Loss: 0.1502
[IL] Epoch 21/100, Loss: 0.1434
[IL] Epoch 22/100, Loss: 0.1447
[IL] Epoch 23/100, Loss: 0.1456
[IL] Epoch 24/100, Loss: 0.1422
[IL] Epoch 25/100, Loss: 0.1449
[IL] Epoch 26/100, Loss: 0.1390
[IL] Epoch 27/100, Loss: 0.1363
[IL] Epoch 28/100, Loss: 0.1360
[IL] Epoch 29/100, Loss: 0.1382
[IL] Epoch 30/100, Loss: 0.1357
[IL] Epoch 31/100, Loss: 0.1358
[IL] Epoch 32/100, Loss: 0.1380
[IL] Epoch 33/100, Loss: 0.1349
[IL] Epoch 34/100, Loss: 0.1407
[IL] Epoch 35/100, Loss: 0.1399
[IL] Epoch 36/100, Loss: 0.1320
[IL] Epoch 37/100, Loss: 0.1310
[IL] Epoch 38/100, Loss: 0.1325
[IL] Epoch 39/100, Loss: 0.1351
[IL] Epoch 40/100, Loss: 0.1323
[IL] Epoch 41/100, Loss: 0.1277
[IL] Epoch 42/100, Loss: 0.1340
[IL] Epoch 43/100, Loss: 0.1324
[IL] Epoch 44/100, Loss: 0.1334
[IL] Epoch 45/100, Loss: 0.1365
[IL] Epoch 46/100, Loss: 0.1305
[IL] Epoch 47/100, Loss: 0.1322
[IL] Epoch 48/100, Loss: 0.1277
[IL] Epoch 49/100, Loss: 0.1253
[IL] Epoch 50/100, Loss: 0.1271
[IL] Epoch 51/100, Loss: 0.1246
[IL] Epoch 52/100, Loss: 0.1269
[IL] Epoch 53/100, Loss: 0.1303
[IL] Epoch 54/100, Loss: 0.1277
[IL] Epoch 55/100, Loss: 0.1272
[IL] Epoch 56/100, Loss: 0.1293
[IL] Epoch 57/100, Loss: 0.1252
[IL] Epoch 58/100, Loss: 0.1281
[IL] Epoch 59/100, Loss: 0.1232
[IL] Epoch 60/100, Loss: 0.1261
[IL] Epoch 61/100, Loss: 0.1220
[IL] Epoch 62/100, Loss: 0.1266
[IL] Epoch 63/100, Loss: 0.1238
[IL] Epoch 64/100, Loss: 0.1261
[IL] Epoch 65/100, Loss: 0.1250
[IL] Epoch 66/100, Loss: 0.1250
[IL] Epoch 67/100, Loss: 0.1244
[IL] Epoch 68/100, Loss: 0.1243
[IL] Epoch 69/100, Loss: 0.1207
[IL] Epoch 70/100, Loss: 0.1194
[IL] Epoch 71/100, Loss: 0.1202
[IL] Epoch 72/100, Loss: 0.1226
[IL] Epoch 73/100, Loss: 0.1210
[IL] Epoch 74/100, Loss: 0.1232
[IL] Epoch 75/100, Loss: 0.1220
[IL] Epoch 76/100, Loss: 0.1241
[IL] Epoch 77/100, Loss: 0.1227
[IL] Epoch 78/100, Loss: 0.1210
[IL] Epoch 79/100, Loss: 0.1240
[IL] Epoch 80/100, Loss: 0.1229
[IL] Epoch 81/100, Loss: 0.1246
[IL] Epoch 82/100, Loss: 0.1259
[IL] Epoch 83/100, Loss: 0.1198
[IL] Epoch 84/100, Loss: 0.1195
[IL] Epoch 85/100, Loss: 0.1185
[IL] Epoch 86/100, Loss: 0.1271
[IL] Epoch 87/100, Loss: 0.1213
[IL] Epoch 88/100, Loss: 0.1270
[IL] Epoch 89/100, Loss: 0.1213
[IL] Epoch 90/100, Loss: 0.1210
[IL] Epoch 91/100, Loss: 0.1226
[IL] Epoch 92/100, Loss: 0.1184
[IL] Epoch 93/100, Loss: 0.1210
[IL] Epoch 94/100, Loss: 0.1232
[IL] Epoch 95/100, Loss: 0.1218
[IL] Epoch 96/100, Loss: 0.1214
[IL] Epoch 97/100, Loss: 0.1251
[IL] Epoch 98/100, Loss: 0.1138
[IL] Epoch 99/100, Loss: 0.1178
test_mean_score: 0.0
[IL] Eval - Success Rate: 0.000
[Checkpoint] Saved to /nfs_global/S/yangrongzheng/RL100/3D-Diffusion-Policy/3D-Diffusion-Policy/checkpoints/offline_iter_3.ckpt

================================================================================
               OFFLINE RL ITERATION 5/5
================================================================================


[RL100Trainer] Line 6 — Training Transition Model T_θ (Iteration 4)

[TransitionModel] Encoding dataset for transition model training...
[TransitionModel] Dataset: 5530 samples, input_dim=260, target_dim=257
[TransitionModel] Epoch    0 | train=5514.20082 | val=3291.50571 | no-improve=0/5
[TransitionModel] Epoch   20 | train=753.80590 | val=1550.89937 | no-improve=1/5
[TransitionModel] Epoch   40 | train=513.84577 | val=1461.12231 | no-improve=0/5
[TransitionModel] Epoch   49 | train=451.81991 | val=1447.73789 | no-improve=5/5
[TransitionModel] Training complete. Elites=[3, 4, 6, 1, 0], val_loss=1395.95564

[RL100Trainer] Phase 2a: Training IQL Critics (Iteration 4)
[IQL] Epoch 0/500, V Loss: 267775.1055, Q Loss: 1403097.0114
[IQL] Epoch 1/500, V Loss: 43432.6863, Q Loss: 586586.3139
[IQL] Epoch 2/500, V Loss: 37175.6784, Q Loss: 439438.3182
[IQL] Epoch 3/500, V Loss: 28209.2861, Q Loss: 341125.4787
[IQL] Epoch 4/500, V Loss: 27975.4025, Q Loss: 286030.8402
[IQL] Epoch 5/500, V Loss: 27799.5587, Q Loss: 247174.5462
[IQL] Epoch 6/500, V Loss: 32352.6476, Q Loss: 223560.1385
[IQL] Epoch 7/500, V Loss: 27719.7579, Q Loss: 204557.1484
[IQL] Epoch 8/500, V Loss: 24216.1339, Q Loss: 180370.4155
[IQL] Epoch 9/500, V Loss: 22225.5087, Q Loss: 163960.4343
[IQL] Epoch 10/500, V Loss: 22818.3042, Q Loss: 151609.0980
[IQL] Epoch 11/500, V Loss: 23569.8637, Q Loss: 145446.1516
[IQL] Epoch 12/500, V Loss: 24452.5528, Q Loss: 138758.4332
[IQL] Epoch 13/500, V Loss: 19579.2750, Q Loss: 123188.6417
[IQL] Epoch 14/500, V Loss: 22913.4058, Q Loss: 121358.8903
[IQL] Epoch 15/500, V Loss: 23615.6325, Q Loss: 117017.6058
[IQL] Epoch 16/500, V Loss: 20765.5426, Q Loss: 110393.8857
[IQL] Epoch 17/500, V Loss: 18377.9705, Q Loss: 103864.7067
[IQL] Epoch 18/500, V Loss: 16724.3149, Q Loss: 96343.4996
[IQL] Epoch 19/500, V Loss: 15462.9517, Q Loss: 92865.0542
[IQL] Epoch 20/500, V Loss: 16355.4373, Q Loss: 89220.8727
[IQL] Epoch 21/500, V Loss: 17438.5070, Q Loss: 87628.1033
[IQL] Epoch 22/500, V Loss: 17783.4086, Q Loss: 90341.9173
[IQL] Epoch 23/500, V Loss: 14170.2216, Q Loss: 79236.5312
[IQL] Epoch 24/500, V Loss: 14765.6768, Q Loss: 77628.9576
[IQL] Epoch 25/500, V Loss: 14192.0925, Q Loss: 76745.5057
[IQL] Epoch 26/500, V Loss: 16549.3914, Q Loss: 75435.2399
[IQL] Epoch 27/500, V Loss: 14158.2538, Q Loss: 74138.2466
[IQL] Epoch 28/500, V Loss: 16239.8366, Q Loss: 73637.3358
[IQL] Epoch 29/500, V Loss: 13287.0708, Q Loss: 71055.2603
[IQL] Epoch 30/500, V Loss: 13168.7849, Q Loss: 68565.2063
[IQL] Epoch 31/500, V Loss: 15661.4949, Q Loss: 72532.2582
[IQL] Epoch 32/500, V Loss: 13769.7987, Q Loss: 69931.8842
[IQL] Epoch 33/500, V Loss: 13422.9719, Q Loss: 65114.1974
[IQL] Epoch 34/500, V Loss: 16148.5971, Q Loss: 69022.1081
[IQL] Epoch 35/500, V Loss: 15089.1210, Q Loss: 67248.5655
[IQL] Epoch 36/500, V Loss: 14640.9611, Q Loss: 68586.9922
[IQL] Epoch 37/500, V Loss: 14396.1865, Q Loss: 64567.7140
[IQL] Epoch 38/500, V Loss: 15626.8679, Q Loss: 66058.3798
[IQL] Epoch 39/500, V Loss: 13953.2460, Q Loss: 65017.8542
[IQL] Epoch 40/500, V Loss: 14018.7537, Q Loss: 63293.6696
[IQL] Epoch 41/500, V Loss: 14475.6366, Q Loss: 65252.1520
[IQL] Epoch 42/500, V Loss: 12611.2299, Q Loss: 60545.2180
[IQL] Epoch 43/500, V Loss: 13951.0502, Q Loss: 63185.6816
[IQL] Epoch 44/500, V Loss: 13283.1134, Q Loss: 61977.9217
[IQL] Epoch 45/500, V Loss: 12395.6268, Q Loss: 58718.8576
[IQL] Epoch 46/500, V Loss: 12873.0650, Q Loss: 60153.5916
[IQL] Epoch 47/500, V Loss: 13782.1110, Q Loss: 62577.5410
[IQL] Epoch 48/500, V Loss: 13220.3027, Q Loss: 61458.5085
[IQL] Epoch 49/500, V Loss: 14233.7760, Q Loss: 56437.5218
[IQL] Epoch 50/500, V Loss: 14349.9411, Q Loss: 57829.2626
[IQL] Epoch 51/500, V Loss: 15742.8225, Q Loss: 56717.1570
[IQL] Epoch 52/500, V Loss: 13761.1491, Q Loss: 55249.6527
[IQL] Epoch 53/500, V Loss: 13188.6447, Q Loss: 54685.2615
[IQL] Epoch 54/500, V Loss: 13570.1002, Q Loss: 54325.2759
[IQL] Epoch 55/500, V Loss: 13319.4450, Q Loss: 53119.4130
[IQL] Epoch 56/500, V Loss: 13371.6174, Q Loss: 54789.1000
[IQL] Epoch 57/500, V Loss: 12773.6267, Q Loss: 52274.6646
[IQL] Epoch 58/500, V Loss: 13593.3259, Q Loss: 54937.1895
[IQL] Epoch 59/500, V Loss: 12620.7377, Q Loss: 53744.3936
[IQL] Epoch 60/500, V Loss: 13380.1186, Q Loss: 53200.1435
[IQL] Epoch 61/500, V Loss: 13897.9128, Q Loss: 55423.2812
[IQL] Epoch 62/500, V Loss: 13823.9054, Q Loss: 53054.2152
[IQL] Epoch 63/500, V Loss: 13180.8530, Q Loss: 49868.0694
[IQL] Epoch 64/500, V Loss: 13930.0087, Q Loss: 50236.2777
[IQL] Epoch 65/500, V Loss: 13211.3012, Q Loss: 49702.1483
[IQL] Epoch 66/500, V Loss: 14105.7315, Q Loss: 49124.6396
[IQL] Epoch 67/500, V Loss: 13814.5755, Q Loss: 50213.8791
[IQL] Epoch 68/500, V Loss: 15552.8810, Q Loss: 51513.5808
[IQL] Epoch 69/500, V Loss: 12698.5162, Q Loss: 51289.7376
[IQL] Epoch 70/500, V Loss: 13534.9628, Q Loss: 48580.4644
[IQL] Epoch 71/500, V Loss: 13971.2136, Q Loss: 49274.6697
[IQL] Epoch 72/500, V Loss: 13893.2983, Q Loss: 47567.5998
[IQL] Epoch 73/500, V Loss: 12798.2461, Q Loss: 46675.0918
[IQL] Epoch 74/500, V Loss: 13531.3081, Q Loss: 48150.7544
[IQL] Epoch 75/500, V Loss: 13090.8582, Q Loss: 46967.1184
[IQL] Epoch 76/500, V Loss: 13022.7788, Q Loss: 47204.9072
[IQL] Epoch 77/500, V Loss: 13281.3161, Q Loss: 45557.3015
[IQL] Epoch 78/500, V Loss: 14241.1325, Q Loss: 46459.7876
[IQL] Epoch 79/500, V Loss: 13829.2803, Q Loss: 47715.5705
[IQL] Epoch 80/500, V Loss: 13522.5721, Q Loss: 46480.5465
[IQL] Epoch 81/500, V Loss: 15090.2236, Q Loss: 48350.4309
[IQL] Epoch 82/500, V Loss: 13618.5024, Q Loss: 48200.3178
[IQL] Epoch 83/500, V Loss: 13020.2509, Q Loss: 49967.8741
[IQL] Epoch 84/500, V Loss: 14503.4288, Q Loss: 45798.0563
[IQL] Epoch 85/500, V Loss: 13008.5482, Q Loss: 48313.0665
[IQL] Epoch 86/500, V Loss: 13502.0278, Q Loss: 47159.4192
[IQL] Epoch 87/500, V Loss: 13947.6531, Q Loss: 48201.4142
[IQL] Epoch 88/500, V Loss: 13367.9541, Q Loss: 48396.0783
[IQL] Epoch 89/500, V Loss: 14461.2068, Q Loss: 48598.5643
[IQL] Epoch 90/500, V Loss: 14320.1067, Q Loss: 49158.9732
[IQL] Epoch 91/500, V Loss: 14013.6842, Q Loss: 45472.1024
[IQL] Epoch 92/500, V Loss: 14215.0248, Q Loss: 45498.4765
[IQL] Epoch 93/500, V Loss: 13930.2685, Q Loss: 44002.3093
[IQL] Epoch 94/500, V Loss: 13314.3157, Q Loss: 46783.6579
[IQL] Epoch 95/500, V Loss: 14340.6510, Q Loss: 47347.9389
[IQL] Epoch 96/500, V Loss: 13175.0158, Q Loss: 43745.5574
[IQL] Epoch 97/500, V Loss: 14596.8016, Q Loss: 45646.9904
[IQL] Epoch 98/500, V Loss: 14269.4731, Q Loss: 47576.9466
[IQL] Epoch 99/500, V Loss: 14950.5495, Q Loss: 49045.4851
[IQL] Epoch 100/500, V Loss: 13243.4977, Q Loss: 45220.2889
[IQL] Epoch 101/500, V Loss: 12609.2579, Q Loss: 52550.8346
[IQL] Epoch 102/500, V Loss: 13996.0118, Q Loss: 48962.3906
[IQL] Epoch 103/500, V Loss: 13468.9241, Q Loss: 45509.3796
[IQL] Epoch 104/500, V Loss: 14513.6611, Q Loss: 44799.5662
[IQL] Epoch 105/500, V Loss: 14464.3334, Q Loss: 47894.5957
[IQL] Epoch 106/500, V Loss: 14489.9093, Q Loss: 44445.2437
[IQL] Epoch 107/500, V Loss: 12725.2358, Q Loss: 45946.1157
[IQL] Epoch 108/500, V Loss: 13942.6374, Q Loss: 44435.2112
[IQL] Epoch 109/500, V Loss: 12810.6804, Q Loss: 47262.7683
[IQL] Epoch 110/500, V Loss: 14396.9963, Q Loss: 45356.5898
[IQL] Epoch 111/500, V Loss: 17530.9326, Q Loss: 47255.2470
[IQL] Epoch 112/500, V Loss: 13728.9517, Q Loss: 42215.2802
[IQL] Epoch 113/500, V Loss: 14872.9240, Q Loss: 44476.2353
[IQL] Epoch 114/500, V Loss: 14513.6897, Q Loss: 48700.3833
[IQL] Epoch 115/500, V Loss: 13019.5912, Q Loss: 46690.8556
[IQL] Epoch 116/500, V Loss: 15799.0893, Q Loss: 43844.9823
[IQL] Epoch 117/500, V Loss: 14575.0084, Q Loss: 44856.6356
[IQL] Epoch 118/500, V Loss: 13090.1081, Q Loss: 45112.4993
[IQL] Epoch 119/500, V Loss: 14771.5970, Q Loss: 46298.1168
[IQL] Epoch 120/500, V Loss: 14441.8853, Q Loss: 44213.5080
[IQL] Epoch 121/500, V Loss: 15262.4436, Q Loss: 48602.0363
[IQL] Epoch 122/500, V Loss: 15468.5037, Q Loss: 48200.8511
[IQL] Epoch 123/500, V Loss: 14265.0068, Q Loss: 49425.8824
[IQL] Epoch 124/500, V Loss: 14239.5169, Q Loss: 43785.5477
[IQL] Epoch 125/500, V Loss: 14713.4548, Q Loss: 48681.2069
[IQL] Epoch 126/500, V Loss: 14990.4921, Q Loss: 42880.5177
[IQL] Epoch 127/500, V Loss: 13509.2729, Q Loss: 42758.3887
[IQL] Epoch 128/500, V Loss: 13980.0244, Q Loss: 43858.0726
[IQL] Epoch 129/500, V Loss: 15028.1894, Q Loss: 41965.1936
[IQL] Epoch 130/500, V Loss: 17425.8404, Q Loss: 45583.0660
[IQL] Epoch 131/500, V Loss: 13667.2181, Q Loss: 46226.8233
[IQL] Epoch 132/500, V Loss: 15004.3676, Q Loss: 41254.0810
[IQL] Epoch 133/500, V Loss: 14347.3417, Q Loss: 44794.4864
[IQL] Epoch 134/500, V Loss: 14878.9258, Q Loss: 48279.4291
[IQL] Epoch 135/500, V Loss: 14669.1234, Q Loss: 46425.0487
[IQL] Epoch 136/500, V Loss: 14797.5087, Q Loss: 49895.1189
[IQL] Epoch 137/500, V Loss: 14593.6120, Q Loss: 40153.2331
[IQL] Epoch 138/500, V Loss: 16535.5926, Q Loss: 54809.9326
[IQL] Epoch 139/500, V Loss: 17716.2215, Q Loss: 53340.2866
[IQL] Epoch 140/500, V Loss: 16715.4897, Q Loss: 46447.9399
[IQL] Epoch 141/500, V Loss: 14612.4744, Q Loss: 49959.8153
[IQL] Epoch 142/500, V Loss: 14518.5074, Q Loss: 44150.5889
[IQL] Epoch 143/500, V Loss: 15273.6931, Q Loss: 43453.1910
[IQL] Epoch 144/500, V Loss: 14855.8574, Q Loss: 41974.2069
[IQL] Epoch 145/500, V Loss: 15445.2384, Q Loss: 44712.4411
[IQL] Epoch 146/500, V Loss: 14781.6295, Q Loss: 48341.3912
[IQL] Epoch 147/500, V Loss: 17011.2184, Q Loss: 46255.1499
[IQL] Epoch 148/500, V Loss: 14590.9191, Q Loss: 46534.2286
[IQL] Epoch 149/500, V Loss: 15941.6070, Q Loss: 40155.4521
[IQL] Epoch 150/500, V Loss: 15726.6179, Q Loss: 42041.6608
[IQL] Epoch 151/500, V Loss: 16402.8927, Q Loss: 43365.3436
[IQL] Epoch 152/500, V Loss: 15452.7561, Q Loss: 46569.0980
[IQL] Epoch 153/500, V Loss: 14431.0993, Q Loss: 43029.7548
[IQL] Epoch 154/500, V Loss: 15067.3844, Q Loss: 43478.0400
[IQL] Epoch 155/500, V Loss: 15089.5993, Q Loss: 42477.9695
[IQL] Epoch 156/500, V Loss: 15949.0969, Q Loss: 45597.5027
[IQL] Epoch 157/500, V Loss: 15731.1282, Q Loss: 43299.1153
[IQL] Epoch 158/500, V Loss: 15647.8994, Q Loss: 48681.5196
[IQL] Epoch 159/500, V Loss: 14281.9069, Q Loss: 38834.9998
[IQL] Epoch 160/500, V Loss: 14537.5779, Q Loss: 40199.4133
[IQL] Epoch 161/500, V Loss: 16626.6661, Q Loss: 45581.9350
[IQL] Epoch 162/500, V Loss: 15734.0484, Q Loss: 43084.9213
[IQL] Epoch 163/500, V Loss: 15926.4043, Q Loss: 45031.4446
[IQL] Epoch 164/500, V Loss: 14543.7994, Q Loss: 48116.9535
[IQL] Epoch 165/500, V Loss: 16517.0624, Q Loss: 57391.1015
[IQL] Epoch 166/500, V Loss: 16498.4626, Q Loss: 45643.4740
[IQL] Epoch 167/500, V Loss: 15772.9935, Q Loss: 44294.5236
[IQL] Epoch 168/500, V Loss: 16520.3335, Q Loss: 39154.6353
[IQL] Epoch 169/500, V Loss: 16802.6438, Q Loss: 43753.2419
[IQL] Epoch 170/500, V Loss: 13782.2679, Q Loss: 44014.6564
[IQL] Epoch 171/500, V Loss: 14716.5396, Q Loss: 42142.9739
[IQL] Epoch 172/500, V Loss: 17679.1437, Q Loss: 39516.7118
[IQL] Epoch 173/500, V Loss: 16151.1204, Q Loss: 50583.3564
[IQL] Epoch 174/500, V Loss: 15821.3875, Q Loss: 44184.6272
[IQL] Epoch 175/500, V Loss: 17060.5265, Q Loss: 43608.0869
[IQL] Epoch 176/500, V Loss: 16065.2937, Q Loss: 44387.7140
[IQL] Epoch 177/500, V Loss: 14535.2638, Q Loss: 46762.1280
[IQL] Epoch 178/500, V Loss: 15246.9348, Q Loss: 44797.2031
[IQL] Epoch 179/500, V Loss: 14775.4543, Q Loss: 42673.3069
[IQL] Epoch 180/500, V Loss: 14757.3704, Q Loss: 38918.0299
[IQL] Epoch 181/500, V Loss: 15040.6491, Q Loss: 49307.8999
[IQL] Epoch 182/500, V Loss: 15828.0606, Q Loss: 44992.2299
[IQL] Epoch 183/500, V Loss: 17272.6927, Q Loss: 47039.7296
[IQL] Epoch 184/500, V Loss: 16352.7688, Q Loss: 37679.3162
[IQL] Epoch 185/500, V Loss: 16938.3715, Q Loss: 40109.9487
[IQL] Epoch 186/500, V Loss: 15214.5825, Q Loss: 44680.0691
[IQL] Epoch 187/500, V Loss: 15854.8829, Q Loss: 46369.3840
[IQL] Epoch 188/500, V Loss: 14447.0678, Q Loss: 38204.4461
[IQL] Epoch 189/500, V Loss: 16541.6496, Q Loss: 48915.7846
[IQL] Epoch 190/500, V Loss: 17135.3184, Q Loss: 44829.3021
[IQL] Epoch 191/500, V Loss: 15472.0878, Q Loss: 47525.3340
[IQL] Epoch 192/500, V Loss: 16175.7720, Q Loss: 44253.3014
[IQL] Epoch 193/500, V Loss: 15498.0783, Q Loss: 39621.2420
[IQL] Epoch 194/500, V Loss: 16298.5399, Q Loss: 46351.6722
[IQL] Epoch 195/500, V Loss: 17082.8504, Q Loss: 39912.4982
[IQL] Epoch 196/500, V Loss: 14999.0475, Q Loss: 42518.9580
[IQL] Epoch 197/500, V Loss: 15172.8942, Q Loss: 50060.0108
[IQL] Epoch 198/500, V Loss: 16834.4358, Q Loss: 49252.6678
[IQL] Epoch 199/500, V Loss: 16612.1962, Q Loss: 48325.9697
[IQL] Epoch 200/500, V Loss: 14012.7181, Q Loss: 47535.6040
[IQL] Epoch 201/500, V Loss: 15675.1562, Q Loss: 42968.8928
[IQL] Epoch 202/500, V Loss: 16605.3689, Q Loss: 41444.2422
[IQL] Epoch 203/500, V Loss: 15088.3361, Q Loss: 47026.4015
[IQL] Epoch 204/500, V Loss: 17745.9222, Q Loss: 45633.4084
[IQL] Epoch 205/500, V Loss: 15831.2012, Q Loss: 39395.7235
[IQL] Epoch 206/500, V Loss: 18388.5169, Q Loss: 41139.4117
[IQL] Epoch 207/500, V Loss: 15550.9970, Q Loss: 40745.5932
[IQL] Epoch 208/500, V Loss: 18005.4628, Q Loss: 43117.0100
[IQL] Epoch 209/500, V Loss: 17731.2678, Q Loss: 44305.2855
[IQL] Epoch 210/500, V Loss: 15875.3623, Q Loss: 43635.5225
[IQL] Epoch 211/500, V Loss: 15976.6628, Q Loss: 42702.0051
[IQL] Epoch 212/500, V Loss: 17308.3107, Q Loss: 43766.9909
[IQL] Epoch 213/500, V Loss: 18358.0203, Q Loss: 53122.6399
[IQL] Epoch 214/500, V Loss: 15218.4686, Q Loss: 44273.5785
[IQL] Epoch 215/500, V Loss: 14572.9230, Q Loss: 37616.1445
[IQL] Epoch 216/500, V Loss: 18508.5075, Q Loss: 40828.4404
[IQL] Epoch 217/500, V Loss: 16110.2849, Q Loss: 38593.1913
[IQL] Epoch 218/500, V Loss: 16706.1658, Q Loss: 46896.1760
[IQL] Epoch 219/500, V Loss: 14029.0197, Q Loss: 45987.6675
[IQL] Epoch 220/500, V Loss: 15189.5508, Q Loss: 42628.8762
[IQL] Epoch 221/500, V Loss: 17442.5779, Q Loss: 45236.5535
[IQL] Epoch 222/500, V Loss: 17835.6376, Q Loss: 46046.9253
[IQL] Epoch 223/500, V Loss: 17791.5750, Q Loss: 43447.5537
[IQL] Epoch 224/500, V Loss: 16210.4700, Q Loss: 48418.1754
[IQL] Epoch 225/500, V Loss: 15031.8708, Q Loss: 46729.4834
[IQL] Epoch 226/500, V Loss: 16552.1322, Q Loss: 41213.0684
[IQL] Epoch 227/500, V Loss: 15928.7412, Q Loss: 43242.4033
[IQL] Epoch 228/500, V Loss: 14847.6246, Q Loss: 52320.6183
[IQL] Epoch 229/500, V Loss: 15607.9720, Q Loss: 41484.3251
[IQL] Epoch 230/500, V Loss: 16815.2690, Q Loss: 43828.1821
[IQL] Epoch 231/500, V Loss: 14353.6540, Q Loss: 43723.1172
[IQL] Epoch 232/500, V Loss: 21141.4037, Q Loss: 46513.7018
[IQL] Epoch 233/500, V Loss: 15471.0963, Q Loss: 41377.9537
[IQL] Epoch 234/500, V Loss: 16193.1557, Q Loss: 39969.0486
[IQL] Epoch 235/500, V Loss: 17013.4053, Q Loss: 48019.3417
[IQL] Epoch 236/500, V Loss: 16163.1288, Q Loss: 36527.6334
[IQL] Epoch 237/500, V Loss: 19263.2341, Q Loss: 41359.3018
[IQL] Epoch 238/500, V Loss: 15307.4602, Q Loss: 43127.7445
[IQL] Epoch 239/500, V Loss: 15462.9838, Q Loss: 40119.7708
[IQL] Epoch 240/500, V Loss: 18098.6432, Q Loss: 42980.8590
[IQL] Epoch 241/500, V Loss: 17464.9933, Q Loss: 35290.2393
[IQL] Epoch 242/500, V Loss: 16011.0578, Q Loss: 41927.8478
[IQL] Epoch 243/500, V Loss: 15382.5772, Q Loss: 37092.7166
[IQL] Epoch 244/500, V Loss: 15124.6685, Q Loss: 38225.9723
[IQL] Epoch 245/500, V Loss: 16158.1357, Q Loss: 43505.7437
[IQL] Epoch 246/500, V Loss: 19158.9956, Q Loss: 38831.1324
[IQL] Epoch 247/500, V Loss: 16546.5811, Q Loss: 40995.7575
[IQL] Epoch 248/500, V Loss: 17211.2253, Q Loss: 43907.3838
[IQL] Epoch 249/500, V Loss: 16580.0740, Q Loss: 48849.5956
[IQL] Epoch 250/500, V Loss: 19152.0595, Q Loss: 46429.1622
[IQL] Epoch 251/500, V Loss: 21214.4976, Q Loss: 51550.5681
[IQL] Epoch 252/500, V Loss: 16490.0793, Q Loss: 45987.1368
[IQL] Epoch 253/500, V Loss: 16295.2529, Q Loss: 44767.7028
[IQL] Epoch 254/500, V Loss: 16250.2493, Q Loss: 45416.8383
[IQL] Epoch 255/500, V Loss: 17450.0529, Q Loss: 44823.4568
[IQL] Epoch 256/500, V Loss: 15006.5338, Q Loss: 41252.5605
[IQL] Epoch 257/500, V Loss: 16784.6011, Q Loss: 41252.5740
[IQL] Epoch 258/500, V Loss: 16154.4104, Q Loss: 46113.7638
[IQL] Epoch 259/500, V Loss: 16457.7935, Q Loss: 43860.4173
[IQL] Epoch 260/500, V Loss: 16573.9541, Q Loss: 41340.8192
[IQL] Epoch 261/500, V Loss: 17520.9706, Q Loss: 42015.6454
[IQL] Epoch 262/500, V Loss: 17675.3853, Q Loss: 43685.7963
[IQL] Epoch 263/500, V Loss: 19976.4032, Q Loss: 43846.5297
[IQL] Epoch 264/500, V Loss: 22099.7560, Q Loss: 41949.8246
[IQL] Epoch 265/500, V Loss: 16063.2171, Q Loss: 42225.8018
[IQL] Epoch 266/500, V Loss: 18593.4636, Q Loss: 46862.8501
[IQL] Epoch 267/500, V Loss: 17773.2579, Q Loss: 42319.2226
[IQL] Epoch 268/500, V Loss: 15872.9731, Q Loss: 46331.4528
[IQL] Epoch 269/500, V Loss: 16974.6698, Q Loss: 40166.4483
[IQL] Epoch 270/500, V Loss: 15889.2378, Q Loss: 43957.3831
[IQL] Epoch 271/500, V Loss: 17560.7143, Q Loss: 51757.5823
[IQL] Epoch 272/500, V Loss: 16204.2551, Q Loss: 42092.9075
[IQL] Epoch 273/500, V Loss: 17115.9405, Q Loss: 42662.4301
[IQL] Epoch 274/500, V Loss: 15557.3653, Q Loss: 46090.0804
[IQL] Epoch 275/500, V Loss: 15189.3317, Q Loss: 42997.9273
[IQL] Epoch 276/500, V Loss: 16663.3770, Q Loss: 46615.6761
[IQL] Epoch 277/500, V Loss: 15573.1158, Q Loss: 40654.4440
[IQL] Epoch 278/500, V Loss: 14015.2961, Q Loss: 45140.1308
[IQL] Epoch 279/500, V Loss: 17270.5887, Q Loss: 43440.9536
[IQL] Epoch 280/500, V Loss: 14371.8017, Q Loss: 42020.0803
[IQL] Epoch 281/500, V Loss: 17901.7129, Q Loss: 46465.4361
[IQL] Epoch 282/500, V Loss: 18358.5306, Q Loss: 42822.6428
[IQL] Epoch 283/500, V Loss: 16620.8341, Q Loss: 40966.2300
[IQL] Epoch 284/500, V Loss: 15162.9622, Q Loss: 48047.7900
[IQL] Epoch 285/500, V Loss: 14796.2740, Q Loss: 49884.1377
[IQL] Epoch 286/500, V Loss: 15444.0084, Q Loss: 43447.9299
[IQL] Epoch 287/500, V Loss: 15028.0532, Q Loss: 38130.9356
[IQL] Epoch 288/500, V Loss: 16312.0092, Q Loss: 43930.1143
[IQL] Epoch 289/500, V Loss: 17267.3705, Q Loss: 36857.4648
[IQL] Epoch 290/500, V Loss: 15597.9372, Q Loss: 42420.1423
[IQL] Epoch 291/500, V Loss: 15857.1075, Q Loss: 41170.4370
[IQL] Epoch 292/500, V Loss: 19053.2951, Q Loss: 42325.3789
[IQL] Epoch 293/500, V Loss: 17491.9422, Q Loss: 46120.4921
[IQL] Epoch 294/500, V Loss: 16683.8020, Q Loss: 43358.6483
[IQL] Epoch 295/500, V Loss: 15973.4619, Q Loss: 42569.8248
[IQL] Epoch 296/500, V Loss: 18881.5207, Q Loss: 36602.9221
[IQL] Epoch 297/500, V Loss: 18554.7617, Q Loss: 51491.0645
[IQL] Epoch 298/500, V Loss: 17539.4678, Q Loss: 48014.8842
[IQL] Epoch 299/500, V Loss: 17710.8883, Q Loss: 48276.4305
[IQL] Epoch 300/500, V Loss: 15922.0862, Q Loss: 46100.4551
[IQL] Epoch 301/500, V Loss: 16250.0450, Q Loss: 41913.4837
[IQL] Epoch 302/500, V Loss: 15075.3837, Q Loss: 42192.3094
[IQL] Epoch 303/500, V Loss: 16099.0722, Q Loss: 43968.8595
[IQL] Epoch 304/500, V Loss: 14562.3168, Q Loss: 48563.3614
[IQL] Epoch 305/500, V Loss: 16443.5411, Q Loss: 40568.4316
[IQL] Epoch 306/500, V Loss: 15678.5582, Q Loss: 41907.9415
[IQL] Epoch 307/500, V Loss: 16622.7428, Q Loss: 42943.4447
[IQL] Epoch 308/500, V Loss: 18456.1812, Q Loss: 36816.7737
[IQL] Epoch 309/500, V Loss: 16494.4580, Q Loss: 49007.7307
[IQL] Epoch 310/500, V Loss: 14635.7093, Q Loss: 40636.3523
[IQL] Epoch 311/500, V Loss: 14890.3397, Q Loss: 43283.1708
[IQL] Epoch 312/500, V Loss: 15994.0621, Q Loss: 39172.6246
[IQL] Epoch 313/500, V Loss: 15509.0751, Q Loss: 44809.9585
[IQL] Epoch 314/500, V Loss: 15788.1275, Q Loss: 47163.9702
[IQL] Epoch 315/500, V Loss: 18732.2756, Q Loss: 53517.4463
[IQL] Epoch 316/500, V Loss: 16454.6130, Q Loss: 38905.7471
[IQL] Epoch 317/500, V Loss: 14144.0643, Q Loss: 39986.1305
[IQL] Epoch 318/500, V Loss: 15753.1466, Q Loss: 43154.1999
[IQL] Epoch 319/500, V Loss: 16210.5229, Q Loss: 45153.4692
[IQL] Epoch 320/500, V Loss: 17187.1324, Q Loss: 40937.1115
[IQL] Epoch 321/500, V Loss: 15655.5899, Q Loss: 43260.2831
[IQL] Epoch 322/500, V Loss: 18554.8396, Q Loss: 37284.6261
[IQL] Epoch 323/500, V Loss: 17875.3373, Q Loss: 43949.7782
[IQL] Epoch 324/500, V Loss: 16042.5547, Q Loss: 42201.8251
[IQL] Epoch 325/500, V Loss: 16451.3695, Q Loss: 40625.8500
[IQL] Epoch 326/500, V Loss: 16699.0378, Q Loss: 42516.7147
[IQL] Epoch 327/500, V Loss: 14480.2065, Q Loss: 42177.1782
[IQL] Epoch 328/500, V Loss: 16669.1745, Q Loss: 53736.6695
[IQL] Epoch 329/500, V Loss: 16799.1669, Q Loss: 42852.8337
[IQL] Epoch 330/500, V Loss: 17358.2019, Q Loss: 46448.5716
[IQL] Epoch 331/500, V Loss: 17889.7634, Q Loss: 49254.4332
[IQL] Epoch 332/500, V Loss: 19209.3939, Q Loss: 41370.4050
[IQL] Epoch 333/500, V Loss: 16152.4163, Q Loss: 47993.1607
[IQL] Epoch 334/500, V Loss: 17947.8642, Q Loss: 51314.9907
[IQL] Epoch 335/500, V Loss: 16011.0277, Q Loss: 39438.8899
[IQL] Epoch 336/500, V Loss: 18188.3626, Q Loss: 47527.5200
[IQL] Epoch 337/500, V Loss: 17759.0115, Q Loss: 54449.5202
[IQL] Epoch 338/500, V Loss: 18822.9104, Q Loss: 44018.8080
[IQL] Epoch 339/500, V Loss: 15995.8212, Q Loss: 39368.1196
[IQL] Epoch 340/500, V Loss: 15634.9466, Q Loss: 40976.1696
[IQL] Epoch 341/500, V Loss: 16332.5164, Q Loss: 40765.3466
[IQL] Epoch 342/500, V Loss: 14708.6852, Q Loss: 49270.1482
[IQL] Epoch 343/500, V Loss: 16466.8913, Q Loss: 43280.6618
[IQL] Epoch 344/500, V Loss: 15612.6091, Q Loss: 49891.3270
[IQL] Epoch 345/500, V Loss: 15005.8454, Q Loss: 42880.3159
[IQL] Epoch 346/500, V Loss: 17075.6444, Q Loss: 42958.0058
[IQL] Epoch 347/500, V Loss: 16699.7103, Q Loss: 44305.1136
[IQL] Epoch 348/500, V Loss: 17560.8290, Q Loss: 45547.0828
[IQL] Epoch 349/500, V Loss: 16352.2051, Q Loss: 50421.6840
[IQL] Epoch 350/500, V Loss: 17050.1073, Q Loss: 41616.8400
[IQL] Epoch 351/500, V Loss: 15361.8881, Q Loss: 45691.0597
[IQL] Epoch 352/500, V Loss: 18694.5926, Q Loss: 51234.1034
[IQL] Epoch 353/500, V Loss: 15707.4483, Q Loss: 44925.7255
[IQL] Epoch 354/500, V Loss: 18127.4780, Q Loss: 44161.6123
[IQL] Epoch 355/500, V Loss: 16169.5992, Q Loss: 44462.9735
[IQL] Epoch 356/500, V Loss: 15468.7359, Q Loss: 45020.2941
[IQL] Epoch 357/500, V Loss: 17105.0505, Q Loss: 47729.3846
[IQL] Epoch 358/500, V Loss: 17899.7394, Q Loss: 47068.9735
[IQL] Epoch 359/500, V Loss: 16007.2513, Q Loss: 44656.3975
[IQL] Epoch 360/500, V Loss: 15744.8923, Q Loss: 38619.4159
[IQL] Epoch 361/500, V Loss: 15870.5955, Q Loss: 39277.7319
[IQL] Epoch 362/500, V Loss: 13997.8191, Q Loss: 36969.3783
[IQL] Epoch 363/500, V Loss: 16062.6501, Q Loss: 36325.1223
[IQL] Epoch 364/500, V Loss: 15642.3465, Q Loss: 38101.1262
[IQL] Epoch 365/500, V Loss: 14368.5627, Q Loss: 42524.7472
[IQL] Epoch 366/500, V Loss: 16049.3315, Q Loss: 41345.3628
[IQL] Epoch 367/500, V Loss: 16794.3946, Q Loss: 40047.6769
[IQL] Epoch 368/500, V Loss: 14649.2941, Q Loss: 37497.3392
[IQL] Epoch 369/500, V Loss: 14473.9704, Q Loss: 40423.0980
[IQL] Epoch 370/500, V Loss: 14552.7454, Q Loss: 41386.3088
[IQL] Epoch 371/500, V Loss: 17985.6030, Q Loss: 37337.4853
[IQL] Epoch 372/500, V Loss: 15754.6867, Q Loss: 46013.6541
[IQL] Epoch 373/500, V Loss: 15913.7547, Q Loss: 42671.3241
[IQL] Epoch 374/500, V Loss: 17459.4721, Q Loss: 47930.5523
[IQL] Epoch 375/500, V Loss: 16602.5998, Q Loss: 36773.3680
[IQL] Epoch 376/500, V Loss: 17010.4399, Q Loss: 43882.0341
[IQL] Epoch 377/500, V Loss: 16016.5439, Q Loss: 40605.5471
[IQL] Epoch 378/500, V Loss: 18340.0529, Q Loss: 38522.0376
[IQL] Epoch 379/500, V Loss: 16038.8211, Q Loss: 36478.0789
[IQL] Epoch 380/500, V Loss: 15518.2674, Q Loss: 38873.7408
[IQL] Epoch 381/500, V Loss: 17639.9212, Q Loss: 36131.0170
[IQL] Epoch 382/500, V Loss: 16726.6373, Q Loss: 47113.5755
[IQL] Epoch 383/500, V Loss: 16436.8866, Q Loss: 47006.5234
[IQL] Epoch 384/500, V Loss: 18439.5032, Q Loss: 44486.2135
[IQL] Epoch 385/500, V Loss: 16749.0459, Q Loss: 38793.5771
[IQL] Epoch 386/500, V Loss: 18085.1948, Q Loss: 37449.2799
[IQL] Epoch 387/500, V Loss: 17526.0811, Q Loss: 41735.0487
[IQL] Epoch 388/500, V Loss: 17242.1706, Q Loss: 37870.6878
[IQL] Epoch 389/500, V Loss: 18141.3347, Q Loss: 45085.4169
[IQL] Epoch 390/500, V Loss: 14863.4665, Q Loss: 46848.8504
[IQL] Epoch 391/500, V Loss: 15555.5057, Q Loss: 46574.5272
[IQL] Epoch 392/500, V Loss: 16634.2481, Q Loss: 48725.5334
[IQL] Epoch 393/500, V Loss: 17928.5162, Q Loss: 47939.9795
[IQL] Epoch 394/500, V Loss: 14848.2932, Q Loss: 42104.0605
[IQL] Epoch 395/500, V Loss: 15516.2804, Q Loss: 57776.2261
[IQL] Epoch 396/500, V Loss: 19711.1436, Q Loss: 55992.9034
[IQL] Epoch 397/500, V Loss: 18403.3054, Q Loss: 50354.2070
[IQL] Epoch 398/500, V Loss: 15377.0516, Q Loss: 35943.2617
[IQL] Epoch 399/500, V Loss: 15729.4974, Q Loss: 40795.6128
[IQL] Epoch 400/500, V Loss: 15718.7984, Q Loss: 44859.3973
[IQL] Epoch 401/500, V Loss: 15617.1749, Q Loss: 36808.4300
[IQL] Epoch 402/500, V Loss: 15365.2551, Q Loss: 40790.2662
[IQL] Epoch 403/500, V Loss: 16180.0491, Q Loss: 46151.3577
[IQL] Epoch 404/500, V Loss: 15624.8224, Q Loss: 42736.4218
[IQL] Epoch 405/500, V Loss: 16136.7825, Q Loss: 34985.2963
[IQL] Epoch 406/500, V Loss: 15006.5764, Q Loss: 45952.1587
[IQL] Epoch 407/500, V Loss: 16066.2521, Q Loss: 41714.4383
[IQL] Epoch 408/500, V Loss: 16616.3411, Q Loss: 36771.5239
[IQL] Epoch 409/500, V Loss: 16063.9120, Q Loss: 42606.2317
[IQL] Epoch 410/500, V Loss: 16307.9709, Q Loss: 42006.8360
[IQL] Epoch 411/500, V Loss: 18149.2789, Q Loss: 33415.7310
[IQL] Epoch 412/500, V Loss: 15588.9933, Q Loss: 36986.6476
[IQL] Epoch 413/500, V Loss: 15306.4262, Q Loss: 37757.1037
[IQL] Epoch 414/500, V Loss: 16067.8439, Q Loss: 48598.7328
[IQL] Epoch 415/500, V Loss: 19272.0463, Q Loss: 39263.7025
[IQL] Epoch 416/500, V Loss: 15718.7256, Q Loss: 41246.1510
[IQL] Epoch 417/500, V Loss: 15141.3919, Q Loss: 31789.5298
[IQL] Epoch 418/500, V Loss: 14919.8936, Q Loss: 34190.6486
[IQL] Epoch 419/500, V Loss: 13757.6601, Q Loss: 34256.8247
[IQL] Epoch 420/500, V Loss: 14595.0720, Q Loss: 42686.0108
[IQL] Epoch 421/500, V Loss: 14999.2727, Q Loss: 38045.8149
[IQL] Epoch 422/500, V Loss: 18412.7141, Q Loss: 41855.1712
[IQL] Epoch 423/500, V Loss: 15908.1408, Q Loss: 44119.9401
[IQL] Epoch 424/500, V Loss: 13874.8852, Q Loss: 34844.8606
[IQL] Epoch 425/500, V Loss: 15653.6552, Q Loss: 37611.7186
[IQL] Epoch 426/500, V Loss: 15742.6583, Q Loss: 39376.1541
[IQL] Epoch 427/500, V Loss: 15915.6234, Q Loss: 34070.9274
[IQL] Epoch 428/500, V Loss: 18360.8707, Q Loss: 35691.7580
[IQL] Epoch 429/500, V Loss: 17275.9860, Q Loss: 46439.1219
[IQL] Epoch 430/500, V Loss: 21479.3418, Q Loss: 43311.9285
[IQL] Epoch 431/500, V Loss: 16581.8775, Q Loss: 35723.2179
[IQL] Epoch 432/500, V Loss: 17471.2151, Q Loss: 36616.7881
[IQL] Epoch 433/500, V Loss: 17255.4208, Q Loss: 42226.8145
[IQL] Epoch 434/500, V Loss: 16749.1820, Q Loss: 45840.4596
[IQL] Epoch 435/500, V Loss: 16936.0834, Q Loss: 36558.9742
[IQL] Epoch 436/500, V Loss: 17285.8676, Q Loss: 37801.1517
[IQL] Epoch 437/500, V Loss: 16381.8835, Q Loss: 37066.0908
[IQL] Epoch 438/500, V Loss: 18509.0293, Q Loss: 34229.2675
[IQL] Epoch 439/500, V Loss: 14471.3713, Q Loss: 37621.3168
[IQL] Epoch 440/500, V Loss: 15910.9387, Q Loss: 41975.4125
[IQL] Epoch 441/500, V Loss: 17744.7139, Q Loss: 40320.2900
[IQL] Epoch 442/500, V Loss: 16489.9208, Q Loss: 39946.5519
[IQL] Epoch 443/500, V Loss: 18423.6561, Q Loss: 36949.2147
[IQL] Epoch 444/500, V Loss: 17056.6512, Q Loss: 34387.8497
[IQL] Epoch 445/500, V Loss: 15065.7790, Q Loss: 37329.2433
[IQL] Epoch 446/500, V Loss: 16118.6537, Q Loss: 39735.0040
[IQL] Epoch 447/500, V Loss: 19001.9371, Q Loss: 33932.6454
[IQL] Epoch 448/500, V Loss: 20277.5449, Q Loss: 43444.0707
[IQL] Epoch 449/500, V Loss: 19963.1152, Q Loss: 39559.1398
[IQL] Epoch 450/500, V Loss: 17414.7558, Q Loss: 47729.2849
[IQL] Epoch 451/500, V Loss: 18548.6080, Q Loss: 37199.9349
[IQL] Epoch 452/500, V Loss: 16288.8284, Q Loss: 36067.9672
[IQL] Epoch 453/500, V Loss: 15718.5179, Q Loss: 51983.6955
[IQL] Epoch 454/500, V Loss: 16319.8690, Q Loss: 43050.2644
[IQL] Epoch 455/500, V Loss: 18279.1191, Q Loss: 36027.3464
[IQL] Epoch 456/500, V Loss: 13585.9131, Q Loss: 37803.1219
[IQL] Epoch 457/500, V Loss: 15408.8730, Q Loss: 36882.4561
[IQL] Epoch 458/500, V Loss: 17741.6649, Q Loss: 39779.7839
[IQL] Epoch 459/500, V Loss: 16248.9724, Q Loss: 32749.3797
[IQL] Epoch 460/500, V Loss: 17028.5558, Q Loss: 39880.7045
[IQL] Epoch 461/500, V Loss: 17236.3348, Q Loss: 36465.8330
[IQL] Epoch 462/500, V Loss: 17201.5956, Q Loss: 44331.4999
[IQL] Epoch 463/500, V Loss: 16363.6232, Q Loss: 33196.0460
[IQL] Epoch 464/500, V Loss: 17530.9684, Q Loss: 40131.0344
[IQL] Epoch 465/500, V Loss: 16230.2095, Q Loss: 41946.3684
[IQL] Epoch 466/500, V Loss: 17044.0239, Q Loss: 45836.4536
[IQL] Epoch 467/500, V Loss: 18184.3772, Q Loss: 39803.5843
[IQL] Epoch 468/500, V Loss: 17809.3325, Q Loss: 42618.7930
[IQL] Epoch 469/500, V Loss: 18222.9978, Q Loss: 43965.1297
[IQL] Epoch 470/500, V Loss: 17059.3420, Q Loss: 34618.1222
[IQL] Epoch 471/500, V Loss: 15335.0594, Q Loss: 36177.8176
[IQL] Epoch 472/500, V Loss: 15197.1720, Q Loss: 36820.6069
[IQL] Epoch 473/500, V Loss: 18202.9621, Q Loss: 34017.6303
[IQL] Epoch 474/500, V Loss: 14851.5498, Q Loss: 38014.6331
[IQL] Epoch 475/500, V Loss: 18160.7788, Q Loss: 32110.4967
[IQL] Epoch 476/500, V Loss: 15850.3605, Q Loss: 36512.3601
[IQL] Epoch 477/500, V Loss: 19482.7981, Q Loss: 43919.0088
[IQL] Epoch 478/500, V Loss: 15961.3950, Q Loss: 37041.6424
[IQL] Epoch 479/500, V Loss: 17523.8627, Q Loss: 40475.2237
[IQL] Epoch 480/500, V Loss: 16379.1048, Q Loss: 36980.8952
[IQL] Epoch 481/500, V Loss: 14728.7411, Q Loss: 36171.3800
[IQL] Epoch 482/500, V Loss: 13562.6425, Q Loss: 36874.6791
[IQL] Epoch 483/500, V Loss: 15698.8386, Q Loss: 43770.7059
[IQL] Epoch 484/500, V Loss: 16001.0403, Q Loss: 37683.0647
[IQL] Epoch 485/500, V Loss: 16725.0811, Q Loss: 41176.9700
[IQL] Epoch 486/500, V Loss: 20789.8772, Q Loss: 31937.8286
[IQL] Epoch 487/500, V Loss: 18162.9213, Q Loss: 33406.1151
[IQL] Epoch 488/500, V Loss: 18333.7645, Q Loss: 36058.9014
[IQL] Epoch 489/500, V Loss: 16531.1444, Q Loss: 42692.7433
[IQL] Epoch 490/500, V Loss: 18271.6602, Q Loss: 37842.0383
[IQL] Epoch 491/500, V Loss: 18380.7374, Q Loss: 33275.9741
[IQL] Epoch 492/500, V Loss: 14341.2060, Q Loss: 36379.8622
[IQL] Epoch 493/500, V Loss: 14591.9302, Q Loss: 31306.1735
[IQL] Epoch 494/500, V Loss: 15468.9764, Q Loss: 30569.1547
[IQL] Epoch 495/500, V Loss: 16969.7402, Q Loss: 42047.6097
[IQL] Epoch 496/500, V Loss: 16324.2465, Q Loss: 37876.7701
[IQL] Epoch 497/500, V Loss: 17085.5136, Q Loss: 32572.9213
[IQL] Epoch 498/500, V Loss: 16182.3491, Q Loss: 44778.4292
[IQL] Epoch 499/500, V Loss: 15307.2395, Q Loss: 41746.5910
[RL100] VIB betas set to factor=0.1: beta_recon=0.000010, beta_kl=0.000010

[RL100Trainer] Phase 2b: Offline RL Optimization (Iteration 4)
[OPE] Behavior policy value J_old = 2928.5904
[Offline RL] Epoch 0/100, PPO Loss: -0.0199, CD Loss: 0.2265
[Offline RL] Epoch 1/100, PPO Loss: -0.0180, CD Loss: 0.2232
[Offline RL] Epoch 2/100, PPO Loss: -0.0171, CD Loss: 0.2246
[Offline RL] Epoch 3/100, PPO Loss: -0.0160, CD Loss: 0.1967
[Offline RL] Epoch 4/100, PPO Loss: -0.0157, CD Loss: 0.1894
[Offline RL] Epoch 5/100, PPO Loss: -0.0142, CD Loss: 0.1958
[Offline RL] Epoch 6/100, PPO Loss: -0.0139, CD Loss: 0.1939
[Offline RL] Epoch 7/100, PPO Loss: -0.0136, CD Loss: 0.1597
[Offline RL] Epoch 8/100, PPO Loss: -0.0133, CD Loss: 0.1625
[Offline RL] Epoch 9/100, PPO Loss: -0.0145, CD Loss: 0.1172
[Offline RL] Epoch 10/100, PPO Loss: -0.0162, CD Loss: 0.1035
[Offline RL] Epoch 11/100, PPO Loss: -0.0166, CD Loss: 0.1157
[Offline RL] Epoch 12/100, PPO Loss: -0.0162, CD Loss: 0.1224
[Offline RL] Epoch 13/100, PPO Loss: -0.0162, CD Loss: 0.1185
[Offline RL] Epoch 14/100, PPO Loss: -0.0174, CD Loss: 0.1131
[Offline RL] Epoch 15/100, PPO Loss: -0.0185, CD Loss: 0.1148
[Offline RL] Epoch 16/100, PPO Loss: -0.0154, CD Loss: 0.1093
[Offline RL] Epoch 17/100, PPO Loss: -0.0146, CD Loss: 0.1073
[Offline RL] Epoch 18/100, PPO Loss: -0.0155, CD Loss: 0.1008
[Offline RL] Epoch 19/100, PPO Loss: -0.0136, CD Loss: 0.1009
[Offline RL] Epoch 20/100, PPO Loss: -0.0137, CD Loss: 0.0952
[Offline RL] Epoch 21/100, PPO Loss: -0.0138, CD Loss: 0.1008
[Offline RL] Epoch 22/100, PPO Loss: -0.0128, CD Loss: 0.0962
[Offline RL] Epoch 23/100, PPO Loss: -0.0122, CD Loss: 0.0948
[Offline RL] Epoch 24/100, PPO Loss: -0.0146, CD Loss: 0.0863
[Offline RL] Epoch 25/100, PPO Loss: -0.0125, CD Loss: 0.0919
[Offline RL] Epoch 26/100, PPO Loss: -0.0124, CD Loss: 0.0946
[Offline RL] Epoch 27/100, PPO Loss: -0.0136, CD Loss: 0.0920
[Offline RL] Epoch 28/100, PPO Loss: -0.0129, CD Loss: 0.0954
[Offline RL] Epoch 29/100, PPO Loss: -0.0127, CD Loss: 0.1007
[Offline RL] Epoch 30/100, PPO Loss: -0.0122, CD Loss: 0.0971
[Offline RL] Epoch 31/100, PPO Loss: -0.0134, CD Loss: 0.0908
[Offline RL] Epoch 32/100, PPO Loss: -0.0151, CD Loss: 0.0859
[Offline RL] Epoch 33/100, PPO Loss: -0.0153, CD Loss: 0.0933
[Offline RL] Epoch 34/100, PPO Loss: -0.0145, CD Loss: 0.0962
[Offline RL] Epoch 35/100, PPO Loss: -0.0146, CD Loss: 0.1026
[Offline RL] Epoch 36/100, PPO Loss: -0.0138, CD Loss: 0.1017
[Offline RL] Epoch 37/100, PPO Loss: -0.0139, CD Loss: 0.1111
[Offline RL] Epoch 38/100, PPO Loss: -0.0134, CD Loss: 0.1209
[Offline RL] Epoch 39/100, PPO Loss: -0.0149, CD Loss: 0.1244
[Offline RL] Epoch 40/100, PPO Loss: -0.0138, CD Loss: 0.1143
[Offline RL] Epoch 41/100, PPO Loss: -0.0144, CD Loss: 0.1190
[Offline RL] Epoch 42/100, PPO Loss: -0.0151, CD Loss: 0.1248
[Offline RL] Epoch 43/100, PPO Loss: -0.0160, CD Loss: 0.1246
[Offline RL] Epoch 44/100, PPO Loss: -0.0149, CD Loss: 0.1289
[Offline RL] Epoch 45/100, PPO Loss: -0.0161, CD Loss: 0.1300
[Offline RL] Epoch 46/100, PPO Loss: -0.0164, CD Loss: 0.1461
[Offline RL] Epoch 47/100, PPO Loss: -0.0166, CD Loss: 0.1552
[Offline RL] Epoch 48/100, PPO Loss: -0.0167, CD Loss: 0.1540
[Offline RL] Epoch 49/100, PPO Loss: -0.0164, CD Loss: 0.1492
[Offline RL] Epoch 50/100, PPO Loss: -0.0156, CD Loss: 0.1521
[Offline RL] Epoch 51/100, PPO Loss: -0.0153, CD Loss: 0.1467
[Offline RL] Epoch 52/100, PPO Loss: -0.0156, CD Loss: 0.1381
[Offline RL] Epoch 53/100, PPO Loss: -0.0141, CD Loss: 0.1285
[Offline RL] Epoch 54/100, PPO Loss: -0.0157, CD Loss: 0.1200
[Offline RL] Epoch 55/100, PPO Loss: -0.0152, CD Loss: 0.1141
[Offline RL] Epoch 56/100, PPO Loss: -0.0167, CD Loss: 0.1108
[Offline RL] Epoch 57/100, PPO Loss: -0.0153, CD Loss: 0.1051
[Offline RL] Epoch 58/100, PPO Loss: -0.0152, CD Loss: 0.1050
[Offline RL] Epoch 59/100, PPO Loss: -0.0148, CD Loss: 0.1059
[Offline RL] Epoch 60/100, PPO Loss: -0.0145, CD Loss: 0.1044
[Offline RL] Epoch 61/100, PPO Loss: -0.0154, CD Loss: 0.1031
[Offline RL] Epoch 62/100, PPO Loss: -0.0154, CD Loss: 0.1064
[Offline RL] Epoch 63/100, PPO Loss: -0.0170, CD Loss: 0.1217
[Offline RL] Epoch 64/100, PPO Loss: -0.0154, CD Loss: 0.1216
[Offline RL] Epoch 65/100, PPO Loss: -0.0165, CD Loss: 0.1191
[Offline RL] Epoch 66/100, PPO Loss: -0.0167, CD Loss: 0.1179
[Offline RL] Epoch 67/100, PPO Loss: -0.0167, CD Loss: 0.1114
[Offline RL] Epoch 68/100, PPO Loss: -0.0167, CD Loss: 0.1145
[Offline RL] Epoch 69/100, PPO Loss: -0.0174, CD Loss: 0.1184
[Offline RL] Epoch 70/100, PPO Loss: -0.0178, CD Loss: 0.1215
[Offline RL] Epoch 71/100, PPO Loss: -0.0184, CD Loss: 0.1308
[Offline RL] Epoch 72/100, PPO Loss: -0.0189, CD Loss: 0.1335
[Offline RL] Epoch 73/100, PPO Loss: -0.0182, CD Loss: 0.1320
[Offline RL] Epoch 74/100, PPO Loss: -0.0176, CD Loss: 0.1304
[Offline RL] Epoch 75/100, PPO Loss: -0.0191, CD Loss: 0.1396
[Offline RL] Epoch 76/100, PPO Loss: -0.0194, CD Loss: 0.1431
[Offline RL] Epoch 77/100, PPO Loss: -0.0189, CD Loss: 0.1444
[Offline RL] Epoch 78/100, PPO Loss: -0.0173, CD Loss: 0.1371
[Offline RL] Epoch 79/100, PPO Loss: -0.0164, CD Loss: 0.1320
[Offline RL] Epoch 80/100, PPO Loss: -0.0166, CD Loss: 0.1293
[Offline RL] Epoch 81/100, PPO Loss: -0.0176, CD Loss: 0.1367
[Offline RL] Epoch 82/100, PPO Loss: -0.0170, CD Loss: 0.1430
[Offline RL] Epoch 83/100, PPO Loss: -0.0169, CD Loss: 0.1430
[Offline RL] Epoch 84/100, PPO Loss: -0.0173, CD Loss: 0.1490
[Offline RL] Epoch 85/100, PPO Loss: -0.0170, CD Loss: 0.1352
[Offline RL] Epoch 86/100, PPO Loss: -0.0170, CD Loss: 0.1380
[Offline RL] Epoch 87/100, PPO Loss: -0.0181, CD Loss: 0.1373
[Offline RL] Epoch 88/100, PPO Loss: -0.0174, CD Loss: 0.1358
[Offline RL] Epoch 89/100, PPO Loss: -0.0176, CD Loss: 0.1432
[Offline RL] Epoch 90/100, PPO Loss: -0.0163, CD Loss: 0.1495
[Offline RL] Epoch 91/100, PPO Loss: -0.0164, CD Loss: 0.1534
[Offline RL] Epoch 92/100, PPO Loss: -0.0164, CD Loss: 0.1539
[Offline RL] Epoch 93/100, PPO Loss: -0.0158, CD Loss: 0.1465
[Offline RL] Epoch 94/100, PPO Loss: -0.0161, CD Loss: 0.1417
[Offline RL] Epoch 95/100, PPO Loss: -0.0166, CD Loss: 0.1524
[Offline RL] Epoch 96/100, PPO Loss: -0.0169, CD Loss: 0.1536
[Offline RL] Epoch 97/100, PPO Loss: -0.0172, CD Loss: 0.1583
[Offline RL] Epoch 98/100, PPO Loss: -0.0172, CD Loss: 0.1709
[Offline RL] Epoch 99/100, PPO Loss: -0.0166, CD Loss: 0.1789
[OPE] Policy REJECTED: J_new=2872.4623 ≤ J_old=2928.5904 + δ=146.4295. Rolling back to behavior policy.

[RL100Trainer] Phase 2c: Collecting New Data (Iteration 4)
[Collect] 50 episodes, success=0.000, steps=1250
[Data Collection] Success Rate: 0.000, Reward: 2305.08, Episodes: 50, Steps: 1250
[Dataset] Merged 50 episodes (1250 steps) → total 8250 steps, 260 episodes
[RL100] VIB betas set to factor=1.0: beta_recon=0.000100, beta_kl=0.000100

[RL100Trainer] Retraining IL on merged dataset...

============================================================
[RL100Trainer] Phase 1: Imitation Learning
============================================================

[IL] Epoch 0/100, Loss: 0.1635
[IL] Epoch 1/100, Loss: 0.1549
[IL] Epoch 2/100, Loss: 0.1590
[IL] Epoch 3/100, Loss: 0.1532
[IL] Epoch 4/100, Loss: 0.1578
[IL] Epoch 5/100, Loss: 0.1575
[IL] Epoch 6/100, Loss: 0.1585
[IL] Epoch 7/100, Loss: 0.1513
[IL] Epoch 8/100, Loss: 0.1505
[IL] Epoch 9/100, Loss: 0.1507
[IL] Epoch 10/100, Loss: 0.1477
[IL] Epoch 11/100, Loss: 0.1494
[IL] Epoch 12/100, Loss: 0.1541
[IL] Epoch 13/100, Loss: 0.1508
[IL] Epoch 14/100, Loss: 0.1532
[IL] Epoch 15/100, Loss: 0.1563
[IL] Epoch 16/100, Loss: 0.1442
[IL] Epoch 17/100, Loss: 0.1498
[IL] Epoch 18/100, Loss: 0.1550
[IL] Epoch 19/100, Loss: 0.1465
[IL] Epoch 20/100, Loss: 0.1547
[IL] Epoch 21/100, Loss: 0.1497
[IL] Epoch 22/100, Loss: 0.1546
[IL] Epoch 23/100, Loss: 0.1523
[IL] Epoch 24/100, Loss: 0.1505
[IL] Epoch 25/100, Loss: 0.1470
[IL] Epoch 26/100, Loss: 0.1482
[IL] Epoch 27/100, Loss: 0.1509
[IL] Epoch 28/100, Loss: 0.1457
[IL] Epoch 29/100, Loss: 0.1457
[IL] Epoch 30/100, Loss: 0.1461
[IL] Epoch 31/100, Loss: 0.1559
[IL] Epoch 32/100, Loss: 0.1447
[IL] Epoch 33/100, Loss: 0.1476
[IL] Epoch 34/100, Loss: 0.1514
[IL] Epoch 35/100, Loss: 0.1441
[IL] Epoch 36/100, Loss: 0.1462
[IL] Epoch 37/100, Loss: 0.1563
[IL] Epoch 38/100, Loss: 0.1510
[IL] Epoch 39/100, Loss: 0.1494
[IL] Epoch 40/100, Loss: 0.1527
[IL] Epoch 41/100, Loss: 0.1496
[IL] Epoch 42/100, Loss: 0.1545
[IL] Epoch 43/100, Loss: 0.1448
[IL] Epoch 44/100, Loss: 0.1456
[IL] Epoch 45/100, Loss: 0.1523
[IL] Epoch 46/100, Loss: 0.1462
[IL] Epoch 47/100, Loss: 0.1475
[IL] Epoch 48/100, Loss: 0.1511
[IL] Epoch 49/100, Loss: 0.1463
[IL] Epoch 50/100, Loss: 0.1474
[IL] Epoch 51/100, Loss: 0.1523
[IL] Epoch 52/100, Loss: 0.1471
[IL] Epoch 53/100, Loss: 0.1462
[IL] Epoch 54/100, Loss: 0.1495
[IL] Epoch 55/100, Loss: 0.1438
[IL] Epoch 56/100, Loss: 0.1494
[IL] Epoch 57/100, Loss: 0.1490
[IL] Epoch 58/100, Loss: 0.1485
[IL] Epoch 59/100, Loss: 0.1464
[IL] Epoch 60/100, Loss: 0.1523
[IL] Epoch 61/100, Loss: 0.1442
[IL] Epoch 62/100, Loss: 0.1467
[IL] Epoch 63/100, Loss: 0.1472
[IL] Epoch 64/100, Loss: 0.1456
[IL] Epoch 65/100, Loss: 0.1424
[IL] Epoch 66/100, Loss: 0.1511
[IL] Epoch 67/100, Loss: 0.1496
[IL] Epoch 68/100, Loss: 0.1426
[IL] Epoch 69/100, Loss: 0.1482
[IL] Epoch 70/100, Loss: 0.1475
[IL] Epoch 71/100, Loss: 0.1423
[IL] Epoch 72/100, Loss: 0.1499
[IL] Epoch 73/100, Loss: 0.1404
[IL] Epoch 74/100, Loss: 0.1472
[IL] Epoch 75/100, Loss: 0.1444
[IL] Epoch 76/100, Loss: 0.1461
[IL] Epoch 77/100, Loss: 0.1409
[IL] Epoch 78/100, Loss: 0.1428
[IL] Epoch 79/100, Loss: 0.1504
[IL] Epoch 80/100, Loss: 0.1447
[IL] Epoch 81/100, Loss: 0.1506
[IL] Epoch 82/100, Loss: 0.1455
[IL] Epoch 83/100, Loss: 0.1471
[IL] Epoch 84/100, Loss: 0.1446
[IL] Epoch 85/100, Loss: 0.1468
[IL] Epoch 86/100, Loss: 0.1362
[IL] Epoch 87/100, Loss: 0.1446
[IL] Epoch 88/100, Loss: 0.1449
[IL] Epoch 89/100, Loss: 0.1421
[IL] Epoch 90/100, Loss: 0.1450
[IL] Epoch 91/100, Loss: 0.1423
[IL] Epoch 92/100, Loss: 0.1471
[IL] Epoch 93/100, Loss: 0.1498
[IL] Epoch 94/100, Loss: 0.1393
[IL] Epoch 95/100, Loss: 0.1485
[IL] Epoch 96/100, Loss: 0.1462
[IL] Epoch 97/100, Loss: 0.1510
[IL] Epoch 98/100, Loss: 0.1451
[IL] Epoch 99/100, Loss: 0.1460
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
mean_traj_rewards: 3292.2072
mean_success_rates: 0.0000
test_mean_score: 0.0000
SR_test_L3: 0.5000
SR_test_L5: 0.4400

[Training] Complete! Checkpoints saved to:
  /nfs_global/S/yangrongzheng/RL100/3D-Diffusion-Policy/3D-Diffusion-Policy/checkpoints
Found 8 GPUs for rendering. Using device 0.
Job end at 2026-03-11 07:52:57
