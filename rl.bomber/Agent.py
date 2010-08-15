import random


ALPHA = 0.8
GAMMA = 0.95
EPSILON = 0.1
ACTIONS = [0,1,2,3,4,5]

class Agent:

	def __init__(self):
		self.qTable = {}
	
	def learn(self, previous, state, action, reward):
		previousValue = self.getQValue(action,previous)
		value = previousValue + ALPHA*(reward + GAMMA*(max([self.getQValue(a,state) for a in ACTIONS])) - previousValue)
		self.setQValue(action,previous,value)
		
	def nextAction(self,state):
		if self.goRandom(): 
			return random.choice(ACTIONS)
		else: 
			qMax = max([self.getQValue(a,state) for a in ACTIONS])	
			return random.choice([a for a in ACTIONS if getQValue(a)==qMax])

	def goRandom(self):
		return random.random() < EPSILON

	def getQValue(self,action,state):
		return self.qTable.get((action,int(state))) or 0.0 #float!
		
	def setQValue(self,action,state,value):
 		self.qTable[(action,int(state))] = value 




