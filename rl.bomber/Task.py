#!/usr/local/bin/python

from Environment import *
from Agent import *

env = Environment()
agent = Agent(env.stateCount(), env.actionCount())

env.startNewGame()

i = 0
MAX = 100000
while i < MAX:
	action = agent.nextAction()
	(stateCode, reward) = env.performAction(action)
	agent.learn(stateCode, reward)
	i += 1