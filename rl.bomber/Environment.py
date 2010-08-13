from Action import *

class Environment:
	
	# for the moment and for simplicity we fix some values
	BOARD_HEIGHT = 8
	BOARD_WIDTH = 8
	EXIT = (7,7)
	WIN_REWARD = 10
	LOSE_REWARD = -10

	def __init__(self):

		self.bombermanPos = (0,0)
		self.bomb = None
		self.isBombDropped = False
		self.walls = []
		self.stones = []
		self.die = False
		
	
	# initialize bomberman game
	def startNewGame(self):
		
		self.bombermanPos= (0,0)
		self.bomb = None
		self.isBombDropped = False
		self.walls = [(1,2),(1,3),(1,5),(1,7),(3,2),(3,3),(3,5),(3,7),(5,2),(5,3),(5,5),(5,7)]
		self.stones = [(2,0),(2,2),(2,4),(2,6),(4,0),(4,2),(4,4),(4,6),(6,0),(6,2),(6,4),(6,6)]
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
		if (self.bombermanPos == EXIT):
			reward  = WIN_REWARD
			self.startNewGame()
		if (self.die):
			reward = LOSE_REWARD
			self.startNewGame()

		stateCode = (self.bombermanPos, self.bomb, self.isBombDropped, self.walls, self.stones)	
				
		# return state code and reward
		return (stateCode, reward)
		
	def destroyStoneIfpossible(self):
		 for stone in self.stones:
			for neighbour in self.neighbours (neighbours):
				if self.bomb == neighbour:
					self.stones.remove(stone)
					
	def neighbours(self, position):
		return [position + (1,0), position + (0,1), position + (-1,0), position + (0, -1)]
		
	def changePosIfpossible(self,mov):
		newPos = self.bombermanPos + mov 
		if (newPos not in self.walls) and  (newPos not in self.stones) and self.onBoard(newPos): self.bombermanPos = newPos
		

	def onBoard(self,newPos):
		
		return (newPos[0]>=0 and newPos[0]<self.BOARD_WIDTH) and (newPos[1]>=0 and newPos[1]<self.BOARD_HEIGHT)
	
	def calculateStateCode(self):

			# calculate state code out of class members
			print "calculating..."
			
			return 0
			
	def stateCount(self):
		return 0
	
	def actionCount(self):
		return Action.COUNT;
