import pymunk as pm
import pygame as pg

import sys
import random
import numpy as np


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BWHITE = (245, 245, 220)
RED = (255, 99, 71)
BLUE = (30, 144, 255)
YELLOW = (255, 255, 0)
TANGERINE = (255, 132, 0)
ORANGE = (255, 165, 0)

# Display Available PyGame Fonts
# fontList = pg.font.get_fonts()
# print(fontList)

pg.init()
pg.display.set_caption('PyGamePyMunkTest1')

size = (1600, 900)
mysize = (1680, 942)
screen = pg.display.set_mode(size)
clock = pg.time.Clock()
# font = pg.font.Font('freesansbold.ttf', 15)
# sysfont = pg.font.SysFont('avenir', 15)
# defaultFont = pg.font.Font(pg.font.get_default_font(), 15)
myFont = pg.font.SysFont('herculanum', 30)

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
    screen.fill(BLACK)

    GameNameDisplayTextL = 'L'
    renderGameNameDisplayTextL = myFont.render(GameNameDisplayTextL, True, RED)
    screen.blit(renderGameNameDisplayTextL, [10, 10])
    GameNameDisplayTextA = 'A'
    renderGameNameDisplayTextA = myFont.render(GameNameDisplayTextA, True, YELLOW)
    screen.blit(renderGameNameDisplayTextA, [30, 10])
    GameNameDisplayTextM = 'M'
    renderGameNameDisplayTextM = myFont.render(GameNameDisplayTextM, True, BLUE)
    screen.blit(renderGameNameDisplayTextM, [55, 10])
    GameNameDisplayTextE = 'E'
    renderGameNameDisplayTextE = myFont.render(GameNameDisplayTextE, True, ORANGE)
    screen.blit(renderGameNameDisplayTextE, [95, 10])

    pg.display.update()
    clock.tick(60)
