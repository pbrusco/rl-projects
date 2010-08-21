from Settings import *

import Maps

class Factor:

	POSITION = 0
	BOMB = 1
	STONES = 2
	DEAD = 3
	DELTABOMB = 4

	FACTORS = [POSITION,BOMB,STONES,DEAD,DELTABOMB] if USE_DELTABOMB_FACTOR else [POSITION,BOMB,STONES,DEAD] 
	
	MAX_FACTORS = {
		POSITION: Maps.BOARD_HEIGHT * Maps.BOARD_WIDTH - len(Maps.WALLS),
		BOMB: Maps.BOARD_HEIGHT * Maps.BOARD_WIDTH- len(Maps.WALLS),
		STONES: len(Maps.STONES),
		DEAD: 2,
		DELTABOMB: Maps.BOARD_HEIGHT * Maps.BOARD_WIDTH
	}
	
	@classmethod
	def getMaxValues(cls, factor):
		return Factor.MAX_FACTORS[factor]