import pygame as pg
import pymunk as pm
import DisplayWindow as DW
import os

class GAMECODE:
    def __init__(self, sidegravity, downgravity, size):
        self.size = size
        self.space = pm.Space()
        self.space.gravity = (sidegravity, downgravity)
    def makeStaticBorder(self, thickness):
        self.borderStatic = pm.Body(body_type=pm.Body.STATIC)
        self.borderStatic.position = (0, 40)
        self.shapeBorderStatic = pm.Poly.create_box(self.borderStatic, (self.size[0], thickness))
        self.space.add(self.borderStatic, self.shapeBorderStatic)
    def setScreenSize(self, size):
        self.size = size
    def drawGameScreen(self, size, display, color):
        pg.draw.rect(display.screen, display.color.COLORLIST[color], [0, 40, size[0], size[1]-40])
    def blitSkyImage(self, size, display):
        image = os.path.join("/Users/matthewgomoka/Documents/VSCode/VSCode-Python/LamePygamePymunkStuff/PyGamePyMunkGameDesignTest/JPGs/hifi.jpg")
        imageSurface = pg.image.load(image)
        imageSurface = pg.transform.scale(imageSurface, size)
        display.screen.blit(imageSurface, (0,40))
    def drawLoadScreen(self, size, display):
        gameLevelValue = 0
        pg.draw.rect(display.screen, display.color.COLORLIST['BLACK'], [((size[0]/2)-(size[0]/8)), ((size[1]/2)-(size[1]/4)), (size[0]/4), (size[1]/2)], border_radius=15)
        # pg.draw.polygon(display.screen, display.color.COLORLIST['BLACK'], [(((size[0]/2)-200), ((size[1]/2)-300)), (((size[0]/2)+200), ((size[1]/2)-300)), (((size[0]/2)+200), ((size[1]/2)+300)), (((size[0]/2)-200), ((size[1]/2)+300))])
        return gameLevelValue
