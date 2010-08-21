from Constants import *
from Settings import *
from Maps import *

class Reward:

	DEAD = 0
	POSITION = 1
	STONE = 2
	NOACTION = 3
	
	REWARDS = [DEAD, POSITION, STONE, NOACTION]
	
	def __init__(self, kind=None,value=0.0):
		self.kinds = {kind: value} if not kind is None else {}
		
	def __float__(self):
		return float(sum(self.kinds.values()))
	
	def __str__(self):
		return "Reward: " + str(self.kinds)
	
	def getRewardForFactor(self, factor):
		return self.kinds.get(factor) or 0.0
	
	@classmethod
	def getRewardForBombPosition(cls,bombPosition):
		if (BOMB_REWARD_POLICY == BOMB_REWARD_PER_STONE_DESTROYED_PROPORTIONAL_TO_EXIT):
			closenessX = abs(MAP_SIZE-1 -(EXIT[0] - bombPosition[0])) 
			closenessY = abs(MAP_SIZE-1 -(EXIT[1] - bombPosition[1]))
			closeness = closenessX + closenessY
			return closeness * BOMB_REWARD
		if (BOMB_REWARD_POLICY == BOMB_REWARD_PER_STONE_DESTROYED):
			return BOMB_REWARD
		return 0
	
	@classmethod
	def getRewardForAgentPosition(cls,agentPosition):
		closenessX = abs(MAP_SIZE-1 -(EXIT[0] - agentPosition[0])) 
		closenessY = abs(MAP_SIZE-1 -(EXIT[1] - agentPosition[1]))
		closeness = closenessX + closenessY
		return closeness
	
	
class MaxReward:
	
	MAX_REWARDS = {
				Reward.DEAD: 0.0, 
				Reward.POSITION: WIN_REWARD, 
				Reward.STONE: max([Reward.getRewardForBombPosition(stone) for stone in STONES]),
				Reward.NOACTION: 0.0
				}

	@classmethod
	def forFactor(cls, factor):
		return MaxReward.MAX_REWARDS[factor]
