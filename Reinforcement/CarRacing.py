import gymnasium as gym
from stable_baselines3.common.evaluation import evaluate_policy
from stable_baselines3 import PPO, DQN
from stable_baselines3.common.callbacks import BaseCallback
from stable_baselines3.common.vec_env import DummyVecEnv, VecFrameStack
from timeit import default_timer as timer
from gymnasium import spaces
import numpy as np
from PIL import Image

def make_env():
    env = gym.make('CarRacing-v2', continuous=False)
    return env


def make_env_human():
    env = gym.make('CarRacing-v2', render_mode='human', continuous=False)
    return env

env = DummyVecEnv([make_env])

# เริ่มต้น environment
model = PPO('CnnPolicy', env, verbose=1, device='cuda')
modelDQN = DQN('CnnPolicy', env, verbose=1, device='cuda', buffer_size=50000)
model_path = ["CarRacing/CarR1", "CarRacing/CarR3Dqn"]

def learn(model=model, steps=300000, model_path=model_path[0]):
    start = timer()
    model.learn(total_timesteps=steps)
    end = timer()
    model.save(model_path)
    print(f"done, {end-start} sec")

#learn(model=modelDQN, model_path=model_path[1])

model_comp = PPO.load(model_path[0], env=env)
model_compDqn = DQN.load(model_path[1], env=env)

env = DummyVecEnv([make_env_human])

def Test(model=model_comp, env=env, score=0):
    observation = env.reset()

    terminated = False
    for _ in range(1000):
        action, _states = model.predict(observation)
    
        observation, reward, terminated, truncated = env.step(action)
        score += reward
        if terminated or truncated[0]['TimeLimit.truncated']:
            observation = env.reset()  # เริ่มใหม่ถ้าเกมจบ
    env.close()
    return score
#scoreR1 = Test(model=model_comp)
scoreR2Dqn = Test(model=model_compDqn)
print(scoreR2Dqn)