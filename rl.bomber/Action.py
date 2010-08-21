class Action:

	COUNT = 6

	UP = 0
	DOWN = 1
	LEFT = 2
	RIGHT = 3
	DROP_BOMB = 4
	EXPLODE = 5
	
	ACTIONS = [UP, DOWN, LEFT, RIGHT, DROP_BOMB, EXPLODE]
	
	@classmethod
	def isNavigationAction(slf,action):
		return action < 4