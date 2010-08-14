from Settings import *

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
		
		def posUniqueId(cords):
			try:
				x,y = cords
			except:
				print cords
				raise
			return x*BOARD_WIDTH + y
		
		if self.die: return -1 #if die stateCode = -1
		else: die = 0 

		pos = posUniqueId(self.bombermanPos)
	
		if self.isBombDropped: bomb =  posUniqueId(self.bomb) 
		else: bomb = BOARD_WIDTH*BOARD_HEIGHT	

		stones = 0
		for i in range(len(self.stones)):
			if self.stones[i]: stones = stones + 2**i

		hashingExponent = int(math.ceil(math.log(BOARD_WIDTH*BOARD_HEIGHT,2))) #exponente dado por la cant de posiciones del trablero.

		return bomb + (2**hashingExponent)*pos + (2**(hashingExponent*hashingExponent))*stones

		
		