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
	elif AGENT == FACTOREDRMAX:
		return FactoredRmaxAgent()

def createTask():
	# TODO: Return flat state stochastic tasks
	if TASK == DETERMINISTIC:
		if AGENT in FACTOREDAGENTS: return Task()
		else: return FlatStateTask()
	elif TASK == STOCHASTIC_NAVIGATION:
		return StochasticNavigationTask()
	elif TASK == STOCHASTIC_EXPLOSION:
		return StochasticExplosionTask()
