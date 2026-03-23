#!/bin/bash

export DATASET_NAME=normal-fix_0
export ONLINE_ITERATIONS=${ONLINE_ITERATIONS:-5}
export ONLINE_COLLECTION_EPISODES=${ONLINE_COLLECTION_EPISODES:-20}
export ONLINE_VALUE_STEPS=${ONLINE_VALUE_STEPS:-200}
export ONLINE_FINETUNE_STEPS=${ONLINE_FINETUNE_STEPS:-1000}

uv run scripts/train_rl100_sim.py \
    --dataset-root datasets/${DATASET_NAME} \
    --task normal-fix \
    --device cuda \
    --wandb \
    --wandb-project rl100-lerobot \
    --wandb-run-name ${DATASET_NAME}-run1 \
    --online-iterations ${ONLINE_ITERATIONS} \
    --online-collection-episodes ${ONLINE_COLLECTION_EPISODES} \
    --online-value-steps ${ONLINE_VALUE_STEPS} \
    --online-finetune-steps ${ONLINE_FINETUNE_STEPS}
