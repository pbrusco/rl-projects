import unittest
import sys

sys.path.append('../rl.bomber')

from Action import *
from Settings import *
from Maps import *
from State import State
from Factor import Factor

MAP_SIZE = 3
BOARD_HEIGHT = 3
BOARD_WIDTH = 3
EXIT = (2,2)
STONES = [(1,2),(2,1)]
WALLS = [(1,1)]

class TestStateHash(unittest.TestCase):
    
    def setUp(self):
        pass
        
    def test_hash_unique(self):
        states = {}
        for state in self.generate_states():
            stateid = int(state)
            self.assertEquals(states.get(stateid), None, "State " + str(state) + " has same id " + str(stateid) + " as state " + str(states.get(stateid)))
            states[stateid] = state
    
    def test_hash_factors_unique(self):
        factors = {}
        
        for factor in Factor.FACTORS:
            factors[factor] = set([]) 
                
        for state in self.generate_states():
            for factor in Factor.FACTORS:
                factorid = state.getFactorIntValue(factor)
                factors[factor].add(factorid)
                
                for otherfactor in Factor.FACTORS:
                    if factor != otherfactor:
                        self.assertTrue(factorid not in factors[otherfactor])
        
    def generate_states(self):
        positions = [(0,0),(0,1),(0,2),(1,0),(1,1),(1,2),(2,0),(2,1),(2,2)]
        for stones in [(0,0),(0,1),(1,0),(1,1)]:
            for man in positions:
                for bomb in positions + [(3,3)]:
                    state = State()
                    state.bomb = bomb
                    state.bombermanPos = man
                    state.stones = stones
                    state.isBombDropped = (bomb != (3,3))
                    state.die = False
                    yield state
        deadstate = State()
        deadstate.die = True
        yield deadstate