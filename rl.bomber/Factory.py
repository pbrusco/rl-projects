from Settings import *
from Task import *
from StochasticNavigationTask import *
from StochasticExplosionTask import *
from Agent import *
from RmaxAgent import *
from FactoredRmaxAgent import *
from SarsaLambdaAgent import *
from SarsaAgent import *

def createAgent():
	if AGENT == QLEARNING:
		return Agent()
	elif AGENT == RMAX:
		return RmaxAgent()
	elif AGENT == FACTOREDRMAX:
		return FactoredRmaxAgent()
	elif AGENT == SARSA:
		return SarsaAgent()
	elif AGENT == SARSALAMBDA:
		return SarsaLambdaAgent()
def createTask():
	if TASK == DETERMINISTIC:
		return Task()
	elif TASK == STOCHASTIC_NAVIGATION:
		return StochasticNavigationTask()
	elif TASK == STOCHASTIC_EXPLOSION:
		return StochasticExplosionTask()
