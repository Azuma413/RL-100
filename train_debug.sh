#!/bin/bash

set -euo pipefail

export DATASET_NAME="${DATASET_NAME:-normal-fix_0}"
export TASK_NAME="${TASK_NAME:-normal-fix}"

run_index=0
export OUTPUT_BASE_DIR="${OUTPUT_BASE_DIR:-outputs/rl100_sim_debug}"
while [ -d "${OUTPUT_BASE_DIR}/${DATASET_NAME}_${run_index}" ]; do
    run_index=$((run_index + 1))
done
export OUTPUT_DIR="${OUTPUT_DIR:-${OUTPUT_BASE_DIR}/${DATASET_NAME}_${run_index}}"
export WANDB_RUN_NAME="${WANDB_RUN_NAME:-$(basename "${OUTPUT_DIR}")}"
export INIT_POLICY_PATH="${INIT_POLICY_PATH:-outputs/base/normal-fix/pretrained_model}"

mkdir -p "${OUTPUT_BASE_DIR}"

uv run scripts/train_rl100_sim.py \
    --dataset-root "datasets/${DATASET_NAME}" \
    --task "${TASK_NAME}" \
    --output-dir "${OUTPUT_DIR}" \
    --use-separate-rgb-encoder-per-camera \
    --device "${DEVICE:-cuda}" \
    --batch-size "${BATCH_SIZE:-2}" \
    --num-workers "${NUM_WORKERS:-0}" \
    --max-episode-steps "${MAX_EPISODE_STEPS:-400}" \
    --il-steps "${IL_STEPS:-1}" \
    --il-retrain-steps "${IL_RETRAIN_STEPS:-1}" \
    --rl-policy-learning-rate "${RL_POLICY_LEARNING_RATE:-2e-5}" \
    --reward-scale "${REWARD_SCALE:-10}" \
    --lambda-cd "${LAMBDA_CD:-0}" \
    --cd-every "${CD_EVERY:-5}" \
    --offline-iterations "${OFFLINE_ITERATIONS:-1}" \
    --critic-steps "${CRITIC_STEPS:-1}" \
    --offline-collection-episodes "${OFFLINE_COLLECTION_EPISODES:-20}" \
    --offline-finetune-steps "${OFFLINE_FINETUNE_STEPS:-1}" \
    --online-iterations "${ONLINE_ITERATIONS:-0}" \
    --online-collection-episodes "${ONLINE_COLLECTION_EPISODES:-10}" \
    --online-value-steps "${ONLINE_VALUE_STEPS:-1}" \
    --online-finetune-steps "${ONLINE_FINETUNE_STEPS:-1}" \
    --eval-episodes "${EVAL_EPISODES:-1}" \
    --transition-train-epochs "${TRANSITION_TRAIN_EPOCHS:-1}" \
    --transition-train-patience "${TRANSITION_TRAIN_PATIENCE:-1}" \
    --transition-max-batches "${TRANSITION_MAX_BATCHES:-1}" \
    --ope-num-batches "${OPE_NUM_BATCHES:-1}" \
    --ope-rollout-horizon "${OPE_ROLLOUT_HORIZON:-2}" \
    --wandb \
    --wandb-project "${WANDB_PROJECT:-rl100-lerobot}" \
    --wandb-run-name "${WANDB_RUN_NAME}" \
    --init-policy-path "${INIT_POLICY_PATH}"
