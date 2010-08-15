import sys


sys.path.append('../rl.bomber')


from Settings import *
from Movements import *
from Maps import *


import pygame as pg
import os

GAMESPEED = 0.3
TAMBLOQUE = 48
COLUMNA = 48
class Map:

	def __init__(self):
		
		#load default images:
		self.stoneImg = pg.image.load(os.path.join("images","Fl-brick.png"))
		self.wallImg = pg.image.load(os.path.join("images","Fl-black.png"))
		self.background  = pg.image.load(os.path.join("images","Fl_lawn.png"))
		self.salidaImg  = pg.image.load(os.path.join("images","salida.png"))
		self.bomberImg1 = pg.image.load(os.path.join("images","fuego.png"))
		self.exitImg = pg.image.load(os.path.join("images","salida.png"))
		self.bombImg1 = pg.image.load(os.path.join("images","bomb1.png"))
		self.explodeImg = pg.image.load(os.path.join("images","explode2.png"))		
		self.deadImg = pg.image.load(os.path.join("images","guason.jpg"))


		#starting positions:
		self.pos = (0, 0)
		self.bombPos = None
		self.explodePos = None
		
	
	
    
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






