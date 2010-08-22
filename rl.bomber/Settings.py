from Constants import *

CONFIGURATION_NAME = "StochasticExploRmax"
ITERATIONS = 300
MAX_TURNS = 1000
#QLEARNING SARSA SARSALAMBDA DYNA
AGENT = RMAX
# STOCHASTIC_NAVIGATION  STOCHASTIC_EXPLOSION  
TASK = STOCHASTIC_EXPLOSION
IS_IMMORTAL = False
MAP_SIZE = 3
BOMB_EXPLODING_PROBABILITY = 0.9
BOMB_REWARD_POLICY = BOMB_NO_REWARD
NAVIGATION_REWARD = NAVIGATION_NO_REWARD
WIN_REWARD = 10000.0
LOSE_REWARD = -10000.0
BOMB_REWARD = 10.0
NO_ACTION_NEGATIVE_REWARD = True
INITIAL_REWARD = -1
USE_DELTABOMB_FACTOR = True