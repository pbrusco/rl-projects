# experiments with module pygame, free from: http://www.pygame.org/
# move an image rectangle to follow the mouse click position (ulc)
# tested with Python25 and PyGame18     vegaseat     07aug2008

import pygame as pg

# initialize pygame
pg.init()

# use an image you have (.bmp  .jpg  .png  .gif)
image_file = "ball_r.gif"

# RGB color tuple for screen background
black = (0,0,0)

# screen width and height
sw = 640
sh = 480
# create a screen
screen = pg.display.set_mode((sw, sh))
# give the screen a title
pg.display.set_caption('image follows mouse click position')

# load an image
# convert() unifies the pixel format for faster blit
image = pg.image.load(image_file).convert()
# get the rectangle the image occupies
# rec(x, y, w, h)
start_rect = image.get_rect()
image_rect = start_rect

running = True
while running:
    event = pg.event.poll()
    keyinput = pg.key.get_pressed()
    # exit on corner 'x' click or escape key press
    if keyinput[pg.K_ESCAPE]:
        raise SystemExit
    elif event.type == pg.QUIT:
        running = False
    elif event.type == pg.MOUSEBUTTONDOWN:
        print event.pos, list(event.pos)  # test
        mouse_loc = "mouse click at (%d, %d)" % event.pos
        pg.display.set_caption(mouse_loc)
        mouse_pos = list(event.pos)
        image_rect = start_rect.move(mouse_pos)
        """
        print image_rect  # test
        print "corner coordinates --> (%d, %d, %d, %d)" % \
            (image_rect.left, image_rect.top, image_rect.right,
            image_rect.bottom)
        """

    # this erases the old sreen with black
    screen.fill(black)
    # put the image on the screen
    screen.blit(image, image_rect)
    # update screen
    pg.display.flip()
