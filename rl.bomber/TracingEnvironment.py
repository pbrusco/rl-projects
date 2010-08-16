from Environment import Environment
from Movements import *
from Settings import *

OUTPUT = 'trace.out'

class TracingEnvironment(Environment):

	def __init__(self):
		Environment.__init__(self)
		self.tracelog = []
		
	def start(self):
		Environment.start(self)
		self.tracelog = []
		
	def clear(self):
		self.tracelog = []
		
	def dropBomb(self):
		r = Environment.dropBomb(self)
		self.trace(BOMBDROP)
		return r
	
	def explodeBomb(self):
		self.trace(BOMBEXPLODE)
		self.stonesDestroyed = 0
		self.bombPos = self.state.bomb
		
		# When exploding the bomb, the destroy stone method is invoked for every wall destroyed. The resulting number is stored in stonesDestroyed and logged.
		exploded = Environment.explodeBomb(self)
		self.trace(self.stonesDestroyed)
		self.stonesDestroyed = 0
		self.bombPos = None
		
		# Store if bomberman died
		if self.state.die: self.trace(DEAD)
		return exploded
	
	def destroyStone(self,index):
		r = Environment.destroyStone(self,index)
		stonei,stonej = STONES[index]
		bombi,bombj = self.bombPos
		diff = (bombi - stonei, bombj - stonej)
		self.stonesDestroyed += BOMBPOS[diff]
		return r
	
	def didntChangePos(self,mov):
		r = Environment.didntChangePos(self,mov)
		self.trace(NOACTION)
		return r
	
	def doChangePos(self,mov):
		r = Environment.doChangePos(self,mov)
		self.trace(MOVDIR[mov])
		return r
	
	def trace(self,num):
		self.tracelog.append(num)
		
	def dump(self,out=OUTPUT):
		output = "Output/" + CONFIGURATION_NAME + "-" + out
		with open(output,'a') as f:
			f.write(str(self.tracelog))
			f.write('\n')