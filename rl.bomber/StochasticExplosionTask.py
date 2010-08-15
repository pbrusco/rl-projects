from Task import *
from Action import *
import random

EXPLODING_PROBABILITY = 0.5

class StochasticExplosionTask(Task):

	def perform(self,action):
		
		if action != Action.EXPLODE:
			return super(StochasticExplosionTask, self).perform(action)
		
		n = random.random()
		if n >= EXPLODING_PROBABILITY:
			newAction = Action.EXPLODE
		else:
			newAction = Action.DROP_BOMB

		return super(StochasticExplosionTask, self).perform(newAction)