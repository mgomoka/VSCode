import pygame as pg
import pygame_menu as pgm
import pymunk as pm
import sys
import DisplayWindow as DW
import GameCode as GC

pg.init()
pg.display.set_caption('')

mysize = (1680, 942)
myDisplay = DW.DISPLAY(mysize)
myGame = GC.GAMECODE(0, 100, mysize)

gScreenColor = 'BLACK'
gLameXOffset = -5
gLameYOffset = 2
gGameName = 'Lemonade'
gVersionName = '1.01'
gGameNameColor = 'LEMONADE'
gGameNameYOffset = 0
gBorderThickness = 1

gameLEVEL = 0

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
    myDisplay.screenFill(gScreenColor)
    myDisplay.screenFillLame(gLameXOffset, gLameYOffset)
    myDisplay.screenFillGameNameRPG(gGameName, gVersionName, gGameNameColor, gGameNameYOffset, gLameXOffset, gLameYOffset)
    myDisplay.drawGameBorder(gBorderThickness)
    myGame.makeStaticBorder(gBorderThickness)
    if gameLEVEL == 0:
        myGame.drawGameScreen(mysize, myDisplay, 'BEIGE')
        myGame.blitSkyImage(mysize, myDisplay)
        # myGame.drawLoadScreen(mysize, myDisplay)
    
    mysize = (pg.display.get_surface().get_width(), pg.display.get_surface().get_height())
    myDisplay.setScreenSize(mysize)
    myGame.setScreenSize(mysize)
    pg.display.update()
    myDisplay.clock.tick(60)
