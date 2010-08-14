# Bomberman Settings

MAP_SIZE = 3

if MAP_SIZE == 3:
	BOARD_HEIGHT = 3
	BOARD_WIDTH = 3
	EXIT = (2,2)
	STONES = [(1,2),(2,1)]
	WALLS = [(1,1)]

elif MAP_SIZE == 5:
	BOARD_HEIGHT = 5
	BOARD_WIDTH = 5
	EXIT = (4,4)
	STONES = [(2,0),(2,2),(2,4),(4,0),(4,2)]
	WALLS = [(1,1),(1,3),(3,1),(3,3)]
	
elif MAP_SIZE == 8:
	BOARD_HEIGHT = 8
	BOARD_WIDTH = 8
	EXIT = (7,7)
	STONES = [(2,0),(2,2),(2,4),(2,6),(4,0),(4,2),(4,4),(4,6),(6,0),(6,2),(6,4),(6,6)]
	WALLS = [(1,1),(1,3),(1,5),(1,7),(3,1),(3,3),(3,5),(3,7),(5,1),(5,3),(5,5),(5,7)]

# RL Settings

WIN_REWARD = 10000.0 #float!
LOSE_REWARD = -1000.0 #float!

# Manager Settings

ITERATIONS = 100
MAX_TURNS = 1000
