from Constants import *

CONFIGURATION_NAME = "RmaxNavigationRewards"
ITERATIONS = 10000
MAX_TURNS = 1000
AGENT = RMAX
TASK = DETERMINISTIC
IS_IMMORTAL = False
MAP_SIZE = 5
BOMB_EXPLODING_PROBABILITY = 0.9
BOMB_REWARD_POLICY = BOMB_NO_REWARD
NAVIGATION_REWARD = NAVIGATION_REWARD_PROPORTIONAL_TO_EXIT
WIN_REWARD = 10000.0
LOSE_REWARD = -10000.0
BOMB_REWARD = 10.0
NO_ACTION_NEGATIVE_REWARD = True
INITIAL_REWARD = -1
USE_DELTABOMB_FACTOR = True

