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
			self.tryChangePos((-1,0))
		elif action == Action.DOWN: 
			self.tryChangePos((1,0))
		elif action == Action.LEFT: 
			self.tryChangePos((0,-1))
		elif action == Action.RIGHT: 
			self.tryChangePos((0,1))
		elif action == Action.DROP_BOMB:
			if not self.state.isBombDropped: 
				self.state.isBombDropped = True
				self.state.bomb = self.state.bombermanPos
		elif action == Action.EXPLODE:
			if self.state.isBombDropped:
				if self.state.bombermanPos in (self.neighbours(self.state.bomb)) or self.state.bombermanPos == self.state.bomb:
					self.state.die = True
				self.destroyStonesIfPossible()
				self.state.isBombDropped = False
				self.state.bomb = None
	
			
	def destroyStonesIfPossible(self):		
		for i in range(len(self.state.stones)):
			if self.state.stones[i] == True and STONES[i] in self.neighbours(self.bomb): 
				self.state.stones[i] = False	
		

	def neighbours(self, position):
		return [self.addPos(position,(-1,0)),
				self.addPos(position,(1,0)),
				self.addPos(position,(0,-1)),
				self.addPos(position,(0,1)),]
		
		
	def tryChangePos(self,mov):
		newPos = self.addPos(self.state.bombermanPos,mov)
		notInWall = newPos not in WALLS
		notInStone = not(newPos in STONES and self.state.stones[STONES.index(newPos)])
		onBoard = self.onBoard(newPos)
		if notInWall and notInStone and onBoard: self.state.bombermanPos = newPos
		

	def onBoard(self,newPos):
		row,col = newPos
		return (row>=0 and row<BOARD_WIDTH) and (col>=0 and col<BOARD_HEIGHT)
	

	def actionCount(self):
		return Action.COUNT;

		
	def addPos(self,pos1,pos2):
		row1,col1 = pos1
		row2,col2 = pos2
		return (row1+row2,col1+col2)