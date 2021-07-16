import pygame as pg
import pymunk as pm
import DisplayWindow as DW

class GAMECODE():
    def __init__(self, sidegravity, downgravity):
        self.space = pm.Space()
        self.space.gravity = (sidegravity, downgravity)
        self.borderStatic = pm.Body(body_type=pm.Body.STATIC)
        self.borderStatic.position = (0, 40)
        self.shapeBorderStatic = pm.Poly.create_box(self.borderStatic, (self.size[0], 1))
        self.space.add(self.borderStatic, self.shapeBorderStatic)
