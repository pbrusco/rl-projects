#!/usr/local/bin/python

from Environment import *
from Agent import *

env = Environment()
agent = Agent()

env.startNewGame()
i = 0
MAX = 100000
previous = 0	
while i < MAX:
	action = agent.nextAction(previous)
	(state, reward) = env.performAction(action)
	agent.learn(previous,state,action,reward)
	previous = state
	i += 1


