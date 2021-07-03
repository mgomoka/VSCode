import pygame as pg

# Define Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 99, 71)
BLUE = (30, 144, 255)
YELLOW = (255, 255, 0)

def recursive_draw(x, y, width, height):
    """ Recursive Rectangle Function """
    pg.draw.rect(screen, BLUE, [x, y, width, height], 2)
    pg.draw.rect(screen, YELLOW, [x+2, y+2, width-4, height-4], 2)
    # Is The Rectangle Wide Enough To Draw Again?
    if(width > 14):
        # Scale Down
        x += width * .1
        y += height * .1
        width *= .8
        height *= .8
        # Recursively Draw Again
        recursive_draw(x, y, width, height)

pg.init()

# Set Screen Height And Width
size = [850, 850]
screen = pg.display.set_mode(size)

pg.display.set_caption("Lame Recursive Rectangle")

# Loop Until The User Clicks The Close Button
done = False

# Used To Manage How Fast The Screen Updates
clock = pg.time.Clock()

# -------- Main Program Loop --------
while not done:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            done = True

    # Set Screen Background
    screen.fill(RED)
    font = pg.font.Font('freesansbold.ttf', 50)
    outputString = "LAME"
    text = font.render(outputString, True, BLUE)
    screen.blit(text, [5, 800])
    # ALL CODE TO DRAW SHOULD GO BELOW THIS COMMENT
    recursive_draw(0, 0, 850, 850)
    # ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT

    # Go Ahead And Update The Screen With What We've Drawn
    pg.display.flip()
 
    # Limit Frames Per Second
    clock.tick(120)

# Be IDLE Friendly. If You Forget this line, the program will 'hang' on exit.
pg.quit()
