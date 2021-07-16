import pygame as pg
import pymunk as pm
import DisplayWindow as DW

class GAMECODE():
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
