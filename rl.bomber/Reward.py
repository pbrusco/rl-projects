class Reward:

	DEAD = 0
	POSITION = 1
	STONE = 2
	
	REWARDS = [DEAD, POSITION, STONE]
	
	def __init__(self, kinds=None):
		self.kinds = kinds or {}
		
	def __float__(self):
		return float(sum(self.kinds.values()))
	
	def __str__(self):
		return "Reward: " + str(self.kinds)
	
	def getRewardForFactor(self, factor):
		return self.kinds.get(factor) or 0.0
		
	def addRewardForFactor(self, factor, value):
		self.kinds[factor] = self.getRewardForFactor(factor) + value
		
	def maxRewardForFactor(self, factor):
		# TODO: Which is max reward for each factor?
		return 0.0
