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

		hashingExponent = self.getHashingExponent()
		return bomb + (2**hashingExponent)*pos + (2**(hashingExponent*2))*stones

	def __eq__(self, nextstate)	:
		if nextstate == None: return False
		bombermanPosEq = (nextstate.bombermanPos == self.bombermanPos)
		bombEq = (nextstate.bomb == self.bomb)
		isBombDroppedEq = (nextstate.isBombDropped == self.isBombDropped)
		stonesEq = (nextstate.stones == self.stones)
		dieEq = (nextstate.die == self.die)
		return (bombermanPosEq and bombEq and isBombDroppedEq and stonesEq and dieEq)
		
	def __str__(self):
		return "(Bomberman %s | Bomb %s | Stones %s)" % (self.bombermanPos, self.bomb, self.stones) if not self.die else "(Dead)"
	
	def getHashingExponent(self,extrapos=0):
		# exponente dado por la cant de posiciones del tablero
		# agregado +1 por bomb fuera de tablero
		return int(math.ceil(math.log(BOARD_WIDTH*BOARD_HEIGHT+1+extrapos,2)))

	def getFactorIntValue(self, factor):
		hashingExponent = self.getHashingExponent(1)
		if factor == Factor.POSITION:
			return (2**hashingExponent) * (self.posUniqueId(self.bombermanPos) + 1)
		elif factor == Factor.BOMB:
			return (self.posUniqueId(self.bomb) if self.isBombDropped else BOARD_WIDTH*BOARD_HEIGHT)+1
		elif factor == Factor.STONES:
			stones = 0
			for i in range(len(self.stones)):
				if self.stones[i]: 
					stones = stones + 2**i
			return (2**(hashingExponent*3)) * (stones+1)
		elif factor == Factor.DEAD:
			return -1 if self.die else -2
		elif factor == Factor.DELTABOMB:
			if self.isBombDropped:
				mi,mj = self.bombermanPos
				bi,bj = self.bomb
				value = self.posUniqueId((int(abs(mi-bi)),int(abs(mj-bj))))
			else:
				value= BOARD_WIDTH * BOARD_HEIGHT
			return (2**(hashingExponent*2)) * (value+1)
		else:
			raise Exception("Unknown factor")
		
	def posUniqueId(self,cords):
		x,y = cords
		return x*BOARD_WIDTH + y
		
	