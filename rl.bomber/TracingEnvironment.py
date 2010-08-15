OUTPUT = 'trace.out'

from Environment import Environment
from Movements import *

class TracingEnvironment(Environment):

	def __init__(self):
		Environment.__init__(self)
		self.tracelog = []
		
	def dropBomb(self):
		Environment.dropBomb(self)
		self.trace(BOMBDROP)
	
	def explodeBomb(self):
		self.trace(BOMBEXPLODE)
		Environment.explodeBomb(self)
	
	def destroyStone(self,index):
		Environment.destroyStone(self,index)
	
	def trace(self,num):
		self.tracelog.append(num)