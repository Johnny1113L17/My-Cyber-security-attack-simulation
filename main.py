import os
from stable_baselines3 import PPO
from env import CyberSecurityEnv

def train_model():
    env = CyberSecurityEnv()
    model = PPO("MlpPolicy", env, verbose=1)
    model.learn(total_timesteps=10000)
    model.save("ppo_cybersecurity")
    print(" 模型訓練完成並儲存為 ppo_cybersecurity.zip")

def test_model():
    env = CyberSecurityEnv()
    if not os.path.exists("ppo_cybersecurity.zip"):
        print(" 請先訓練模型")
        return
    model = PPO.load("ppo_cybersecurity", env=env)
    obs = env.reset()
    for i in range(100):
        action, _ = model.predict(obs, deterministic=True)
        obs, reward, done, _ = env.step(action)
        print(f"Step {i}: Action={action}, Reward={reward}, Done={done}, State={obs}")
        if done:
            print(" 目標被攻陷，模擬結束！")
            break

if __name__ == '__main__':
    mode = input("請輸入模式（train/test）：").strip().lower()
    if mode == "train":
        train_model()
    elif mode == "test":
        test_model()
    else:
        print("請輸入 'train' 或 'test'")
