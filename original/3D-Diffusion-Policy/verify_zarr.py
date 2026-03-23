"""
Verify a MetaWorld expert demonstration zarr file.

Usage:
    python verify_zarr.py data/metaworld_dial-turn_expert.zarr
"""
import sys
import zarr
import numpy as np


def verify(zarr_path: str):
    root = zarr.open(zarr_path, 'r')

    print(f"\n{'='*60}")
    print(f"Zarr path: {zarr_path}")
    print(f"{'='*60}")

    # --- Keys ---
    data_keys = list(root['data'].keys())
    print(f"\n[Keys]  data/: {data_keys}")
    print(f"        meta/: {list(root['meta'].keys())}")

    # --- Shapes ---
    print(f"\n[Shapes]")
    for k in data_keys:
        arr = root['data'][k]
        print(f"  {k:20s}: {arr.shape}  dtype={arr.dtype}")

    episode_ends = root['meta']['episode_ends'][:]
    n_episodes = len(episode_ends)
    n_steps    = int(episode_ends[-1]) if n_episodes > 0 else 0
    episode_starts = np.concatenate([[0], episode_ends[:-1]])
    ep_lengths = episode_ends - episode_starts

    print(f"\n[Episodes]  n={n_episodes},  total_steps={n_steps}")
    print(f"  length  min={ep_lengths.min()}  max={ep_lengths.max()}  "
          f"mean={ep_lengths.mean():.1f}")

    # --- Reward ---
    if 'reward' in data_keys:
        reward = root['data']['reward'][:]
        print(f"\n[Reward]  min={reward.min():.4f}  max={reward.max():.4f}  "
              f"mean={reward.mean():.4f}  sum={reward.sum():.4f}")
        nonzero = np.count_nonzero(reward)
        print(f"  nonzero steps: {nonzero} / {n_steps}  "
              f"({100*nonzero/n_steps:.2f}%)")

        # Check per-episode reward pattern
        last_step_rewards = reward[episode_ends - 1]
        mid_rewards = []
        for s, e in zip(episode_starts, episode_ends):
            if e - s > 1:
                mid_rewards.extend(reward[s:e-1].tolist())

        print(f"\n  Last-step reward:  min={last_step_rewards.min():.4f}  "
              f"max={last_step_rewards.max():.4f}  "
              f"mean={last_step_rewards.mean():.4f}")
        if mid_rewards:
            mid = np.array(mid_rewards)
            print(f"  Mid-step reward:   min={mid.min():.4f}  "
                  f"max={mid.max():.4f}  mean={mid.mean():.4f}")
            if mid.max() == 0.0:
                print("  => SPARSE reward confirmed (all mid-step rewards = 0)")
            else:
                print("  => DENSE reward (mid-step rewards are non-zero)")
    else:
        print("\n[Reward]  *** NOT FOUND in zarr ***")

    # --- Done ---
    if 'done' in data_keys:
        done = root['data']['done'][:]
        n_terminals = int(done.sum())
        print(f"\n[Done]  terminals={n_terminals}  (expected={n_episodes})")
        if n_terminals == n_episodes:
            print("  => done flags match episode count ✓")
        else:
            print(f"  => MISMATCH: {n_terminals} terminals vs {n_episodes} episodes")

        # Check that done=1 is at episode_ends-1
        last_done = done[episode_ends - 1]
        print(f"  Last-step done:  all=1? {bool((last_done == 1).all())}")
    else:
        print("\n[Done]  *** NOT FOUND in zarr ***")

    # --- Action / State range ---
    if 'action' in data_keys:
        act = root['data']['action'][:]
        print(f"\n[Action]  min={act.min():.4f}  max={act.max():.4f}  "
              f"mean={act.mean():.4f}")
    if 'state' in data_keys:
        st = root['data']['state'][:]
        print(f"[State]   min={st.min():.4f}  max={st.max():.4f}  "
              f"mean={st.mean():.4f}")

    print(f"\n{'='*60}\n")


if __name__ == '__main__':
    path = sys.argv[1] if len(sys.argv) > 1 else 'data/metaworld_dial-turn_expert.zarr'
    verify(path)
