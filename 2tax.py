#!/usr/bin/env python
import gym
import numpy as np
import os
import time
env=gym.make('Taxi-v2')
Q=np.zeros((500,6))
gamma=0.618
for episode in range(1500):
	env.reset()
	state=env.env.s=episode%500
	reward=0
	count=0
	while reward!=20:
		action=np.argmax(Q[state])
		state2,reward,done,info=env.step(action)
		Q[state,action]=reward+gamma*np.max(Q[state2])
		state=state2
		count=count+1
	if episode%50==0:
		print 'State :',episode,'No. of moves : ',count
print 'Q matrix \n',Q
for episode in range(100):
	pos=state=env.reset()
	reward=0
	count=0
	while reward!=20:
		os.system('clear')
		action=np.argmax(Q[state])
		state,reward,done,info=env.step(action)
		count=count+1
		print 'State : ',env.env.s
		print 'Moves : ',count
		print 'Reward : ',reward
		env.render()
		if action==5 or action==4:
			print 'pick/drop'
			#time.sleep(2)
		else:
			print '   '
		time.sleep(1)
	print 'Iteration : ',episode
	print 'State : ',pos
	print 'Number of moves : ',count
	time.sleep(3)
