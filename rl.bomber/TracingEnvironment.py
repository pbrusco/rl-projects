OUTPUT = 'trace.out'

from Environment import Environment
from Movements import *
from Settings import *


class TracingEnvironment(Environment):

	def __init__(self):
		Environment.__init__(self)
		self.tracelog = []
		
	def start(self):
		Environment.reset(self)
		self.tracelog = []
		
	def clear(self):
		self.tracelog = []
		
	def dropBomb(self):
		Environment.dropBomb(self)
		self.trace(BOMBDROP)
	
	def explodeBomb(self):
		self.trace(BOMBEXPLODE)
		self.stonesDestroyed = 0
		self.bombPos = self.state.bomb
		
		# When exploding the bomb, the destroy stone method is invoked for every wall destroyed. The resulting number is stored in stonesDestroyed and logged.
		Environment.explodeBomb(self)
		self.trace(self.stonesDestroyed)
		self.stonesDestroyed = 0
		self.bombPos = None
		
		# Store if bomberman died
		if self.state.die: self.trace(DEAD)
	
	def destroyStone(self,index):
		Environment.destroyStone(self,index)
		stonei,stonej = STONES[index]
		bombi,bombj = self.bombpos
		diff = (bombi - stonei, bombj - stonej)
		self.stonesDestroyed += BOMBPOS[diff]
	
	def didntChangePos(self,mov):
		Environment.didntChangePos(self,mov)
		self.trace(NOACTION)
	
	def doChangePos(self,mov):
		Environment.doChangePos(self,mov)
		self.trace(MOVDIR[mov])
	
	def trace(self,num):
		self.tracelog.append(num)
		
	def dump(self,out=OUTPUT):
		with open(out,'wa') as f:
			f.write(str(self.tracelog))
			f.write('\n')