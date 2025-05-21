import gym
from gym import spaces

class CyberSecurityEnv(gym.Env):
    def __init__(self):
        super(CyberSecurityEnv, self).__init__()
        self.observation_space = spaces.Box(low=0, high=1, shape=(5,), dtype=int)
        self.action_space = spaces.Discrete(3)  # 3種攻擊動作
        self.state = self.reset()

    def reset(self):
        self.state = [0, 0, 0, 0, 0]
        return self.state

    def step(self, action):
        reward = 0
        done = False
        info = {}

        if action == 0:  # 掃描
            reward = 0.1
            self.state[0] = 1  # 發現漏洞
        elif action == 1:  # 攻擊漏洞
            if self.state[0] == 1:
                reward = 1.0
                done = True
            else:
                reward = -0.5
        elif action == 2:  # 嘗試橫向移動
            reward = -0.1

        return self.state, reward, done, info
