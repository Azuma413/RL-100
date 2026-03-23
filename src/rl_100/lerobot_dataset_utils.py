from __future__ import annotations

from pathlib import Path
from typing import Any

import numpy as np

from lerobot.datasets.lerobot_dataset import LeRobotDataset
from lerobot.utils.constants import DONE, REWARD
from rl_100.env.tasks.normal import AGENT_DIM, joints_name

STATE_NAMES = [
    "eef_pos_x",
    "eef_pos_y",
    "eef_pos_z",
    "eef_quat_w",
    "eef_quat_x",
    "eef_quat_y",
    "eef_quat_z",
    "grip_left",
    "grip_right",
]


def make_lerobot_features(
    observation_space,
    observation_height: int,
    observation_width: int,
    include_rl_labels: bool = False,
) -> dict[str, dict[str, Any]]:
    features: dict[str, dict[str, Any]] = {
        "action": {"dtype": "float32", "shape": (AGENT_DIM,), "names": joints_name},
    }
    for key in observation_space.spaces:
        if key == "observation.state":
            features[key] = {"dtype": "float32", "shape": (9,), "names": STATE_NAMES}
        elif key.startswith("observation.images"):
            features[key] = {
                "dtype": "video",
                "shape": (observation_height, observation_width, 3),
                "names": ("height", "width", "channels"),
            }

    if include_rl_labels:
        features[REWARD] = {"dtype": "float32", "shape": (1,), "names": None}
        features[DONE] = {"dtype": "bool", "shape": (1,), "names": None}
        features["next.success"] = {"dtype": "bool", "shape": (1,), "names": None}

    return features


def create_lerobot_dataset(
    dataset_root: str | Path,
    env,
    include_rl_labels: bool = False,
    fps: int = 30,
    robot_type: str = "franka",
) -> LeRobotDataset:
    dataset_root = Path(dataset_root)
    return LeRobotDataset.create(
        repo_id=dataset_root.name,
        root=dataset_root,
        fps=fps,
        robot_type=robot_type,
        use_videos=True,
        features=make_lerobot_features(
            observation_space=env.observation_space,
            observation_height=env.observation_height,
            observation_width=env.observation_width,
            include_rl_labels=include_rl_labels,
        ),
        batch_encoding_size=10,
    )


def convert_env_obs_to_lerobot_frame(numpy_observation: dict[str, Any]) -> dict[str, Any]:
    converted_obs: dict[str, Any] = {}
    for key, value in numpy_observation.items():
        if key.startswith("observation.images."):
            converted_obs[key] = value.copy() if isinstance(value, np.ndarray) else value
        elif key == "observation.state":
            converted_obs[key] = np.asarray(value, dtype=np.float32)
        else:
            converted_obs[key] = value
    return converted_obs


def build_frame(
    numpy_observation: dict[str, Any],
    action: np.ndarray,
    task: str,
    reward: float | None = None,
    done: bool | None = None,
    success: bool | None = None,
) -> dict[str, Any]:
    frame = convert_env_obs_to_lerobot_frame(numpy_observation)
    frame["action"] = np.asarray(action, dtype=np.float32)
    frame["task"] = task
    if reward is not None:
        frame[REWARD] = np.asarray([reward], dtype=np.float32)
    if done is not None:
        frame[DONE] = np.asarray([done], dtype=bool)
    if success is not None:
        frame["next.success"] = np.asarray([success], dtype=bool)
    return frame
