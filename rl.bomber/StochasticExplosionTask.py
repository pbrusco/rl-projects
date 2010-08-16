from Task import *
from Action import *
import random

class StochasticExplosionTask(Task):

	def perform(self,action):
		
		if action != Action.EXPLODE:
			return super(StochasticExplosionTask, self).perform(action)
		
		n = random.random()
		if n >= BOMB_EXPLODING_PROBABILITY:
			newAction = Action.EXPLODE
		else:
			newAction = Action.DROP_BOMB

		return super(StochasticExplosionTask, self).perform(newAction)