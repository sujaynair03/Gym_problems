import gym
import time
import numpy as np
from utils import getPongState


env = gym.make('Pong-v0')
print(env.unwrapped.get_action_meanings())
for ep in range(1000):
	env.reset()
	next_action = 0
	for step in range(1000000):
	    action = 1
	    ob, reward, over, _ = env.step(next_action)
	    my_y, opp_y, ball_x, ball_y = getPongState(ob)
	    if my_y > ball_y:
	    	next_action = 2
	    elif my_y < ball_y:
	    	next_action = 3
	    elif my_y == ball_y:
	    	next_action = 2
	    print my_y, ball_y, next_action
	    if step % 2 == 0:
	    	next_action = 0
	    # if (np.abs(ball_y - my_y) <= 10):
	    # 	next_action = 0
	    env.render()
	    # print over
	    # time.sleep(0.1)
	    if over:
	    	break
    # time.sleep()
print "score = "
