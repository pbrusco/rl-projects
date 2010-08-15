
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
			

MOVEMENTS = [3, 6, 2, 1, 4, 6, 0, 3, 3, 3, 3, 2, 6, 2, 1, 6, 6, 5, 8, 0, 6, 1, 6, 6, 6, 6, 6, 4, 0, 5, 8, 7]


#0000 = 0 indica no se rompio ninguna
#0001 = 1 se rompio solo derecha
#0010 = 2 se rompio solo izq
#0100 = 3 se rompio solo arriba
#...
#1101 = 13 se rompio abajo, arriba y derecha

#entonces N va a estar entre 0 y 15




