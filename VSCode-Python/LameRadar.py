import pygame as pg
import math as mt

# Initialize Game Engine
pg.init()

pg.display.set_caption("Lame Radar")

# Define Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 99, 71)
BLUE = (30, 144, 255)
YELLOW = (255, 255, 0)

PI = 3.141592653

# Set Screen Height And Width
size = [850, 850]
screen = pg.display.set_mode(size)

clock = pg.time.Clock()

# Loop Until The User Clicks The Close Button
done = False

angle = 0

while not done:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            done = True

    # Set The Screen Background
    screen.fill(RED)
    font = pg.font.Font('freesansbold.ttf', 100)
    outputString = "LAME"
    text = font.render(outputString, True, BLUE)
    screen.blit(text, [15, 750])

    # Dimensions Of Radar Sweep
    # Start with the top left at (20, 20)
    # Width/height of 250
    box_dimensions = [125, 125, 600, 600]

    # Draw The Outline Of A Circle To 'Sweep' The Line Around
    pg.draw.ellipse(screen, YELLOW, box_dimensions, 2)

    # Draw A Box Around The Circle
    #pg.draw.rect(screen, BLUE, box_dimensions, 5)

    # Calculate The X, Y For The End Point Of Our 'Sweep' Based On The Current Angle
    x = 300 * mt.sin(angle) + 425
    y = 300 * mt.cos(angle) + 425

    # Draw The Line From The Center At 145, 145 To The Calculated End Spot
    pg.draw.line(screen, BLUE, [425, 425], [x, y], 2)

    # Increase The Angle By 0.03 Radians
    angle = angle + .03

    # If We Have Done A Full Sweep, Reset The Angle To 0
    if angle > 2 * PI:
        angle = angle - 2 * PI

    # Flip The Display, Wait Out The Clock Tick
    pg.display.flip()
    clock.tick(120)

# Be IDLE Friendly. If You Forget This Line, The Program Will 'Hang' On Exit!
pg.quit()
