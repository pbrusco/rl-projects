from Factor import Factor
from Action import Action

class DBN(object):
	
	def __init__(self, dependencies):
		self.dependencies = dependencies
	
	def getParents(self, action, factor):
		return self.dependencies[action][factor]
		
class BombermanDBN(DBN):
	
	def __init__(self):
		
		nav_dep = {
			Factor.POSITION:	[Factor.POSITION, Factor.STONES],
			Factor.BOMB:		[Factor.BOMB],
			Factor.STONES: 		[Factor.STONES],
			Factor.DEAD: 		[Factor.DEAD],
		}
		
		drop_dep = {
			Factor.POSITION:	[Factor.POSITION],
			Factor.BOMB:		[Factor.BOMB],
			Factor.STONES: 		[Factor.STONES],
			Factor.DEAD: 		[Factor.DEAD],
		}
		
		explode_dep = {
			Factor.POSITION:	[Factor.POSITION],
			Factor.BOMB:		[Factor.BOMB],
			Factor.STONES: 		[Factor.STONES,Factor.BOMB],
			Factor.DEAD: 		[Factor.POSITION,Factor.BOMB,Factor.DEAD],
		}
		
		DBN.__init__(self, {
			Action.UP: nav_dep,
			Action.LEFT: nav_dep,
			Action.RIGHT: nav_dep,
			Action.DOWN: nav_dep,
			Action.DROP_BOMB: drop_dep,
			Action.EXPLODE: explode_dep
		})