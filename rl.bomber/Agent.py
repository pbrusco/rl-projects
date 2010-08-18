import random
import Print

from Action import *

ALPHA = 0.8
GAMMA = 0.95
EPSILON = 0.1
ACTIONS = Action.ACTIONS

class Agent:

	def __init__(self):
		self.qTable = {}
	
	def learn(self, previous, state, action, reward, nextChosenAction):
		previousValue = self.getQValue(action,previous)
		value = previousValue + ALPHA*(reward + GAMMA*(max([self.getQValue(a,state) for a in ACTIONS])) - previousValue)
		self.setQValue(action,previous,value)
		#print self.qTable
		
	def nextAction(self,state):
		if self.goRandom(): 
			return random.choice(ACTIONS)
		else: 
			qMax = max([self.getQValue(a,state) for a in Action.ACTIONS])	
			return random.choice([a for a in Action.ACTIONS if self.getQValue(a,state)==qMax])

	def goRandom(self):
		return random.random() < EPSILON

	def getQValue(self,action,state):
		return self.qTable.get((action,int(state))) or 0.0 #float!
		
	def setQValue(self,action,state,value):
 		self.qTable[(action,int(state))] = value

	def inspect(self):
		return Print.prnDict(self.qTable)