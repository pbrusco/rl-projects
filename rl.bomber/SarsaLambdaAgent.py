import random
from Action import *
import Print

MAXTURN = 1000
LAMBDA = 0.9
ALPHA = 0.8
GAMMA = 0.95
EPSILON = 0.1
ACTIONS = [0,1,2,3,4,5]

class SarsaLambdaAgent:

	def __init__(self):
		self.qTable = {}
		self.sarsaTable = {}
	
	def learn(self, state, nextState, action, reward, nextChosenAction):
		delta = reward + GAMMA*(self.getQValue(nextChosenAction,nextState))- self.getQValue(action,state) 
		self.setSarsaValue(action,state,self.getSarsaValue(action,state)+1)
		for a,s in self.sarsaTable.keys(): #Actualizo los diccionarios Q y Sarsa.
			self.setQValue(a,s,self.getQValue(a,s) + ALPHA*self.getSarsaValue(a,s)*delta)   
			self.setSarsaValue(a,s,LAMBDA * GAMMA)
		
		
		
		
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

	def getSarsaValue(self,action,state):
		return self.sarsaTable.get((action,int(state))) or 0.0 #float!
		
	def setSarsaValue(self,action,state,value):
 		self.sarsaTable[(action,int(state))] = value


	def inspect(self):
		return Print.prnDict(self.qTable)
