import pygame
 
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
 
pygame.init()
 
# Set the width and height of the screen [width, height]
size = (600, 400)
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("My Game")
 
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 
background_image = pygame.image.load("background_game1.jpg").convert()
player_image = pygame.image.load("player.png").convert()
player_image.set_colorkey(WHITE)
# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
 
    # --- Game logic should go here
    # Get the current mouse position. This returns the position
    # as a list of two numbers.
    player_position = pygame.mouse.get_pos()
    x = player_position[0]
    y = player_position[1]
 
    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.blit(background_image, [0,0])
    screen.blit(player_image, [x, y])
    # --- Drawing code should go here

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
 
# Close the window and quit.
pygame.quit()


