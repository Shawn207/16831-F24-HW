import numpy as np
import rob831.infrastructure.pytorch_util as ptu

class ArgMaxPolicy(object):

    def __init__(self, critic):
        self.critic = critic

    def get_action(self, obs):
        if len(obs.shape) > 3:
            observation = obs
        else:
            observation = obs[None]
        
        ## TODO return the action that maxinmizes the Q-value 
        # at the current observation as the output
        
        # transform the observation to a tensor
        observation = ptu.from_numpy(observation)
        action = self.critic.q_net(observation).argmax(dim=1)
        # return the action as a numpy array
        action = ptu.to_numpy(action)

        return action.squeeze()
