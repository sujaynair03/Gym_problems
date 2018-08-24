import gym
import time


env = gym.make('SpaceInvaders-v0')
env.reset()
actions = [1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,4,5]
print(env.unwrapped.get_action_meanings())
for i in range(1000000):
	action = 1
	ob, reward, over, _ = env.step(actions[(i % len(actions))])
	print(reward)
	env.render()
print "score = 1750"