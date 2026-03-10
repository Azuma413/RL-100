# VIB 在 IL 阶段的正确实现说明

## 一、论文要求（Eq.14-17）

```
L_IL(θ) = E[‖ε - ε_θ(a^τ, τ, ct)‖²]              (14)  ← 扩散 BC 损失

L_recon = β_recon(d_Chamfer(ô, o) + ‖q̂ - q‖²_2)   (15)  ← 重建损失
L_KL    = β_KL · KL(φ(z|o,s) ‖ N(0,I))              (16)  ← KL 散度

L^IL_total = L_IL + L_recon + L_KL                   (17)  ← 合并损失
```

- `o` = 观测点云，`q` = 机器人本体感知（关节角度等）
- `ô` = VIB decoder 重建的点云，`q̂` = state decoder 重建的状态
- `φ(z|o,s)` = PointNet 编码器输出的分布 N(μ, σ²)
- **训练时**：用重参数化 z = μ + ε·σ（ε ~ N(0,I)）作为特征（梯度可传播）
- **推理时**：用确定性 μ 作为特征（KL 保证 σ 小，μ ≈ z，但消除随机噪声）

---

## 二、已发现并修复的问题

### Bug 1：推理时返回随机 z 而非确定性 μ（已修复）

**位置**：`model/vision/pointnet_extractor.py` → `PointNetEncoderXYZ.forward()` 和 `PointNetEncoderXYZRGB.forward()`

**问题**：
```python
# 修复前（错误）：推理路径（return_recon=False）仍然返回随机 z
feat = z  # z = mu + eps*std
return feat   # ← 每次调用结果不同！
```

**修复后**：
```python
if return_recon:
    # 训练路径：返回随机 z（重参数化 trick，梯度可流向 mu_layer/logvar_layer）
    recon_pc = self.recon_decoder(z).reshape(-1, 512, in_channels)
    return feat, mu, logvar, recon_pc
else:
    # 推理路径：返回确定性 μ（消除推理噪声）
    return mu
```

**影响**：修复前，同一观测在推理时每次得到不同特征向量，导致动作预测随机波动，降低成功率和稳定性。

---

### Bug 2：VIB 不能"补插"到已有的无-VIB Checkpoint 上（设计约束，已文档化）

**根本原因**（论文第7页，Shared and frozen encoders）：
> "During offline RL, we keep φ^IL fixed"

VIB 层（`mu_layer`, `logvar_layer`, `recon_decoder`, `state_recon_decoder`）是 encoder 的一部分，必须在 IL 阶段从第一个 epoch 开始训练。

若从无 VIB 的 checkpoint 加载再开启 VIB：
```
随机初始化的 recon_decoder
→ Chamfer(random_recon, pc) ≈ 5~20（极大）
→ L_recon = β_recon × (5~20 + state_mse) ≈ 5~20
→ 远大于 BC loss ≈ 0.3
→ IL 训练梯度以重建损失为主，策略崩溃
```

**当前配置**：`use_recon_vib: false`（保持与已有 checkpoint 一致）

---

## 三、VIB 的正确调用链（已验证 ✅）

### IL 训练路径（compute_loss）

```
dp3.py::compute_loss(batch)
    ↓ normalizer.normalize(batch['obs'])
    ↓ this_nobs = reshape to (B*n_obs_steps, ...)
    ↓ obs_encoder(this_nobs, return_reg_loss=True)
        ↓ DP3Encoder.forward(obs, return_reg_loss=True)
            ↓ extractor(points, return_recon=True)  ← VIB 训练路径
                → returns (z, mu, logvar, recon_pc)
            ↓ kl_loss = -0.5·Σ(1 + logvar - mu² - exp(logvar))
            ↓ recon_loss_pc = chamfer_distance(original_pc_xyz, recon_pc)
            ↓ recon_state = state_recon_decoder(state_feat)
            ↓ recon_loss_state = MSE(recon_state, state)
            ↓ total_reg_loss = β_recon·(recon_pc + recon_state) + β_kl·kl
            → returns (final_feat=cat[z, state_feat], reg_loss_dict)
    ↓ total_loss = bc_loss + total_reg_loss
    ↓ total_loss.backward()     ← 梯度流向 mu_layer, logvar_layer, recon_decoder, UNet
```

### 推理路径（predict_action）

```
dp3.py::predict_action(obs_dict)
    ↓ normalizer.normalize(obs_dict)
    ↓ obs_encoder(this_nobs)           ← return_reg_loss=False（默认）
        ↓ DP3Encoder.forward(obs, return_reg_loss=False)
            ↓ extractor(points)        ← return_recon=False（默认）
                → returns mu           ← 确定性特征（修复后）
            → returns cat[mu, state_feat]
    ↓ global_cond = feature.reshape(B, -1)
    ↓ conditional_sample(...)          ← DDIM 采样
```

---

## 四、各组件对应论文公式（已验证 ✅）

| 组件 | 论文 | 代码位置 | 状态 |
|------|------|----------|------|
| 重参数化 z = μ + ε·σ | Eq.15 φ(z\|o,s) | `pointnet_extractor.py` VIB branch | ✅ |
| KL(N(μ,σ²) ‖ N(0,I)) | Eq.16 | `-0.5·Σ(1+logvar-μ²-exp(logvar))` | ✅ |
| d_Chamfer(ô, o) | Eq.15 | `pytorch3d.chamfer_distance` / MSE fallback | ✅ |
| ‖q̂ - q‖² | Eq.15 | `F.mse_loss(recon_state, state)` | ✅ |
| β_recon 乘括号内两项 | Eq.15 | `β_recon*(pc_loss + state_loss)` | ✅ |
| L^IL_total = L_IL + L_recon + L_KL | Eq.17 | `total_loss = bc_loss + reg_loss` | ✅ |
| **推理用 μ（非随机）** | VAE 标准实践 | **本次修复** | ✅ |

---

## 五、如何从头启用 VIB 训练

```yaml
# rl100.yaml
use_recon_vib: true
beta_recon: 1.0      # 若初期不稳定可降至 0.1
beta_kl: 0.001

# training
resume: false        # 必须从头训练，不能加载无 VIB checkpoint
il_epochs: 1000
```

训练结束后，`after_il.ckpt` 中包含完整的 VIB 层权重，可正常用于后续 RL 阶段。RL 阶段 encoder 会被冻结（`requires_grad_(False)`），VIB 层也随之冻结，不再更新。

---

## 六、VIB 的实际作用（为什么要用）

1. **稳定特征空间**：encoder 进入 RL 后被冻结，VIB 保证在 IL 阶段学到的特征是紧凑、有意义的，而非过拟合到演示数据
2. **压缩信息**：KL 损失迫使 z 不保留冗余信息，避免特征空间在 RL 阶段被不稳定的 Q 梯度破坏（即使 encoder 冻结，特征质量仍影响 Q 学习效果）
3. **重建约束**：decoder 能重建点云和状态，证明 z 中确实保留了几何和本体感知信息，而非任意映射
