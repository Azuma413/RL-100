# RL-100 论文-代码对应审计文档

> 论文：[RL-100: A Real-World Reinforcement Learning Framework](https://arxiv.org/abs/2510.14830)
> 实验环境：Meta-World dial-turn 任务
> 审计时间：2026-03-09

---

## 目录

1. [总体结构对应](#1-总体结构对应)
2. [Phase 1：模仿学习 IL](#2-phase-1模仿学习-il)
3. [Phase 2：迭代离线 RL](#3-phase-2迭代离线-rl)
4. [Phase 3：在线 RL 微调](#4-phase-3在线-rl-微调)
5. [网络架构对应](#5-网络架构对应)
6. [奖励设计对应](#6-奖励设计对应)
7. [关键超参数对比](#7-关键超参数对比)
8. [⚠️ 实现偏差与未实现项汇总](#8-️-实现偏差与未实现项汇总)

---

## 1. 总体结构对应

### 论文 Algorithm 1（三阶段流程）

```
输入: 专家演示数据集 D_0（100条）
输出: 最终策略 π_θ

Stage 1: π_θ ← IL(D_0)
Stage 2: For m = 1..M:
   T_θ ← TrainTransitionModel(D_m)       // Line 6
   Q_ψ, V_ψ ← IQL(D_m, T_θ)             // Line 5
   π_θ ← OfflineRL(π_θ, Q_ψ, V_ψ)       // Line 7-8 + OPE Gate
   D_new ← Rollout(π_θ)                  // Line 10
   D_{m+1} ← D_m ∪ D_new                 // Line 11
   π_θ ← IL(D_{m+1})                     // Line 13
Stage 3: π_θ ← OnlineRL(π_θ)            // GAE + fresh rollouts
```

### 代码对应（`rl100_trainer.py: run_pipeline`）

| 步骤 | 论文 | 代码位置 | 状态 |
|------|------|----------|------|
| Stage 1 | IL(D_0) | `train_imitation_learning()` | ✅ 实现 |
| Line 6 | TrainTransitionModel | `train_transition_model()` | ✅ 实现 |
| Line 5 | IQL(D, T_θ) | `train_iql_critics()` | ✅ 实现 |
| Line 7-8 | OfflineRL + OPE | `offline_rl_optimize()` | ✅ 部分实现（见§8） |
| Line 10 | Rollout | `collect_new_data()` | ✅ 实现 |
| Line 11 | D∪D_new | `dataset.merge_episodes()` | ✅ 实现 |
| Line 13 | IL(D_{m+1}) | `train_imitation_learning()` | ✅ 实现 |
| Stage 3 | OnlineRL | `run_pipeline() online block` | ❌ **未完整实现** |

---

## 2. Phase 1：模仿学习 (IL)

### 论文描述

**损失函数（Eq.14）：**
```
L_IL(θ) = E_{(a^τ0, ct)~D, τ, ε} [ ||ε - ε_θ(a^τ, τ, ct)||² ]

L_total_IL = L_IL + β_recon·(d_Chamfer(ô,o) + ||q̂-q||²) + β_KL·KL(ϕ(z|o,s) || N(0,I))
```
- 观测条件向量 `c_t = [ϕ(o_i, q_i)]_{i=t-n_o+1}^{t}`，n_o=2
- 在 RL 微调时 β_recon 和 β_KL 减小 10 倍

### 代码对应

| 组件 | 代码位置 | 状态 |
|------|----------|------|
| 扩散损失 L_IL | `dp3.py: compute_loss()` → `noise_scheduler.add_noise` + MSE | ✅ |
| 重建损失（Chamfer + prop）| `pointnet_extractor.py`（VIB 路径）| ✅ `use_recon_vib=true` |
| KL 散度损失 | `pointnet_extractor.py` | ✅ `beta_kl=0.001` |
| β 动态缩放 | `rl100_trainer.py: _apply_vib_betas(0.1)` | ✅ |
| n_obs_steps=2 | `rl100.yaml: n_obs_steps: 2` | ✅ |
| EMA 策略 | `EMAModel` + `ema.step()` | ✅ |

**注意**：`_apply_vib_betas(0.1)` 在 RL 阶段将 β_recon 从 1.0 → 0.1，β_KL 从 0.001 → 0.0001，符合论文"减小 10 倍"的描述。

---

## 3. Phase 2：迭代离线 RL

### 3a. IQL Critics

**论文描述（Eq.15-17）：**
```
L_V = E_{(s,a)~D} [ L_τ^2(Q_ψ(s,a) - V_ψ(s)) ]   // Expectile regression, τ=0.7
  其中 L_τ^2(u) = |τ - 1{u<0}| · u²

L_Q = E_{(s,a,r,s')~D} [ (r + γV_ψ^-(s') - Q_ψ(s,a))² ]

A(s,a) = Q_ψ(s,a) - V_ψ(s)
```

**代码对应（`iql_critics.py`，`rl100_trainer.py: train_iql_critics`）：**

| 组件 | 代码位置 | 状态 |
|------|----------|------|
| V 网络 Expectile 回归 (τ=0.7) | `iql_critics.py: compute_v_loss()` | ✅ |
| Q 网络 Bellman 回归 | `iql_critics.py: compute_q_loss()` | ✅ |
| 目标 V 网络软更新 (τ_target=0.005) | `update_target_network(tau=0.005)` | ✅ |
| 优势 A = Q - V | `critics.compute_advantage()` | ✅ |
| 用 T_θ 预测下一步 obs features | `transition_model.predict_next_features()` | ✅ |
| 训练期间冻结 Diffusion Actor | `policy.eval()` + `requires_grad_(False)` | ✅ |
| 专家演示奖励重标注（sparse） | `_relabel_demo_rewards()` | ✅ |

### 3b. PPO 策略优化（两级 MDP）

**论文描述（Eq.7-8）：**

扩散去噪过程建模为 K 步子 MDP：
```
π_θ(a|s) = ∏_{k=1}^{K} π_θ(a^{τ_{k-1}} | a^{τ_k}, s)

每步为高斯分布：π_θ(·|a^{τ_k}, s) = N(μ_θ(a^{τ_k}, τ_k, s), σ_k²·I)

离线 PPO 目标（Eq.18）：
J_i(π) = E[ Σ_{k=1}^{K} min(r_k(π)·A_t, clip(r_k(π), 1-ε, 1+ε)·A_t) ]

r_k^off(π) = π(a^{τ_{k-1}}|s^k) / π_i(a^{τ_{k-1}}|s^k)
A_t^off = Q_ψ(s_t, a_t) - V_ψ(s_t)   // IQL 优势
```

**DDIM 均值计算（Eq.5）：**
```
μ_θ(x_t, t→m) = √ᾱ_m · x̂_0(x_t, t) + √(1 - ᾱ_m - σ²_{t→m}) · ε_θ(x_t, t)
```

**方差裁剪（Eq.23）：**
```
σ̃_k = clip(σ_k, σ_min, σ_max)
```

**代码对应（`rl100_policy.py`）：**

| 组件 | 代码位置 | 状态 |
|------|----------|------|
| K 步子 MDP 分解 | `conditional_sample_with_trajectory()` | ✅ |
| 高斯分布 log prob | `compute_gaussian_log_prob()` | ✅ |
| 单步去噪 + log prob | `denoising_step_with_log_prob()` | ✅ |
| DDIM 均值公式（Eq.5） | `mean = sqrt(α_{t-1})*x̂_0 + sqrt(1-α_{t-1}-σ²)*ε` | ✅ |
| 方差裁剪（Eq.23） | `get_variance_at_timestep()` with clamp | ✅ |
| PPO 损失计算 | `compute_ppo_loss()` | ✅ |
| K 步平均（非求和） | `sum(ppo_losses) / len(ppo_losses)` | ✅ |
| 优势归一化 | `(A - mean) / (std + 1e-8)` | ✅ |
| 旧轨迹采样一次（固定 π_old） | `sample_for_ppo()` + `no_grad` | ✅ |
| 内层 PPO 循环 | `ppo_inner_steps=4` 个梯度步 | ✅ |
| RL 阶段冻结 obs_encoder | `obs_encoder.requires_grad_(False)` | ✅ |
| RL 阶段降低 LR（10×） | `rl_policy_lr=1e-5`（IL 为 1e-4） | ✅ |
| 梯度裁剪 | `clip_grad_norm_(max_grad_norm=1.0)` | ✅ |

### 3c. 一致性蒸馏

**论文描述（Eq.9，Eq.22）：**
```
L_CD(θ) = E_{x_0,τ,ε}[ ||C_θ(x^τ, τ) - sg[Ψ_φ(x^τ, τ→0)]||² ]

组合损失（Eq.22）：L_total = L_RL + λ_CD · L_CD
```
推理时：单步生成 `x_0 ≈ C_θ(x^{τ_K}, τ_K)`，实现 K 倍加速。

**代码对应（`consistency_model.py`，`offline_rl_optimize`）：**

| 组件 | 代码位置 | 状态 |
|------|----------|------|
| 一致性模型架构（同 DP3） | `ConsistencyModel`（ConditionalUnet1D） | ✅ |
| 蒸馏损失（L2，Teacher=K步DDIM） | `ConsistencyDistillation.train_step()` | ✅ |
| 每 N 步执行蒸馏 | `cd_every=5` | ✅ |
| **Eq.22 组合损失 `L_RL + λ_CD·L_CD`** | **CD 与 PPO 使用独立优化器，未加权求和** | ❌ |
| 快速单步推理（eval 时用 CM） | `eval_rl100.py`（需确认） | ⚠️ 待确认 |

### 3d. OPE Gate（离线策略评估门控）

**论文描述（Eq.20）：**
```
Ĵ^{AM-Q}(π) - Ĵ^{AM-Q}(π_i) ≥ δ
δ = 0.05 · |Ĵ^{AM-Q}(π_i)|   // 自适应阈值

AM-Q 通过 H 步 transition model rollout 估计策略价值
```

**代码对应（`rl100_trainer.py: _evaluate_policy_amq`，`offline_rl_optimize`）：**

| 组件 | 代码位置 | 状态 |
|------|----------|------|
| OPE 接受/拒绝门控 | `j_new - j_old >= 0.05 * abs(j_old)` | ✅ |
| 拒绝时回滚 policy snapshot | `policy.load_state_dict(policy_snapshot)` | ✅ |
| **AM-Q 多步 rollout（H 步 transition model）** | **代码仅做 H=1 单步估计 E[Q(s,π(s))]** | ❌ |

### 3e. 数据收集与融合

| 组件 | 代码位置 | 状态 |
|------|----------|------|
| 环境 rollout 收集 | `MetaworldRunner.run_and_collect()` | ✅ |
| 数据集 episode 合并 | `MetaworldDataset.merge_episodes()` | ✅ |
| 合并后重建 sampler | `SequenceSampler` 重建 | ✅ |
| 合并后继续 IL 训练 | `retrain_il_after_collection=true` | ✅ |

---

## 4. Phase 3：在线 RL 微调

**论文描述（Algorithm 1 Stage 3）：**
- 使用在线 GAE 优势（Eq.21）：`A_t^on = GAE(λ, γ; r_t, V_ψ)`
- 损失：`L_RL^on = -J_i(π) + λ_V · E[(V_ψ(s_t) - V̂_t)²]`
- 继续 PPO 更新，不再做 IL 重训练

**代码对应：**

| 组件 | 代码位置 | 状态 |
|------|----------|------|
| 在线数据收集 | `collect_new_data()` | ✅ 结构存在 |
| **GAE 优势计算** | **未实现，代码仅有占位注释** | ❌ |
| **Critic + Policy 在线更新** | **关键行被注释掉** | ❌ |
| 配置关闭 | `run_online_rl: false` | ⚠️ 整个 Phase 3 默认关闭 |

`rl100_trainer.py:930-941` 中的 Phase 3 代码：
```python
# Update critics and policy
# Note: Would need online dataset here
# self.train_iql_critics(...)
# self.offline_rl_optimize(...)
```
这两行被注释，Phase 3 目前仅收集数据，**不执行任何梯度更新**。

---

## 5. 网络架构对应

### 5.1 扩散策略骨干

| 参数 | 论文 | 代码（rl100.yaml） | 状态 |
|------|------|-------------------|------|
| 观测窗口 n_o | 2 | `n_obs_steps: 2` | ✅ |
| 动作块大小 n_c | 8-16 | `n_action_steps: 8`，`horizon: 16` | ✅ |
| 去噪步数 K | 5-10 | `num_inference_steps: 10` | ✅ |
| 扩散训练步数 | 100 | `num_train_timesteps: 100` | ✅ |
| 噪声调度器 | DDIM | `DDIMScheduler` | ✅ |
| 预测类型 | epsilon | `prediction_type: epsilon` | ✅ |
| 噪声调度 | squaredcos_cap_v2 | `beta_schedule: squaredcos_cap_v2` | ✅ |
| UNet 通道 | 未具体指定 | `down_dims: [512, 1024, 2048]` | ✅ 合理 |
| 嵌入维度 | 未具体指定 | `diffusion_step_embed_dim: 128` | ✅ 合理 |
| 条件类型 | FiLM | `condition_type: film` | ✅ |

### 5.2 点云编码器（DP3 PointNet）

| 参数 | 论文 | 代码 | 状态 |
|------|------|------|------|
| 输出维度 | 未指定 | `encoder_output_dim: 64` | ✅ |
| VIB 正则化 | ✅（重建+KL） | `use_recon_vib: true` | ✅ |
| LayerNorm | 论文提及 | `use_layernorm: true` | ✅ |
| shape_meta 点数 | — | `[512, 3]` | ✅ |
| **Runner 实际采样点数** | — | `num_points: 1024` | ⚠️ **与 shape_meta 512 不符** |

### 5.3 IQL Critics

| 参数 | 论文 | 代码 | 状态 |
|------|------|------|------|
| V 网络结构 | MLP | `hidden_dims: [256, 256, 256]` | ✅ |
| Q 网络（双网络） | Twin Q | Twin Q networks | ✅ |
| Expectile τ | 0.7 | `tau: 0.7` | ✅ |
| 折扣因子 γ | 0.99 | `gamma: 0.99` | ✅ |
| 目标 V 软更新 | ✅ | `target_update_tau: 0.005` | ✅ |

### 5.4 Transition Model（集成世界模型）

| 参数 | 论文 | 代码 | 状态 |
|------|------|------|------|
| 集成数量 | 未指定 | 7 成员 | ✅ 合理 |
| Elite 数量 | 未指定 | 5 | ✅ 合理 |
| 激活函数 | 未指定 | Swish | ✅ 合理 |
| 预测残差 Δfeatures | ✅ | ✅ | ✅ |
| 隐藏层维度 | 未指定 | `(200, 200, 200, 200)` | ⚠️ 可能偏小 |
| 提前停止 | ✅ | `max_epochs_since_update=5` | ✅ |

### 5.5 一致性模型

| 参数 | 论文 | 代码 | 状态 |
|------|------|------|------|
| 架构（同 Teacher） | ✅ | 同 ConditionalUnet1D | ✅ |
| 蒸馏损失 | L2 | MSE(student, sg[teacher]) | ✅ |
| **λ_CD 加权组合** | Eq.22 中存在 | **无权重，独立优化** | ❌ |

---

## 6. 奖励设计对应

### 论文描述

**稀疏奖励（大多数任务）：**
```
r_t = 0，最终成功时 r_T = +1
+ 步骤惩罚（discourage long trajectories）
+ 动作抖动惩罚：-α · ||a_t - avg(a_{t-k:t})||²
```

**动作块折扣奖励（chunk mode）：**
```
R_chunk = Σ_{j=0}^{n_c-1} γ^j · R_{t+j}
```

### 代码对应（dial-turn 任务）

| 组件 | 论文 | 代码 | 状态 |
|------|------|------|------|
| 任务环境稀疏奖励 | ✅ | 使用 Meta-World 环境原生奖励 | ✅ |
| 专家演示奖励重标注 | ✅ | `_relabel_demo_rewards()`（末步=1）| ✅ |
| **步骤惩罚（step penalty）** | ✅ | **未实现** | ❌ |
| **动作抖动惩罚（jitter penalty）** | ✅ | **未实现** | ❌ |
| **动作块折扣奖励 R_chunk** | ✅ | **未实现，使用单步奖励** | ❌ |

---

## 7. 关键超参数对比

| 超参数 | 论文 | 代码（dial-turn） | 差异 |
|--------|------|-------------------|------|
| 专家演示数量 | **100** | `max_train_episodes: 90` | ⚠️ 少 10 条 |
| 去噪步数 K | 5-10 | 10 | ✅ |
| 观测窗口 n_o | 2 | 2 | ✅ |
| 动作块 n_c | 8-16 | 8 | ✅ |
| PPO clip ε | 0.2 | `ppo_clip_eps: 0.2` | ✅ |
| σ_min | 0.01 | 0.01 | ✅ |
| **σ_max** | **0.8（论文值）** | **0.1（代码：chunk mode）** | ⚠️ 差异 8× |
| OPE 阈值 δ | 0.05·\|J_old\| | `0.05 * abs(j_old)` | ✅ |
| RL 阶段 β 缩放 | 10× 缩小 | `_apply_vib_betas(0.1)` | ✅ |
| 离线 RL 迭代 M | 未指定 | `num_offline_iterations: 5` | ✅ 合理 |
| 每轮收集 episodes | 未指定 | `collection_episodes: 50` | ✅ 合理 |
| PPO 内层步数 | 未指定 | `ppo_inner_steps: 4` | ✅ 合理 |
| IL LR | 未指定 | `1e-4` | ✅ 合理 |
| RL LR | 未指定（10× 缩小） | `rl_policy_lr: 1e-5` | ✅ |
| IQL V/Q LR | 未指定 | `3e-4` | ✅ 合理 |
| batch_size | 未指定 | 256 | ✅ 合理 |

---

## 8. ⚠️ 实现偏差与未实现项汇总

### 🔴 严重缺失（功能性未实现）

#### [Missing-1] Phase 3 在线 RL 完全未实现

- **论文**：Stage 3 使用 GAE 优势进行在线 PPO 更新，包含 value loss（Eq.21）
- **代码**：`run_online_rl: false`，critic/policy 更新代码被注释（`rl100_trainer.py:930-941`）
- **影响**：实验仅执行到离线 RL 阶段，无法达到论文中的在线性能上限
- **代码证据**：
  ```python
  # self.train_iql_critics(...)   # 被注释
  # self.offline_rl_optimize(...) # 被注释
  ```

#### [Missing-2] GAE 优势计算未实现

- **论文（Eq.21）**：`A_t^on = GAE(λ, γ; r_t, V_ψ)`，在线 RL 使用时序差分 GAE 优势
- **代码**：仅有 IQL 离线优势 A = Q - V，无 GAE 实现
- **影响**：即使启用 Phase 3，也无法正确计算在线优势估计

#### [Missing-3] 奖励塑形（Reward Shaping）未实现

- **论文**：稀疏奖励 **+** 步骤惩罚 **+** 动作抖动惩罚（`-α·||a_t - ā_t||²`）
- **代码**：dial-turn 仅使用 Meta-World 环境原生稀疏奖励（0/1 success），无额外惩罚项
- **影响**：策略可能产生不必要的长轨迹和高频抖动动作；收敛速度可能慢于论文
- **建议**：在 `MetaworldRunner.run_and_collect()` 收集时叠加步骤惩罚和抖动惩罚

#### [Missing-4] 动作块折扣奖励（Chunk Reward）未实现

- **论文**：`R_chunk = Σ_{j=0}^{n_c-1} γ^j · R_{t+j}`（一个 chunk 对应多步累积折扣奖励）
- **代码**：`dataset.__getitem__` 中奖励取单步标量 `sample['reward'][0]`
- **影响**：Q 值估计的目标奖励与论文设计不一致，n_action_steps=8 时影响明显

---

### 🟡 实现与论文存在差异

#### [Diff-1] σ_max 偏差显著（8×）

- **论文**：`σ_max = 0.8`（探索方差上限）
- **代码**：`sigma_max: 0.1`（注释说明为 chunk mode 设定）
- **分析**：论文中 0.8 可能针对 single-step control；chunk mode 下 0.1 降低探索强度，对 RL 改进幅度可能有影响
- **位置**：`rl100.yaml: sigma_max: 0.1`

#### [Diff-2] AM-Q OPE 为 H=1 单步近似

- **论文**：AM-Q 通过 H 步 Transition Model 展开来估计策略价值（多步前瞻）
- **代码**：`_evaluate_policy_amq()` 仅计算单步 `E[Q(s, π(s))]`，代码注释已标注为"H=1 approximation"
- **影响**：OPE gate 的判断精度降低，特别是对长视野任务（如 dial-turn）可能误判

#### [Diff-3] 一致性蒸馏损失未与 PPO 联合优化

- **论文（Eq.22）**：`L_total = L_RL + λ_CD · L_CD`（单一优化目标）
- **代码**：PPO 使用 `policy_optimizer` 独立优化，CD 使用 `consistency_optimizer` 独立优化，两者无梯度耦合
- **影响**：Policy 和 Consistency Model 的参数不共享梯度流，可能导致推理时性能差距

#### [Diff-4] 专家演示使用数量偏少

- **论文**："RL-100" = 使用 100 条专家演示
- **代码**：`max_train_episodes: 90`（加上 val_ratio=0.02 约取 2 条验证，训练实际用 90 条）
- **分析**：少 10 条演示对 BC 初始化质量有一定影响

#### [Diff-5] 点云数量不一致（Runner vs Dataset）

- **Dataset shape_meta**：`point_cloud shape: [512, 3]`
- **Runner 采样**：`num_points: 1024`（`metaworld_dial-turn.yaml`）
- **现状**：`use_point_crop=true` 可能在 Runner 中将 1024 点裁剪为 512，但需确认
- **风险**：若裁剪逻辑不一致，训练与推理的点云分布可能不同

---

### 🟢 已实现但值得关注的细节

#### [Note-1] VIB Beta 缩放的实际作用域

- `_apply_vib_betas(0.1)` 在 `offline_rl_optimize` 之前调用
- 但 `offline_rl_optimize` 内部冻结了 `obs_encoder`（`requires_grad_(False)`）
- 因此 VIB beta 缩小在 RL 优化阶段**对 obs_encoder 梯度无实际影响**
- 其效果仅体现在：RL 完成后 `_apply_vib_betas(1.0)` 恢复之前，IL 重训练阶段的 VIB 正则化强度

#### [Note-2] 混合数据集的奖励分布差异

- 专家演示：`reward=1` at terminal，其余为 0（人工重标注）
- 在线收集数据：使用 Meta-World 原生奖励（实时 success 信号，数值范围可能不同）
- 混合后 Q 网络看到两种不同奖励尺度，建议统一奖励归一化

---

## 附录：文件与论文章节对应关系

| 代码文件 | 对应论文章节 |
|----------|-------------|
| `rl100_trainer.py` | Algorithm 1（完整三阶段流程） |
| `rl100_policy.py` | §3.2 Denoising MDP + Eq.7-8（K步PPO） |
| `model/rl/iql_critics.py` | §3.3 IQL Critics + Eq.15-17 |
| `model/rl/consistency_model.py` | §3.4 Consistency Distillation + Eq.9, 22 |
| `model/rl/transition_model.py` | Algorithm 1 Line 6（集成世界模型） |
| `model/vision/pointnet_extractor.py` | §3.1 Visual Encoder + VIB（Eq.14） |
| `dataset/metaworld_dataset.py` | §4.1 Dataset 管理 |
| `env_runner/metaworld_runner.py` | §4.2 Environment 交互 |
| `config/rl100.yaml` | §4 实验超参数 |
| `config/task/metaworld_dial-turn.yaml` | §4 dial-turn 任务配置 |
