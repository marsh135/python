from pathlib import Path
import gymnasium as gym
import ale_py
from stable_baselines3 import DQN
from stable_baselines3.common.env_util import make_atari_env
from stable_baselines3.common.vec_env import VecFrameStack

gym.register_envs(ale_py)

# Copy your final saved model here and name the copy my_model.zip.
MODEL_PATH = Path(__file__).resolve().parent / "models/my_model.zip"
WATCH_STEPS = 2000

agent = DQN.load(MODEL_PATH, device="cpu")

# TODO: Match your training game and wrappers, with render_mode="human".
watch_env = None
if watch_env is None:
    raise NotImplementedError("Complete the viewing environment setup.")
watch_env = VecFrameStack(watch_env, n_stack=4)
try:
    observation = watch_env.reset()
    for step in range(WATCH_STEPS):
        action, _ = agent.predict(observation, deterministic=True)
        observation, rewards, dones, infos = watch_env.step(action)
finally:
    watch_env.close()
