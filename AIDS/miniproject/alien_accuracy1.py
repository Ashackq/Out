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

total_rewards = []
successful_episodes = 0

def evaluate_model(model, env, episodes = 10):
    total_rewards =[]
    
    for episode in range(episodes):
        obs = env.reset()
        done = False
        episode_reward = 0
        
        while not done:
            action, _=model.predict(obs)
            obs, reward, done, _=env.step(action)
            
            episode_reward += reward[0]
        
        total_rewards.append(episode_reward)
        print(f"Episode {episode + 1}: Reward = {episode_reward}")
    
        if episode_reward > max(total_rewards):
            successful_episodes += 1

    mean_reward = sum(total_rewards) / episodes
    accuracy_reward = (mean_reward / max(total_rewards)) * 100
    
    print(f"Average Reward over {episodes} episodes: {accuracy_reward}")
    
episodes = 10

evaluate_model(model, env, episodes=10)

for ep in range(episodes):
    obs = env.reset()
    done = False
    while not done:
        env.render()
        action, _ = model.predict(obs)
        obs, reward, done, info = env.step(action)

env.close()