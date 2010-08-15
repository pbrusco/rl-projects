from Settings import *
from Action import *

RMAX_GAMMA_VALUE_ITER = 0.95
RMAX_EPSILON_VALUE_ITER = 0.05

class RmaxAgent: #usa kwik-rmax. ver p24 slide 5 del curso
	
	def __init__(self):
		self.learnedRewards = {} #el acumulado, no el valor real
		self.learnedTransitions = {} #la cantidad de veces que nos movimos
		self.learnedCount = {} #dado un par (accion, estado), la cantidad de veces que hicimos la accion partiendo del estado
		self.visitedStates = []
		self.vmax = WIN_REWARD / (1 - RMAX_GAMMA_VALUE_ITER)
		self.reachableStates = []
	
	def getRValue(self, action, intState): #dado un estado y una accion, su reward empirico, o rmax si alguno no conocido
		reward = self.learnedRewards.get((action,intState))
		count = self.learnedCount.get((action,intState))
		if reward is None:
			return WIN_REWARD
		else:
			return reward/count
		
	def updateRValue(self, action, intState, reward): #se updatea el reward dado un estado y la accion
		prevReward = self.learnedRewards.get((action,intState)) or 0.0
		self.learnedRewards[(action,intState)] = reward + prevReward
		
			
	
	def getTValue(self, action, intState, intNextState): #dado un estado, la accion y el siguiente estado, devuelve la probabilidad de moverse
		movements = self.learnedTransitions.get((action,intState,intNextState))
		count = self.learnedCount.get((action,intState))
		if movements is None:
			if intState == intNextState:
				return 1.0
			else:
				return 0.0
		else:
			return float(movements)/float(count)
			
	def increaseTValue(self, action, intState, intNextState):
		prevMovs = self.learnedTransitions.get((action,intState,intNextState)) or 0
		self.learnedTransitions[(action,intState,intNextState)] = prevMovs + 1
		
	def increaseCount(self, action, intState):
		prevCount = self.learnedCount.get((action,intState)) or 0
		self.learnedCount[(action, intState)] = prevCount + 1
		
	def learn(self, state, nextState, action, reward):
		intState = int(state)
		intNextState = int(nextState)
		self.increaseCount(action, intState) #actualizo cantidad de veces que hicimos de estado a accion
		self.updateRValue(action, intState, reward) #actualizo reward
		self.increaseTValue(action, intState, intNextState) #actualizo chance de nuevo estado dado accion estado
		if intState not in self.visitedStates: #actualizo visitados (blancos)
			self.visitedStates.append(intState)
		if intState not in self.reachableStates: #actualizo alcanzables (blancos o grises)
			self.reachableStates.append(intState)
		if intNextState not in self.reachableStates: #actualizo alcanzables (blancos o grises)
			self.reachableStates.append(intNextState)
		
	def nextAction(self, state):
		intState = int(state)
		values = {} #los que visitamos, o sea, los aproximables. los no visitados asumimos Vmax. el valor va a ser una tupla (previous, current).
		#necesitamos previous y current para comparar (current - previous) con el epsilon
		Q = {} #los q estimados
		for visited in self.visitedStates: #inicializo en 0 los previous que son aproximables, el current no importa, asi que 0
			values[visited] = (0,0)
		errorBig = True #si seguimos iterando
		while errorBig:
			for visited in self.visitedStates:
				for action in Action.ACTIONS:
					partialQ = self.getRValue(action, visited) #inicializo con el reward dado el estado y la accion
					for possible in self.reachableStates: #todos los posibles, si no está en reachable el T va a ser 0 y no vale la pena iterar
						if values.get(possible) is None:
							valueToUse = self.vmax #si no está, uso vmax
						else:
							previous, current = values.get(possible) #si está, uso el previous
							valueToUse = previous #da lo mismo cuál usar entre previous y current, a esta altura son lo mismo
							#a continuacion, cambio current para comparar con el error, pero, al final de la iteracion
							#seteo el previous con el current
						partialQ += RMAX_GAMMA_VALUE_ITER * self.getTValue(action, visited, possible) * valueToUse
						#pongo el valor anterior si es aproximable, o vmax si no es aproximable (si nunca voy a saber nada)
						#todo multiplicado por el gamma, obvio
					Q[(action,visited)] = partialQ
				previous, current = values[visited]
				values[visited] = previous, max([Q(a,visited) for a in Action.ACTIONS]) #el valor es el maximo de los Q
				#actualizo el current con el maximo de los Q, o sea, el V obtenido
			errorBig = (sum([(i-j)**2 for(i,j) in zip(currentValues, previousValues)]) ** 0.5) > RMAX_EPSILON_VALUE_ITER
			# obtengo la norma dos de la diferencia entre current y previous. si la norma es mayor al epsilon, sigo iterando, si no, no itero
			#ahora pongo en previous el valor de current
			for (key, value) in values:
				previous, current = value
				values[key] = (current, current) # el previous lo seteo en el current
		
		#bien, ya salí
		#ahora, dado el Q, quiero la accion que maximice
		qMax = max([Q(a,intState) for a in Action.ACTIONS])	
		return random.choice([a for a in Action.ACTIONS if Q(a,intState)==qMax])
		
		#Old: pick first
		#return max(Action.ACTIONS, key=(lambda a: Q(a,intState)))
			