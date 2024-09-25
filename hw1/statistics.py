import numpy as np
import matplotlib.pyplot as plt


# Learning rates and corresponding mean and standard deviation values
lr = np.array([5e-2, 1e-2, 5e-3, 1e-3, 5e-4, 1e-5])
mean = np.array([766.4500732421875, 4601.04931640625, 4555.95751953125, 4561.1240234375, 4489.0341796875, 847.0061645507812])
std = np.array([2.1913602352142334, 57.07187271118164, 51.607460021972656, 160.3817138671875, 57.8711051940918, 38.20732498168945])

# Create a new figure
plt.figure()

# Plot the learning rates against the mean rewards
plt.plot(lr, mean, marker='o', linestyle='-', color='b', label='Mean Reward')

# Fill the area between mean - std and mean + std
plt.fill_between(lr, mean - std, mean + std, color='b', alpha=0.2)

# Set both x and y axes to log scale
plt.xscale('log')
plt.yscale('log')

# Add title and labels
plt.title('Learning Rate vs. Mean and Standard Deviation')
plt.xlabel('Learning Rate')
plt.ylabel('Reward')

# Add legend
plt.legend()

# Show the plot
plt.show()


# ants
iters = range(10)
mean_dagger_ant = np.array([4555.95751953125, 4712.51318359375, 4656.0478515625, 4715.6435546875, 4648.4072265625, 4705.625, 4093.333740234375, 4718.92724609375, 4771.13671875, 4690.2744140625])
std_dagger_ant = np.array([51.607460021972656, 54.799888610839844, 75.46704864501953, 90.97648620605469, 36.743743896484375, 85.1937026977539, 1184.3753662109375, 110.6090316772461, 74.78446197509766, 130.94337463378906])
expert_mean_dagger_ant = np.array([4713.6533203125, 770.1326293945312, 4827.9150390625, 4799.74609375, 4699.9755859375, 4727.1962890625, 4770.154296875, 4566.970703125, 4739.24609375, 4725.1455078125])
mean_bc_ant = np.ones(10) * 4555.95751953125
# Create a new figure
# plt.figure()

# # Plot the iterations against the mean rewards， std rewards and expert mean rewards
# plt.plot(iters, mean_dagger, marker='o', linestyle='-', color='b', label='Mean Reward')
# plt.plot(iters, expert_mean_dagger, marker='o', linestyle='-', color='g', label='Expert Mean Reward')
# plt.plot(iters, mean_bc, marker='o', linestyle='-', color='r', label='BC Mean Reward')

# # Fill the area between mean - std and mean + std
# plt.fill_between(iters, mean_dagger - std_dagger, mean_dagger + std_dagger, color='b', alpha=0.2)


# # Add title and labels
# plt.title('Iteration vs. Performance ')
# plt.xlabel('Iterations')
# plt.ylabel('Reward')

# # Add legend
# plt.legend()

# # Show the plot
# plt.show()


# hoppers
iters = range(10)
mean_dagger_hopper = np.array([1073.1201171875, 1719.9921875, 1858.41357421875, 3772.207763671875, 3753.44580078125, 3777.035888671875, 3774.341796875, 3771.155029296875, 3772.78271484375, 3781.10107421875])
std_dagger_hopper = np.array([90.93077850341797, 434.211181640625, 273.31866455078125, 6.090365409851074, 13.204084396362305, 1.9861047267913818, 3.3804917335510254, 2.5168323516845703, 1.8829894065856934, 4.62257719039917])
expert_mean_dagger_hopper = np.array([3772.67041015625, 1041.944580078125, 1824.1131591796875, 1575.2913818359375, 3762.341796875, 3747.60888671875, 3778.61572265625, 3769.655517578125, 3770.76220703125, 3775.27880859375])
mean_bc_hopper = np.ones(10) * 1073.1201171875

# # Create a new figure
# plt.figure()

# # Plot the iterations against the mean rewards， std rewards and expert mean rewards
# plt.plot(iters, mean_dagger, marker='o', linestyle='-', color='b', label='Mean Reward')
# plt.plot(iters, expert_mean_dagger, marker='o', linestyle='-', color='g', label='Expert Mean Reward')
# plt.plot(iters, mean_bc, marker='o', linestyle='-', color='r', label='BC Mean Reward')

# # Fill the area between mean - std and mean + std
# plt.fill_between(iters, mean_dagger - std_dagger, mean_dagger + std_dagger, color='b', alpha=0.2)


# # Add title and labels
# plt.title('Iteration vs. Performance ')
# plt.xlabel('Iterations')
# plt.ylabel('Reward')

# # Add legend
# plt.legend()

# # Show the plot
# plt.show()


# make 2 subplots for ant and hopper
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))  # 1 row, 2 columns
ax1.plot(iters, mean_dagger_ant, marker='o', linestyle='-', color='b', label='Mean Reward')
ax1.plot(iters, expert_mean_dagger_ant, marker='o', linestyle='-', color='g', label='Expert Mean Reward')
ax1.plot(iters, mean_bc_ant, marker='o', linestyle='-', color='r', label='BC Mean Reward')
ax1.fill_between(iters, mean_dagger_ant - std_dagger_ant, mean_dagger_ant + std_dagger_ant, color='b', alpha=0.2)

ax2.plot(iters, mean_dagger_hopper, marker='o', linestyle='-', color='b', label='Mean Reward')
ax2.plot(iters, expert_mean_dagger_hopper, marker='o', linestyle='-', color='g', label='Expert Mean Reward')
ax2.plot(iters, mean_bc_hopper, marker='o', linestyle='-', color='r', label='BC Mean Reward')
ax2.fill_between(iters, mean_dagger_hopper - std_dagger_hopper, mean_dagger_hopper + std_dagger_hopper, color='b', alpha=0.2)

ax1.set_title('ant')
ax1.set_xlabel('iters')
ax1.set_ylabel('reward')
ax1.legend()

ax2.set_title('hopper')
ax2.set_xlabel('iters')
ax2.set_ylabel('reward')
ax2.legend()

# Adjust layout for better spacing
plt.tight_layout()

# Show the plot
plt.show()