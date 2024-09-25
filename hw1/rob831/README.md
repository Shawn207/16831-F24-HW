Assignments for [CMU 16-831 Introduction to Robot Learning](https://16-831.github.io/fall24/).

To reproduce Q1 Part3 ant env, run:
```
python rob831/scripts/run_hw1.py \
	--expert_policy_file rob831/policies/experts/Ant.pkl \
	--env_name Ant-v2 --exp_name bc_ant --n_iter 1 \
	--expert_data rob831/expert_data/expert_data_Ant-v2.pkl \
	--video_log_freq -1 \
    --num_agent_train_steps_per_iter 2000 \
    --eval_batch_size 5000
```


To reproduce Q1 Part3 Hopper env, run:
```
python rob831/scripts/run_hw1.py \
    --expert_policy_file rob831/policies/experts/Hopper.pkl \
    --env_name Hopper-v2 --exp_name bc_hopper --n_iter 1 \
    --expert_data rob831/expert_data/expert_data_Hopper-v2.pkl \
    --video_log_freq -1 \
    --num_agent_train_steps_per_iter 2000 \
    --eval_batch_size 5000
```


To reproduce the numbers with different lr, run: 
```
python rob831/scripts/run_hw1.py \
	--expert_policy_file rob831/policies/experts/Ant.pkl \
	--env_name Ant-v2 --exp_name bc_ant --n_iter 1 \
	--expert_data rob831/expert_data/expert_data_Ant-v2.pkl \
	--video_log_freq -1 \
    --num_agent_train_steps_per_iter 2000 \
    --eval_batch_size 5000 \
    --learning_rate ${learning_rate in {5e-2, 1e-2, 5e-3, 1e-3, 5e-4, 1e-5}}
```


To reproduce Q2 in ant, run: 
```
python rob831/scripts/run_hw1.py \
    --expert_policy_file rob831/policies/experts/Ant.pkl \
    --env_name Ant-v2 --exp_name dagger_ant --n_iter 10 \
    --do_dagger --expert_data rob831/expert_data/expert_data_Ant-v2.pkl \
    --video_log_freq -1 \
    --num_agent_train_steps_per_iter 2000 \
    --eval_batch_size 5000
```

To reproduce Q2 in Hopper, run: 
```
python rob831/scripts/run_hw1.py \
    --expert_policy_file rob831/policies/experts/Hopper.pkl \
    --env_name Hopper-v2 --exp_name dagger_hopper --n_iter 10 \
    --do_dagger --expert_data rob831/expert_data/expert_data_Hopper-v2.pkl \
    --video_log_freq -1 \
    --num_agent_train_steps_per_iter 2000 \
    --eval_batch_size 5000
```
