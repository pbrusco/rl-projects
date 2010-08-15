# ------------------
# Bomberman Settings
# ------------------

# an immortal bomberman does not die due to bomb explosions
IS_IMMORTAL = False

# -------------------
# Stochastic Settings
# -------------------

BOMB_EXPLODING_PROBABILITY = 0.9

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
ITERATIONS = 1000
MAX_TURNS = 1000
