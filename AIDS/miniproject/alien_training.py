import gymnasium as gym
from stable_baselines3 import PPO
from stable_baselines3.common.vec_env import DummyVecEnv, VecFrameStack, VecMonitor
from stable_baselines3.common.monitor import Monitor
import ale_py
import os
import time

models_dir = f"models/PPO-{int(time.time())}"
logs_dir = f"logs/PPO-{int(time.time())}"

if not os.path.exists(models_dir):
    os.makedirs(models_dir)

if not os.path.exists(logs_dir):
    os.makedirs(logs_dir)

env = gym.make("ALE/Alien-v5")
env = Monitor(env)
env = DummyVecEnv([lambda: env])
env = VecFrameStack(env, n_stack=4)
env = VecMonitor(env)

env.reset()

model = PPO(
    "CnnPolicy",
    env,
    verbose=1,
    tensorboard_log=logs_dir,
    learning_rate=3e-4,
    n_steps=2048,
    batch_size=64,
    n_epochs=10,
    gamma=0.99,
    gae_lambda=0.95,
    clip_range=0.2,
    ent_coef=0.01,
)

TIMESTEPS = 50000
ITERATIONS = 20
EVAL_EPISODES = 10


def evaluate_model(model, env, num_episodes):
    total_rewards = []
    for episode in range(num_episodes):
        obs = env.reset()
        done = False
        episode_reward = 0
        while not done:
            action, _ = model.predict(obs, deterministic=True)
            obs, reward, done, info = env.step(action)
            episode_reward += reward[0]
            done = done[0]
        total_rewards.append(episode_reward)
    avg_reward = sum(total_rewards) / num_episodes
    print(f"Average reward over {num_episodes} episodes: {avg_reward}")
    return avg_reward


for i in range(1, ITERATIONS + 1):
    model.learn(total_timesteps=TIMESTEPS, reset_num_timesteps=False, tb_log_name="PPO")
    model.save(f"{models_dir}/{TIMESTEPS * i}")

    avg_reward = evaluate_model(model, env, num_episodes=EVAL_EPISODES)
    print(
        f"Iteration {i} completed, model saved at {models_dir}/{TIMESTEPS * i}, Average Reward: {avg_reward}"
    )

env.close()
