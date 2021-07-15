import pygame as pg
import ColorsFonts as CF

class DISPLAY():
    def __init__(self, size):
        self.screen = pg.display.set_mode(size)
        self.clock = pg.time.Clock()
        self.color = CF.COLOR()
        self.font = CF.FONT()
        self.font.setFontSF('herculanum', 30)
    def screenFillLame(self, color):
        self.screen.fill(color)
        GameNameDisplayTextL = 'L'
        renderGameNameDisplayTextL = self.font.font.render(GameNameDisplayTextL, True, self.color.COLORLIST["RED"])
        self.screen.blit(renderGameNameDisplayTextL, [10, 10])
        GameNameDisplayTextA = 'A'
        renderGameNameDisplayTextA = self.font.font.render(GameNameDisplayTextA, True, self.color.COLORLIST["YELLOW"])
        self.screen.blit(renderGameNameDisplayTextA, [30, 10])
        GameNameDisplayTextM = 'M'
        renderGameNameDisplayTextM = self.font.font.render(GameNameDisplayTextM, True, self.color.COLORLIST["BLUE"])
        self.screen.blit(renderGameNameDisplayTextM, [55, 10])
        GameNameDisplayTextE = 'E'
        renderGameNameDisplayTextE = self.font.font.render(GameNameDisplayTextE, True, self.color.COLORLIST["ORANGE"])
        self.screen.blit(renderGameNameDisplayTextE, [95, 10])
