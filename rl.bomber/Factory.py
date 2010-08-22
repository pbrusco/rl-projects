from Settings import *
from Task import *
from StochasticNavigationTask import *
from StochasticExplosionTask import *
from QLearningAgent import *
from RmaxAgent import *
from FactoredRmaxAgent import *
from SarsaLambdaAgent import *
from SarsaAgent import *
from DynaAgent import *

def createAgent():
	if AGENT == QLEARNING:
		return QLearningAgent()
	elif AGENT == RMAX:
		return RmaxAgent()
	elif AGENT == FACTOREDRMAX:
		return FactoredRmaxAgent()
	elif AGENT == SARSA:
		return SarsaAgent()
	elif AGENT == SARSALAMBDA:
		return SarsaLambdaAgent()
	elif AGENT == DYNA:
		return DynaAgent()	

def createTask(env=None):
	env = env or Environment()
	if TASK == DETERMINISTIC:
		return Task(env)
	elif TASK == STOCHASTIC_NAVIGATION:
		return StochasticNavigationTask(env)
	elif TASK == STOCHASTIC_EXPLOSION:
		return StochasticExplosionTask(env)
