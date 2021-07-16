import pygame as pg

class COLOR:
    def __init__(self):
        self.COLORLIST = {
            "BLACK": (0, 0, 0),
            "WHITE": (255, 255, 255),
            "BEIGE": (245, 245, 220),
            "RED": (255, 99, 71),
            "BLUE": (30, 144, 255),
            "YELLOW": (255, 255, 0),
            "ORANGE": (255, 165, 0),
            "TANGERINE": (255, 132, 0),
            "LEMONADE": (253, 185, 200)
        }
    def printCOLORLIST(self):
        print(self.COLORLIST)
    def returnCOLORLIST(self):
        return self.COLORLIST

class FONT:
    def __init__(self):
        self.font = pg.font.Font(pg.font.get_default_font(), 12)
    def returnAvailableFonts():
        fontList = pg.font.get_fonts()
        return fontList
    def printAvailableFonts():
        fontList = pg.font.get_fonts()
        print(fontList)
    def setFontF(self, font, size):
        self.font = pg.font.Font(font, size)
    def setFontSF(self, font, size):
        self.font = pg.font.SysFont(font, size)
