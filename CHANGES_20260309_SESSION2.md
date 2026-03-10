# 本次会话修改记录（2026-03-09 第二轮）

## 背景：什么出了问题

用户在 IDE 中手动将 `use_recon_vib: true`（开启 VIB），随后训练出现：
- IL 阶段 loss 高居 0.2 无法下降
- 把 beta_recon 调到 0.01 后 loss 下降，但成功率从 0.5 跌至 0.05-0.15

---

## 一、根本原因分析

### VIB 为何不能加载到无-VIB checkpoint 上

**论文原文（第7页，Shared and frozen encoders 节）：**
> "all components in our offline RL pipeline share the same **fixed visual encoder φ pre-trained during imitation learning**. During offline RL, we keep φ^IL fixed and only update the task-specific heads of each module."

关键事实：
1. **VIB 层（mu_layer, logvar_layer, recon_decoder, state_recon_decoder）是 encoder 的一部分**
2. Encoder 需要在 IL 阶段与 VIB 一起从头训练，才能学会有意义的均值/方差和重建
3. `after_il.ckpt` 是用 `use_recon_vib: false` 训练的，**不含这些层**
4. 用 `strict=False` 加载后，VIB 层随机初始化
5. IL 重训练时，随机 decoder 产生极大的重建 loss（`β_recon * chamfer(random_recon, pc)`）
6. 这个 loss 压倒 BC loss，将策略彻底破坏 → 成功率崩溃

**结论：VIB 必须从 IL 阶段第一个 epoch 开始训练，不能在已有 checkpoint 上"补插"。**

---

## 二、本次修改内容

### 2.1 修复：关闭 VIB（恢复原始行为）

**文件：`diffusion_policy_3d/config/rl100.yaml`**

```yaml
# 修改前
use_recon_vib: true

# 修改后
use_recon_vib: false
# 新增注释：如需 VIB，必须从 demo 数据重新训练 IL，不可加载非 VIB checkpoint
```

**效果：恢复到 checkpoint 原始架构，IL 阶段不再有随机 decoder 造成的 loss 爆炸。**

---

### 2.2 新增：Chunk 折扣奖励（论文缺失实现）

**论文原文（第6页 Action Chunk 节）：**
> R_chunk = R_{t:t+n_c-1} = Σ_{j=0}^{n_c-1} γ^j R_{t+j}
> "the equivalent discount factor between chunks is γ^n_c"

**原始代码问题：**
```python
data['reward'] = np.array(sample['reward'][0])  # 只取第 0 步奖励
next_idx = buffer_start_idx + 1                 # next_obs 仅前进 1 步
```

**修复后（`dataset/metaworld_dataset.py`）：**
```python
# R_chunk = Σ_{j=0}^{n_c-1} γ^j · r_{t+j}
raw_rewards = sample['reward'][:nc]
discount = [gamma**j for j in range(nc)]
chunk_reward = dot(discount, raw_rewards)

# done = 任意 chunk 内步骤终止
done = sample['done'][:nc].any()

# next_obs 前进 n_action_steps=8 步
next_idx = buffer_start_idx + nc
```

**配套配置修改：**

`metaworld_dial-turn.yaml` dataset 新增参数：
```yaml
n_action_steps: ${n_action_steps}  # 传入 chunk 大小 = 8
gamma: 0.99                         # 步级 gamma
```

`rl100.yaml` critics gamma 修改为 chunk 级有效折扣：
```yaml
# 修改前
gamma: 0.99

# 修改后
gamma: 0.9227   # = 0.99^8 = γ^n_c（chunk-level Bellman backup）
```

---

## 三、上一轮修改中发现的一个逻辑矛盾（无需额外修改，但需了解）

**Note-1（来自 PAPER_CODE_AUDIT.md）：**

代码在 `offline_rl_optimize` 之前调用 `_apply_vib_betas(0.1)` 降低 VIB 正则化权重。但 `offline_rl_optimize` 内部对 `obs_encoder` 执行了 `requires_grad_(False)`——encoder 在 RL 阶段是**冻结的**，VIB beta 对 RL 梯度没有任何影响。

**真正起作用的地方**：`_apply_vib_betas(1.0)` 在 IL retrain 前恢复原值，这意味着 VIB beta 的"降低/恢复"实际只影响 IL retrain 阶段的正则化强度，与 RL 阶段无关。

这与论文文字（"During RL fine-tuning, reduce β"）有细微歧义，但实现逻辑本身是自洽的（因为 RL 阶段 encoder 冻结，所以 β 无论何值都不起作用）。

**当前 `use_recon_vib: false` 时，此逻辑完全不生效，无需关注。**

---

## 四、上一轮修改回溯（确认仍然有效）

| 修改 | 状态 | 说明 |
|------|------|------|
| `sigma_max: 0.1` | ✅ 保留 | chunk mode 稳定性，符合 tags |
| `critic_epochs: 150` | ✅ 保留 | Q loss 在 50 epoch 时斜率仍大，未收敛 |
| `rl_policy_lr: 1e-5` | ✅ 保留 | RL 精调 LR 降 10×，符合论文 |
| IQL 训练冻结 policy | ✅ 保留 | 论文：只训练 QV 网络 |
| `offline_rl_optimize` LR 降低 | ✅ 保留 | 同上 |
| VIB beta 动态降低/恢复 | ✅ 保留（不生效） | use_recon_vib=false 时无影响 |
| Lrecon 公式（β 乘两项） | ✅ 保留 | 论文 Eq.15 确认 β 乘括号内两项 |
| `load_checkpoint` strict=False | ✅ 保留 | 防御性措施，兼容未来架构变更 |
| **`use_recon_vib: true` → `false`** | **✅ 本次修复** | 消除随机 decoder loss 爆炸 |
| **Chunk 奖励实现** | **✅ 本次新增** | 论文 R_chunk = Σγ^j·r_{t+j} |
| **critics gamma 0.99 → 0.9227** | **✅ 本次新增** | chunk 级有效折扣 γ^8 |

---

## 五、如果以后要启用 VIB

正确流程：
```
1. 设置 use_recon_vib: true
2. 设置 resume: false（不加载旧 checkpoint）
3. 重新从 demo 数据完整训练 IL（il_epochs: 1000）
4. IL 收敛（loss ≈ 0.01 量级）后，再进入 RL 阶段
```

不要在已有 checkpoint 上直接开启 VIB。

---

## 六、当前遗留的论文-代码差异（不影响正确性的未实现项）

| 项 | 影响评估 |
|----|---------|
| 步骤惩罚 + 动作抖动惩罚（reward shaping）| 中：影响收敛速度，sparse reward 可以工作但较慢 |
| AM-Q OPE 仅 H=1 单步（论文是多步展开）| 低：OPE gate 仍有效，只是精度略低 |
| CD 与 PPO 使用独立优化器（论文是联合损失）| 低：功能等价，梯度不耦合 |
| Phase 3 在线 RL 未实现（run_online_rl: false）| 仅影响最终性能上限 |
