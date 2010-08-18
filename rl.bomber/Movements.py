
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
			

MOVEMENTS =[1, 4, 0, 3, 5, 8, 3, 1, 4, 0, 3, 5, 8, 3, 1, 4, 0, 2, 5, 8, 3, 1, 1, 1, 4, 0, 2, 5, 8, 6, 2, 1, 4, 0, 2, 5, 8, 2, 1, 4, 0, 3, 5, 8, 2, 1, 1, 1, 0, 1, 4, 6, 0, 3, 5, 8, 3, 1, 4, 0, 3, 5, 8, 3, 1, 4, 0, 3, 5, 8, 4, 2, 0, 5, 1, 1, 4, 3, 6, 2, 2, 6, 6, 3, 2, 2, 2, 6, 5, 0, 6, 6, 2, 3, 6, 6, 3, 3, 3, 0, 0, 3, 4, 2, 1, 1, 5, 1, 3, 3, 1, 4, 0, 0, 5, 8, 1, 1, 1, 1, 3]
#0000 = 0 indica no se rompio ninguna
#0001 = 1 se rompio solo derecha
#0010 = 2 se rompio solo izq
#0100 = 3 se rompio solo arriba
#...
#1101 = 13 se rompio abajo, arriba y derecha

#entonces N va a estar entre 0 y 15




