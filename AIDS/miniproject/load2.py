import gymnasium as gym
from stable_baselines3 import A2C
from stable_baselines3 import PPO
from stable_baselines3.common.vec_env import DummyVecEnv
import ale_py
import os
import time

env = gym.make('ALE/Alien-v5', render_mode='human')
env = DummyVecEnv([lambda: env])

models_dir = 'models/PPO-1726035502'
model_path = f"{models_dir}/50000.zip"

model = PPO.load(model_path, env=env)

episodes = 10

for ep in range(episodes):
    obs = env.reset()
    done = False
    while not done:
        env.render()
        action, _ = model.predict(obs)
        obs, reward, done, info = env.step(action)

env.close()