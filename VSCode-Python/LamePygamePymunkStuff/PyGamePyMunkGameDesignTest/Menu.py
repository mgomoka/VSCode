import pygame as pg
import pygame_menu as pgm

class MENU:
    def __init__(self, header, xSize, ySize, theme):
        menu = pgm.Menu(header, xSize, ySize, theme)
        