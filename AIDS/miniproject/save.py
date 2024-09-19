import gymnasium as gym
from stable_baselines3 import A2C
from stable_baselines3 import PPO
import ale_py
import os
import time

models_dir = f'models/A2C-{int(time.time())}'
logdir = f'logs/A2C-{int(time.time())}'

if not os.path.exists(models_dir):
    os.makedirs(models_dir)

if not os.path.exists(logdir):
    os.makedirs(logdir)

env = gym.make("ALE/Alien-v5")

env.reset()

model = PPO('CnnPolicy', env, verbose=1, tensorboard_log=logdir)

TIMESTEPS = 10000
ITERATIONS = 100

for i in range(1, ITERATIONS+1):
    model.learn(total_timesteps=TIMESTEPS, reset_num_timesteps=False, tb_log_name="A2C")
    model.save(f"{models_dir}/{TIMESTEPS * i}")
    # print(f"Iteration {i} completed, model saved at {models_dir}/{TIMESTEPS * i}")

env.close()