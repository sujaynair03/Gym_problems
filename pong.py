import gym
import time
import numpy as np
from utils import getPongState


env = gym.make('Pong-v0')
env.reset()
actions = [2, 3]
print(env.unwrapped.get_action_meanings())
for i in range(1000000):
    action = 1
    ob, reward, over, _ = env.step(actions[(i % len(actions))])
    print(getPongState(ob))

    env.render()
    time.sleep(0.1)
print "score = 1750"
