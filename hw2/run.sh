#!/bin/bash

# q2
#b=1500
#lr=9e-2
#python rob831/scripts/run_hw2.py --env_name InvertedPendulum-v4 --ep_len 1000 --discount 0.9 -n 100 -l 2 -s 64 -b $b -lr $lr -rtg --exp_name q2_b_${b}_r_${lr}

# q3
# python rob831/scripts/run_hw2.py \
# --env_name LunarLanderContinuous-v2 --ep_len 1000 \
# --discount 0.99 -n 100 -l 2 -s 64 -b 10000 -lr 0.005 \
# --reward_to_go --nn_baseline --exp_name q3_b10000_r0.005


# Experiment 4: search for best hyperparameters
b=1500
lr=9e-2
python ../../run_hw2.py --env_name InvertedPendulum-v4 --ep_len 1000 --discount 0.9 -n 100 -l 2 -s 64 -b $b -lr $lr -rtg --exp_name q2_b_${b}_r_${lr}
write code to run the above command with b=[10000, 30000, 50000] and lr=[5e-3, 1e-2, 2e-2]
for b in 10000 30000 50000
do
    for lr in 5e-3 1e-2 2e-2
    do
        python rob831/scripts/run_hw2.py --env_name HalfCheetah-v4 --ep_len 150 \
        --discount 0.95 -n 100 -l 2 -s 32 -b $b -lr $lr -rtg --nn_baseline \
        --exp_name q4_search_b_${b}_lr_${lr}_rtg_nnbaseline
    done
done

# b=10000
# lr=0.01
# python rob831/scripts/run_hw2.py --env_name HalfCheetah-v4 --ep_len 150 \
#     --discount 0.95 -n 100 -l 2 -s 32 -b $b -lr $lr -rtg --nn_baseline \
#     --exp_name q4_search_b_${b}_lr_${lr}_rtg_nnbaseline
    
# python rob831/scripts/run_hw2.py --env_name HalfCheetah-v4 --ep_len 150 \
# --discount 0.95 -n 100 -l 2 -s 32 -b 10000 -lr 0.02 \
# --exp_name q4_search_b10000_lr0.02
# python rob831/scripts/run_hw2.py --env_name HalfCheetah-v4 --ep_len 150 \
# --discount 0.95 -n 100 -l 2 -s 32 -b 10000 -lr 0.02 -rtg \
# --exp_name q4_search_b10000_lr0.02_rtg
# python rob831/scripts/run_hw2.py --env_name HalfCheetah-v4 --ep_len 150 \
# --discount 0.95 -n 100 -l 2 -s 32 -b 10000 -lr 0.02 --nn_baseline \
# --exp_name q4_search_b10000_lr0.02_nnbaseline
# python rob831/scripts/run_hw2.py --env_name HalfCheetah-v4 --ep_len 150 \
# --discount 0.95 -n 100 -l 2 -s 32 -b 10000 -lr 0.02 -rtg --nn_baseline \
# --exp_name q4_search_b10000_lr0.02_rtg_nnbaseline

# python rob831/scripts/run_hw2.py --env_name HalfCheetah-v4 --ep_len 150 \
# --discount 0.95 -n 100 -l 2 -s 32 -b 30000 -lr 2e-2 \
# --exp_name q4_b30000_r2e-2

# python rob831/scripts/run_hw2.py --env_name HalfCheetah-v4 --ep_len 150 \
# --discount 0.95 -n 100 -l 2 -s 32 -b 30000 -lr 2e-2 -rtg \
# --exp_name q4_b30000_r2e-2_rtg

# python rob831/scripts/run_hw2.py --env_name HalfCheetah-v4 --ep_len 150 \
# --discount 0.95 -n 100 -l 2 -s 32 -b 30000 -lr 2e-2 --nn_baseline \
# --exp_name q4_b30000_r2e-2_nnbaseline

# python rob831/scripts/run_hw2.py --env_name HalfCheetah-v4 --ep_len 150 \
# --discount 0.95 -n 100 -l 2 -s 32 -b 30000 -lr 2e-2 -rtg --nn_baseline \
# --exp_name q4_b30000_r2e-2_rtg_nnbaseline

# generalized advantage estimation

# experiment 5: GAE
# for lambda in 0 0.95 0.99 1.0
# do
#     python rob831/scripts/run_hw2.py \
#     --env_name Hopper-v4 --ep_len 1000 \
#     --discount 0.99 -n 300 -l 2 -s 32 -b 2000 -lr 0.001 \
#     --reward_to_go --nn_baseline --action_noise_std 0.5 --gae_lambda $lambda \
#     --exp_name q5_b2000_r0.001_lambda${lambda}
# done
