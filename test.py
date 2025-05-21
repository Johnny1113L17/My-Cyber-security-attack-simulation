from stable_baselines3 import PPO
from env import CyberSecurityEnv

def test_agent():
    env = CyberSecurityEnv()
    model = PPO.load("ppo_cybersecurity")

    obs = env.reset()
    for i in range(100):
        action, _states = model.predict(obs, deterministic=True)
        obs, reward, done, info = env.step(action)
        print(f"Step {i}: Action={action}, Reward={reward}, Done={done}, State={obs}")
        if done:
            print("目標被攻陷！")
            break

if __name__ == "__main__":
    test_agent()
