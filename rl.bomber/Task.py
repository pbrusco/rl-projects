from Settings import *
from Status import *
from Environment import Environment

class Task:
	
	def __init__(self,env=Environment()):
		self.env = env
		
	def start(self):
		self.env.start()
	
	def perform(self,action):
		bombsExploded = self.env.performAction(action)
		
		reward = 0.0 #float
		status = Status.CONTINUE
		state = self.env.state
		
		# TODO: Clone state before returning it
		
		for i in range(len(bombsExploded)):
			reward += self.getRewardForPosition(state.bombExplodedPosition)
		
		if (state.bombermanPos == EXIT):
			reward = WIN_REWARD
			status = Status.WIN
		if (state.die):
			reward = LOSE_REWARD
			status = Status.DIE

		return (state, reward, status)
		
	def getState(self):
		return self.env.state
		
	def getRewardForPosition(self, bombPosition):
		if (BOMB_REWARD_POLICY == BOMB_REWARD_PER_STONE_DESTROYED_PROPORTIONAL_TO_EXIT):
			closenessX = abs(MAP_SIZE -(EXIT[0] - bombPosition[0])) 
			closenessY = abs(MAP_SIZE -(EXIT[1] - bombPosition[1]))
			closeness = deltaX + deltaY
			return closeness * BOMB_REWARD
		if (BOMB_REWARD_POLICY == BOMB_REWARD_PER_STONE_DESTROYED):
			return BOMB_REWARD