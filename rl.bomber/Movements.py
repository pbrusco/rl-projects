
UP = 0
DOWN = 1
LEFT = 2
RIGHT = 3
BOMBDROP = 4
BOMBEXPLODE = 5
NOACTION = 6
DEAD = 7

BOMBPOS = {	(0,-1): 0b0001,
			(0,1): 0b0010,
			(-1,0): 0b1000,
			(1,0): 0b0100,
			}
			
MOVDIR = {	(0,-1): LEFT,
			(0,1): RIGHT,
			(-1,0): UP,
			(1,0): DOWN,
			}
			

MOVEMENTS = [DOWN,DOWN,DOWN,DOWN,DOWN,DOWN,DOWN,RIGHT,RIGHT,RIGHT,RIGHT,RIGHT,RIGHT,RIGHT]


#used code after bomb explosion:
#0000 = 0 no stones destroyed.
#0001 = 1 right stone from bomb position destroyed
#0010 = 2 left stone from bomb position destroyed
#0100 = 3 up stone from bomb position destroyed
#...
#1101 = 13 down, up and right stones destroyed.

#then the code is in range [0,15]




