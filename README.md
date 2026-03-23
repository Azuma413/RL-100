# RL-100 on LeRobot Diffusion Policy
`original/3D-Diffusion-Policy` の RL-100 実装を踏まえて、LeRobot の Diffusion Policy を RL-100 向けに拡張したシミュレーション実装です。

今回の実装では、単なる「成功軌跡の追加 BC」ではなく、以下を含む RL-100 の algorithmic core を移植しています。

- 初期 IL
- IQL 形式の critic 学習
- denoising step ごとの PPO ratio を使う diffusion actor 更新
- rollout 収集と replay への反映
- IL / offline RL の反復
- online RL 時の decision-level trajectory 保存と GAE ベースの PPO

一方で、`original` 側にある consistency model / runtime policy 切り替え / transition model / OPE gate は今回の実装では省いています。Genesis `normal-fix` で RL-100 の本質的な RL 更新則を持ち込むことを優先しています。

## Setup
```bash
uv sync
```

## 1. Expert Dataset
まずは Genesis `normal-fix` の expert dataset を作成します。

```bash
uv run python scripts/make_sim_dataset.py
```

## 2. Train RL-100
次に、LeRobot Diffusion Policy をベースにした RL-100 学習ループを回します。

```bash
uv run python scripts/train_rl100_sim.py \
  --dataset-root datasets/normal-fix_0 \
  --task normal-fix \
  --il-steps 5000 \
  --offline-iterations 5 \
  --critic-steps 1000 \
  --offline-collection-episodes 20 \
  --offline-finetune-steps 1000 \
  --il-retrain-steps 1000 \
  --online-iterations 5 \
  --online-collection-episodes 20 \
  --online-value-steps 200 \
  --online-finetune-steps 1000
```

主な引数:

- `--critic-steps`: offline RL 各反復で IQL critic を何 step 学習するか
- `--offline-finetune-steps`: denoising-step PPO による actor 更新 step 数
- `--il-retrain-steps`: rollout merge 後に IL を再学習する step 数
- `--online-value-steps`: online RL で value 回帰を行う step 数
- `--online-finetune-steps`: online PPO の step 数
- `--ppo-inner-steps`: 同じ sampled denoising trajectory に対して何回 PPO を回すか
- `--hf-cache-root`: read-only cache 環境を避けるための Hugging Face cache 置き場

## 実装の対応関係
今回追加した主要ファイル:

- `src/rl_100/training/rl100_policy.py`
  LeRobot Diffusion Policy を継承し、DDIM denoising trajectory の保存、step-wise Gaussian log-prob、K-step PPO loss を実装
- `src/rl_100/training/rl100_critics.py`
  IQL の twin Q / value network
- `src/rl_100/training/rl100_dataset.py`
  LeRobot dataset から RL-100 用の `(obs, action horizon, next_obs, chunk reward, done)` を組み立てる wrapper
- `src/rl_100/training/sim_rl100.py`
  IL -> Offline RL -> rollout merge -> IL retrain -> Online RL の trainer
- `scripts/train_rl100_sim.py`
  Genesis `normal-fix` 用の entrypoint

## 現時点の制約
- `original` 側の consistency model / transition model / AM-Q based OPE gate は未実装です。
- 3D point cloud 固有の分岐は Genesis `normal-fix` では省略しています。
- 既存の `datasets/normal-fix_0` が壊れている場合は、`scripts/make_sim_dataset.py` で作り直した dataset を使ってください。
