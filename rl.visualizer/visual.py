BOARD_HEIGHT = 8
BOARD_WIDTH = 8
EXIT = (7,7)
STONES = [(2,0),(2,2),(2,4),(2,6),(4,0),(4,2),(4,4),(4,6),(6,0),(6,2),(6,4),(6,6)]
WALLS = [(1,2),(1,3),(1,5),(1,7),(3,2),(3,3),(3,5),(3,7),(5,2),(5,3),(5,5),(5,7)]

import pygame
import os
class Map:

	def __init__(self):
		self.size = (BOARD_HEIGHT*10, BOARD_WIDTH*10)
		self.pos = (0, 0)
		self.stoneImg = pygame.image.load(os.path.join("images","wallImg.png"))
		self.wallImg = pygame.image.load(os.path.join("images","wall.png"))
		self.background  = pygame.image.load(os.path.join("images","map.PNG"))
		self.matriz = []
		self.tam_mapa = [BOARD_WIDTH,BOARD_HEIGHT]
		#inicia a matriz
		for i in range(self.tam_mapa[0]):
			l1 = []
			for j in range(self.tam_mapa[1]):
				l1.append(0)
			self.matriz.append(l1)
          
	def mapear(self,screen):
		tamBloque= 48
		columna = 48
		screen.blit(self.background, (0,0))
		for i in range(BOARD_WIDTH):
			for j in range(BOARD_HEIGHT):
				if (i,j) in STONES:
					
					screen.blit(self.stoneImg,((j+1)*tamBloque + columna ,(i+1)*tamBloque+columna))
				if (i,j) in WALLS:

				
					screen.blit(self.wallImg,((j+1)*tamBloque + columna+ 48,(i+1)*tamBloque+columna+ 48))

screen = pygame.display.set_mode((720,640),0,32)
m = Map()
m.mapear(screen)
while 1:
    pygame.display.flip()
