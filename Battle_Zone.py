import gym
import time


env = gym.make('BattleZone-ram-v0')
env.reset()
actions = [1,10,11,12,1,10,11,12,1,10,11,12]
print(env.unwrapped.get_action_meanings())
for i in range(1000000):
	action = 1
	ob, reward, over, _ = env.step(actions[(i % len(actions))])
	print(reward)
	env.render()
print "score = 11000"
print(env.unwrapped.get_action_meanings())