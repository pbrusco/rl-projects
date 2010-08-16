class Reward:

	DEAD = 0
	POSITION = 1
	STONE = 2
	
	REWARDS = [DEAD, POSITION, STONE]
	
	def __init__(self, kinds={}):
		self.kinds = kinds
		
	def __float__(self):
		return sum(self.kinds.values)
		
	def getRewardForFactor(self, factor):
		return self.kinds.get(factor) or 0.0
		
	def addRewardForFactor(self, factor, value):
		self.kinds[factor] = self.getRewardForFactor(factor) + value
