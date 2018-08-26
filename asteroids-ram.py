import gym
import time


env = gym.make('Asteroids-ram-v0')
env.reset()
actions = []
print(env.unwrapped.get_action_meanings())
for i in range(1000000):
    action = 1
    ob, reward, over, _ = env.step(actions[(i % len(actions))])
    print(reward)
    env.render()
print "score = 6040"
print(env.unwrapped.get_action_meanings())
