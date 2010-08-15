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
		self.perform(Action.RIGHT, 1)
		self.perform(Action.RIGHT, 2)
		self.perform(Action.LEFT, 1)
		self.perform(Action.LEFT, 0)
		
		self.perform(Action.RIGHT, 1)
		self.perform(Action.DOWN, 0)
		
		
		
		
		
		
		
	def perform(self, action, expectedReward):
		state, reward, status = self.task.perform(action)
		self.assertEquals(reward, expectedReward)
		
	