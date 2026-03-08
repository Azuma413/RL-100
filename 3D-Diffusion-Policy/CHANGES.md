# RL-100 代码修改记录

## 概述

本文档记录了对 RL-100 训练框架（基于 3D Diffusion Policy）的全部修改，涵盖 Bug 修复、算法补全和新模块实现。

---

## 一、Config / 启动脚本修复

### 问题
1. `train_rl100.py` 中 `cfg.output_dir = output_dir` 报 `ConfigAttributeError`
2. `task.task_name: ${.name}` 插值 key 找不到，报 `InterpolationKeyError`

### 修复
- `hydra` config 中添加 `output_dir: ""`，使其成为合法的 struct key
- 修正 `task_name` 的插值引用路径

---

## 二、IQL Critics 维度不匹配修复

### 问题
```
RuntimeError: mat1 and mat2 shapes cannot be multiplied (256x260 and 132x256)
```
Critics 用 `obs_feature_dim=128` 初始化，但实际传入的是拼接后的
`obs_feature_dim × n_obs_steps = 128 × 2 = 256`，再加 action_dim=4，共 260。

### 修复（`rl100_trainer.py`）
```python
# 旧
obs_dim = self.policy.obs_feature_dim

# 新
obs_dim = self.policy.obs_feature_dim * self.policy.n_obs_steps
```

---

## 三、ConsistencyModel global_cond_dim 重复乘 n_obs_steps

### 问题
Teacher policy 用 `global_cond_dim = 256`，但 ConsistencyModel（student）被初始化为
`256 × 2 = 512`，与 teacher 架构不匹配。

### 修复（`rl100_trainer.py`）
```python
# 旧
global_cond_dim=obs_dim * self.policy.n_obs_steps   # 512，错误

# 新
global_cond_dim=obs_dim   # 256，与 teacher 一致
```

---

## 四、IQL Q 网络从未被训练

### 问题
```python
if 'reward' in batch and 'next_obs' in batch:   # next_obs 不在 zarr 数据集中
    ...  # Q 网络更新代码永远不执行
```

### 修复（`rl100_trainer.py`）
删除 `next_obs` 条件，改为通过 **TransitionModel** 预测 `next_obs_features`：
```python
if 'reward' in batch:
    next_obs_features, _ = self.transition_model.predict_next_features(
        obs_features, naction
    )
    q_loss, q_info = self.critics.compute_q_loss(
        obs_features, naction, reward, next_obs_features, done
    )
```

---

## 五、支持从 IL checkpoint 续训（跳过 IL 阶段）

### 背景
IL 训练耗时，希望加载 `after_il.ckpt` 后直接进入 Offline RL，不重跑 IL。

### 修改

**`rl100_trainer.py` — `run_pipeline` 新增 `skip_il` 参数**
```python
def run_pipeline(self, ..., skip_il: bool = False):
    if skip_il:
        # 从 dataset 同步 normalizer，跳过 IL 训练
        normalizer = initial_dataset.get_normalizer()
        self.policy.set_normalizer(normalizer)
        ...
    else:
        self.train_imitation_learning(...)
        self.save_checkpoint(tag='after_il')
```

Offline RL 循环也支持从中途迭代续训：
```python
start_iteration = self.offline_rl_iteration + 1 if skip_il and self.offline_rl_iteration > 0 else 0
for iteration in range(start_iteration, num_offline_iterations):
```

**`train_rl100.py`**
```python
skip_il = False
if cfg.training.resume and cfg.training.resume_path:
    trainer.load_checkpoint(cfg.training.resume_path)
    skip_il = True

trainer.run_pipeline(..., skip_il=skip_il)
```

**使用方式**
```bash
python train_rl100.py task=metaworld_dial-turn \
    training.resume=true \
    training.resume_path="/path/to/checkpoints/after_il.ckpt"
```

---

## 六、新增 Transition Model T_θ(s'|s, a)

### 背景
Algorithm 1 第 6 行要求训练世界模型 `T_θm(s'|s,a)`，原代码完全缺失。
参考 Uni-O4（`/home/yrz/Uni-O4/transition_model/`）的集成动力学模型实现。

### 新文件：`diffusion_policy_3d/model/rl/transition_model.py`

| 类 | 作用 |
|---|---|
| `EnsembleLinear` | 并行运行所有 ensemble member 的向量化线性层 |
| `EnsembleDynamicsModel` | 7 成员集成网络，输出 `(mean, logvar)` |
| `StandardScaler` | 对输入做 z-score 归一化 |
| `TransitionModel` | 高层封装，适配 DP3 的 obs feature 空间 |

**关键设计：在 obs feature 空间建模**
- 输入：`[obs_features(256) | norm_action(4)]` → 260 维
- 输出：`Δobs_features(256) + reward(1)` → 257 维（预测残差）
- 训练：7 成员集成，高斯 NLL + logvar 正则化 + 权重衰减，按 holdout MSE 选 top-5 elite

**集成进 `rl100_trainer.py`**
- `__init__` 中初始化 `self.transition_model`
- 新增 `train_transition_model()` 方法（Algorithm 1 Line 6）
- `run_pipeline` 中在每次 offline 迭代的 IQL 之前调用
- `save_checkpoint` / `load_checkpoint` 包含 transition model state

---

## 七、对照原文修复成功率归零问题

### 问题现象
IL 阶段成功率约 55%，进入 Offline RL 后降为 0%。

### 根因分析（对照论文 arXiv:2510.14830v3）

#### Bug A：OPE Gate（AM-Q 评估门控）缺失 ← 最关键
论文 Eq.20 / Algorithm 1 Lines 7-8 明确要求：
> PPO 训练后，用学习到的 transition model 评估候选策略，**只有当 `J_new - J_old ≥ 0.05|J_old|` 时才接受更新，否则回滚**。

原代码 PPO 训练完直接写入权重，没有任何门控，策略一旦被 PPO 推偏无法挽回。

#### Bug B：Offline RL 阶段 encoder 未冻结
论文原文：
> *"we keep ϕIL fixed and only update the task-specific heads of each module"*

原代码 PPO 更新了整个 policy 包括 obs_encoder，破坏了 IL 训练好的表征。

#### Bug C：DDIM mean 公式错误
论文 Eq.5a：
```
μ = √ᾱₘ · x̂₀ + √(1 - ᾱₘ - σ²) · εθ
```
原代码：
```python
mean = sqrt(alpha_t_prev) * pred_x0 + sqrt(1 - alpha_t_prev) * noise_pred
#                                         ↑ 缺少 -σ² 项
```
导致 log prob 基于错误分布，PPO 梯度方向出错。

#### Bug D：Advantage 未归一化 + PPO 损失按 K 步求和未归一化
原始优势值量级 5-10，K=10 步累加，梯度量级失控。

---

### 修复详情

#### Fix A：新增 `_evaluate_policy_amq` 方法 + OPE Gate（`rl100_trainer.py`）

```python
def _evaluate_policy_amq(self, dataset, num_batches=20) -> float:
    """
    AM-Q offline policy evaluation: E[Q(s, π(s))]
    用于判断候选策略是否优于 behavior policy
    """
    ...

def offline_rl_optimize(self, dataset, num_epochs):
    # Step 0: 评估 behavior policy 基准值
    j_old = self._evaluate_policy_amq(dataset)

    # Step 1: 保存权重快照
    policy_snapshot = copy.deepcopy(self.policy.state_dict())

    # Step 2: 冻结 encoder
    for param in self.policy.obs_encoder.parameters():
        param.requires_grad_(False)

    # Step 3: PPO 训练（含 advantage 归一化）
    for epoch in ...:
        advantages = (advantages - advantages.mean()) / (advantages.std() + 1e-8)
        ...

    # Step 4: 解冻 encoder
    for param in self.policy.obs_encoder.parameters():
        param.requires_grad_(True)

    # Step 5: OPE Gate — 接受/回滚
    j_new = self._evaluate_policy_amq(dataset)
    if j_new - j_old >= 0.05 * abs(j_old):
        # accept
    else:
        self.policy.load_state_dict(policy_snapshot)  # rollback
```

#### Fix B：冻结 encoder（见 Fix A Step 2/4）

#### Fix C：修正 DDIM mean 公式（`rl100_policy.py`）

```python
# 旧（错误）
mean = sqrt(alpha_t_prev) * pred_x0 + sqrt(1 - alpha_t_prev) * noise_pred

# 新（论文 Eq.5a）
noise_coeff = sqrt(max(1 - alpha_t_prev - sigma², 0))
mean = sqrt(alpha_t_prev) * pred_x0 + noise_coeff * noise_pred
```
同时修复 `denoising_step_with_log_prob` 和 `compute_ppo_loss` 两处。

#### Fix D：Advantage 归一化 + PPO 损失按 K 平均（两个文件）

```python
# rl100_trainer.py — advantage 归一化
advantages = (advantages - advantages.mean()) / (advantages.std() + 1e-8)

# rl100_policy.py — 按 K 步平均，不累加
total_ppo_loss = sum(ppo_losses) / len(ppo_losses)
```

---

## 修改文件列表

| 文件 | 修改类型 |
|---|---|
| `train_rl100.py` | 续训逻辑（skip_il） |
| `diffusion_policy_3d/rl100_trainer.py` | IQL 维度、Q 网络训练、TransitionModel 集成、OPE Gate、encoder 冻结、advantage 归一化 |
| `diffusion_policy_3d/policy/rl100_policy.py` | DDIM mean 公式、PPO loss 归一化 |
| `diffusion_policy_3d/model/rl/transition_model.py` | **新文件**，完整实现 T_θ(s'\|s,a) |

---

## 八、实现数据集合并（Algorithm 1 Lines 10-11）

### 背景
`run_pipeline` 中 "Merge D_{m+1} = D_m ∪ D_new" 仅有占位注释，`collect_new_data` 只返回 metrics，不保存轨迹数据。

### 修改

#### `metaworld_runner.py` — 新增 `run_and_collect()`
```python
def run_and_collect(self, policy, num_episodes) -> (metrics, episodes):
    # 与 run() 逻辑相同，额外在每步收集：
    #   state       = obs['agent_pos'][-1]       # [state_dim]
    #   action      = policy_output[0]           # first action of chunk [Da]
    #   point_cloud = obs['point_cloud'][-1]     # [N, 6]
    #   reward      = env.step() return          # scalar
    #   done        = episode termination flag
    # 每个 episode 打包为 numpy dict，返回 episodes 列表
```

#### `metaworld_dataset.py` — 新增 `merge_episodes()`
```python
def merge_episodes(self, episodes: list) -> int:
    for ep in episodes:
        self.replay_buffer.add_episode(ep)   # 调用 ReplayBuffer.add_episode()
    # 重建 SequenceSampler（包含全部 episodes，无 episode cap）
    self.sampler = SequenceSampler(replay_buffer=..., episode_mask=all_true)
    return n_new_steps
```

#### `rl100_trainer.py` — `collect_new_data` 返回 episodes，pipeline 调用合并
```python
# collect_new_data 现在返回 (metrics, episodes)
collection_metrics, new_episodes = self.collect_new_data(env_runner, num_episodes)

# Algorithm 1 Line 11: D_{m+1} = D_m ∪ D_new
if new_episodes:
    n_new = current_dataset.merge_episodes(new_episodes)
    # → current_dataset 已包含新数据，后续 IL retrain 自动在扩充后的数据集上训练
```

### 数据流
```
env_runner.run_and_collect()
    → per-step (state, action, pc, reward, done)
    → episodes: list[dict[str, np.ndarray]]

current_dataset.merge_episodes(episodes)
    → replay_buffer.add_episode() × N
    → SequenceSampler 重建（包含新 episodes）

下一迭代的 train_transition_model / train_iql_critics / offline_rl_optimize
    → 自动使用扩充后的 current_dataset
```

---

## 当前仍未实现的部分

| 功能 | 状态 | 说明 |
|---|---|---|
| Online RL（Phase 3） | ⚠️ 只收集 + 合并数据 | IQL + PPO online 更新逻辑被注释 |
