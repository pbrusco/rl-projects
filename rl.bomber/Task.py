from Settings import *
from Status import *
from Environment import Environment

class Task:
	
	def __init__(self,env=Environment()):
		self.env = env
		
	def start(self):
		self.env.start()
	
	def perform(self,action):
		self.env.performAction(action)
		
		reward = 0.0 #float
		status = Status.CONTINUE
		state = self.env.state
		
		# TODO: Clone state before returning it
		
		if (state.bombermanPos == EXIT):
			reward = WIN_REWARD
			status = Status.WIN
		if (state.die):
			reward = LOSE_REWARD
			status = Status.DIE

		return (state, reward, status)
		
	def getState(self):
		return self.env.state
