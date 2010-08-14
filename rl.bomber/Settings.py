# ------------------
# Bomberman Settings
# ------------------

# an immortal bomberman does not die due to bomb explotions
IS_IMMORTAL = False

# ------------
# Map Settings
# ------------

MAP_SIZE = 8

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

# -----------
# RL Settings
# -----------

# Bomb Rewards Policy
BOMB_NO_REWARD = 0
BOMB_REWARD_PER_STONE_DESTROYED = 1
BOMB_REWARD_PER_STONE_DESTROYED_PROPORTIONAL_TO_EXIT = 2

BOMB_REWARD_POLICY = BOMB_NO_REWARD

# Navigation Rewards Policy
NAVIGATION_NO_REWARD = 0
NAVIGATION_REWARD_PROPORTIONAL_TO_EXIT = 1

NAVIGATION_REWARD = NAVIGATION_NO_REWARD

# Win/Lose Rewards Relation
WIN_REWARD = 10000.0
LOSE_REWARD = -10000.0
BOMB_REWARD = 10.0

# ----------------
# Manager Settings
# ----------------
ITERATIONS = 100
MAX_TURNS = 1000
