import pygame as pg
import pymunk as pm
import sys
import DisplayWindow as DW
import GameCode as GC

pg.init()
pg.display.set_caption('')

mysize = (1680, 942)
myDisplay = DW.DISPLAY(mysize)

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
    myDisplay.screenFill('BLACK')
    myDisplay.screenFillLame(-5, 2)
    myDisplay.screenFillGameNameRPG('Lemonade', '1.01', 'LEMONADE', 0)
    myDisplay.drawGameBorder(1)

    myDisplay.setScreenSize(pg.display.get_surface().get_width(), pg.display.get_surface().get_height())
    pg.display.update()
    myDisplay.clock.tick(60)
