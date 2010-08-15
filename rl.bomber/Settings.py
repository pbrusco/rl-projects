from Constants import *

# ---------------------------------------
# Manager Settings and Run Configurations
# ---------------------------------------

# amount of games the agent will play
ITERATIONS = 100
# if more than MAX_TURNS are used the bomberman dies
MAX_TURNS = 1000

AGENT = QLEARNING

TASK = DETERMINISTIC

# ------------------
# Bomberman Settings
# ------------------

# an immortal bomberman does not die due to bomb explosions
IS_IMMORTAL = False

# size of the map, look in Maps.py file for details
MAP_SIZE = 5

# -------------------
# Stochastic Settings
# -------------------

# bomb exploding probability for StochasticExplosionTask
BOMB_EXPLODING_PROBABILITY = 0.9

# -----------
# RL Settings
# -----------

# bomb rewards policy (options in Constants.py)
BOMB_REWARD_POLICY = BOMB_NO_REWARD

# navigation rewards policy (options in Constants.py)
NAVIGATION_REWARD = NAVIGATION_NO_REWARD

# win/lose rewards
WIN_REWARD = 10000.0
LOSE_REWARD = -10000.0
BOMB_REWARD = 10.0