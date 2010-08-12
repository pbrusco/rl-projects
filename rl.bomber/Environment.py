from Action import *

class Environment:
	
	# for the moment and for simplicity we fix some values
	BOARD_HEIGHT = 8;
	BOARD_WIDTH = 8;	
	EXIT = (7,7)

	def __init__(self):

		self.bomberman = (0,0)
		self.bomb = (-1,-1)
		self.isBombDropped = False
		self.walls = []
		self.stones = []
	
	# initialize bomberman game
	def startNewGame(self):
		
		self.bomberman = (0,0)
		self.bomb = (-1,-1)
		self.isBombDropped = False
		self.walls = [(1,2),(1,3),(1,5),(1,7),(3,2),(3,3),(3,5),(3,7),(5,2),(5,3),(5,5),(5,7)]
		self.stones = [(2,0),(2,2),(2,4),(2,6),(4,0),(4,2),(4,4),(4,6),(6,0),(6,2),(6,4),(6,6)]
	
	def performAction(self, action):
		
		# perform action
		
		# convert state to state code
		stateCode = self.calculateStateCode()
		
		# return state code and reward
		return (stateCode, 0)

	def calculateStateCode(self):

			# calculate state code out of class members
			print "calculating..."
			
			return 0
			
	def stateCount(self):
		return 0
	
	def actionCount(self):
		return Action.COUNT;