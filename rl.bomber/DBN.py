from Factor import Factor
from Action import Action
from Reward import Reward

from Settings import USE_DELTABOMB_FACTOR

class DBN(object):
	
	def __init__(self, dependencies):
		self.dependencies = dependencies
	
	def getParents(self, action, factor):
		return self.dependencies[action][factor]
		
class BombermanDBN(DBN):
	
	def __init__(self):
		
		nav_dep = {
			Factor.POSITION:	(Factor.POSITION, Factor.STONES),
			Factor.BOMB:		(Factor.BOMB,),
			Factor.STONES: 		(Factor.STONES,),
			Factor.DEAD: 		(Factor.DEAD,),
		} if not USE_DELTABOMB_FACTOR else {
			Factor.POSITION:	(Factor.POSITION, Factor.STONES),
			Factor.BOMB:		(Factor.BOMB,),
			Factor.STONES: 		(Factor.STONES,),
			Factor.DEAD: 		(Factor.DEAD,),
			Factor.DELTABOMB:	(Factor.POSITION, Factor.DELTABOMB, Factor.STONES)
		}
		
		drop_dep = {
			Factor.POSITION:	(Factor.POSITION,),
			Factor.BOMB:		(Factor.POSITION,Factor.BOMB),
			Factor.STONES: 		(Factor.STONES,),
			Factor.DEAD: 		(Factor.DEAD,),
		} if not USE_DELTABOMB_FACTOR else {
			Factor.POSITION:	(Factor.POSITION,),
			Factor.BOMB:		(Factor.POSITION,Factor.BOMB),
			Factor.STONES: 		(Factor.STONES,),
			Factor.DEAD: 		(Factor.DEAD,),
			Factor.DELTABOMB: 	(Factor.DELTABOMB,),
		}
		
		explode_dep = {
			Factor.POSITION:	(Factor.POSITION,),
			Factor.BOMB:		(Factor.BOMB,),
			Factor.STONES: 		(Factor.STONES,Factor.BOMB),
			Factor.DEAD: 		(Factor.POSITION,Factor.BOMB,Factor.DEAD),
		} if not USE_DELTABOMB_FACTOR else {
			Factor.POSITION:	(Factor.POSITION,),
			Factor.BOMB:		(Factor.BOMB,),
			Factor.STONES: 		(Factor.STONES,Factor.BOMB),
			Factor.DEAD: 		(Factor.DEAD,Factor.DELTABOMB),
			Factor.DELTABOMB:	(Factor.DELTABOMB,)
		}
		
		DBN.__init__(self, {
			Action.UP: nav_dep,
			Action.LEFT: nav_dep,
			Action.RIGHT: nav_dep,
			Action.DOWN: nav_dep,
			Action.DROP_BOMB: drop_dep,
			Action.EXPLODE: explode_dep
		})
		
class RewardsDBN(object):
	
	def __init__(self):
		pass
	
	def getParents(self, rewardfactor):
		if rewardfactor == Reward.DEAD:
			return (Factor.DEAD,Factor.DELTABOMB) if USE_DELTABOMB_FACTOR else (Factor.POSITION, Factor.BOMB, Factor.DEAD)
		elif rewardfactor == Reward.POSITION:
			return (Factor.POSITION,)
		elif rewardfactor == Reward.STONE:
			return (Factor.BOMB, Factor.STONES)
		elif rewardfactor == Reward.NOACTION:
			return (Factor.POSITION, Factor.STONES)
		else:
			raise Exception("Unknown reward factor: " + str(rewardfactor))