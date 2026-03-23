# RL-100 on 3D-Diffusion-Policy

本リポジトリは、[3D Diffusion Policy (DP3)](https://3d-diffusion-policy.github.io) をベースに実装・整理された **RL-100** バージョンであり、以下を含みます：

- DP3 行動クローニングの学習と評価
- RL-100 の IL -> Offline RL -> Online RL の3段階学習
- MetaWorld / Adroit / DexArt デモデータ収集スクリプト
- DDIM メインポリシーと Consistency Model の評価エントリ

論文：

- DP3: <https://arxiv.org/abs/2403.03954>
- RL-100: <https://arxiv.org/abs/2510.14830>

<div align="center">
  <img src="rl100.png" alt="RL-100 framework" width="100%">
</div>

## リポジトリ構成

コアコードは [3D-Diffusion-Policy](/home/yrz/RL-100/3D-Diffusion-Policy) にあります：

- [train_rl100.py](/home/yrz/RL-100/3D-Diffusion-Policy/train_rl100.py)：RL-100 学習エントリ
- [eval_rl100.py](/home/yrz/RL-100/3D-Diffusion-Policy/eval_rl100.py)：RL-100 単一チェックポイント評価エントリ
- [rl100.yaml](/home/yrz/RL-100/3D-Diffusion-Policy/diffusion_policy_3d/config/rl100.yaml)：RL-100 メイン設定
- [config/task](/home/yrz/RL-100/3D-Diffusion-Policy/diffusion_policy_3d/config/task)：各タスク設定
- [scripts](/home/yrz/RL-100/scripts)：データ収集、DP3 学習および評価スクリプト

## 環境構築

環境設定は **DP3 を直接流用** しており、追加の変更はありません。

- インストール手順は [INSTALL.md](/home/yrz/RL-100/INSTALL.md) を参照してください。
- よくあるエラーについては [ERROR_CATCH.md](/home/yrz/RL-100/ERROR_CATCH.md) を参照してください。

すでに DP3 を正常に実行できている場合は、そのまま RL-100 を実行できます。

## データ収集

すべてのデモデータはデフォルトで [3D-Diffusion-Policy/data](/home/yrz/RL-100/3D-Diffusion-Policy/data) に書き込まれます。

### MetaWorld

スクリプト： [gen_demonstration_metaworld.sh](/home/yrz/RL-100/scripts/gen_demonstration_metaworld.sh)

```bash
bash scripts/gen_demonstration_metaworld.sh dial-turn
bash scripts/gen_demonstration_metaworld.sh basketball sparse
bash scripts/gen_demonstration_metaworld.sh push dense
```

説明：

- 最初の引数は MetaWorld のタスク名です。
- 2番目の引数は報酬タイプで、デフォルトは `sparse` です。
- 現在のスクリプトでは固定で 100 エピソードを収集します。

### Adroit

スクリプト： [gen_demonstration_adroit.sh](/home/yrz/RL-100/scripts/gen_demonstration_adroit.sh)

```bash
bash scripts/gen_demonstration_adroit.sh door
bash scripts/gen_demonstration_adroit.sh hammer
bash scripts/gen_demonstration_adroit.sh pen
```

説明：

- 現在のスクリプトでは固定で 10 エピソードを収集します。
- `third_party/VRL3/ckpts/` 配下の expert チェックポイントに依存します。

### DexArt

スクリプト： [gen_demonstration_dexart.sh](/home/yrz/RL-100/scripts/gen_demonstration_dexart.sh)

```bash
bash scripts/gen_demonstration_dexart.sh laptop
bash scripts/gen_demonstration_dexart.sh faucet
bash scripts/gen_demonstration_dexart.sh bucket
bash scripts/gen_demonstration_dexart.sh toilet
```

説明：

- 現在のスクリプトでは固定で 100 エピソードを収集します。
- `third_party/dexart-release/assets/rl_checkpoints/` に依存します。

## DP3 ベースラインの学習と評価

オリジナルの DP3 行動クローニングフローのみを実行したい場合は、引き続き元のスクリプトを使用できます。

### 学習

スクリプト： [train_policy.sh](/home/yrz/RL-100/scripts/train_policy.sh)

```bash
bash scripts/train_policy.sh dp3 metaworld_dial-turn exp1 0 0
bash scripts/train_policy.sh dp3 adroit_hammer exp1 0 0
bash scripts/train_policy.sh simple_dp3 dexart_laptop exp1 0 0
```

引数の順序：

1. アルゴリズム名：`dp3` または `simple_dp3`
2. タスク名：例 `metaworld_dial-turn`
3. 追加文字列：実験名の構成に使用されます
4. 乱数シード
5. GPU ID

### 評価

スクリプト： [eval_policy.sh](/home/yrz/RL-100/scripts/eval_policy.sh)

```bash
bash scripts/eval_policy.sh dp3 metaworld_dial-turn exp1 0 0
```

## RL-100 学習

RL-100 はシェルスクリプトを使用せず、直接 Hydra エントリを使用します。

まずプロジェクトディレクトリに移動します：

```bash
cd 3D-Diffusion-Policy
```

### 基本的な学習

```bash
python train_rl100.py task=metaworld_dial-turn
```

### よく使われるオーバーライド設定

```bash
python train_rl100.py \
  task=metaworld_dial-turn \
  training.seed=0 \
  training.device=cuda:0 \
  logging.use_wandb=true \
  task.env_runner.eval_episodes=100
```

### 特定のチェックポイントから再開する場合

```bash
python train_rl100.py \
  task=metaworld_dial-turn \
  training.resume=true \
  training.resume_path=/path/to/checkpoints/after_il.ckpt
```

### 学習フェーズ

`train_rl100.py` はデフォルトで以下のフローを実行します：

1. IL：デモンストレーションを使用して DP3/RL100 ポリシーを事前に学習します。
2. Offline RL：遷移モデル、IQL critics、offline PPO を学習し、OPE gate を実行します。
3. Data Collection + IL Retrain：新しい軌跡を収集してデータセットに統合し、IL retrain を実行します。
4. Online RL：新しいロールアウトに対して on-policy PPO + GAE を実行します。
5. Final Eval：設定に従って ddim および/または cm を評価します。

関連するメイン設定は [rl100.yaml](/home/yrz/RL-100/3D-Diffusion-Policy/diffusion_policy_3d/config/rl100.yaml) を参照してください。

## RL-100 評価

スクリプトエントリ： [eval_rl100.py](/home/yrz/RL-100/3D-Diffusion-Policy/eval_rl100.py)

### メインモデル DDIM の評価

```bash
python eval_rl100.py \
  task=metaworld_dial-turn \
  checkpoint_path=/path/to/checkpoints/final.ckpt \
  runtime.eval_policy_mode=ddim \
  runtime.eval_use_ema=false \
  task.env_runner.eval_episodes=100
```

### EMA-DDIM の評価

```bash
python eval_rl100.py \
  task=metaworld_dial-turn \
  checkpoint_path=/path/to/checkpoints/final.ckpt \
  runtime.eval_policy_mode=ddim \
  runtime.eval_use_ema=true \
  task.env_runner.eval_episodes=100
```

### Consistency Model の評価

```bash
python eval_rl100.py \
  task=metaworld_dial-turn \
  checkpoint_path=/path/to/checkpoints/final.ckpt \
  runtime.eval_policy_mode=cm \
  runtime.eval_use_ema=true \
  task.env_runner.eval_episodes=100
```

## 出力内容

学習出力ディレクトリは Hydra によって管理され、デフォルトは以下の通りです：

```bash
3D-Diffusion-Policy/outputs/rl100_<task>_seed<seed>/<date>_<time>/
```

通常、以下が含まれます：

- `checkpoints/after_il.ckpt`
- `checkpoints/offline_iter_<N>.ckpt`
- `checkpoints/online_iter_<N>.ckpt`
- `checkpoints/final.ckpt`
- `plots/` 配下の各種 loss / success 曲線

## 重要な設定項目

よく使われる項目は基本的に [rl100.yaml](/home/yrz/RL-100/3D-Diffusion-Policy/diffusion_policy_3d/config/rl100.yaml) にあります：

- `training.num_offline_iterations`
- `training.critic_epochs`
- `training.ppo_epochs`
- `training.ppo_inner_steps`
- `training.collection_episodes`
- `training.online_rl_iterations`
- `training.online_collection_episodes`
- `training.rl_policy_lr`
- `runtime.collection_policy`
- `runtime.collection_use_ema`
- `runtime.merge_success_only`
- `runtime.final_eval_policies`
- `runtime.final_eval_use_ema`
- `task.env_runner.eval_episodes`

タスクデータのパス、観測次元、評価エピソード数は各タスクの yaml で定義されています。例：

- [metaworld_dial-turn.yaml](/home/yrz/RL-100/3D-Diffusion-Policy/diffusion_policy_3d/config/task/metaworld_dial-turn.yaml)

## 注意事項

### 1. `eval_episodes` はタスク yaml が優先されます

最終的な学習評価と `eval_rl100.py` はどちらも直接 `task.env_runner.eval_episodes` を読み込みます。  
評価回数を変更する場合は、タスク yaml を変更するか、コマンドラインでオーバーライドしてください：

```bash
python train_rl100.py task=metaworld_dial-turn task.env_runner.eval_episodes=100
```

### 2. `merge_success_only` は IL retrain にのみ影響し、RL 自体には影響しません

現在のロジックは以下の通りです：

- Offline RL / Online RL はどちらも、失敗した軌跡を含む完全なサンプリング軌跡を使用します。
- `success-only` は、その後の `IL retrain` のデータフィルタリングにのみ作用します。

これにより、RL 学習と IL 再学習のセマンティクスが分離されています。

### 3. `prediction_type` は `epsilon` である必要があります

RL-100 の PPO ratio 計算は `epsilon` パラメータ化に依存しています。現在の設定は以下のように固定されています：

```yaml
policy:
  noise_scheduler:
    prediction_type: epsilon
```

`sample` に変更しないでください。

### 4. `sigma_max` を安易に共有しないでください

RL-100 論文 `2510.14830 v4` のアブレーション結果に基づき、stochastic DDIM の標準差の上限は制御モードごとに区別する必要があります：

- `sigma_max = 0.8`
  - Adroit
  - Mujoco locomotion
  - 実機単一ステップ制御タスク
- `sigma_max = 0.1`
  - MetaWorld
  - 実機 chunk-action 制御タスク

リポジトリの現在のデフォルト設定：

```yaml
policy:
  sigma_max: 0.1
```

これは MetaWorld / chunk-action に適しています。  
実機単一ステップ制御を行う場合は、論文の推奨に従って `0.8` に変更する必要があります。

### 5. `reward_type=dense` は、実際に dense reward ラベルがあるデータにのみ使用してください

現在の MetaWorld デモスクリプトのデフォルトは以下の通りです：

```bash
bash scripts/gen_demonstration_metaworld.sh <task> sparse
```

dense を実行する場合は、以下のことを確認してください：

- 収集スクリプトが実際に dense reward を生成していること。
- 設定内の `critics.reward_type` がデータと一致していること。

sparse データを dense reward として扱わないでください。

### 6. `use_recon_vib=true` の場合は最初から学習する必要があります

チェックポイントが Recon/VIB で学習されたものでない場合は、途中で有効にしないでください：

```yaml
policy:
  use_recon_vib: true
```

これにより、ランダムに初期化された decoder/VIB 分岐が導入され、既存のポリシーが破壊されます。  
使用する場合は、デモンストレーションから再学習する必要があります。

### 7. EMA とメインモデルは別物です

- 学習時に実際に誤差逆伝播で更新されるのはメインモデルの `policy` です。
- `ema_policy` は、メインモデルのパラメータの指数移動平均です。
- 最終的な評価で EMA を使用するかどうかは、以下に依存します：
  - `runtime.final_eval_use_ema`
  - `runtime.eval_use_ema`

### 8. WandB は必須ではありません

WandB を使用したくない場合は、設定で直接無効にしてください：

```bash
python train_rl100.py task=metaworld_dial-turn logging.use_wandb=false
```

## 参考文献

- RL-100 コード説明： [RL100_README.md](/home/yrz/RL-100/3D-Diffusion-Policy/RL100_README.md)
- DP3 インストール手順： [INSTALL.md](/home/yrz/RL-100/INSTALL.md)
- インストールのトラブルシューティング： [ERROR_CATCH.md](/home/yrz/RL-100/ERROR_CATCH.md)

## Citation

本リポジトリが役立つ場合は、以下を引用してください：

```bibtex
@inproceedings{Ze2024DP3,
  title={3D Diffusion Policy: Generalizable Visuomotor Policy Learning via Simple 3D Representations},
  author={Yanjie Ze and Gu Zhang and Kangning Zhang and Chenyuan Hu and Muhan Wang and Huazhe Xu},
  booktitle={Proceedings of Robotics: Science and Systems (RSS)},
  year={2024}
}

@article{lei2025rl100,
  title={RL-100: Performant Robotic Manipulation with Real-World Reinforcement Learning},
  author={Lei, Kun and Li, Huanyu and Yu, Dongjie and Wei, Zhenyu and Guo, Lingxiao and Jiang, Zhennan and Wang, Ziyu and Liang, Shiyu and Xu, Huazhe},
  journal={arXiv preprint arXiv:2510.14830},
  year={2025}
}
```
