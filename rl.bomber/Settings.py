from Constants import *

# ---------------------------------------
# Manager Settings and Run Configurations
# ---------------------------------------

# prefix for output files
CONFIGURATION_NAME = "default"

# amount of games the agent will play
ITERATIONS = 100
# if more than MAX_TURNS are used the bomberman dies
MAX_TURNS = 1000

AGENT = FACTOREDRMAX

TASK = DETERMINISTIC

# ------------------
# Bomberman Settings
# ------------------

# an immortal bomberman does not die due to bomb explosions
IS_IMMORTAL = False

# size of the map, look in Maps.py file for details
MAP_SIZE = 3

# -------------------
# Stochastic Settings
# -------------------

# bomb exploding probability for StochasticExplosionTask
BOMB_EXPLODING_PROBABILITY = 0.9

# ------------------
# Factoring Settings
# ------------------

# whether to use delta bomb as a redundant factor 
USE_DELTABOMB_FACTOR = True

# -----------
# RL Settings
# -----------

# bomb rewards policy (options in Constants.py)
BOMB_REWARD_POLICY = BOMB_REWARD_PER_STONE_DESTROYED_PROPORTIONAL_TO_EXIT

# navigation rewards policy (options in Constants.py)
NAVIGATION_REWARD = NAVIGATION_REWARD_PROPORTIONAL_TO_EXIT

# win/lose rewards
WIN_REWARD = 10000.0
LOSE_REWARD = -10000.0
BOMB_REWARD = 10.0