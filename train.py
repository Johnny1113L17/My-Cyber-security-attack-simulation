from stable_baselines3 import PPO
from env import CyberSecurityEnv

def train_agent():
    env = CyberSecurityEnv()
    model = PPO("MlpPolicy", env, verbose=1)
    model.learn(total_timesteps=10000)
    model.save("ppo_cybersecurity")

if __name__ == "__main__":
    train_agent()
