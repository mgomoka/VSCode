'''2D Simulation Of Free Fall With Obstacles'''

# Importing Modules
import pymunk as pm
import pygame as pg
import sys
import random

sideGravity = 0
downGravity = 200
fps = 120

def create_apple(space, pos):
    body = pm.Body(1, 100, body_type=pm.Body.DYNAMIC)
    #body.position = (400, 0)
    body.position = pos
    shape = pm.Circle(body, 8)
    space.add(body, shape)
    return shape

def draw_apples(apples):
    for apple in apples:
        pos_x = int(apple.body.position.x)
        pos_y = int(apple.body.position.y)
        pg.draw.circle(screen, (30, 144, 255), (pos_x, pos_y), 8)
        # 1/2 CODE TO ADD IMAGE OF APPLE BELOW (2 LINES):
        #apple_rect = apple_surface.get_rect(center = (pos_x,pos_y))
        #screen.blit(apple_surface, apple_rect)

def static_ball(space, pos):
    body = pm.Body(body_type=pm.Body.STATIC)
    body.position = pos
    shape = pm.Circle(body, 50)
    space.add(body, shape)
    return shape

def draw_static_ball(balls):
    for ball in balls:
        pos_x = int(ball.body.position.x)
        pos_y = int(ball.body.position.y)
        pg.draw.circle(screen, (255, 255, 0), (pos_x, pos_y), 50)

def draw_static_border():
    for x in range(0, 825, 25):
        pg.draw.rect(screen, (0, 0, 0), [x, 0, 25, 25])
        pg.draw.rect(screen, (0, 0, 0), [x, 825, 25, 25])
    for x in range(0, 850, 25):
        pg.draw.rect(screen, (0, 0, 0), [0, x, 25, 25])
        pg.draw.rect(screen, (0, 0, 0), [825, x, 25, 25])



pg.init() # Initiating Pygame
pg.font.init()
screen = pg.display.set_mode((850, 850)) # Creating The Display Surface
pg.display.set_caption('Lame Physics Simulation 1')
font = pg.font.Font('freesansbold.ttf', 20)
black = (0, 0, 0)
clock = pg.time.Clock() # Creating The Game Clock
space = pm.Space()
space.gravity = (sideGravity, downGravity)
bodyBorderOne = pm.Body(body_type=pm.Body.STATIC)
bodyBorderOne.position = (0, 425)
shapeBorderOne = pm.Poly.create_box(bodyBorderOne, (50, 850))
space.add(bodyBorderOne, shapeBorderOne)
bodyBorderTwo = pm.Body(body_type=pm.Body.STATIC)
bodyBorderTwo.position = (425, 0)
shapeBorderTwo = pm.Poly.create_box(bodyBorderTwo, (850, 50))
space.add(bodyBorderTwo, shapeBorderTwo)
bodyBorderThree = pm.Body(body_type=pm.Body.STATIC)
bodyBorderThree.position = (425, 850)
shapeBorderThree = pm.Poly.create_box(bodyBorderThree, (850, 50))
space.add(bodyBorderThree, shapeBorderThree)
bodyBorderFour = pm.Body(body_type=pm.Body.STATIC)
bodyBorderFour.position = (850, 425)
shapeBorderFour = pm.Poly.create_box(bodyBorderFour, (50, 850))
space.add(bodyBorderFour, shapeBorderFour)
# 2/2 CODE TO ADD IMAGE OF APPLE BELOW (1 LINE):
#apple_surface = pg.image.load('apple_red.png')
apples = []
#apples.append(create_apple(space))
balls = []
''' ADDS 5
balls.append(static_ball(space, (random.randint(50, 100), random.randint(50, 750))))
balls.append(static_ball(space, (random.randint(200, 250), random.randint(50, 750))))
balls.append(static_ball(space, (random.randint(350, 450), random.randint(50, 750))))
balls.append(static_ball(space, (random.randint(550, 600), random.randint(50, 750))))
balls.append(static_ball(space, (random.randint(700, 750), random.randint(50, 750))))
'''
''' ADDS 25
balls.append(static_ball(space, (random.randint(50, 100), random.randint(50, 100))))
balls.append(static_ball(space, (random.randint(200, 250), random.randint(50, 100))))
balls.append(static_ball(space, (random.randint(350, 450), random.randint(50, 100))))
balls.append(static_ball(space, (random.randint(550, 600), random.randint(50, 100))))
balls.append(static_ball(space, (random.randint(700, 750), random.randint(50, 100))))
balls.append(static_ball(space, (random.randint(50, 100), random.randint(200, 250))))
balls.append(static_ball(space, (random.randint(200, 250), random.randint(200, 250))))
balls.append(static_ball(space, (random.randint(350, 450), random.randint(200, 250))))
balls.append(static_ball(space, (random.randint(550, 600), random.randint(200, 250))))
balls.append(static_ball(space, (random.randint(700, 750), random.randint(200, 250))))
balls.append(static_ball(space, (random.randint(50, 100), random.randint(350, 450))))
balls.append(static_ball(space, (random.randint(200, 250), random.randint(350, 450))))
balls.append(static_ball(space, (random.randint(350, 450), random.randint(350, 450))))
balls.append(static_ball(space, (random.randint(550, 600), random.randint(350, 450))))
balls.append(static_ball(space, (random.randint(700, 750), random.randint(350, 450))))
balls.append(static_ball(space, (random.randint(50, 100), random.randint(550, 600))))
balls.append(static_ball(space, (random.randint(200, 250), random.randint(550, 600))))
balls.append(static_ball(space, (random.randint(350, 450), random.randint(550, 600))))
balls.append(static_ball(space, (random.randint(550, 600), random.randint(550, 600))))
balls.append(static_ball(space, (random.randint(700, 750), random.randint(550, 600))))
balls.append(static_ball(space, (random.randint(50, 100), random.randint(700, 750))))
balls.append(static_ball(space, (random.randint(200, 250), random.randint(700, 750))))
balls.append(static_ball(space, (random.randint(350, 450), random.randint(700, 750))))
balls.append(static_ball(space, (random.randint(550, 600), random.randint(700, 750))))
balls.append(static_ball(space, (random.randint(700, 750), random.randint(700, 750))))
'''
'''LOOP FOR ADDING 25'''
xCount = 1
yCount = 1
xRangeMin = 50 + 50
xRangeMax = 100 + 50
yRangeMin = 50 + 50
yRangeMax = 100 + 50
while xCount <= 5:
    while yCount<= 5:
        balls.append(static_ball(space, (random.randint(xRangeMin, xRangeMax), random.randint(yRangeMin, yRangeMax))))
        xRangeMin += 150
        xRangeMax += 150
        yCount += 1
    xRangeMin = 50 + 50
    xRangeMax = 100 + 50
    yRangeMin += 150
    yRangeMax += 150
    yCount = 1
    xCount += 1



while True: # Game Loop
    for event in pg.event.get(): # Cheaking For User Input
        if event.type == pg.QUIT: # Input To Close The Game
            pg.quit()
            sys.exit()
        if event.type == pg.MOUSEBUTTONDOWN:
            apples.append(create_apple(space, event.pos))

    screen.fill((255, 99, 71)) # Background Color
    draw_static_border()
    outputString = "LAME"
    text = font.render(outputString, True, (30, 144, 255))
    screen.blit(text, [50, 830])
    draw_apples(apples)
    draw_static_ball(balls)
    ''' Output Text
    output_string1 = "PHYSICS SIMULATOR"
    text = font.render(output_string1, True, (30, 144, 255))
    screen.blit(text, [10, 10])
    '''
    space.step(1/50)
    pg.display.update() # Rendering The Frame
    clock.tick(fps) # Limiting The Frames Per Second To 120
