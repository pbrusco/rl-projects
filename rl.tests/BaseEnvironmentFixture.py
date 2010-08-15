import unittest
import sys

sys.path.append('../rl.bomber')

from Action import *
from Settings import *
from Maps import *

class BaseTestEnvironment(unittest.TestCase):
	
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

	def assertAlive(self,status):
		self.assertEqual(self.env.state.die, not status)
		
	def assertPos(self,i,j):
		self.assertEqual(self.env.state.bombermanPos,(i,j))
		
	def assertStonesBroken(self,*stones):
		for index,stone in enumerate(STONES):
			if stone in stones: self.assertFalse(self.env.state.stones[index])
			else: self.assertTrue(self.env.state.stones[index])
