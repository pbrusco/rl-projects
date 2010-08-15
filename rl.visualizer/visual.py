import sys

sys.path.append('../rl.bomber')


from Settings import *
from Movements import *

TAMBLOQUE = 48
COLUMNA = 48

import pygame as pg
import os
class Map:

	def __init__(self):
		self.size = (BOARD_HEIGHT*10, BOARD_WIDTH*10)
		
		self.stoneImg = pg.image.load(os.path.join("images","wall.png"))
		self.wallImg = pg.image.load(os.path.join("images","wallImg.png"))
		self.background  = pg.image.load(os.path.join("images","ansontsui.jpg"))
		self.salidaImg  = pg.image.load(os.path.join("images","salida.png"))
		self.bomberImg1 = pg.image.load(os.path.join("images","ICON0SuperMarioWar.png"))
		self.exitImg = pg.image.load(os.path.join("images","salida.png"))
		self.bombImg1 = pg.image.load(os.path.join("images","bomb1.png"))
		self.explodeImg = pg.image.load(os.path.join("images","explode.png"))		
		
		self.pos = (0, 0)
		self.bombPos = None
		self.explodePos = None
		
		self.matriz = []
		self.tam_mapa = [BOARD_WIDTH,BOARD_HEIGHT]
		#inicia a matriz
		for i in range(self.tam_mapa[0]):
			l1 = []
			for j in range(self.tam_mapa[1]):
				l1.append(0)
			self.matriz.append(l1)
          
    
	def posTablero(self,j,i): 
		return (i*TAMBLOQUE  ,j*COLUMNA)
		
	def addPos(self,pos,dire):
		a = pos[0] + dire[0]
		b = pos[1] + dire[1]
		return (a,b)
		
		
	def move(self,dire,obj,screen):
		self.pos = self.addPos(self.pos,dire)
		self.mapear(screen)
		pg.display.flip()
      

	def mapear(self,screen):
		for i in range(BOARD_WIDTH):
			for j in range(BOARD_HEIGHT):
				screen.blit(self.background, self.posTablero(i,j))		
				if (i,j) in STONES:
					screen.blit(self.stoneImg, self.posTablero(i,j))
				if (i,j) in WALLS:
					screen.blit(self.wallImg, self.posTablero(i,j))
				
		screen.blit(self.bomberImg1, self.posTablero(self.pos[0],self.pos[1]))
		screen.blit(self.exitImg,self.posTablero(7,7))
		if self.bombPos != None:
			screen.blit(self.bombImg1,self.posTablero(self.posBomb[0],self.posBomb[1]))
		if self.explodePos != None:
			self.screen.blit(self.explodeImg,self.posTablero(self.posExplote[0],self.posExplote[1]))
		





i = 0
pg.display.set_caption('Bomberman!!!')
screen = pg.display.set_mode((720,640),0,32)
m = Map()

m.mapear(screen)

running = True
while running:

	event = pg.event.poll()
	keyinput = pg.key.get_pressed()

	if keyinput[pg.K_ESCAPE]:
		raise SystemExit
	elif event.type == pg.QUIT:
		running = False
	if event.type == pg.MOUSEBUTTONDOWN:
		nextMove = MOVEMENTS[i]
		i = (i+1) % len(MOVEMENTS)
		if nextMove == UP:
			m.move((-1,0),m.bomberImg1,screen)
			print "UP" 
		elif nextMove == RIGHT:
			m.move((0,1),m.bomberImg1,screen)
			print "RIGHT"
		elif nextMove == DOWN:
			m.move((1,0),m.bomberImg1,screen)
			print "DOWN"
		elif nextMove == LEFT:
			m.move((0,-1),m.bomberImg1,screen)
			print "LEFT"	
		elif nextMove == BOMBDROP:
			m.bombPos= m.pos
			m.mapear(screen)
			pg.display.flip()

		
			print "BOMBDROP"	
		elif nextMove == BOMBEXPLODE:	
			m.explodePos = m.bombPos
			m.bombPos = None
			m.mapear(screen)
			pg.display.flip()
			print "BOMBEXPLODE"	
		else:
			print "ILEGAL ACTION"
			exit()



