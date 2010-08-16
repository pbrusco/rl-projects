from Settings import *
from Maps import *
from Status import *
from Environment import Environment
from copy import copy, deepcopy

class Task(object):
	
	def __init__(self,env=Environment()):
		self.env = env
		
	def start(self):
		self.env.start()
	
	def perform(self,action):
		bombsExploded = self.env.performAction(action)
		
		reward = 0.0 #float
		status = Status.CONTINUE
		state = self.env.state
		
		# Intermediate
		if (BOMB_REWARD_POLICY != BOMB_NO_REWARD):
			for i in range(len(bombsExploded)):
				reward += self.getRewardForBombPosition(bombsExploded[i])
				
		if (NAVIGATION_REWARD != NAVIGATION_NO_REWARD):
			if (self.env.positionChangedInLastAction == True):
				reward += self.getRewardForAgentPosition(state.bombermanPos)
			
		if (state.bombermanPos == EXIT):
			reward = WIN_REWARD
			status = Status.WIN
		if (state.die):
			reward = LOSE_REWARD
			status = Status.DIE

		return (self.getState(), reward, status)
		
	def getState(self):
		return deepcopy(self.env.state)
		
	def getRewardForBombPosition(self, bombPosition):
		if (BOMB_REWARD_POLICY == BOMB_REWARD_PER_STONE_DESTROYED_PROPORTIONAL_TO_EXIT):
			closenessX = abs(MAP_SIZE-1 -(EXIT[0] - bombPosition[0])) 
			closenessY = abs(MAP_SIZE-1 -(EXIT[1] - bombPosition[1]))
			closeness = closenessX + closenessY
			return closeness * BOMB_REWARD
		if (BOMB_REWARD_POLICY == BOMB_REWARD_PER_STONE_DESTROYED):
			return BOMB_REWARD
		return 0
		
	def getRewardForAgentPosition(self, agentPosition):
		closenessX = abs(MAP_SIZE-1 -(EXIT[0] - agentPosition[0])) 
		closenessY = abs(MAP_SIZE-1 -(EXIT[1] - agentPosition[1]))
		closeness = closenessX + closenessY
		return closeness
		
class FlatStateTask(Task):
	def getState(self):
		return int(self.env.state)
