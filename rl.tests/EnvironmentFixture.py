import unittest
import sys

sys.path.append('../rl.bomber')

from Environment import Environment
from BaseEnvironmentFixture import BaseTestEnvironment

from Action import *
from Settings import *
from Maps import *

class TestEnvironment(BaseTestEnvironment):
	
	def setUp(self):
		self.env = Environment()
	
	def test_settings(self):
		self.assertEquals(MAP_SIZE, 8)
		self.assertEquals(IS_IMMORTAL, False)
	
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
		self.assertAlive(False)
	
	def test_die_next_to_bomb(self):
		self.drop()
		self.movechk(Action.RIGHT,0,1)
		self.explode()
		self.assertAlive(False)
	
	def test_cannot_move_dead(self):
		self.drop()
		self.explode()
		self.assertAlive(False)		
		self.assertRaises(Exception, self.movechk, Action.RIGHT, 0, 1)
		
	def test_break_stone(self):
		self.movechk(Action.DOWN, 1, 0)
		self.drop()
		self.movechk(Action.UP, 0, 0)
		self.movechk(Action.RIGHT, 0, 1)
		self.explode()
		self.assertAlive(True)		
		self.assertStonesBroken((2,0))
		self.movechk(Action.LEFT, 0, 0)
		self.movechk(Action.DOWN, 1, 0)
		self.movechk(Action.DOWN, 2, 0)
		self.movechk(Action.DOWN, 3, 0)
	
	def test_break_two_stones(self):
		self.test_break_stone()
		self.movechk(Action.DOWN, 3, 0)
		self.drop()
		self.movechk(Action.UP, 2, 0)
		self.movechk(Action.UP, 1, 0)
		self.explode()
		self.assertAlive(True)		
		self.assertStonesBroken((2,0),(4,0))
		self.movechk(Action.DOWN, 2, 0)
		self.movechk(Action.DOWN, 3, 0)
		self.movechk(Action.DOWN, 4, 0)
		self.movechk(Action.DOWN, 5, 0)
		self.movechk(Action.DOWN, 5, 0)
	