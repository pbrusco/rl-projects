import sys
import random

sys.path.append('images')


from Maps import *
from ToVisualize import *
from VisualSettings import *
import pygame as pg
import os

class Map:

	def __init__(self):
		self.restart()		
					
	def restart(self):
		self.pos = (0, 0)
		self.bombPos = None
		self.explodePos = None
		

		self.background  = pg.image.load(os.path.join("images/backgrounds",random.choice(os.listdir("images/backgrounds"))))
		self.stoneImg  = pg.image.load(os.path.join("images/stones",random.choice(os.listdir("images/stones"))))
		self.wallImg  = pg.image.load(os.path.join("images/walls",random.choice(os.listdir("images/walls"))))
		self.exitImg  = pg.image.load(os.path.join("images/exits",random.choice(os.listdir("images/exits"))))
		self.bomberImg1  = pg.image.load(os.path.join("images/players",random.choice(os.listdir("images/players"))))
		self.bombImg1  = pg.image.load(os.path.join("images/bombs",random.choice(os.listdir("images/bombs"))))
		self.explodeImg  = pg.image.load(os.path.join("images/explotions",random.choice(os.listdir("images/explotions"))))
		self.deadImg  = pg.image.load(os.path.join("images/deads",random.choice(os.listdir("images/deads"))))
		self.winImg  = pg.image.load(os.path.join("images/wins",random.choice(os.listdir("images/wins"))))

	
    
    #for screen position:
	def posTablero(self,j,i): 
		return (i*TAMBLOQUE ,j*COLUMNA)
		
	#list sum coord to coord i.e: coorSum([3,4,5],[6,6,6,4]) = [9,10,11,4] 
	def coordSum(self,l1,l2):
		return (l1[0]+l2[0],l1[1]+l2[1])
		
	#move object in screen.	
	def move(self,dire,obj,screen):
		self.pos = self.coordSum(self.pos,dire)
		self.drawScreen(screen)
		pg.display.flip()
      

	def drawScreen(self,screen):
		self.drawBackground(screen)
		self.drawStones(screen)
		self.drawBomb(screen)
		self.drawExplosion(screen)
		self.drawExit(screen)
		self.drawBomberman(screen)
		self.drawWalls(screen)
		
	def drawBackground(self,screen):
		for i in range(BOARD_WIDTH):
			for j in range(BOARD_HEIGHT):
				screen.blit(self.background, self.posTablero(i,j))		

	def drawStones(self,screen):			
		for i in range(BOARD_WIDTH):
			for j in range(BOARD_HEIGHT):
				if (i,j) in STONES:
					screen.blit(self.stoneImg, self.posTablero(i,j))
				
	def drawBomberman(self,screen):				
		screen.blit(self.bomberImg1, self.posTablero(self.pos[0],self.pos[1]))

	def drawExit(self,screen):
		screen.blit(self.exitImg,self.posTablero(BOARD_WIDTH-1,BOARD_HEIGHT-1))

	def drawBomb(self,screen):
		if self.bombPos != None:
			screen.blit(self.bombImg1,self.posTablero(self.bombPos[0],self.bombPos[1]))

	def drawExplosion(self,screen):
		if self.explodePos != None:
			screen.blit(self.explodeImg,self.posTablero(self.explodePos[0],self.explodePos[1]))

	def drawWalls(self,screen):
		for i in range(BOARD_WIDTH):
			for j in range(BOARD_HEIGHT):
				if (i,j) in WALLS:
						screen.blit(self.wallImg, self.posTablero(i,j))






