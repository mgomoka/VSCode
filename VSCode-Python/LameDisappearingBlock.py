import pygame as pg
import random

# Define Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 99, 71)
BLUE = (30, 144, 255)
YELLOW = (255, 255, 0)

class Block(pg.sprite.Sprite):
    """ This Class Represents The Ball. It Derives From The "Sprite" Class In pg. """
    def __init__(self, color, width, height):
        """ Constructor. Pass In The Color Of The Block And Its Size. """

        # Call The Parent Class (Sprite) Constructor
        super().__init__()

        # Create An Image Of The Block, And Fill It With A Color
        # This Could Also Be An Image Loaded From The Disk.
        self.image = pg.Surface([width, height])
        self.image.fill(color)
 
        # Fetch The Rectangle Object That Has The Dimensions Of The Image
        # Update The Position Of This Object By Setting The Values Of rect.x And rect.y
        self.rect = self.image.get_rect()

# Initialize Pygame
pg.init()

# Set Screen Height And Weight
screen_width = 850
screen_height = 850
screen = pg.display.set_mode([screen_width, screen_height])
pg.display.set_caption("Lame Disappearing Blocks")

# This Is A List Of 'Sprites.' Each Block In The Program Ss Added To This List. The List Is Managed By A Class Called 'Group.'
block_list = pg.sprite.Group()

# This Is A List Of Every Sprite. All Blocks And The Player Block As Well.
all_sprites_list = pg.sprite.Group()

for i in range(1000):
    # Represents A Block
    block = Block(BLUE, 25, 25)

    # Set A Random Location For The Block
    block.rect.x = random.randrange(screen_width-25)
    block.rect.y = random.randrange(screen_height-25)

    # Add The Block To The List Of Objects
    block_list.add(block)
    all_sprites_list.add(block)

# Create A Player Block
player = Block(YELLOW, 25, 25)
all_sprites_list.add(player)

# Loop Until The User Clicks The Close Button
done = False

# Used To Manage How Fast The Screen Updates
clock = pg.time.Clock()

score = 0

# -------- Main Program Loop --------
while not done:
    for event in pg.event.get(): 
        if event.type == pg.QUIT: 
            done = True

    # Fill Screen
    screen.fill(RED)

    # Get The Current Mouse Position. This Returns The Position As A List Of Two Numbers.
    pos = pg.mouse.get_pos()

    # Fetch The x And y Out Of The List, Just Like We'd Fetch Letters Out Of A String.
    # Set The Player Object To The Mouse Location
    player.rect.x = pos[0]
    player.rect.y = pos[1]

    # See If The Player Block Has Collided With Anything
    blocks_hit_list = pg.sprite.spritecollide(player, block_list, True)

    # Check The List Of Collisions
    for block in blocks_hit_list:
        score += 1
        print(score)

    # Draw All The Sprites
    all_sprites_list.draw(screen)

    # Go Ahead And Update The Screen With What We've Drawn
    pg.display.flip()
 
    # Limit Frames Per Second
    clock.tick(120)

pg.quit()
