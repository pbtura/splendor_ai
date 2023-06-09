import matplotlib
import numpy as np
import gym
from gym import spaces
import matplotlib.pyplot as plt
from matplotlib import animation


class GameEnvironment(gym.Env):
    n_actions = 4

    def __init__(self):
        super(GameEnvironment, self).__init__()
        # Steps so far
        self.stepnum = 0

        # The action space
        self.action_space = spaces.Discrete(self.n_actions)
        # The observation space
        self.observation_space = gym.spaces.Dict(
            spaces={
                "position": gym.spaces.Box(low=0, high=(self.grid_size - 1), shape=(2,), dtype=np.int32),
                "direction": gym.spaces.Box(low=-1, high=1, shape=(2,), dtype=np.int32),
                "grid": gym.spaces.Box(low=0, high=3, shape=(self.grid_size, self.grid_size), dtype=np.uint8),
            })

    def reset(self):
        # Reset to initial positions
        self.stepnum = 0
        return self._get_obs()

    def _get_obs(self):
        pass

    def step(self, action):
        pass

    def render(self, mode='rgb_array'):
        pass

    def close(self):
        pass
