import gym
import time


env = gym.make('AirRaid-v0')
env.reset()
actions = [1, 4, 2, 3, 5, 3, 4, 2, 5, 3, 4, 1]
print(env.unwrapped.get_action_meanings())
for i in range(1000000):
    action = 1
    ob, reward, over, _ = env.step(actions[(i % len(actions))])
    print(reward)
    env.render()
print "score = 1750 on first try, score will vary even if code is the same"
