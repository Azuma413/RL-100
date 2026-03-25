# RL-100 on LeRobot Diffusion Policy
`original/3D-Diffusion-Policy` の RL-100 実装を、point cloud 分岐を除いて LeRobot の Diffusion Policy 上へできるだけ忠実に移植するための実装です。

今回の状態では、単なる「成功 rollout を足して BC」ではなく、RL-100 の offline / online RL 構造を以下まで持ち込んでいます。

- initial IL
- IQL critic
- denoising step ごとの PPO actor loss
- rollout replay merge
- offline / online loop
- consistency distillation
- observation feature space 上の transition model
- AM-Q based OPE gate
- reward / done / next.success / episode.success 付き dataset 収集
- unlabeled expert demo への sparse reward / done relabel fallback

## Setup
```bash
uv sync
```

cache 書き込み先を明示しておくと、HuggingFace / matplotlib / Taichi / Quadrants 系で詰まりにくくなります。

```bash
export HF_HOME=/tmp/rl100_hf_cache
export HF_HUB_CACHE=/tmp/rl100_hf_cache/hub
export HF_DATASETS_CACHE=/tmp/rl100_hf_cache/datasets
export MPLCONFIGDIR=/tmp/matplotlib
export XDG_CACHE_HOME=/tmp/xdg-cache
export TAICHI_CACHE_DIR=/tmp/taichi
export QUADRANTS_CACHE_DIR=/tmp/quadrants
```

## Expert Dataset
`normal-fix_0` を作り直す場合:

```bash
uv run scripts/make_sim_dataset.py
```

新規収集 dataset には frame-level で以下が入ります。

- `next.reward`
- `next.done`
- `next.success`
- `episode.success`

加えて `meta/rl100_episode_summaries.jsonl` に episode-level success / return / target cube を残します。

既存の `datasets/normal-fix_0` のような unlabeled demo に対しては、trainer 側で original 同様の terminal sparse relabel fallback を残しています。

## Train
通常実行:

```bash
uv run scripts/train_rl100_sim.py \
  --dataset-root datasets/normal-fix_0 \
  --task normal-fix \
  --device cuda \
  --il-steps 5000 \
  --offline-iterations 5 \
  --critic-steps 1000 \
  --offline-finetune-steps 1000 \
  --offline-collection-episodes 20 \
  --il-retrain-steps 1000 \
  --online-iterations 5 \
  --online-collection-episodes 20 \
  --online-value-steps 200 \
  --online-finetune-steps 1000 \
  --lambda-cd 1.0 \
  --rollout-policy-mode ddim \
  --eval-policy-mode ddim
```

短い GPU smoke test:

```bash
uv run scripts/train_rl100_sim.py \
  --dataset-root datasets/normal-fix_0 \
  --task normal-fix \
  --device cuda \
  --batch-size 2 \
  --num-workers 0 \
  --max-episode-steps 10 \
  --il-steps 1 \
  --il-retrain-steps 1 \
  --offline-iterations 1 \
  --critic-steps 1 \
  --offline-finetune-steps 1 \
  --offline-collection-episodes 1 \
  --eval-episodes 1 \
  --online-iterations 0 \
  --transition-train-epochs 1 \
  --transition-train-patience 1 \
  --transition-max-batches 1 \
  --ope-num-batches 1 \
  --ope-rollout-horizon 2
```

主な追加引数:

- `--lambda-cd`: PPO と同時に足す consistency distillation loss の係数
- `--cd-every`: CD を何 step ごとに適用するか
- `--rollout-policy-mode {ddim,cm}`: rollout 時の policy 実行モード
- `--eval-policy-mode {ddim,cm}`: eval 時の policy 実行モード
- `--transition-*`: transition model 学習設定
- `--ope-*`: AM-Q gate 設定
- `--max-episode-steps`: smoke 向けに eval / rollout episode 長を短くする
- `--disable-sparse-relabel`: expert demo relabel を無効化
- `--wandb --wandb-project <name>`: wandb logging を有効化

## Success Criteria
学習成功の一次指標は `eval/<phase>/success_rate` です。

- `eval/il/success_rate`: IL 初期方策の到達点
- `eval/offline/success_rate`: offline RL 後に本当に改善したか
- `eval/online/success_rate`: online RL を回した場合の最終指標

補助的に見るべき指標:

- `collect/offline/success_rate`, `collect/online/success_rate`: rollout で成功軌跡をどれだけ集められているか
- `transition/transition_val_loss`: transition model が feature-space dynamics を学べているか
- `offline_critic/q_loss`, `offline_critic/v_loss`: critic 学習が壊れていないか
- `offline_ppo/ppo_loss`, `offline_ppo/approx_kl`, `offline_ppo/clip_frac`: PPO 更新の安定性
- `offline_ppo_ope/ope_accepted`: OPE gate が update を受理したか
- `offline_ppo/cd_loss`, `online_ppo/cd_loss`: consistency distillation の追従状況

wandb では phase ごとに namespaced に記録されます。例えば:

- `eval/offline/success_rate`
- `collect/offline/success_rate`
- `transition/transition_val_loss`
- `offline_critic/q_loss`
- `offline_ppo/ppo_loss`
- `offline_ppo_ope/ope_accepted`

## Fidelity
original RL-100 に対して忠実に再現した点:

- teacher actor は multi-step DDIM diffusion policy のまま
- actor 更新は denoising step ごとの PPO ratio で計算
- offline RL は `critic -> actor PPO(+CD) -> rollout -> IL retrain` の流れ
- `rollouts/offline_001` は IL 直後ではなく、1 回目の offline PPO 後の policy で収集される
- consistency model は teacher policy からの 1-step distillation
- transition model は raw observation ではなく actor の observation conditioning feature 上で学習
- transition model は ensemble / elite selection / holdout validation / early stopping / state restore を持つ
- offline PPO の前後で AM-Q による `J_old / J_new` を比較し、改善不足なら rollback
- common random numbers 付き AM-Q 評価を使う
- reward の無い expert demo は terminal sparse reward / done に relabel
- 新規収集 dataset では reward / done / success を収集時に保存する

まだ残っている差分:

- point cloud 専用分岐は未実装（というか点群処スコープ外なので実装する必要はない）
- original の point-cloud encoder / task-specific environment wrappers そのものは持ってこない
- 既存 unlabeled demo については original 同様の sparse relabel fallback で、過去 dataset を厳密再収集したわけではない
- consistency student 自体を online actor として最適化する完全な分離まではしておらず、teacher PPO と joint distillation
- reward は Genesis task 定義に沿った sparse success reward で、original task ごとの dense reward 一般化まではしていない

## Files
主要な変更箇所:

- `scripts/make_sim_dataset.py`
- `src/rl_100/training/rl100_policy.py`
- `src/rl_100/training/rl100_critics.py`
- `src/rl_100/training/rl100_dataset.py`
- `src/rl_100/training/rl100_consistency.py`
- `src/rl_100/training/rl100_transition.py`
- `src/rl_100/training/sim_rl100.py`
- `scripts/train_rl100_sim.py`
- `src/rl_100/lerobot_dataset_utils.py`
- `src/rl_100/env/genesis_env.py`
- `src/rl_100/env/tasks/normal.py`

## Verification
今回確認できた内容:

- `.venv` + RTX 3090 上で GPU smoke を実行
- `IL -> eval -> transition training -> critic training -> offline PPO + CD -> AM-Q OPE rollback -> rollout collection -> IL retrain -> eval` を実際に通した
- `history.json` に transition / critic / PPO / OPE / collection / eval が記録されることを確認
- rollout dataset に `episode.success`, `next.reward`, `next.done`, `next.success` と `meta/rl100_episode_summaries.jsonl` が保存されることを確認

GPU smoke 実行例:

```bash
.venv/bin/python scripts/train_rl100_sim.py \
  --dataset-root datasets/normal-fix_0 \
  --task normal-fix \
  --output-dir outputs/rl100_sim/normal-fix_0_gpu_smoke \
  --device cuda \
  --batch-size 2 \
  --num-workers 0 \
  --max-episode-steps 10 \
  --il-steps 1 \
  --il-retrain-steps 1 \
  --offline-iterations 1 \
  --critic-steps 1 \
  --offline-finetune-steps 1 \
  --offline-collection-episodes 1 \
  --eval-episodes 1 \
  --online-iterations 0 \
  --transition-train-epochs 1 \
  --transition-train-patience 1 \
  --transition-max-batches 1 \
  --ope-num-batches 1 \
  --ope-rollout-horizon 2 \
  --wandb \
  --wandb-project rl100-lerobot
```

## Conclusion
今回の状態は、point cloud を除く RL-100 の algorithmic core と補助機構を LeRobot Diffusion Policy 上でかなり忠実に再現し、GPU smoke でも実際に動くところまで持ってきています。ただし point cloud 分岐や task 群全体の完全一致まではまだ残るため、まだ `完全再現` とまでは言いません。
