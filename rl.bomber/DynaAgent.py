import random
from Action import *
import Print

LEARNING_RATE = 0.8
DISCOUNT_FACTOR = 0.95
EPSILON = 0.1
N = 1000

class DynaAgent:

	def __init__(self):
		self.qTable = {}
		self.model = {} 
	
	def learn(self, state, nextState, action, reward, nextChosenAction):

		previousQValue = self.getQValue(action,state) #valor previo de Q(s,a)
		maxFutureValue = max([self.getQValue(a,nextState) for a in Action.ACTIONS]) #valor futuro maximo desde el nuevo estado
		expectedDiscountedReward = reward + DISCOUNT_FACTOR*(maxFutureValue) 
		
		self.setQValue(action,state, previousQValue + LEARNING_RATE*(expectedDiscountedReward - previousQValue))
		
		self.setModelValue(action,state,(reward,nextState)) 
		for i in range(N): #Expande lo aprendido en estados visitados para reforzar el aprendizaje sin tener que actuar en el mundo.
			randomVisited = random.choice(self.qTable.keys())
			randomVisitedState = randomVisited[1]
			randomVisitedAction = randomVisited[0]
			oldReward,oldNextState = self.getModelValue(randomVisitedAction,randomVisitedState)
			
			previousQValue = self.getQValue(randomVisitedAction,randomVisitedState) 
			maxFutureValue = max([self.getQValue(a,oldNextState) for a in Action.ACTIONS])
			expectedDiscountedReward = oldReward + DISCOUNT_FACTOR*(maxFutureValue) 
		
			self.setQValue(randomVisitedAction,randomVisitedState, previousQValue + LEARNING_RATE*(expectedDiscountedReward - previousQValue))
		
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

	def setModelValue(self,action,state,value):
		self.model[(action,int(state))] = (value[0],int(value[1]))
		
	def getModelValue(self,action,state):
		return self.model.get((action,int(state))) or  (0.0,0.0)
		
	def inspect(self):
		return Print.prnDict(self.qTable) + Print.prnDict(self.modelTable)
