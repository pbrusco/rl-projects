import unittest
import sys

sys.path.append('../rl.bomber')

from Environment import Environment
from TracingEnvironment import TracingEnvironment
from BaseEnvironmentFixture import BaseTestEnvironment
from EnvironmentFixture import TestEnvironment

from Action import *
from Settings import *
from Maps import *
from Movements import *

class TestTracingEnvironment(TestEnvironment):
	
	def setUp(self):
		self.env = TracingEnvironment()
	
	def assertTrace(self, *trace):
		self.assertEquals(self.env.tracelog, list(trace))
	
	def test_simple_nav(self):
		TestEnvironment.test_simple_nav(self)
		self.assertTrace(RIGHT,RIGHT,DOWN,UP,LEFT)
	
	def test_nav_top_edge(self):
		TestEnvironment.test_nav_top_edge(self)
		self.assertTrace(NOACTION,NOACTION,RIGHT,NOACTION,RIGHT,RIGHT,RIGHT,RIGHT,RIGHT,RIGHT,NOACTION,NOACTION,NOACTION,NOACTION,NOACTION)
		
	def test_nav_bottom_edge(self):
		TestEnvironment.test_nav_bottom_edge(self)
		self.assertTrace(NOACTION,NOACTION,RIGHT,NOACTION,RIGHT,RIGHT,RIGHT,RIGHT,RIGHT,RIGHT,NOACTION,NOACTION,NOACTION,NOACTION,NOACTION)
		
	def test_nav_walls(self):
		TestEnvironment.test_nav_walls(self)
		self.assertTrace(RIGHT,NOACTION,RIGHT,DOWN,NOACTION)
		
	def test_nav_stone(self):
		TestEnvironment.test_nav_stone(self)
		self.assertTrace(DOWN,NOACTION,UP,RIGHT,RIGHT,DOWN,NOACTION)
	
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
	
	