import pygame as pg
import pymunk as pm
import sys
import Display

pg.init()
pg.display.set_caption('')

size = (1600, 900)
mysize = (1680, 942)
myDisplay = Display.DISPLAY(size)

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
    myDisplay.screenFillLame(myDisplay.color.COLORLIST["BLACK"])

    pg.display.update()
    myDisplay.clock.tick(60)
