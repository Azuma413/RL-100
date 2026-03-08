import wandb
import numpy as np
import torch
import collections
import tqdm
from diffusion_policy_3d.env import MetaWorldEnv
from diffusion_policy_3d.gym_util.multistep_wrapper import MultiStepWrapper
from diffusion_policy_3d.gym_util.video_recording_wrapper import SimpleVideoRecordingWrapper

from diffusion_policy_3d.policy.base_policy import BasePolicy
from diffusion_policy_3d.common.pytorch_util import dict_apply
from diffusion_policy_3d.env_runner.base_runner import BaseRunner
import diffusion_policy_3d.common.logger_util as logger_util
from termcolor import cprint

class MetaworldRunner(BaseRunner):
    def __init__(self,
                 output_dir,
                 eval_episodes=20,
                 max_steps=1000,
                 n_obs_steps=8,
                 n_action_steps=8,
                 fps=10,
                 crf=22,
                 render_size=84,
                 tqdm_interval_sec=5.0,
                 n_envs=None,
                 task_name=None,
                 n_train=None,
                 n_test=None,
                 device="cuda:0",
                 use_point_crop=True,
                 num_points=512
                 ):
        super().__init__(output_dir)
        self.task_name = task_name


        def env_fn(task_name):
            return MultiStepWrapper(
                SimpleVideoRecordingWrapper(
                    MetaWorldEnv(task_name=task_name,device=device, 
                                 use_point_crop=use_point_crop, num_points=num_points)),
                n_obs_steps=n_obs_steps,
                n_action_steps=n_action_steps,
                max_episode_steps=max_steps,
                reward_agg_method='sum',
            )
        self.eval_episodes = eval_episodes
        self.env = env_fn(self.task_name)

        self.fps = fps
        self.crf = crf
        self.n_obs_steps = n_obs_steps
        self.n_action_steps = n_action_steps
        self.max_steps = max_steps
        self.tqdm_interval_sec = tqdm_interval_sec

        self.logger_util_test = logger_util.LargestKRecorder(K=3)
        self.logger_util_test10 = logger_util.LargestKRecorder(K=5)

    def run(self, policy: BasePolicy, save_video=False):
        device = policy.device
        dtype = policy.dtype

        all_traj_rewards = []
        all_success_rates = []
        env = self.env

        
        for episode_idx in tqdm.tqdm(range(self.eval_episodes), desc=f"Eval in Metaworld {self.task_name} Pointcloud Env", leave=False, mininterval=self.tqdm_interval_sec):
            
            # start rollout
            obs = env.reset()
            policy.reset()

            done = False
            traj_reward = 0
            is_success = False
            while not done:
                np_obs_dict = dict(obs)
                obs_dict = dict_apply(np_obs_dict,
                                      lambda x: torch.from_numpy(x).to(
                                          device=device))

                with torch.no_grad():
                    obs_dict_input = {}
                    obs_dict_input['point_cloud'] = obs_dict['point_cloud'].unsqueeze(0)
                    obs_dict_input['agent_pos'] = obs_dict['agent_pos'].unsqueeze(0)
                    action_dict = policy.predict_action(obs_dict_input)

                np_action_dict = dict_apply(action_dict,
                                            lambda x: x.detach().to('cpu').numpy())
                action = np_action_dict['action'].squeeze(0)

                obs, reward, done, info = env.step(action)


                traj_reward += reward
                done = np.all(done)
                is_success = is_success or max(info['success'])

            all_success_rates.append(is_success)
            all_traj_rewards.append(traj_reward)
            

        max_rewards = collections.defaultdict(list)
        log_data = dict()

        log_data['mean_traj_rewards'] = np.mean(all_traj_rewards)
        log_data['mean_success_rates'] = np.mean(all_success_rates)

        log_data['test_mean_score'] = np.mean(all_success_rates)
        
        cprint(f"test_mean_score: {np.mean(all_success_rates)}", 'green')

        self.logger_util_test.record(np.mean(all_success_rates))
        self.logger_util_test10.record(np.mean(all_success_rates))
        log_data['SR_test_L3'] = self.logger_util_test.average_of_largest_K()
        log_data['SR_test_L5'] = self.logger_util_test10.average_of_largest_K()
        

        videos = env.env.get_video()
        if len(videos.shape) == 5:
            videos = videos[:, 0]  # select first frame
        
        if save_video:
            videos_wandb = wandb.Video(videos, fps=self.fps, format="mp4")
            log_data[f'sim_video_eval'] = videos_wandb

        _ = env.reset()
        videos = None

        return log_data

    def run_and_collect(self, policy: BasePolicy, num_episodes: int):
        """
        Roll out policy and collect trajectory data for dataset merging.

        Stores one entry per policy call (action-chunk level), matching the
        format of the existing MetaWorld zarr dataset:
            state        : [T, state_dim]    robot proprioception
            action       : [T, action_dim]   first action of chunk
            point_cloud  : [T, N, 6]         current point cloud
            reward       : [T]               cumulative chunk reward
            done         : [T]               episode termination flag

        Returns:
            metrics  : same dict as run()
            episodes : list of per-episode dicts (numpy arrays)
        """
        device = policy.device
        env = self.env

        all_traj_rewards = []
        all_success_rates = []
        collected_episodes = []

        for episode_idx in tqdm.tqdm(
            range(num_episodes),
            desc=f"Collect in {self.task_name}",
            leave=False,
            mininterval=self.tqdm_interval_sec,
        ):
            obs = env.reset()
            policy.reset()

            done = False
            traj_reward = 0
            is_success = False

            ep_state, ep_action, ep_pc, ep_reward, ep_done = [], [], [], [], []

            while not done:
                np_obs_dict = dict(obs)

                # Current observation (latest frame in the n_obs_steps buffer)
                cur_state = np_obs_dict['agent_pos'][-1]        # [state_dim]
                cur_pc    = np_obs_dict['point_cloud'][-1]      # [N, 6]

                obs_dict_input = {
                    'point_cloud': torch.from_numpy(np_obs_dict['point_cloud']).unsqueeze(0).to(device),
                    'agent_pos':   torch.from_numpy(np_obs_dict['agent_pos']).unsqueeze(0).to(device),
                }

                with torch.no_grad():
                    action_dict = policy.predict_action(obs_dict_input)

                np_action = action_dict['action'].squeeze(0).detach().cpu().numpy()  # [n_action_steps, Da]
                first_action = np_action[0]   # [Da] — store first action, matching dataset format

                obs, reward, done, info = env.step(np_action)

                traj_reward += reward
                done = bool(np.all(done))
                is_success = is_success or bool(max(info['success']))

                ep_state.append(cur_state.astype(np.float32))
                ep_action.append(first_action.astype(np.float32))
                ep_pc.append(cur_pc.astype(np.float32))
                ep_reward.append(np.float32(reward))
                ep_done.append(np.float32(done))

            all_success_rates.append(is_success)
            all_traj_rewards.append(traj_reward)

            if len(ep_state) > 0:
                collected_episodes.append({
                    'state':       np.stack(ep_state,  axis=0),
                    'action':      np.stack(ep_action, axis=0),
                    'point_cloud': np.stack(ep_pc,     axis=0),
                    'reward':      np.array(ep_reward, dtype=np.float32),
                    'done':        np.array(ep_done,   dtype=np.float32),
                })

        metrics = {
            'mean_traj_rewards':  float(np.mean(all_traj_rewards)),
            'mean_success_rates': float(np.mean(all_success_rates)),
            'test_mean_score':    float(np.mean(all_success_rates)),
            'n_episodes':         len(collected_episodes),
            'n_steps':            sum(len(e['state']) for e in collected_episodes),
        }

        cprint(f"[Collect] {len(collected_episodes)} episodes, "
               f"success={metrics['mean_success_rates']:.3f}, "
               f"steps={metrics['n_steps']}", 'cyan')

        _ = env.reset()
        return metrics, collected_episodes
