import time
from Map import *

print "Wellcome to bomberRL"
print "Press S to start, F for fullscreen, UP and DOWN for speed change, 1 to 4 for diferent plays"
pg.display.set_caption("S or SPACE to start, F for FullScreen")
screen = pg.display.set_mode((BOARD_HEIGHT*TAMBLOQUE, BOARD_WIDTH*TAMBLOQUE),0,32)

pg.mouse.set_visible(0)

StonesCopy = STONES[:]
m = Map()

movements = MOVEMENTS
m.drawScreen(screen,StonesCopy)
notPaused = False
i = 0
while True:
	pg.display.set_caption('S or SPACE to start, F for FullScreen, Up and Down for speed')

	

	for event in pg.event.get():
		if event.type == pg.KEYDOWN:
			if event.key == pg.K_q:
				exit()
			elif event.key == pg.K_UP:
				GAMESPEED = GAMESPEED/2
				print "Speed increased"
			elif event.key == pg.K_DOWN:
				GAMESPEED = GAMESPEED*2
				print "Speed decreased"
			elif event.key == pg.K_1:
				print "RESTABLECIDO"
				StonesCopy = STONES[:]
				movements = MOVEMENTS
				m.restart()
				notPaused = False
				i = 0
				m.drawScreen(screen,StonesCopy)
				break
			elif event.key == pg.K_2:
				movements = MOVEMENTS2
				StonesCopy = STONES[:]
				m.restart()
				i = 0
				m.drawScreen(screen,StonesCopy)	
				notPaused = False
				break
			elif event.key == pg.K_3:
				movements = MOVEMENTS3
				notPaused = False
				i = 0 
				StonesCopy = STONES[:]
				m.restart()
				m.drawScreen(screen,StonesCopy)	
				break
			elif event.key == pg.K_4:
				movements = MOVEMENTS4
				notPaused = False
				i = 0 
				StonesCopy = STONES[:]
				m.restart()
				m.drawScreen(screen,StonesCopy)	
				break

			elif event.key == pg.K_f:
				pg.display.toggle_fullscreen()
			elif event.key == pg.K_s or event.key == pg.K_SPACE:
				notPaused = not notPaused
				if notPaused:
					print "PAUSE"
				else:
					print "STARTED"
	
	m.drawScreen(screen,StonesCopy)
	pg.display.flip()

	
	if notPaused:
		nextMove = movements[i]
	else:
		continue
		
	time.sleep(GAMESPEED)
   	
	if nextMove == UP:
		m.move((-1,0),m.bomberImg1,screen,StonesCopy)
		m.explodePos = None
	elif nextMove == RIGHT:
		m.move((0,1),m.bomberImg1,screen,StonesCopy)
		m.explodePos = None
	elif nextMove == DOWN:
		m.move((1,0),m.bomberImg1,screen,StonesCopy)
		m.explodePos = None
	elif nextMove == LEFT:
		m.move((0,-1),m.bomberImg1,screen,StonesCopy)
		m.explodePos = None
	elif nextMove == BOMBDROP:
		m.bombPos= m.pos
		m.explodePos = None
		m.drawScreen(screen,StonesCopy)
		pg.display.flip()

	
	elif nextMove == BOMBEXPLODE:
		i = i + 1
		
		
		stonesBroken = movements[i]
		
		if stonesBroken % 2 == 1: 
			StonesCopy.remove(m.coordSum(m.bombPos,(0,+1)))
		stonesBroken = stonesBroken/2
		if stonesBroken % 2 == 1:
			StonesCopy.remove(m.coordSum(m.bombPos,(0,-1)))
		stonesBroken = stonesBroken/2
		if stonesBroken % 2 == 1: 
			StonesCopy.remove(m.coordSum(m.bombPos,(-1,0)))
		stonesBroken = stonesBroken/2
		if stonesBroken % 2 == 1: 
			StonesCopy.remove(m.coordSum(m.bombPos,(+1,0)))
		m.explodePos  = m.coordSum(m.bombPos,(-1,-1)) 
		m.bombPos = None
		m.drawScreen(screen,StonesCopy)
		pg.display.flip()

		
	
	elif nextMove == NOACTION:	
		m.explodePos = None
		m.drawScreen(screen,StonesCopy)
		pg.display.flip()
		
	elif nextMove == DEAD:		
		screen.fill((0,0,0))	
		screen.blit(m.deadImg,(0,0))
		pg.display.flip()
		time.sleep(2)
		StonesCopy = STONES[:]
		
		m.restart()

		

	else:
		print "ILEGAL ACTION"
	
	i = i + 1
	if i == len(movements): 
		if movements[-1] != DEAD:
			screen.fill((0,0,0))
			screen.blit(m.winImg,(0,0))
			pg.display.flip()
			time.sleep(2)
			print "YOU WIN.. "
		StonesCopy = STONES[:]

		m.restart()
		i = 0
		m.drawScreen(screen,StonesCopy)	
		notPaused = False		


exit()
