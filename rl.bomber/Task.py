from Status import *
from Settings import *
from Maps import *
from Reward import Reward
from Environment import Environment
from copy import copy, deepcopy

class Task(object):
	
	def __init__(self,env=None):
		self.env = env or Environment()
		
	def start(self):
		self.env.start()
	
	def perform(self,action):
		bombsExploded = self.env.performAction(action)
		
		reward = INITIAL_REWARD
		status = Status.CONTINUE
		state = self.env.state
		
		# Intermediate
		if (BOMB_REWARD_POLICY != BOMB_NO_REWARD):
			value = sum([Reward.getRewardForBombPosition(b) for b in bombsExploded])
			reward = Reward(Reward.STONE, value)
				
		if (NAVIGATION_REWARD != NAVIGATION_NO_REWARD):
			if (self.env.positionChangedInLastAction == True):
				reward = Reward(Reward.POSITION, Reward.getRewardForAgentPosition(state.bombermanPos))
			else:
				if (NO_ACTION_NEGATIVE_REWARD):
					reward = -10  
			
		if (state.bombermanPos == EXIT):
			reward = Reward(Reward.POSITION, WIN_REWARD)
			status = Status.WIN
		if (state.die):
			reward = Reward(Reward.DEAD, LOSE_REWARD)
			status = Status.DIE

		return (state, reward or Reward(), status)
		
	def getState(self):
		return self.env.state
		
	