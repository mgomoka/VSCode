import pygame as pg
import random

# Define Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 99, 71)
BLUE = (30, 144, 255)
YELLOW = (255, 255, 0)

pg.init()

# Set Screen Height And Width
size = [850, 850]
screen = pg.display.set_mode(size)

pg.display.set_caption("Lame Bouncing Rectangle")

# Loop Until The User Clicks The Close Button
done = False

# Used To Manage How Fast The Screen Updates
clock = pg.time.Clock()

# Starting Position Of Rectangle
rect_x = random.randint(50,750)
rect_y = random.randint(50,750)

# Speed And Direction Of Rectangle
rect_change_x = 2
rect_change_y = 2

# -------- Main Program Loop --------
while not done:
    # --- Event Processing ---
    for event in pg.event.get():
        if event.type == pg.QUIT:
            done = True

    # --- Logic ---
    # Move The Rectangle Starting Point
    rect_x += rect_change_x
    rect_y += rect_change_y

    # Bounce The Ball If Needed
    if rect_y > 795 or rect_y < 5:
        rect_change_y = rect_change_y * -1
    if rect_x > 795 or rect_x < 5:
        rect_change_x = rect_change_x * -1

    # --- Drawing ---
    # Set The Screen Background
    screen.fill(RED)
    pg.draw.rect(screen, (0, 0, 0), [0, 0, 10, 850])
    pg.draw.rect(screen, (0, 0, 0), [0, 0, 850, 10])
    pg.draw.rect(screen, (0, 0, 0), [840, 0, 10, 850])
    pg.draw.rect(screen, (0, 0, 0), [0, 840, 850, 10])
    font = pg.font.Font('freesansbold.ttf', 100)
    outputString = "LAME"
    text = font.render(outputString, True, BLUE)
    screen.blit(text, [15, 750])

    # Draw The Rectangle
    #pg.draw.rect(screen, BLUE, [rect_x, rect_y, 50, 50])
    pg.draw.rect(screen, YELLOW, [rect_x + 5, rect_y + 5, 40, 40])

    # --- Wrap-up ---
    # Limit Frames Per Second
    clock.tick(120)

    # Go Ahead And Ppdate The Screen With What We've Drawn
    pg.display.flip()

# Close Everything Down
pg.quit()
