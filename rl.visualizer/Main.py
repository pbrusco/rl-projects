import time
from Visual import *

pg.display.set_caption('Bomberman!!!')
screen = pg.display.set_mode((BOARD_HEIGHT*TAMBLOQUE, BOARD_WIDTH*TAMBLOQUE),0,32)

pg.display.toggle_fullscreen()

m = Map()


m.drawScreen(screen)

i = 0
while i < len(MOVEMENTS):
	time.sleep(GAMESPEED)
	nextMove = MOVEMENTS[i]
	if nextMove == UP:
		m.move((-1,0),m.bomberImg1,screen)
		m.explodePos = None
		print "UP" 
	elif nextMove == RIGHT:
		m.move((0,1),m.bomberImg1,screen)
		m.explodePos = None
		print "RIGHT"
	elif nextMove == DOWN:
		m.move((1,0),m.bomberImg1,screen)
		m.explodePos = None
		print "DOWN"
	elif nextMove == LEFT:
		m.move((0,-1),m.bomberImg1,screen)
		m.explodePos = None
		print "LEFT"	
	elif nextMove == BOMBDROP:
		m.bombPos= m.pos
		m.explodePos = None
		m.drawScreen(screen)
		pg.display.flip()

	
		print "BOMBDROP"	
	elif nextMove == BOMBEXPLODE:
		i = i + 1
		stonesBroken = MOVEMENTS[i]
		print "BOMBEXPLODE"	
		print stonesBroken
		if stonesBroken % 2 == 1: 
			print STONES
			print m.coordSum(m.bombPos,(-1,0))
			print m.bombPos
			STONES.remove(m.coordSum(m.bombPos,(0,+1)))
		stonesBroken = stonesBroken/2
		if stonesBroken % 2 == 1: 
			STONES.remove(m.coordSum(m.bombPos,(0,-1)))
		stonesBroken = stonesBroken/2
		if stonesBroken % 2 == 1: 
			STONES.remove(m.coordSum(m.bombPos,(-1,0)))
		stonesBroken = stonesBroken/2
		if stonesBroken % 2 == 1: 
			STONES.remove(m.coordSum(m.bombPos,(+1,0)))

		m.explodePos  = m.coordSum(m.bombPos,(-1,-1)) 
		m.bombPos = None
		m.drawScreen(screen)
		pg.display.flip()

		
	
	elif nextMove == NOACTION:	
		m.explodePos = None
		m.drawScreen(screen)
		pg.display.flip()
		print "NOACTION"	

	elif nextMove == DEAD:		
		screen.fill((0,0,0))	
		screen.blit(m.deadImg,(0,0))
		pg.display.flip()
		time.sleep(2)
		print "DEAD"	


	else:
		print "ILEGAL ACTION"
	
	i = i + 1


if MOVEMENTS[-1] != DEAD:
	screen.fill((0,0,0))	
	screen.blit(m.winImg,(0,0))
	pg.display.flip()
	time.sleep(2)
	print "YOU WIN.. FLAWLESS VICTORY"
exit()
