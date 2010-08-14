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
		
	def test_nav_walls(self):
		self.movechk(Action.RIGHT,0,1)
		self.movechk(Action.DOWN,0,1)
		self.movechk(Action.RIGHT,0,2)
		self.movechk(Action.DOWN,1,2)
		self.movechk(Action.LEFT,1,2)
		
	def test_nav_stone(self):
		self.movechk(Action.DOWN,1,0)
		self.movechk(Action.DOWN,1,0)
		self.movechk(Action.UP,0,0)
		self.movechk(Action.RIGHT,0,1)
		self.movechk(Action.RIGHT,0,2)
		self.movechk(Action.DOWN,1,2)
		self.movechk(Action.DOWN,1,2)
	
	def test_not_destroy_wall(self):
		self.movechk(Action.RIGHT,0,1)
		self.drop()
		self.movechk(Action.RIGHT,0,2)
		self.movechk(Action.RIGHT,0,3)
		self.explode()
		self.movechk(Action.LEFT,0,2)
		self.movechk(Action.LEFT,0,1)
		self.movechk(Action.DOWN,0,1)
		
	def test_die_on_bomb(self):
		self.drop()
		self.explode()
		self.assertStatus(Status.DIE)
	
	def drop(self):
		return self.env.performAction(Action.DROP_BOMB)
		
	def explode(self):
		return self.env.performAction(Action.EXPLODE)
	
	def move(self,dir):
		return self.env.performAction(dir)
		
	def movechk(self,dir,i,j):
		s = self.env.performAction(dir)
		self.assertPos(i,j)
		return s
		
	def setPos(self,i,j):
		self.env.state.bombermanPos = (i,j)

	def assertPos(self,i,j):
		self.assertEqual(self.env.state.bombermanPos,(i,j))
		