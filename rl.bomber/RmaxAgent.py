from Action import *
import random
import Print
from Settings import *

 
RMAX_GAMMA_VALUE_ITER = 0.85
RMAX_EPSILON_VALUE_ITER = 1

class RmaxAgent: #usa kwik-rmax. ver p24 slide 5 del curso
	
	def __init__(self):
		self.learnedRewards = {} #el acumulado, no el valor real
		self.learnedTransitions = {} #la cantidad de veces que nos movimos
 		self.learnedCount = {} #dado un par (accion, estado), la cantidad de veces que hicimos la accion partiendo del estado
 		self.visitedStates = set([])
 		self.vmax = WIN_REWARD / (1 - RMAX_GAMMA_VALUE_ITER)
 		self.reachableStates = set([])
 		self.values = {}
 	
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
 			return 0.0
 		else:
 			return float(movements)/float(count)
 			
 	def increaseTValue(self, action, intState, intNextState):
  		prevMovs = self.learnedTransitions.get((action,intState,intNextState)) or 0
  		self.learnedTransitions[(action,intState,intNextState)] = prevMovs + 1
  		
  	def increaseCount(self, action, intState):
  		prevCount = self.learnedCount.get((action,intState)) or 0
  		self.learnedCount[(action, intState)] = prevCount + 1
  		
  	def learn(self, state, nextState, action, reward, nextChosenAction):
  		intState = int(state)
  		intNextState = int(nextState)
  		self.increaseCount(action, intState) #actualizo cantidad de veces que hicimos de estado a accion
  		self.updateRValue(action, intState, reward) #actualizo reward
  		self.increaseTValue(action, intState, intNextState) #actualizo chance de nuevo estado dado accion estado
  		#actualizo visitados (blancos)
  		self.visitedStates.add(intState)
  		#actualizo alcanzables (blancos o grises)
  		self.reachableStates.add(intState)
  		#actualizo alcanzables (blancos o grises)
  		if intNextState != -1: 
  			self.reachableStates.add(intNextState)
  		
  	def nextAction(self, state):
  		intState = int(state)
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
  						if values.get(possible) is None:
  							valueToUse = 0.0 if possible in self.visitedStates else self.vmax #si no esta, uso vmax
  						else:
  							previous, current = values.get(possible) #si esta, uso el previous
  							valueToUse = previous #da lo mismo cual usar entre previous y current, a esta altura son lo mismo
  							#a continuacion, cambio current para comparar con el error, pero, al final de la iteracion
  							#seteo el previous con el current
  						partialQ += RMAX_GAMMA_VALUE_ITER * self.getTValue(action, visited, possible) * valueToUse
  						#pongo el valor anterior si es aproximable, o vmax si no es aproximable (si nunca voy a saber nada)
  						#todo multiplicado por el gamma, obvio
  					Q[(action,visited)] = partialQ
  				previous, current = values.get(visited) or (0.0,0.0)
  				values[visited] = previous, max([Q[(a,visited)] for a in Action.ACTIONS]) #el valor es el maximo de los Q
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
  		qMax = max([(Q.get((a,intState)) or 0.0) for a in Action.ACTIONS])
  		return random.choice([a for a in Action.ACTIONS if (Q.get((a,intState))or 0.0)==qMax])
  		
  		#Old: pick first
  		#return max(Action.ACTIONS, key=(lambda a: Q(a,intState)))
  		#si no esta definido, elijo al azar
  			
  	def inspect(self):
  		return "\n\n".join([
  			"Learned rewards",
  			Print.prnDict(self.learnedRewards),
  			"Learned transitions",
  			Print.prnDict(self.learnedTransitions),
  			"Learned count",
  			Print.prnDict(self.learnedCount),
  			"Blancos",
  			str(self.visitedStates),
  			"Grises y blancos",
  			str(self.reachableStates),
  		])