import pygame

# Define Some Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)


pygame.init()

# Set The Height And Width Of The Screen
size = [800, 800]
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Lame TimePRO9000")

# Loop Until The User Clicks The Close Button
done = False

# Used To Manage How Fast The Screen Updates
clock = pygame.time.Clock()

font = pygame.font.Font('freesansbold.ttf', 100)

frame_count = 0
frame_rate = 60
start_time = 90

# -------- Main Program Loop --------
while not done:
    for event in pygame.event.get(): # User Did Something
        if event.type == pygame.QUIT: # If User Clicked Close
            done = True # Flag That We Are Done So We Exit This Loop

    # Set The Screen Background
    screen.fill((255, 99, 71))

    # ALL CODE TO DRAW SHOULD GO BELOW THIS COMMENT

    # --- Timer Going Up ---
    # Calculate Total Seconds
    total_seconds = frame_count // frame_rate

    # Divide By 60 To Get Total Minutes
    minutes = total_seconds // 60

    # Use Modulus (Remainder) To Get Seconds
    seconds = total_seconds % 60

    # Use Python String Formatting To Format In Leading Zeros
    output_string1 = "LAME"
    output_string2 = "{0:02}:{1:02}".format(minutes, seconds)
    # Blit To The Screen
    text = font.render(output_string1, True, (30, 144, 255))
    screen.blit(text, [10, 10])
    text = font.render(output_string2, True, (255, 255, 0))
    screen.blit(text, [520, 700])
    ''' TIME LEFT CODE?
    # --- Timer Going Down ---
    # --- Timer Going Up ---
    # Calculate Total Seconds
    total_seconds = start_time - (frame_count // frame_rate)
    if total_seconds < 0:
        total_seconds = 0

    # Divide By 60 To Get Total Minutes
    minutes = total_seconds // 60

    # Use Modulus (Remainder) To Get Seconds
    seconds = total_seconds % 60

    # Use Python String Formatting To Format In Leading Zeros
    output_string = "Time left: {0:02}:{1:02}".format(minutes, seconds)

    # Blit To The Screen
    text = font.render(output_string, True, WHITE)
    screen.blit(text, [350, 425])
    '''

    # ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT
    frame_count += 1

    # Limit Frames Per Second
    clock.tick(frame_rate)

    # Go Ahead And Update The Screen With What We've Drawn
    pygame.display.flip()

# Be IDLE Friendly. If You Forget This Line, The Program Will 'Hang' On Exit!
pygame.quit()
