# bash scripts/gen_demonstration_metaworld.sh basketball [sparse|dense]



cd third_party/Metaworld

task_name=${1}
reward_type=${2:-sparse}

export CUDA_VISIBLE_DEVICES=0
python gen_demonstration_expert.py --env_name=${task_name} \
            --num_episodes 100 \
            --root_dir "../../3D-Diffusion-Policy/data/" \
            --reward_type ${reward_type}
