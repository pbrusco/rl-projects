from Status import *
from Settings import *
from Maps import *
from Reward import Reward
from Environment import Environment
from copy import copy, deepcopy

class Task(object):
	
	def __init__(self,env=Environment()):
		self.env = env
		
	def start(self):
		self.env.start()
	
	def perform(self,action):
		bombsExploded = self.env.performAction(action)
		
		reward = Reward()
		status = Status.CONTINUE
		state = self.env.state
		
		# Intermediate
		if (BOMB_REWARD_POLICY != BOMB_NO_REWARD):
			for i in range(len(bombsExploded)):
				reward.addRewardForFactor(Reward.STONE, self.getRewardForBombPosition(bombsExploded[i]))
				
		if (NAVIGATION_REWARD != NAVIGATION_NO_REWARD):
			if (self.env.positionChangedInLastAction == True):
				reward.addRewardForFactor(Reward.POSITION, self.getRewardForAgentPosition(state.bombermanPos))
			
		if (state.bombermanPos == EXIT):
			reward.addRewardForFactor(Reward.POSITION, WIN_REWARD)
			status = Status.WIN
		if (state.die):
			reward.addRewardForFactor(Reward.DEAD, LOSE_REWARD)
			status = Status.DIE

		return (self.processState(state), self.processReward(reward), status)
		
	def getState(self):
		return self.processState(self.env.state)
		
	def processState(self,state):
		return deepcopy(state)
		
	def processReward(self,reward):
		return reward
		
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
	
	def processState(self,state):
		return int(state)
	
	def processReward(self,reward):
		return float(reward)
