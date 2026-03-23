import argparse
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
sys.path.insert(0, str(ROOT / "lerobot" / "src"))

from rl_100.training.sim_rl100 import SimRL100Trainer, make_default_config


def parse_args():
    parser = argparse.ArgumentParser(description="Train a LeRobot Diffusion Policy with an RL-100 style sim loop.")
    parser.add_argument("--dataset-root", type=str, required=True, help="Path to the base LeRobot dataset.")
    parser.add_argument("--task", type=str, default="normal-fix", help="Genesis task name.")
    parser.add_argument("--output-dir", type=str, default=None, help="Directory used for checkpoints and rollouts.")
    parser.add_argument("--device", type=str, default="cuda")
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--batch-size", type=int, default=16)
    parser.add_argument("--num-workers", type=int, default=2)
    parser.add_argument("--learning-rate", type=float, default=1e-4)
    parser.add_argument("--critic-learning-rate", type=float, default=3e-4)
    parser.add_argument("--weight-decay", type=float, default=1e-6)
    parser.add_argument("--il-steps", type=int, default=5000)
    parser.add_argument("--il-retrain-steps", type=int, default=1000)
    parser.add_argument("--offline-iterations", type=int, default=5)
    parser.add_argument("--critic-steps", type=int, default=1000)
    parser.add_argument("--offline-collection-episodes", type=int, default=20)
    parser.add_argument("--offline-finetune-steps", type=int, default=1000)
    parser.add_argument("--ppo-inner-steps", type=int, default=1)
    parser.add_argument("--online-iterations", type=int, default=0)
    parser.add_argument("--online-collection-episodes", type=int, default=20)
    parser.add_argument("--online-value-steps", type=int, default=200)
    parser.add_argument("--online-finetune-steps", type=int, default=1000)
    parser.add_argument("--eval-episodes", type=int, default=20)
    parser.add_argument("--save-every", type=int, default=1)
    parser.add_argument("--observation-height", type=int, default=224)
    parser.add_argument("--observation-width", type=int, default=224)
    parser.add_argument("--show-viewer", action="store_true")
    parser.add_argument("--keep-failures", action="store_true")
    parser.add_argument("--horizon", type=int, default=16)
    parser.add_argument("--n-obs-steps", type=int, default=2)
    parser.add_argument("--n-action-steps", type=int, default=8)
    parser.add_argument("--num-inference-steps", type=int, default=10)
    parser.add_argument("--ppo-clip-eps", type=float, default=0.2)
    parser.add_argument("--sigma-min", type=float, default=0.01)
    parser.add_argument("--sigma-max", type=float, default=0.1)
    parser.add_argument("--gamma", type=float, default=0.92274469442792)
    parser.add_argument("--expectile", type=float, default=0.7)
    parser.add_argument("--target-update-tau", type=float, default=0.005)
    parser.add_argument("--reward-scale", type=float, default=1.0)
    parser.add_argument("--gae-lambda", type=float, default=0.95)
    parser.add_argument("--max-grad-norm", type=float, default=1.0)
    parser.add_argument("--hf-cache-root", type=str, default="/tmp/rl100_hf_cache")
    parser.add_argument("--amp", action="store_true")
    return parser.parse_args()


def main():
    args = parse_args()
    cfg = make_default_config(dataset_root=args.dataset_root, task=args.task)
    cfg.output_dir = args.output_dir or cfg.output_dir
    cfg.device = args.device
    cfg.seed = args.seed
    cfg.batch_size = args.batch_size
    cfg.num_workers = args.num_workers
    cfg.learning_rate = args.learning_rate
    cfg.critic_learning_rate = args.critic_learning_rate
    cfg.weight_decay = args.weight_decay
    cfg.il_steps = args.il_steps
    cfg.il_retrain_steps = args.il_retrain_steps
    cfg.offline_iterations = args.offline_iterations
    cfg.critic_steps = args.critic_steps
    cfg.offline_collection_episodes = args.offline_collection_episodes
    cfg.offline_finetune_steps = args.offline_finetune_steps
    cfg.ppo_inner_steps = args.ppo_inner_steps
    cfg.online_iterations = args.online_iterations
    cfg.online_collection_episodes = args.online_collection_episodes
    cfg.online_value_steps = args.online_value_steps
    cfg.online_finetune_steps = args.online_finetune_steps
    cfg.eval_episodes = args.eval_episodes
    cfg.save_every = args.save_every
    cfg.observation_height = args.observation_height
    cfg.observation_width = args.observation_width
    cfg.show_viewer = args.show_viewer
    cfg.merge_success_only = not args.keep_failures
    cfg.horizon = args.horizon
    cfg.n_obs_steps = args.n_obs_steps
    cfg.n_action_steps = args.n_action_steps
    cfg.num_inference_steps = args.num_inference_steps
    cfg.ppo_clip_eps = args.ppo_clip_eps
    cfg.sigma_min = args.sigma_min
    cfg.sigma_max = args.sigma_max
    cfg.gamma = args.gamma
    cfg.expectile = args.expectile
    cfg.target_update_tau = args.target_update_tau
    cfg.reward_scale = args.reward_scale
    cfg.gae_lambda = args.gae_lambda
    cfg.max_grad_norm = args.max_grad_norm
    cfg.hf_cache_root = args.hf_cache_root
    cfg.amp = args.amp

    trainer = SimRL100Trainer(cfg)
    trainer.run()


if __name__ == "__main__":
    main()
