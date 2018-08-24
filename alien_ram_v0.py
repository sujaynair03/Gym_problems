import gym
import time


env = gym.make('Alien-ram-v0')
env.reset()
actions = [1,9,11,2,5,10,3,11,4,10,1,5,2,5,13,6,14,15,1,5,4,13,5,15,1,2,3,4,12,5,14,15,3,5,12,3,1]
print(env.unwrapped.get_action_meanings())
for i in range(1000000):
	action = 1
	ob, reward, over, _ = env.step(actions[(i % len(actions))])
	print(reward)
	env.render()
print "score = "
