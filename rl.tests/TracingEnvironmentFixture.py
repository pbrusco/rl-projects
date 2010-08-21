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
		TestEnvironment.test_not_destroy_wall(self)
		self.assertTrace(RIGHT,BOMBDROP,RIGHT,RIGHT,BOMBEXPLODE,0,LEFT,LEFT,NOACTION)
		
	def test_die_on_bomb(self):
		TestEnvironment.test_die_on_bomb(self)
		self.assertTrace(BOMBDROP,BOMBEXPLODE,0,DEAD)
	
	def test_die_next_to_bomb(self):
		TestEnvironment.test_die_next_to_bomb(self)
		self.assertTrace(BOMBDROP,RIGHT,BOMBEXPLODE,0,DEAD)
	
	def test_cannot_move_dead(self):
		TestEnvironment.test_cannot_move_dead(self)
		
	def test_break_stone(self):
		TestEnvironment.test_break_stone(self)
		self.assertTrace(DOWN,BOMBDROP,UP,RIGHT,BOMBEXPLODE,0b1000,LEFT,DOWN,DOWN,DOWN)

	def test_break_two_stones(self):
		TestEnvironment.test_break_two_stones(self)
		self.assertTrace(DOWN,BOMBDROP,UP,RIGHT,BOMBEXPLODE,0b1000,LEFT,DOWN,DOWN,DOWN,
						 NOACTION,BOMBDROP,UP,UP,BOMBEXPLODE,0b1000,DOWN,DOWN,DOWN,DOWN,NOACTION)
