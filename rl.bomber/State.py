from Maps import *
from Factor import Factor

import math

class State:

	def __init__(self):
		self.bombermanPos = (0,0)
		self.bomb = None
		self.isBombDropped = False
		self.stones = [True] * len(STONES) # position i is true iif stone i is still present and has not been destroyed
		self.die = False
			
	def __int__(self):
		return self.__hash__()
	
	def __hash__(self):
		if self.die: return -1 #if die stateCode = -1
		else: die = 0 

		pos = self.posUniqueId(self.bombermanPos)
	
		if self.isBombDropped: bomb =  self.posUniqueId(self.bomb) 
		else: bomb = BOARD_WIDTH*BOARD_HEIGHT	

		stones = 0
		for i in range(len(self.stones)):
			if self.stones[i]: stones = stones + 2**i

		hashingExponent = int(math.ceil(math.log(BOARD_WIDTH*BOARD_HEIGHT,2))) #exponente dado por la cant de posiciones del trablero.

		return bomb + (2**hashingExponent)*pos + (2**(hashingExponent*hashingExponent))*stones

	def getFactorIntValue(self, factor):
		if factor == Factor.POSITION:
			return self.posUniqueId(self.bombermanPos)
		elif factor == Factor.BOMB:
			return self.posUniqueId(self.bomb) if self.isBombDropped else BOARD_WIDTH*BOARD_HEIGHT
		elif factor == Factor.STONES:
			stones = 0
			for i in range(len(self.stones)):
				if self.stones[i]: 
					stones = stones + 2**i
			return stones
		elif factor == Factor.DEAD:
			return -1 if self.die else 1
		else:
			raise Exception("Unknown factor")
		
	def posUniqueId(self,cords):
		try:
			x,y = cords
		except:
			print cords
			raise
		return x*BOARD_WIDTH + y
		