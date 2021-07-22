import math
import pygame as pg
import pymunk as pm
import sys
import random
import numpy as np

def quadrilateral_init(self, sideOne, sideTwo, sideThree, sideFour, angleOne, angleTwo, angleThree, angleFour):
    self.type = ''
    self.numberofsides = 4
    self.sumofangles = 360.0
    self.sidelengthOne = float(sideOne)
    self.sidelengthTwo = float(sideTwo)
    self.sidelengthThree = float(sideThree)
    self.sidelengthFour = float(sideFour)
    self.angleOne = float(angleOne)
    self.angleTwo = float(angleTwo)
    self.angleThree = float(angleThree)
    self.angleFour = float(angleFour)
def get_type(self):
    return self.type
def get_numberofsides(self):
    return self.numberofsides
def get_sumofangles(self):
    return self.sumofangles
def get_firstside(self):
    return self.sidelengthOne
def get_secondside(self):
    return self.sidelengthTwo
def get_thirdside(self):
    return self.sidelengthThree
def get_fourthside(self):
    return self.sidelengthFour
def get_firstangle(self):
    return self.angleOne
def get_secondangle(self):
    return self.angleTwo
def get_thirdangle(self):
    return self.angleThree
def get_fourthangle(self):
    return self.angleFour
def find_perimeter(self):
    return self.sidelengthOne + self.sidelengthTwo + self.sidelengthThree + self.sidelengthFour
def find_area(self):
    return ((1/2)*(self.sidelengthOne)*(self.sidelengthTwo)*math.sin(math.radians(self.angleTwo)))+((1/2)*(self.sidelengthThree)*(self.sidelengthFour)*math.sin(math.radians(self.angleThree)))
quadrilateral_class = type("quadrilateral_class", (), {"__init__": quadrilateral_init, 
                           "get_type": get_type, "get_numberofsides": get_numberofsides, "get_sumofangles": get_sumofangles, 
                           "get_firstside": get_firstside, "get_secondside": get_secondside, 
                           "get_thirdside": get_thirdside, "get_fourthside": get_fourthside, 
                           "get_firstangle": get_firstangle, "get_secondangle": get_secondangle, 
                           "get_thirdangle": get_thirdangle, "get_fourthangle": get_fourthangle, 
                           "find_perimeter": find_perimeter, "find_area": find_area})

def trapezoid_init(self, toplength, leftsidelength, bottomlength, rightsidelength, toprightangle, topleftangle, bottomleftangle, bottomrightangle):
    quadrilateral_class.__init__(self, toplength, leftsidelength, bottomlength, rightsidelength, toprightangle, topleftangle, bottomleftangle, bottomrightangle)
    self.type = 'trapezoid'
def isoscelestrapezoid_init(self, toplength, bottomlength, sideslength, topangles, bottomangles):
    quadrilateral_class.__init__(self, toplength, sideslength, bottomlength, sideslength, topangles, topangles, bottomangles, bottomangles)
    self.type = 'isosceles trapezoid'
def parallelogram_init(self, TBlength, LRlength, TRBLangles, TLBRangles):
    quadrilateral_class.__init__(self, TBlength, LRlength, TBlength, LRlength, TRBLangles, TLBRangles, TRBLangles, TLBRangles)
    self.type = 'parallelogram'
def rectangle_init(self, TBlength, LRlength):
    quadrilateral_class.__init__(self, TBlength, LRlength, TBlength, LRlength, 90, 90, 90, 90)
    self.type = 'rectangle'
def rhombus_init(self, sidelength, TBangles, LRangles):
    quadrilateral_class.__init__(self, sidelength, sidelength, sidelength, sidelength, TBangles, LRangles, TBangles, LRangles)
    self.type = 'rhombus'
def square_init(self, sidelength):
    quadrilateral_class.__init__(self, sidelength, sidelength, sidelength, sidelength, 90, 90, 90 ,90)
    self.type = 'square'
trapezoid_class = type("trapezoid_class", (quadrilateral_class, ), {"__init__": trapezoid_init})
isoscelestrapezoid_class = type("isoscelestrapezoid_class", (quadrilateral_class, ), {"__init__": isoscelestrapezoid_init})
parallelogram_class = type("parallelogram_class", (quadrilateral_class, ), {"__init__": parallelogram_init})
rectangle_class = type("rectangle_class", (quadrilateral_class, ), {"__init__": rectangle_init})
rhombus_class = type("rhombus_class", (quadrilateral_class, ), {"__init__": rhombus_init})
square_class = type("square_class", (quadrilateral_class, ), {"__init__": square_init})



BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BWHITE = (245, 245, 220)
RED = (255, 99, 71)
BLUE = (30, 144, 255)
YELLOW = (255, 255, 0)
TANGERINE = (255, 132, 0)
ORANGE = (255, 165, 0)

pg.init()
pg.display.set_caption('Quadrilateral')

size = (1600, 900)
mysize = (1680, 942)
screen = pg.display.set_mode(size, pg.RESIZABLE)
clock = pg.time.Clock()
myFont = pg.font.SysFont('herculanum', 30)

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
    screen.fill(BLACK)

    GameNameDisplayTextL = 'L'
    renderGameNameDisplayTextL = myFont.render(GameNameDisplayTextL, True, RED)
    screen.blit(renderGameNameDisplayTextL, [10, 10])
    GameNameDisplayTextA = 'A'
    renderGameNameDisplayTextA = myFont.render(GameNameDisplayTextA, True, YELLOW)
    screen.blit(renderGameNameDisplayTextA, [30, 10])
    GameNameDisplayTextM = 'M'
    renderGameNameDisplayTextM = myFont.render(GameNameDisplayTextM, True, BLUE)
    screen.blit(renderGameNameDisplayTextM, [55, 10])
    GameNameDisplayTextE = 'E'
    renderGameNameDisplayTextE = myFont.render(GameNameDisplayTextE, True, ORANGE)
    screen.blit(renderGameNameDisplayTextE, [95, 10])



    pg.display.update()
    clock.tick(60)

"""
while True:
    print("1. Create New Shape")
    print("2. Quit Program")
    mainmenuinput = input("Please Enter Choice ")
    if mainmenuinput == '1':
        print("1. Create General Quadrilateral")
        print("2. Create Trapezoid")
        print("3. Create Isosceles Trapezoid")
        print("4. Create Parallelogram")
        print("5. Create Rectangle")
        print("6. Create Rhombus")
        print("7. Create Square")
        print("8. Return To Main Menu")
        print("9. Quit Program")
        newshapemenuinput = input("Please Enter Choice ")
        if newshapemenuinput == '1':
            sideone = float(input("Enter First Side "))
            sidetwo = float(input("Enter Second Side "))
            sidethree = float(input("Enter Third Side "))
            sidefour = float(input("Enter Fourth Side "))
            angleone = float(input("Enter First Angle "))
            angletwo = float(input("Enter Second Angle "))
            anglethree = float(input("Enter Third Angle "))
            anglefour = float(input("Enter Fourth Angle "))
            quadgentemp = quadrilateral_class(sideone, sidetwo, sidethree, sidefour, angleone, angletwo, anglethree, anglefour)
            print("1. Find Perimeter")
            print("2. Find Area")
            print("3. Return To Main Menu")
            print("4. Quit Program")
            quadmenuinput = input("Please Enter Choice ")
            if quadmenuinput == '1':
                print("The Perimeter Of The General Quadrilateral Is Equal To " + str(quadgentemp.find_perimeter()) + ".")
            elif quadmenuinput == '2':
                print("The Area Of The General Quadrilateral Is Equal To " + str(quadgentemp.find_area()) + ".")
            elif quadmenuinput == '3':
                continue
            elif quadmenuinput == '4':
                break
        elif newshapemenuinput == '2':
            sideone = float(input("Enter First Side "))
            sidetwo = float(input("Enter Second Side "))
            sidethree = float(input("Enter Third Side "))
            sidefour = float(input("Enter Fourth Side "))
            angleone = float(input("Enter First Angle "))
            angletwo = float(input("Enter Second Angle "))
            anglethree = float(input("Enter Third Angle "))
            anglefour = float(input("Enter Fourth Angle "))
            trapezoidtemp = trapezoid_class(sideone, sidetwo, sidethree, sidefour, angleone, angletwo, anglethree, anglefour)
            print("1. Find Perimeter")
            print("2. Find Area")
            print("3. Return To Main Menu")
            print("4. Quit Program")
            trapezoidmenuinput = input("Please Enter Choice ")
            if trapezoidmenuinput == '1':
                print("The Perimeter Of The Trapezoid Is Equal To " + str(trapezoidtemp.find_perimeter()) + ".")
            elif trapezoidmenuinput == '2':
                print("The Area Of The Trapezoid Is Equal To " + str(trapezoidtemp.find_area()) + ".")
            elif trapezoidmenuinput == '3':
                continue
            elif trapezoidmenuinput == '4':
                break
        elif newshapemenuinput == '3':
            sidetop = float(input("Enter Top Side "))
            sidebottom = float(input("Enter Bottom Side "))
            sideleftright = float(input("Enter Left/Right Side "))
            angletop = float(input("Enter Top Angle "))
            anglebottom = float(input("Enter Bottom Angle "))
            itrapezoidtemp = isoscelestrapezoid_class(sidetop, sidebottom, sideleftright, angletop, anglebottom)
            print("1. Find Perimeter")
            print("2. Find Area")
            print("3. Return To Main Menu")
            print("4. Quit Program")
            itrapezoidmenuinput = input("Please Enter Choice ")
            if itrapezoidmenuinput == '1':
                print("The Perimeter Of The Isosceles Trapezoid Is Equal To " + str(itrapezoidtemp.find_perimeter()) + ".")
            elif itrapezoidmenuinput == '2':
                print("The Area Of The Isosceles Trapezoid Is Equal To " + str(itrapezoidtemp.find_area()) + ".")
            elif itrapezoidmenuinput == '3':
                continue
            elif itrapezoidmenuinput == '4':
                break
        elif newshapemenuinput == '4':
            sidetopbottom = float(input("Enter Top/Bottom Side "))
            sideleftright = float(input("Enter Left/Right Side ")) 
            angleTRBL = float(input("Enter Top Right/Bottom Left Angle "))
            angleTLBR = float(input("Enter Top Left/Bottom Right Angle "))
            parallelogramtemp = parallelogram_class(sidetopbottom, sideleftright, angleTRBL, angleTLBR)
            print("1. Find Perimeter")
            print("2. Find Area")
            print("3. Return To Main Menu")
            print("4. Quit Program")
            parallelogrammenuinput = input("Please Enter Choice ")
            if parallelogrammenuinput == '1':
                print("The Perimeter Of The Parallelogram Is Equal To " + str(parallelogramtemp.find_perimeter()) + ".")
            elif parallelogrammenuinput == '2':
                print("The Area Of The Parallelogram Is Equal To " + str(parallelogramtemp.find_area()) + ".")
            elif parallelogrammenuinput == '3':
                continue
            elif parallelogrammenuinput == '4':
                break
        elif newshapemenuinput == '5':
            sidetopbottom = float(input("Enter Top/Bottom Side "))
            sideleftright = float(input("Enter Left/Right Side ")) 
            rectangletemp = rectangle_class(sidetopbottom, sideleftright)
            print("1. Find Perimeter")
            print("2. Find Area")
            print("3. Return To Main Menu")
            print("4. Quit Program")
            rectanglemenuinput = input("Please Enter Choice ")
            if rectanglemenuinput == '1':
                print("The Perimeter Of The Parallelogram Is Equal To " + str(rectangletemp.find_perimeter()) + ".")
            elif rectanglemenuinput == '2':
                print("The Area Of The Parallelogram Is Equal To " + str(rectangletemp.find_area()) + ".")
            elif rectanglemenuinput == '3':
                continue
            elif rectanglemenuinput == '4':
                break
        elif newshapemenuinput == '6':
            sides = float(input("Enter Sides "))
            angletopbottom = float(input("Enter Top/Bottom Angle ")) 
            angleleftright = float(input("Enter Left/Right Angle ")) 
            rhombustemp = rhombus_class(sides, angletopbottom, angleleftright)
            print("1. Find Perimeter")
            print("2. Find Area")
            print("3. Return To Main Menu")
            print("4. Quit Program")
            rhombusmenuinput = input("Please Enter Choice ")
            if rhombusmenuinput == '1':
                print("The Perimeter Of The Parallelogram Is Equal To " + str(rhombustemp.find_perimeter()) + ".")
            elif rhombusmenuinput == '2':
                print("The Area Of The Parallelogram Is Equal To " + str(rhombustemp.find_area()) + ".")
            elif rhombusmenuinput == '3':
                continue
            elif rhombusmenuinput == '4':
                break
        elif newshapemenuinput == '7':
            sides = float(input("Enter Sides "))
            squaretemp = square_class(sides)
            print("1. Find Perimeter")
            print("2. Find Area")
            print("3. Return To Main Menu")
            print("4. Quit Program")
            squaremenuinput = input("Please Enter Choice ")
            if squaremenuinput == '1':
                print("The Perimeter Of The Parallelogram Is Equal To " + str(squaretemp.find_perimeter()) + ".")
            elif squaremenuinput == '2':
                print("The Area Of The Parallelogram Is Equal To " + str(squaretemp.find_area()) + ".")
            elif squaremenuinput == '3':
                continue
            elif squaremenuinput == '4':
                break
        elif newshapemenuinput == '8':
            continue
        elif newshapemenuinput == '9':
            break
    elif mainmenuinput == '2':
        break
"""
