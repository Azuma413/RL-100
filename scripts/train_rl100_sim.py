import argparse
from rl_100.training.sim_rl100 import SimRL100Trainer, make_default_config

def parse_args():
    parser = argparse.ArgumentParser(description="Train a LeRobot Diffusion Policy with an RL-100 style sim loop.")
    parser.add_argument("--dataset-root", type=str, required=True, help="Path to the base LeRobot dataset.")
    parser.add_argument("--task", type=str, default="normal-fix", help="Genesis task name.")
    parser.add_argument("--output-dir", type=str, default=None, help="Directory used for checkpoints and rollouts.")
    parser.add_argument("--init-policy-path", type=str, default=None, help="Checkpoint directory or pretrained_model directory used to initialize the diffusion policy.")
    parser.add_argument(
        "--use-separate-rgb-encoder-per-camera",
        dest="use_separate_rgb_encoder_per_camera",
        action="store_true",
        help="Use a separate RGB encoder for each camera view. Enabled by default for RL100 training.",
    )
    parser.add_argument(
        "--shared-rgb-encoder",
        dest="use_separate_rgb_encoder_per_camera",
        action="store_false",
        help="Use a single shared RGB encoder across camera views.",
    )
    parser.add_argument("--device", type=str, default="cuda")
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--batch-size", type=int, default=16)
    parser.add_argument("--num-workers", type=int, default=2)
    parser.add_argument("--learning-rate", type=float, default=1e-4)
    parser.add_argument("--rl-policy-learning-rate", type=float, default=2e-5)
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
    parser.add_argument("--max-episode-steps", type=int, default=700)
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
    parser.add_argument("--disable-sparse-relabel", action="store_true")
    parser.add_argument("--assume-expert-failure", action="store_true")
    parser.add_argument("--lambda-cd", type=float, default=1.0)
    parser.add_argument("--cd-every", type=int, default=1)
    parser.add_argument("--rollout-policy-mode", type=str, default="ddim", choices=["ddim", "cm"])
    parser.add_argument("--eval-policy-mode", type=str, default="ddim", choices=["ddim", "cm"])
    parser.add_argument("--online-record-policy-mode", type=str, default="ddim", choices=["ddim", "cm"])
    parser.add_argument("--transition-train-epochs", type=int, default=50)
    parser.add_argument("--transition-train-patience", type=int, default=5)
    parser.add_argument("--transition-holdout-ratio", type=float, default=0.2)
    parser.add_argument("--transition-logvar-loss-coef", type=float, default=0.01)
    parser.add_argument("--transition-learning-rate", type=float, default=1e-3)
    parser.add_argument("--transition-max-batches", type=int, default=0)
    parser.add_argument("--stochastic-transition-eval", action="store_true")
    parser.add_argument("--disable-ope", action="store_true")
    parser.add_argument("--ope-num-batches", type=int, default=8)
    parser.add_argument("--ope-rollout-horizon", type=int, default=5)
    parser.add_argument("--ope-delta-coef", type=float, default=0.05)
    parser.add_argument("--ope-delta-abs-min", type=float, default=0.0)
    parser.add_argument("--ope-seed", type=int, default=42)
    parser.add_argument("--disable-ope-common-random-numbers", action="store_true")
    parser.add_argument("--wandb", action="store_true")
    parser.add_argument("--wandb-project", type=str, default="rl100-lerobot")
    parser.add_argument("--wandb-entity", type=str, default=None)
    parser.add_argument("--wandb-run-name", type=str, default=None)
    parser.add_argument("--force-initial-il-after-init-policy", action="store_true")
    parser.set_defaults(use_separate_rgb_encoder_per_camera=True)
    return parser.parse_args()


def main():
    args = parse_args()
    cfg = make_default_config(dataset_root=args.dataset_root, task=args.task)
    cfg.output_dir = args.output_dir or cfg.output_dir
    cfg.init_policy_path = args.init_policy_path
    cfg.use_separate_rgb_encoder_per_camera = args.use_separate_rgb_encoder_per_camera
    cfg.device = args.device
    cfg.seed = args.seed
    cfg.batch_size = args.batch_size
    cfg.num_workers = args.num_workers
    cfg.learning_rate = args.learning_rate
    cfg.rl_policy_learning_rate = args.rl_policy_learning_rate
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
    cfg.max_episode_steps = args.max_episode_steps
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
    cfg.relabel_sparse_reward = not args.disable_sparse_relabel
    cfg.assume_expert_success = not args.assume_expert_failure
    cfg.lambda_cd = args.lambda_cd
    cfg.cd_every = args.cd_every
    cfg.rollout_policy_mode = args.rollout_policy_mode
    cfg.eval_policy_mode = args.eval_policy_mode
    cfg.online_record_policy_mode = args.online_record_policy_mode
    cfg.transition_train_epochs = args.transition_train_epochs
    cfg.transition_train_patience = args.transition_train_patience
    cfg.transition_holdout_ratio = args.transition_holdout_ratio
    cfg.transition_logvar_loss_coef = args.transition_logvar_loss_coef
    cfg.transition_learning_rate = args.transition_learning_rate
    cfg.transition_max_batches = args.transition_max_batches
    cfg.transition_deterministic_eval = not args.stochastic_transition_eval
    cfg.ope_enabled = not args.disable_ope
    cfg.ope_num_batches = args.ope_num_batches
    cfg.ope_rollout_horizon = args.ope_rollout_horizon
    cfg.ope_delta_coef = args.ope_delta_coef
    cfg.ope_delta_abs_min = args.ope_delta_abs_min
    cfg.ope_seed = args.ope_seed
    cfg.ope_use_common_random_numbers = not args.disable_ope_common_random_numbers
    cfg.use_wandb = args.wandb
    cfg.wandb_project = args.wandb_project
    cfg.wandb_entity = args.wandb_entity
    cfg.wandb_run_name = args.wandb_run_name
    cfg.skip_initial_il_if_init_policy = not args.force_initial_il_after_init_policy

    trainer = SimRL100Trainer(cfg)
    trainer.run()


if __name__ == "__main__":
    main()
