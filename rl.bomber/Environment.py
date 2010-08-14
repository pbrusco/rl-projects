from Action import *
from Settings import *
from State import State

class Environment:
	
	def __init__(self):
		self.state = State()
	
	def start(self):
		self.state = State()
	
	def performAction(self, action):
		if action == Action.UP: 
			self.tryChangePos((0,1))
		elif action == Action.DOWN: 
			self.tryChangePos((0,-1))
		elif action == Action.RIGHT: 
			self.tryChangePos((1,0))
		elif action == Action.LEFT: 
			self.tryChangePos((-1,0))
		elif action == Action.DROP_BOMB:
			if not self.state.isBombDropped: 
				self.state.isBombDropped = True
				self.state.bomb = self.state.bombermanPos
		elif action == Action.EXPLODE:
			if self.state.isBombDropped:
				if self.state.bombermanPos in (self.neighbours(self.state.bombermanPos)) or self.state.bombermanPos == self.state.bomb:
					self.state.die = True
				self.destroyStoneIfpossible()
				self.state.isBombDropped = False
				self.state.bomb = None
	
			
	def destroyStoneIfpossible(self):		
		for i in range(len(self.state.stones)):
			if self.state.stones[i] == True and STONES[i] in self.neighbours(self.bomb): 
				self.state.stones[i] = False	
		

	def neighbours(self, position):
		return [position + (1,0), position + (0,1), position + (-1,0), position + (0, -1)]
		
		
	def tryChangePos(self,mov):
		newPos = self.state.bombermanPos + mov 
		notInWall = newPos not in WALLS
		notInStone = newPos in STONES and self.state.stones[STONES.index(newPos)] 
		onBoard = self.onBoard(newPos)
		if notInWall and notInStone and onBoard: self.state.bombermanPos = newPos
		

	def onBoard(self,newPos):		
		return (newPos[0]>=0 and newPos[0]<BOARD_WIDTH) and (newPos[1]>=0 and newPos[1]<BOARD_HEIGHT)
	

	def actionCount(self):
		return Action.COUNT;
