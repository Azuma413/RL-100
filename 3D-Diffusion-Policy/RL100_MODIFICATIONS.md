# RL-100 代码修改文档

> 论文: [RL-100: Reinforcement Learning for 100% Robot Manipulation Success](https://arxiv.org/abs/2510.14830)
> 任务: MetaWorld dial-turn
> 修改日期: 2026-03-11

---

## 修改总览

| 编号 | 严重度 | 修改内容 | 文件 | 论文依据 |
|------|--------|----------|------|----------|
| **Fix-1** | 🔴 致命 | DDIM 时间步处理错误 | `rl100_policy.py` | Eq.5, Eq.7-8 |
| **Fix-2** | 🔴 致命 | 专家演示奖励标注不匹配 | `rl100_trainer.py` | §4 Reward Design |
| **Fix-3** | 🟡 重要 | 缺少奖励塑形 | `metaworld_runner.py` | §4 Reward Shaping |
| **Fix-4** | 🟡 重要 | CD 未与 PPO 联合优化 | `rl100_trainer.py`, `rl100.yaml` | Eq.22 |
| **Fix-5** | 🟡 重要 | AM-Q OPE 只用 H=1 | `rl100_trainer.py` | Eq.20 |
| **Fix-6** | 🟠 中等 | Phase 3 在线 RL 未实现 | `rl100_trainer.py`, `rl100.yaml` | Algorithm 1 Stage 3, Eq.21 |
| **Fix-7** | 🟡 重要 | VIB 缺少 LayerNorm + 解码器容量不足 | `pointnet_extractor.py` | Eq.15 |

---

## Fix-1: DDIM 时间步处理错误（致命 Bug）

### 问题描述

DDIM 使用子采样调度时（`num_train_timesteps=100`, `num_inference_steps=10`），调度器产生时间步序列如 `[90, 80, 70, 60, 50, 40, 30, 20, 10, 0]`。

**原代码**在 `denoising_step_with_log_prob` 和 `compute_ppo_loss` 中:
```python
alpha_t_prev = alphas_cumprod[t_tensor - 1]  # t=90 → 取 alphas_cumprod[89]
```

**正确做法**是取调度中的实际上一步:
```python
# t=90 → t_prev=80 → 取 alphas_cumprod[80]
```

### 影响分析

此 Bug 导致:
1. **DDIM 均值计算错误** (Paper Eq.5a): `μ = √ᾱ_{t_prev}·x̂₀ + √(1-ᾱ_{t_prev}-σ²)·ε_θ` 中的 `ᾱ_{t_prev}` 取值全部错误
2. **方差计算错误** (Paper Eq.23): `σ² = (1-ᾱ_{t_prev})/(1-ᾱ_t)·(1-ᾱ_t/ᾱ_{t_prev})` 同样错误
3. **Log probability 全部失效**: PPO 的重要性比率 `r_k = π_new/π_old` 基于错误的 log prob 计算
4. **PPO 更新方向错误**: 梯度信号完全被噪声主导，策略不可能通过 RL 改进

### 修改内容

**文件: `rl100_policy.py`**

1. `get_variance_at_timestep(timestep, prev_timestep)` — 新增 `prev_timestep` 参数
2. `denoising_step_with_log_prob(x_t, t, t_prev, global_cond)` — 新增 `t_prev` 参数
3. `conditional_sample_with_trajectory()` — 从 scheduler.timesteps 正确计算 t_prev
4. `compute_ppo_loss()` — 同步使用正确的 t_prev

**关键代码变更**:
```python
# 遍历时间步时计算真实的 t_prev
timesteps = scheduler.timesteps  # [90, 80, 70, ..., 0]
for i, t in enumerate(timesteps):
    if i + 1 < len(timesteps):
        t_prev = timesteps[i + 1]  # 90→80, 80→70, ...
    else:
        t_prev = torch.tensor(-1)  # 最后一步: 无噪声
```

---

## Fix-2: 专家演示奖励标注不匹配（致命 Bug）

### 问题描述

**原代码** `_relabel_demo_rewards()`:
- 专家轨迹：只在最后一步给 `reward=1.0`，其余为 `0.0`
- Chunk reward: 绝大多数转移的 `R_chunk ≈ 0`（仅最后一个 chunk 有 `≈ γ^j ≈ 很小值`）

**收集数据**（MetaWorld shaped reward）:
- 每步奖励高达 `~10`
- Chunk reward: `R_chunk = Σ γ^j·r_{t+j} ≈ 70-80`

**结果**: Q-network 看到两种完全不同尺度的奖励:
- 专家数据 Q-target ≈ 0 → 认为专家行为很差
- 收集数据 Q-target ≈ 70 → 认为随机行为很好
- IQL advantage 完全错误 → PPO 更新方向错误

### 修改内容

**文件: `rl100_trainer.py`**

将 `_relabel_demo_rewards()` 改为**每步密集奖励** `reward=10.0`，与 MetaWorld shaped reward 尺度一致:

```python
reward_per_step = 10.0  # 匹配 MetaWorld shaped reward 尺度
reward_array[start:end] = reward_per_step  # 专家全程 dense reward
```

这样专家轨迹的 chunk reward ≈ `10 * Σ γ^j ≈ 77`，与在线收集成功轨迹的 chunk reward 在同一数量级。

---

## Fix-3: 缺少奖励塑形（步骤惩罚 + 抖动惩罚）

### 论文依据 (§4)

论文明确描述了三部分奖励:
```
r_shaped = r_env + step_penalty + (-α · ||a_t - avg(a_{t-k:t})||²)
```
- **Step penalty**: 惩罚不必要的长轨迹
- **Jitter penalty**: 惩罚高频动作抖动

### 修改内容

**文件: `metaworld_runner.py`**

在 `run_and_collect()` 中添加奖励塑形:

```python
def run_and_collect(self, policy, num_episodes,
                    step_penalty=-0.01,          # 每步惩罚
                    jitter_penalty_alpha=0.1,    # 抖动惩罚系数
                    jitter_window=3):            # 抖动计算窗口

    # Step penalty
    shaped_reward += step_penalty

    # Jitter penalty: -α · ||a_t - mean(recent)||²
    recent_actions.append(first_action)
    if len(recent_actions) > 1:
        action_mean = np.mean(recent_actions[-window:], axis=0)
        jitter = np.sum((first_action - action_mean) ** 2)
        shaped_reward -= jitter_penalty_alpha * jitter
```

---

## Fix-4: 一致性蒸馏未与 PPO 联合优化

### 论文依据 (Eq.22)

```
L_total = L_RL + λ_CD · L_CD
```

论文要求 PPO 损失和 CD 损失在**同一个优化步**中联合反向传播。

### 原代码问题

PPO 和 CD 使用独立优化器、独立梯度步，无梯度耦合:
```python
# PPO: policy_optimizer.step()
# CD:  consistency_optimizer.step()  (完全独立)
```

### 修改内容

**文件: `rl100_trainer.py`**

在 `offline_rl_optimize()` 的内层 PPO 循环中联合计算:

```python
total_loss = ppo_loss
if self.global_step % cd_every == 0:
    cd_loss, cd_info = self.consistency_distillation.compute_distillation_loss(obs_dict)
    total_loss = ppo_loss + lambda_cd * cd_loss

# 同一 backward + 同时 step 两个优化器
total_loss.backward()
policy_optimizer.step()
consistency_optimizer.step()
```

**文件: `rl100.yaml`**

新增配置:
```yaml
lambda_cd: 1.0  # Paper Eq.22: L_total = L_RL + λ_CD·L_CD
```

---

## Fix-5: AM-Q OPE 改为多步 Transition Model Rollout

### 论文依据 (Eq.20)

```
Ĵ^{AM-Q}(π) = E_{(s,a)~(T̂,π)} [ Σ_{h=0}^{H-1} Q_ψ(s_h, a_h) ]
```

AM-Q 应通过 H 步 Transition Model 展开来估计策略价值。

### 原代码问题

仅做 H=1 单步估计 `E[Q(s, π(s))]`，不使用 Transition Model。

### 修改内容

**文件: `rl100_trainer.py`**

`_evaluate_policy_amq()` 改为 H=5 步 rollout:

```python
for h in range(rollout_horizon):  # H=5
    q = critics.get_q_value(cur_features, naction)
    batch_q_sum += (gamma ** h) * q
    # 使用 Transition Model 预测下一步
    next_features, _ = transition_model.predict_next_features(cur_features, naction)
    cur_features = next_features
```

---

## Fix-6: Phase 3 在线 RL 完整实现

### 论文依据 (Algorithm 1 Stage 3, Eq.21)

```
A_t^on = GAE(λ, γ; r_t, V_ψ)
L_RL^on = -J_i(π) + λ_V · E[(V_ψ(s_t) - V̂_t)²]
```

### 原代码问题

Phase 3 完全是 stub：关键训练行被注释掉，GAE 未实现。

### 修改内容

**文件: `rl100_trainer.py`**

完整实现 Phase 3:

1. **GAE 计算**: 对收集的在线轨迹，使用时序差分计算 GAE 优势
2. **V Loss**: `λ_V · MSE(V(s), Returns)` 更新 Value Network
3. **Q Loss**: Bellman backup 更新 Q Network
4. **PPO 更新**: 使用 GAE advantages 通过 `offline_rl_optimize` 更新策略
5. **数据融合**: 在线数据合并到 dataset

**文件: `rl100.yaml`**

新增配置:
```yaml
lambda_v: 0.5     # Value loss weight
gae_lambda: 0.95  # GAE λ parameter
```

---

## Fix-7: VIB 缺少 LayerNorm + 重建解码器容量不足

### 问题描述

VIB 开启后 IL 效果显著变差，beta_recon/beta_kl 必须设置极小值（0.0001）才能勉强不影响训练。

### Bug 1: VIB 路径跳过 LayerNorm

**非 VIB 路径**:
```python
x = self.final_projection(x)  # Linear(256→64) + LayerNorm(64)
```

**VIB 路径**（修复前）:
```python
mu = self.mu_layer(x)  # Linear(256→64)，无 LayerNorm
feat = z               # 直接输出，尺度不一致
```

下游 UNet 的 FiLM conditioning 是按 LayerNorm'd 特征设计的。VIB 特征缺少归一化导致条件信号尺度不稳定，扩散损失上升。

### Bug 2: 重建解码器容量严重不足

修复前 `recon_decoder`: `64→256→1536`（单隐层）。

经过 max-pooling 后空间信息已丢失，64 维向量通过单隐层 256 维无法重建 512×3=1536 个值。Chamfer distance 永远大且不收敛，产生噪声梯度反传破坏编码器。

### 修改内容

**文件: `pointnet_extractor.py`**（PointNetEncoderXYZ 和 PointNetEncoderXYZRGB）

1. 添加 `vib_norm`（与 `final_projection` 的归一化一致）:
```python
if final_norm == 'layernorm':
    self.vib_norm = nn.LayerNorm(out_channels)
else:
    self.vib_norm = nn.Identity()
```

2. 在 forward 中对 VIB 输出应用归一化:
```python
feat = self.vib_norm(z)       # 训练时
return self.vib_norm(mu)      # 推理时
```

3. 增大解码器容量:
```python
self.recon_decoder = nn.Sequential(
    nn.Linear(out_channels, 256),
    nn.ReLU(),
    nn.Linear(256, 512),       # 新增中间层
    nn.ReLU(),
    nn.Linear(512, 512 * 3)
)
```

### 修复后建议

修复后可适当增大 beta 值进行测试：
- `beta_recon: 0.001`（从 0.0001 提升 10 倍）
- `beta_kl: 0.001`
- 如果 IL 效果不降，可继续尝试 `beta_recon: 0.01`

---

## 附加说明: 未修改但值得关注的差异

### σ_max = 0.1 vs 论文 0.8

当前配置 `sigma_max: 0.1`（chunk mode），论文默认 `0.8`（single-step mode）。
0.1 是论文 chunk mode 的推荐值，保持不变。如果效果仍然不好可尝试适当增大到 0.2-0.3。

### PPO Loss 平均 vs 求和

```
论文: L = Σ_{k=1}^K (...)      # 求和
代码: L = (Σ_{k=1}^K (...)) / K  # 平均
```

平均相当于将学习率缩小 K 倍，效果等价于调整 LR。当前 `rl_policy_lr=1e-5` 已考虑此因素，保持不变。

### max_train_episodes = 90 vs 论文 100

少 10 条演示，影响有限。如有更多演示数据可增加至 100。

---

## 修改文件清单

| 文件 | 修改类型 |
|------|----------|
| `diffusion_policy_3d/policy/rl100_policy.py` | Fix-1: DDIM 时间步修复 |
| `diffusion_policy_3d/rl100_trainer.py` | Fix-2: 奖励重标注, Fix-4: CD联合优化, Fix-5: 多步AM-Q, Fix-6: Phase 3 |
| `diffusion_policy_3d/env_runner/metaworld_runner.py` | Fix-3: 奖励塑形 |
| `diffusion_policy_3d/config/rl100.yaml` | Fix-4/6: 新增 lambda_cd, lambda_v, gae_lambda |
| `diffusion_policy_3d/model/vision/pointnet_extractor.py` | Fix-7: VIB LayerNorm + 解码器容量 |

---

## 预期效果

1. **Fix-1 (DDIM时间步)**: PPO 梯度方向从完全随机 → 正确的策略改进方向。**这是效果提升的最关键修复。**
2. **Fix-2 (奖励尺度)**: Q-network 能正确评估专家行为的价值，advantage 信号有意义。
3. **Fix-3 (奖励塑形)**: 减少抖动和无效长轨迹，提升 sample efficiency。
4. **Fix-4 (CD联合优化)**: 1-step 推理质量与 K-step teacher 更好对齐。
5. **Fix-5 (多步AM-Q)**: OPE gate 判断更准确，减少误接受/误拒绝。
6. **Fix-6 (Online RL)**: 开启后可进一步利用在线交互数据提升性能上限。
7. **Fix-7 (VIB)**: VIB 特征与非 VIB 特征尺度一致，解码器梯度更稳定，可安全提升 beta 值增强正则化效果。
