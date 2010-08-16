import unittest
import sys

sys.path.append('../rl.bomber')

from Environment import Environment
from Task import Task

from Action import *
from Settings import *
from Maps import *

class TestRewards(unittest.TestCase):
	
	def setUp(self):
		self.env = Environment()
		self.task = Task(self.env)
	
	def test_settings(self):
		self.assertEquals(MAP_SIZE, 8)
		self.assertEquals(IS_IMMORTAL, False)
	
	def test_simple_nav(self):
		if (NAVIGATION_REWARD == NAVIGATION_REWARD_PROPORTIONAL_TO_EXIT and BOMB_REWARD_POLICY == BOMB_NO_REWARD):
			self.perform(Action.RIGHT, 1)
			self.perform(Action.RIGHT, 2)
			self.perform(Action.LEFT, 1)
			self.perform(Action.LEFT, 0)
		
			self.perform(Action.RIGHT, 1)
			self.perform(Action.DOWN, 0) #wall position didn't change
		
			self.perform(Action.RIGHT, 2)
			self.perform(Action.DOWN, 3)		
			self.perform(Action.DOWN, 0) #wall position didn't change
			self.perform(Action.RIGHT, 0) #wall position didn't change
			
		
	def test_bombs_reward(self):
		if (NAVIGATION_REWARD == NAVIGATION_NO_REWARD and BOMB_REWARD_POLICY == BOMB_REWARD_PER_STONE_DESTROYED):
			self.perform(Action.RIGHT, 0)
			self.perform(Action.RIGHT, 0)
			self.perform(Action.DOWN, 0)
			
			self.perform(Action.DROP_BOMB, 0)
			self.perform(Action.UP, 0)
			self.perform(Action.LEFT, 0)
			self.perform(Action.EXPLODE, 10) 
			
			self.perform(Action.RIGHT, 0)
			self.perform(Action.DOWN, 0)
			self.perform(Action.DOWN, 0)
			self.perform(Action.DOWN, 0)
			self.perform(Action.DROP_BOMB, 0)
			self.perform(Action.EXPLODE, LOSE_REWARD) #agent die whitout reward for exploding bomb
			
	def test_bombs_reward(self):
		if (NAVIGATION_REWARD == NAVIGATION_NO_REWARD and BOMB_REWARD_POLICY == BOMB_REWARD_PER_STONE_DESTROYED_PROPORTIONAL_TO_EXIT):	
			self.perform(Action.RIGHT, 0)
			self.perform(Action.RIGHT, 0)
			self.perform(Action.DOWN, 0)
			
			self.perform(Action.DROP_BOMB, 0)
			self.perform(Action.UP, 0)
			self.perform(Action.LEFT, 0)
			self.perform(Action.EXPLODE, 10 * 4) 
			
			self.perform(Action.RIGHT, 0)
			self.perform(Action.DOWN, 0)
			self.perform(Action.DOWN, 0)
			self.perform(Action.DOWN, 0)
			self.perform(Action.DROP_BOMB, 0)
			self.perform(Action.UP, 0)
			self.perform(Action.UP, 0)
			self.perform(Action.EXPLODE, 10 * 6) 
			self.perform(Action.DOWN, 0)
			self.perform(Action.DOWN, 0)
			self.perform(Action.DOWN, 0)
			self.perform(Action.DOWN, 0)
			self.perform(Action.DROP_BOMB, 0)
			self.perform(Action.UP, 0)
			self.perform(Action.UP, 0)
			self.perform(Action.EXPLODE, 10 * 8)
			self.perform(Action.DOWN, 0)
			self.perform(Action.DOWN, 0)
			self.perform(Action.DOWN, 0)
			self.perform(Action.DOWN, 0)
			self.perform(Action.RIGHT, 0)
			self.perform(Action.RIGHT, 0)
			self.perform(Action.RIGHT, 0)
			self.perform(Action.RIGHT, 0)
			self.perform(Action.RIGHT, WIN_REWARD)
			
			
			
				
			

		
	def perform(self, action, expectedReward):
		state, reward, status = self.task.perform(action)
		self.assertEquals(reward, expectedReward)
		
	