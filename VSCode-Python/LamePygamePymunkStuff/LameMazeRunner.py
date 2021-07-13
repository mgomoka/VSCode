"""
Sample Python/pg Programs
Simpson College Computer Science
http://programarcadegames.com/
http://simpson.edu/computer-science/

From: http://programarcadegames.com/python_examples/f.php?file=maze_runner.py

Explanation Video: http://youtu.be/5-SbFanyUkQ

Part Of A Series:
http://programarcadegames.com/python_examples/f.php?file=move_with_walls_example.py
http://programarcadegames.com/python_examples/f.php?file=maze_runner.py
http://programarcadegames.com/python_examples/f.php?file=platform_jumper.py
http://programarcadegames.com/python_examples/f.php?file=platform_scroller.py
http://programarcadegames.com/python_examples/f.php?file=platform_moving.py
http://programarcadegames.com/python_examples/sprite_sheets/
"""

import pygame as pg

# Define Colors
BLACK = (0, 0, 0)
WHITE = (245, 245, 220)
RED = (255, 99, 71)
BLUE = (30, 144, 255)
YELLOW = (255, 255, 0)



class Wall(pg.sprite.Sprite):
    """This Class Represents The Bar At The Bottom That The Player Controls """

    def __init__(self, x, y, width, height, color):
        """ Constructor Function """

        # Call The Parent's Constructor
        super().__init__()

        # Make A Wall, Of The Size Specified In The Parameters
        self.image = pg.Surface([width, height])
        self.image.fill(color)

        # Make Our Top-Left Corner The Passed-In Location
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x



class Player(pg.sprite.Sprite):
    """ This Class Represents The Bar At The Bottom That The Player Controls """

    # Set Speed Vector
    change_x = 0
    change_y = 0

    def __init__(self, x, y):
        """ Constructor Function """

        # Call The Parent's Constructor
        super().__init__()

        # Set Height And Width
        self.image = pg.Surface([15, 15])
        self.image.fill(YELLOW)

        # Make Our Top-Left Corner The Passed-In Location
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x

    def changespeed(self, x, y):
        """ Change The Speed Of The Player. Called With A Keypress. """
        self.change_x += x
        self.change_y += y

    def move(self, walls):
        """ Find A New Position For The Player """

        # Move Left/Right
        self.rect.x += self.change_x

        # Did This Update Cause Us To Hit A Wall?
        block_hit_list = pg.sprite.spritecollide(self, walls, False)
        for block in block_hit_list:
            # If We Are Moving Right, Set Our Right Side To The Left Side Of The Item We Hit
            if self.change_x > 0:
                self.rect.right = block.rect.left
            else:
                # Otherwise If We Are Moving Left, Do The Opposite
                self.rect.left = block.rect.right

        # Move Up/Down
        self.rect.y += self.change_y

        # Check And See If We Hit Anything
        block_hit_list = pg.sprite.spritecollide(self, walls, False)
        for block in block_hit_list:

            # Reset Our Position Based On The Top/Bottom Of The Object
            if self.change_y > 0:
                self.rect.bottom = block.rect.top
            else:
                self.rect.top = block.rect.bottom



class Room(object):
    """ Base Class For All Rooms """

    # Each Room Has A List Of Walls, And Of Enemy Sprites
    wall_list = None
    enemy_sprites = None

    def __init__(self):
        """ Constructor, Create Our Lists. """
        self.wall_list = pg.sprite.Group()
        self.enemy_sprites = pg.sprite.Group()



class Room1(Room):
    """ This Creates All The Walls In Room 1 """
    def __init__(self):
        super().__init__()
        # Make The Walls. (x_pos, y_pos, width, height)

        # This Is A List Of Walls. Each Is In The Form [x, y, width, height, color].
        walls = [[0, 0, 20, 250, RED],
                 [0, 350, 20, 250, RED],
                 [780, 0, 20, 250, RED],
                 [780, 350, 20, 250, RED],
                 [20, 0, 760, 20, RED],
                 [20, 580, 760, 20, RED],
                 [390, 50, 20, 500, BLUE]]

        # Loop Through The List. Create The Wall, Add It To The List.
        for item in walls:
            wall = Wall(item[0], item[1], item[2], item[3], item[4])
            self.wall_list.add(wall)



class Room2(Room):
    """This Creates All The Walls In Room 2 """
    def __init__(self):
        super().__init__()

        walls = [[0, 0, 20, 250, RED],
                 [0, 350, 20, 250, RED],
                 [780, 0, 20, 250, RED],
                 [780, 350, 20, 250, RED],
                 [20, 0, 760, 20, RED],
                 [20, 580, 760, 20, RED],
                 [190, 50, 20, 500, BLUE],
                 [590, 50, 20, 500, BLUE]]

        for item in walls:
            wall = Wall(item[0], item[1], item[2], item[3], item[4])
            self.wall_list.add(wall)



class Room3(Room):
    """This Creates All The Walls In Room 3 """
    def __init__(self):
        super().__init__()

        walls = [[0, 0, 20, 250, BLUE],
                 [0, 350, 20, 250, BLUE],
                 [780, 0, 20, 250, BLUE],
                 [780, 350, 20, 250, BLUE],
                 [20, 0, 760, 20, BLUE],
                 [20, 580, 760, 20, BLUE]]

        for item in walls:
            wall = Wall(item[0], item[1], item[2], item[3], item[4])
            self.wall_list.add(wall)

        for x in range(100, 800, 100):
            for y in range(50, 451, 300):
                wall = Wall(x, y, 20, 200, RED)
                self.wall_list.add(wall)

        for x in range(150, 700, 100):
            wall = Wall(x, 200, 20, 200, YELLOW)
            self.wall_list.add(wall)





def main():
    """ Main Program """

    # Call This Function So The PG Library Can Initialize Itself
    pg.init()

    # Create An 800x600 Sized Screen
    screen = pg.display.set_mode([800, 600])

    pg.display.set_caption('Maze Runner')

    # Create The Player Paddle Object
    player = Player(50, 50)
    movingsprites = pg.sprite.Group()
    movingsprites.add(player)

    rooms = []

    room = Room1()
    rooms.append(room)

    room = Room2()
    rooms.append(room)

    room = Room3()
    rooms.append(room)

    current_room_no = 0
    current_room = rooms[current_room_no]

    clock = pg.time.Clock()

    done = False

    while not done:

        # --- Event Processing ---

        for event in pg.event.get():
            if event.type == pg.QUIT:
                done = True

            if event.type == pg.KEYDOWN:
                if event.key == pg.K_LEFT:
                    player.changespeed(-5, 0)
                if event.key == pg.K_RIGHT:
                    player.changespeed(5, 0)
                if event.key == pg.K_UP:
                    player.changespeed(0, -5)
                if event.key == pg.K_DOWN:
                    player.changespeed(0, 5)

            if event.type == pg.KEYUP:
                if event.key == pg.K_LEFT:
                    player.changespeed(5, 0)
                if event.key == pg.K_RIGHT:
                    player.changespeed(-5, 0)
                if event.key == pg.K_UP:
                    player.changespeed(0, 5)
                if event.key == pg.K_DOWN:
                    player.changespeed(0, -5)

        # --- Game Logic ---

        player.move(current_room.wall_list)

        if player.rect.x < -15:
            if current_room_no == 0:
                current_room_no = 2
                current_room = rooms[current_room_no]
                player.rect.x = 790
            elif current_room_no == 2:
                current_room_no = 1
                current_room = rooms[current_room_no]
                player.rect.x = 790
            else:
                current_room_no = 0
                current_room = rooms[current_room_no]
                player.rect.x = 790

        if player.rect.x > 801:
            if current_room_no == 0:
                current_room_no = 1
                current_room = rooms[current_room_no]
                player.rect.x = 0
            elif current_room_no == 1:
                current_room_no = 2
                current_room = rooms[current_room_no]
                player.rect.x = 0
            else:
                current_room_no = 0
                current_room = rooms[current_room_no]
                player.rect.x = 0

        # --- Drawing ---
        screen.fill(WHITE)

        movingsprites.draw(screen)
        current_room.wall_list.draw(screen)
        font = pg.font.Font('freesansbold.ttf', 15)
        outputString = "LAME"
        text = font.render(outputString, True, YELLOW)
        screen.blit(text, [35, 583])

        pg.display.flip()

        clock.tick(60)

    pg.quit()

if __name__ == "__main__":
    main()
