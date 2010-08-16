from Settings import *
from Task import *
from StochasticNavigationTask import *
from StochasticExplosionTask import *
from Agent import *
from RmaxAgent import *

def createAgent():
	if AGENT == QLEARNING:
		return Agent()
	elif AGENT == RMAX:
		return RmaxAgent()

def createTask():
	if TASK == DETERMINISTIC:
		return Task()
	elif TASK == STOCHASTIC_NAVIGATION:
		return StochasticNavigationTask()
	elif TASK == STOCHASTIC_EXPLOSION:
		return StochasticExplosionTask()
