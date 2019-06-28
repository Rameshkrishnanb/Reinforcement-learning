#!/usr/bin/env python
import gym
import numpy as np
env=gym.make('Taxi-v2')
Q=np.zeros((500,6))
gamma=0.618
for episode in range(1,1000):
	pos=state=env.reset()
	reward=0
	count=0
	while reward!=20:
		action=np.argmax(Q[state])
		state2,reward,done,info=env.step(action)
		Q[state,action]=reward+gamma*np.max(Q[state2])
		state=state2
		count=count+1
	if episode%50==0:
		print 'Starting Position: ',pos,' No of moves required ',count,' in episode ',episode

print 'Q matrix \n',Q
