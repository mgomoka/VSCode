import pygame as pg
import ColorsFonts as CF

class DISPLAY():
    def __init__(self, size):
        self.size = size
        self.screen = pg.display.set_mode(self.size, pg.RESIZABLE)
        self.clock = pg.time.Clock()
        self.color = CF.COLOR()
        self.font = CF.FONT()
        self.font.setFontSF('herculanum', 20)
    def screenFill(self, color):
        self.screen.fill(self.color.COLORLIST[color])
    def setScreenSize(self, size):
        self.size = size
    def screenFillLame(self, xOff, yOff):
        GameNameDisplayTextL = 'L'
        textXOffset = xOff
        textYOffset = yOff
        renderGameNameDisplayTextL = self.font.font.render(GameNameDisplayTextL, True, self.color.COLORLIST["RED"])
        self.screen.blit(renderGameNameDisplayTextL, [10+textXOffset, 7+textYOffset])
        GameNameDisplayTextA = 'A'
        renderGameNameDisplayTextA = self.font.font.render(GameNameDisplayTextA, True, self.color.COLORLIST["YELLOW"])
        self.screen.blit(renderGameNameDisplayTextA, [23+textXOffset, 7+textYOffset])
        GameNameDisplayTextM = 'M'
        renderGameNameDisplayTextM = self.font.font.render(GameNameDisplayTextM, True, self.color.COLORLIST["BLUE"])
        self.screen.blit(renderGameNameDisplayTextM, [37+textXOffset, 7+textYOffset])
        GameNameDisplayTextE = 'E'
        renderGameNameDisplayTextE = self.font.font.render(GameNameDisplayTextE, True, self.color.COLORLIST["ORANGE"])
        self.screen.blit(renderGameNameDisplayTextE, [60+textXOffset, 7+textYOffset])
    def blitText(self, text, font, size, colorOf, whereAt):
        blitFont = CF.FONT()
        blitFont.setFontSF(font, size)
        storedString = text
        renderString = blitFont.font.render(storedString, True, self.color.COLORLIST[colorOf])
        self.screen.blit(renderString, whereAt)
    def getTextWidth(self, text, font, size):
        blitFont = CF.FONT()
        blitFont.setFontSF(font, size)
        storedString = text
        renderString = blitFont.font.render(storedString,True, self.color.COLORLIST['BLACK'])
        renderedWidth = renderString.get_width()
        return renderedWidth
    def screenFillGameNameRPG(self, gamename, versionID, gamecolor, yOffset):
        gamenameWidth = self.getTextWidth(gamename, 'herculanum', 30)
        rWidth = self.getTextWidth('R', 'herculanum', 30)
        pWidth = self.getTextWidth('P', 'herculanum', 30)
        gWidth = self.getTextWidth('G', 'herculanum', 30)
        versionWidth = self.getTextWidth('Version ' + versionID, 'herculanum', 20)
        self.blitText(gamename, 'herculanum', 30, gamecolor, [(self.size[0]/2)-((gamenameWidth+5+rWidth+1+pWidth+1+gWidth+1)/2), 5+yOffset])
        self.blitText('R', 'herculanum', 30, 'RED', [(self.size[0]/2)-((gamenameWidth+5+rWidth+1+pWidth+1+gWidth+1)/2)+(gamenameWidth+5), 5+yOffset])
        self.blitText('P', 'herculanum', 30, 'YELLOW', [(self.size[0]/2)-((gamenameWidth+5+rWidth+1+pWidth+1+gWidth+1)/2)+(gamenameWidth+5+rWidth+1), 5+yOffset])
        self.blitText('G', 'herculanum', 30, 'BLUE', [(self.size[0]/2)-((gamenameWidth+5+rWidth+1+pWidth+1+gWidth+1)/2)+(gamenameWidth+5+rWidth+1+pWidth), 5+yOffset])
        self.blitText('Version ' + versionID, 'herculanum', 20, 'WHITE', [(self.size[0])-5-versionWidth, 9])
    def drawGameBorder(self, thickness):
        pg.draw.rect(self.screen, self.color.COLORLIST['WHITE'], [0, 40, self.size[0], thickness])
