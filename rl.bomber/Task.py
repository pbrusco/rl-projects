#!/usr/local/bin/python

from Environment import *
from Agent import *
import time

env = Environment()
agent = Agent()

env.startNewGame()

# This function returns the time as a floating point number expressed in seconds since the epoch, in UTC.
start = time.time()
actionsCount = 0
state = 0
previous = 0
while(no termino el juego): 
	
	action = agent.nextAction(previous)
	
	(state, reward) = env.performAction(action)
	agent.learn(previous,state,action,reward)
	previous = state
	actionsCount += 1
total = time.time() - start
didAgentWin = (reward == env.WIN_REWARD)
	


