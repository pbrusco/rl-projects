from Action import *

class Environment:
	
	# for the moment and for simplicity we fix some values
	BOARD_HEIGHT = 8
	BOARD_WIDTH = 8
	EXIT = (7,7)
	WIN_REWARD = 10
	LOSE_REWARD = -10
	STONES = [(2,0),(2,2),(2,4),(2,6),(4,0),(4,2),(4,4),(4,6),(6,0),(6,2),(6,4),(6,6)]
	WALLS = [(1,2),(1,3),(1,5),(1,7),(3,2),(3,3),(3,5),(3,7),(5,2),(5,3),(5,5),(5,7)]

	def __init__(self):

		self.bombermanPos = (0,0)
		self.bomb = None
		self.isBombDropped = False
		self.walls = WALLS 
		self.stones = [False] * STONES.len()
		self.die = False
	

	def _hash_(self):
		
		if self.die:
			return -1 #if die stateCode = -1
		else 
			die = 0 

		pos = self.posUniqueId(self.bombermanPos)
		
		if self.isBombDropped:
			bomb =  self.posUniqueId(self.bomb) else bomb = BOARD_WIDTH*BOARD_HEIGHT	
	
		walls = 0
		for i in range(self.stones.len()):
			if self.stones[i]: stones = stones + 2**i

		hashingExponent = int(math.ceil(math.log(BOARD_WIDTH*BOARD_HEIGHT,2)))) #exponente dado por la cant de posiciones del trablero.

		return bomb + (2**hashingExponent)*pos + (2**(hashingExponent*hashingExponent))*stones
	
	
	def posUniqueId(self,cords):
		return cords[0]*BOARD_WIDTH + cords[1]
	
	# initialize bomberman game
	def startNewGame(self):
		
		self.bombermanPos= (0,0)
		self.bomb = None
		self.isBombDropped = False
		self.stones = [True] * STONES.len()
		self.die = False
	
	def performAction(self, action):
		
		# perform action
		if action == Action.UP: self.changePosIfpossible((0,1))
		elif action == Action.DOWN: self.changePosIfpossible((0,-1))
		elif action == Action.RIGHT: self.changePosIfpossible((1,0))
		elif action == Action.LEFT: self.changePosIfpossible((-1,0))
		elif action == Action.DROP_BOMB:
			if not self.isBombDroped: 
				self.isBombDropped = True
				self.bomb = self.bombermanPos
		elif action == Action.EXPLODE:
			if self.isBombDroped:
				if self.bombermanPos in (self.neighbours(self.bombermanPos)) or self.bombermanPos == self.bomb:
					self.die = True
				self.destroyStoneIfpossible()
				self.isBombDropped = False
				self.bomb = None
		
		reward = 0
		if (self.bombermanPos == self.EXIT):
			reward  = self.WIN_REWARD
			self.startNewGame()
		if (self.die):
			reward = self.LOSE_REWARD
			self.startNewGame()

		state = (self.bombermanPos, self.bomb, self.isBombDropped, self.walls, self.stones)	
		stateCode = self.hash(state)
		# return state code and reward
		return (stateCode, reward)
		
	def destroyStoneIfpossible(self):
		
		for i in range(self.stones.len()):
			if self.stones[i] == True and STONES[i] in self.neighbours(self.bomb): self.stones[i] = False	
		


	def neighbours(self, position):
		return [position + (1,0), position + (0,1), position + (-1,0), position + (0, -1)]
		
	def changePosIfpossible(self,mov):
		newPos = self.bombermanPos + mov 
		notInWall = newPos not in self.walls
		notInStone = if newPos in STONES: return self.stones[STONES.index(newPos)] 
		onBoard = self.onBoard(newPos)
		return notInWall and notInStone and onBoard: self.bombermanPos = newPos
		

	def onBoard(self,newPos):
		
		return (newPos[0]>=0 and newPos[0]<self.BOARD_WIDTH) and (newPos[1]>=0 and newPos[1]<self.BOARD_HEIGHT)
	
	def calculateStateCode(self):

			# calculate state code out of class members
			print "calculating..."
			
			return 0
			
	def stateCount(self):
		return 0

	def currentState(self):

	
	def actionCount(self):
		return Action.COUNT;
