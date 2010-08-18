import random
import Print

from Action import *

LEARNING_RATE = 0.8
DISCOUNT_FACTOR = 0.95
EPSILON = 0.1


class QLearningAgent:

	def __init__(self):
		self.qTable = {}
	
	def learn(self, state, nextState, action, reward, nextChosenAction):
		
		previousQValue = self.getQValue(action,state) #valor previo de Q(s,a)
		maxFutureValue = max([self.getQValue(a,nextState) for a in Action.ACTIONS]) #valor futuro maximo desde el nuevo estado
		expectedDiscountedReward = reward + DISCOUNT_FACTOR*(maxFutureValue) 
		
		self.setQValue(action,state, previousQValue + LEARNING_RATE*(expectedDiscountedReward - previousQValue))
		
		
	def nextAction(self,state):
		if self.goRandom(): 
			return random.choice(Action.ACTIONS)
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