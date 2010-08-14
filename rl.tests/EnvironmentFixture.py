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
		self.assertPos(0,1)
		self.move(Action.RIGHT)
		self.assertPos(0,2)
		self.move(Action.DOWN)
		self.assertPos(1,2)
		self.move(Action.UP)
		self.assertPos(0,2)
		self.move(Action.LEFT)
		self.assertPos(0,1)
	
	def test_nav_top_edge(self):
		self.move(Action.LEFT)
		self.assertPos(0,0)
		self.move(Action.UP)
		self.assertPos(0,0)
		self.move(Action.RIGHT)
		self.assertPos(0,1)
		self.move(Action.UP)
		self.assertPos(0,1)
		for i in range(10): self.move(Action.RIGHT)
		self.assertPos(0,7)
		self.move(Action.UP)
		self.assertPos(0,7)
		
	def test_nav_bottom_edge(self):
		self.setPos(7,0)
		self.move(Action.LEFT)
		self.assertPos(7,0)
		self.move(Action.DOWN)
		self.assertPos(7,0)
		self.move(Action.RIGHT)
		self.assertPos(7,1)
		self.move(Action.DOWN)
		self.assertPos(7,1)
		for i in range(10): self.move(Action.RIGHT)
		self.assertPos(7,7)
		self.move(Action.DOWN)
		self.assertPos(7,7)
	
	def move(self,dir):
		return self.env.performAction(dir)
		
	def setPos(self,i,j):
		return self.env.state.bombermanPos = (i,j)

	def assertPos(self,i,j):
		self.assertEqual(self.env.state.bombermanPos,(i,j))