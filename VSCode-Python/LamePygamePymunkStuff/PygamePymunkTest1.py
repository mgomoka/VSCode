import pymunk as pm
import pygame as pg

import sys
import random
import numpy as np



# Define Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BWHITE = (245, 245, 220)
RED = (255, 99, 71)
BLUE = (30, 144, 255)
YELLOW = (255, 255, 0)


pg.init()
pg.display.set_caption('PyGamePyMunkTest1')

size = (850, 850)
screen = pg.display.set_mode(size)
clock = pg.time.Clock()
font = pg.font.Font('freesansbold.ttf', 15) # pg.font.SysFont('avenir', 15)

