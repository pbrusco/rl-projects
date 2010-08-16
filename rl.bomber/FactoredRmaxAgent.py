from Factor import *
from State import *
from DBN import *
from Reward import *
import random

RMAX_GAMMA_VALUE_ITER = 0.85
RMAX_EPSILON_VALUE_ITER = 1

class FactoredRmaxAgent: #usa kwik-rmax. ver p24 slide 5 del curso
	
	def __init__(self):
		self.Bdbn = BombermanDBN() #dbn para transiciones
		self.Rdbn = RewardsDBN()
		self.learnedFTransitions = {} #la cantidad de veces que nos movimos, tripla: action, valor de factores parent, valor de factor destino
		self.learnedFRewards = {} #acumulado, tripla: action, valor de factores estado parents, nombre factor reward.
		self.learnedFTCount = {} #dado un par (accion, tupla(factor)). cuantas veces realizamos dicha accion con dicha tupla, para Trans
		self.learnedFRCount = {} #dado un par (accion, tupla(factor)). cuantas veces realizamos dicha accion con dicha tupla, para Rewards
		self.visitedStates = set([])
		self.vmax = WIN_REWARD / (1 - RMAX_GAMMA_VALUE_ITER)
		self.reachableStates = set([])
		self.values = {}
		
	def increaseFTCount(self, action, factorsVal):
		prevCount = self.learnedFTCount.get((action, factorsVal)) or 0
		self.learnedFTCount[(action, factorsVal)] = prevCount + 1
	
	def increaseFRCount(self, action, factorsVal, rFact):
		prevCount = self.learnedFRCount.get((action, factorsVal, rFact)) or 0
		self.learnedFRCount[(action, factorsVal, rFact)] = prevCount + 1
		
	def getTValue(self, action, state, nextState):	#dado un estado, la accion y el siguiente estado, devuelve la probabilidad de moverse
		#TODO: si no nos movimos todavia de un factor a otro, que onda?
		#invalidamos toda la cuenta (o sea, 0)? o ignoramos (o sea, 1)? algun plan intermedio
		probability = 1.0
		for factor in Factor.FACTORS:
			factorValue = nextState.getFactorIntValue(factor) #el valor del factor
			parents = self.Bdbn.getParents(action, factor) #obtengo los parents
			parentsValuesList = []
			for parent in parents:
				parentsValuesList.append(state.getFactorIntValue(parent)) #el valor de los factores parent
			movements = self.learnedFTransitions.get((action, tuple(parentsValuesList), factorValue)) or 0 #ver el todo por el 1.0
			count = self.learnedFTCount.get((action, tuple(parentsValuesList))) or 1 #para que 1.0/1 = 1
			probability *= float(movements) / float(count)
		return probability
		
	def increaseFTValue(self, action, intParents, nextFactorVal):
		prevMovs = self.learnedFTransitions.get((action,intParents,nextFactorVal)) or 0
		self.learnedFTransitions[(action,intParents,nextFactorVal)] = prevMovs + 1
	
	def getRValue(self, action, state):
		#dado un estado y una accion, la suma del factor de reward empirico, o frmax si no es conocido
		sum = 0
		for rfact in Reward.REWARDS:
			sparents = self.Rdbn.getParents(rfact) #tupla de factores de estado de la que depende el factor reward
			parentsValuesList = []
			for parent in sparents:
				parentsValuesList.append(state.getFactorIntValue(parent))			
			rewardAcum = self.learnedFRewards.get((action, tuple(parentsValuesList), rfact)) or MaxReward.forFactor(rfact)
			#obtengo el dato empirico de, dado una accion y el valor de cada factor de estado de los parents del factor reward
			#o su rmax factorizado si no esta en la coleccion
			count = self.learnedFRCount.get((action, tuple(parentsValuesList), rfact)) or 1
			#la cantidad de veces que hicimos la accion dado los valores que me interesan
			#o 1 si no esta para que la division frmax / count = frmax
			sum += rewardAcum / count
		return sum
	
	def updateFRValue(self, action, intParents, rewardFactor, rewardValue):
		prevRew = self.learnedFRewards.get((action, intParents, rewardFactor)) or 0.0
		self.learnedFRewards[(action, intParents, rewardFactor)] = rewardValue + prevRew
		
	def learn(self, state, nextState, action, reward, dummy):
		self.updateTransitions(state, nextState, action)
		self.updateRewards(state, action, reward)
		#actualizo visitados (blancos)
		self.visitedStates.add(state)
		#actualizo alcanzables (blancos o grises)
		self.reachableStates.add(state)
		#actualizo alcanzables (blancos o grises)
		if int(nextState) != -1: 
			self.reachableStates.add(nextState)
				
	def updateTransitions(self, state, nextState, action):
		for factor in Factor.FACTORS:
			parents = self.Bdbn.getParents(action, factor)
			parentsValuesList = []
			for parent in parents:
				parentsValuesList.append(state.getFactorIntValue(parent))
			self.increaseFTCount(action, tuple(parentsValuesList)) #aca incremento el count de transiciones
			nextFactorVal = nextState.getFactorIntValue(factor) #el valor del factor de next
			self.increaseFTValue(action, tuple(parentsValuesList), nextFactorVal) #incremento cantidad de movimiento de factores a factor
	
	def updateRewards(self, state, action, reward):
		for rfact in Reward.REWARDS:
			sparents = self.Rdbn.getParents(rfact)
			parentsValuesList = []
			rVal = reward.getRewardForFactor(rfact)
			for parent in sparents:
				parentsValuesList.append(state.getFactorIntValue(parent))
			self.increaseFRCount(action, tuple(parentsValuesList), rfact) #incremento el count para rewards
			self.updateFRValue(action, tuple(parentsValuesList), rfact, rVal) #incremento el valor del reward
			
	def nextAction(self, state):
		#values = {} #los que visitamos, o sea, los aproximables. los no visitados asumimos Vmax. el valor va a ser una tupla (previous, current).
		values = self.values
		#necesitamos previous y current para comparar (current - previous) con el epsilon
		Q = {} #los q estimados
		#for visited in self.visitedStates: #inicializo en 0 los previous que son aproximables, el current no importa, asi que 0
		#	values[visited] = (0.0,0.0)
		errorBig = True #si seguimos iterando
		iterCount = 0
		errs = []
		while errorBig:
			iterCount += 1
			for visited in self.visitedStates:
				for action in Action.ACTIONS:
					partialQ = self.getRValue(action, visited) #inicializo con el reward dado el estado y la accion
					for possible in self.reachableStates: #todos los estados que se que existen
						if values.get(int(possible)) is None:
							valueToUse = 0.0 if possible in self.visitedStates else self.vmax #si no esta, uso vmax
						else:
							previous, current = values.get(int(possible)) #si esta, uso el previous
							valueToUse = previous #da lo mismo cual usar entre previous y current, a esta altura son lo mismo
							#a continuacion, cambio current para comparar con el error, pero, al final de la iteracion
							#seteo el previous con el current
						partialQ += RMAX_GAMMA_VALUE_ITER * self.getTValue(action, visited, possible) * valueToUse
						#pongo el valor anterior si es aproximable, o vmax si no es aproximable (si nunca voy a saber nada)
						#todo multiplicado por el gamma, obvio
					Q[(action,int(visited))] = partialQ
				previous, current = values.get(int(visited)) or (0.0,0.0)
				values[int(visited)] = previous, max([Q[(a,int(visited))] for a in Action.ACTIONS]) #el valor es el maximo de los Q
				#actualizo el current con el maximo de los Q, o sea, el V obtenido
			
			differences = [abs((i-j)) for(i,j) in values.values()]
			err = max(differences) if differences != [] else 0 #norma infinito, norma 2 tiraba overflow
			errs.append(err)
			errorBig = err > RMAX_EPSILON_VALUE_ITER #si es mayor al epsilon, sigo iterando. si no, no.
			for (key, value) in values.iteritems():
				previous, current = value
				values[key] = (current, current) # el previous lo seteo en el current
		
		#bien, ya sali
		#ahora, dado el Q, quiero la accion que maximice
		qMax = max([(Q.get((a,int(state))) or 0.0) for a in Action.ACTIONS])
		#print [(a,self.getRValue(a, state)) for a in Action.ACTIONS]
		return random.choice([a for a in Action.ACTIONS if (Q.get((a,int(state)))or 0.0)==qMax])
		
		#Old: pick first
		#return max(Action.ACTIONS, key=(lambda a: Q(a,intState)))
		#si no esta definido, elijo al azar			