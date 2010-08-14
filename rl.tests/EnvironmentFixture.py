import unittest
import sys

sys.path.append('../rl.bomber')
from Environment import Environment
from Action import *

class TestEnvironment(unittest.TestCase):
	
	def setUp(self):
		self.env = Environment()
	
	def test_simple_nav(self):
		self.move(Action.RIGHT)
		self.assertPos(1,0)
		self.move(Action.RIGHT)
		self.assertPos(2,0)
		self.move(Action.DOWN)
		self.assertPos(2,1)
		self.move(Action.UP)
		self.assertPos(2,0)
		self.move(Action.LEFT)
		self.assertPos(1,0)
		
	def move(self,dir):
		return self.env.performAction(dir)

	def assertPos(self,x,y):
		self.assertEqual(self.env.state.bombermanPos,(x,y))