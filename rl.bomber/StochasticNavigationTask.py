from Task import *
from Action import *
import random

class StochasticNavigationTask(Task):

	def perform(self,action):
		
		# probability of doing action passed as parameter = 0.8
		# probability of doing another action1 or action2 = 0.1 each
		
		if action not in [Action.UP, Action.DOWN, Action.LEFT, Action.RIGHT]:
			return super(StochasticNavigationTask, self).perform(action)
		
		n = random.random()
		if n >= 0.2:
			return super(StochasticNavigationTask, self).perform(action)
		elif n >= 0.1:
		 	index = 0
		else:
			index = 1

		if action == Action.UP or action == Action.DOWN : 
			newAction =  [Action.LEFT, Action.RIGHT][index]
		elif action == Action.LEFT or action == Action.RIGHT : 
			newAction =  [Action.UP, Action.DOWN][index]
			
		return super(StochasticNavigationTask, self).perform(newAction)