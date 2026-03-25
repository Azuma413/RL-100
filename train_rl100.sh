#!/bin/bash

set -euo pipefail

export DATASET_NAME=normal-fix_0
export TASK_NAME=normal-fix

run_index=0
export OUTPUT_BASE_DIR=outputs/rl100_sim
while [ -d "${OUTPUT_BASE_DIR}/${DATASET_NAME}_${run_index}" ]; do
    run_index=$((run_index + 1))
done
export OUTPUT_DIR="${OUTPUT_DIR:-${OUTPUT_BASE_DIR}/${DATASET_NAME}_${run_index}}"
export WANDB_RUN_NAME="${WANDB_RUN_NAME:-$(basename "${OUTPUT_DIR}")}"
mkdir -p "${OUTPUT_BASE_DIR}"

echo "dataset_root=datasets/${DATASET_NAME}"
echo "output_dir=${OUTPUT_DIR}"
echo "wandb_run_name=${WANDB_RUN_NAME}"

uv run scripts/train_rl100_sim.py \
    --dataset-root "datasets/${DATASET_NAME}" \
    --task "${TASK_NAME}" \
    --output-dir "${OUTPUT_DIR}" \
    --max-episode-steps 500 \
    --use-separate-rgb-encoder-per-camera \
    --device cuda \
    --batch-size "${BATCH_SIZE:-256}" \
    --num-workers "${NUM_WORKERS:-8}" \
    --wandb \
    --wandb-project "rl100-lerobot" \
    --wandb-run-name "${WANDB_RUN_NAME}" \
    --rl-policy-learning-rate "${RL_POLICY_LEARNING_RATE:-2e-5}" \
    --reward-scale "${REWARD_SCALE:-1}" \
    --lambda-cd "${LAMBDA_CD:-0}" \
    --cd-every "${CD_EVERY:-5}" \
    --offline-iterations "${OFFLINE_ITERATIONS:-10}" \
    --online-iterations "${ONLINE_ITERATIONS:-10}" \
    --online-collection-episodes "${ONLINE_COLLECTION_EPISODES:-20}" \
    --online-value-steps "${ONLINE_VALUE_STEPS:-200}" \
    --online-finetune-steps "${ONLINE_FINETUNE_STEPS:-1000}" \
    --init-policy-path outputs/base/normal-fix/pretrained_model
