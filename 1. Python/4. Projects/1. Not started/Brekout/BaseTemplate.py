import pygame
 
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
 
pygame.init()
 
# Set the width and height of the screen [width, height]
size = (700, 500)
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("My Game")
 
player_image = pygame.image.load("paddle.png")


class Player(pygame.sprite.Sprite):

    def __init__(self):
 
        super().__init__()

        self.image = player_image

        # Set a referance to the image rect.
        self.rect = self.image.get_rect()
        self.change_x = 0
        self.change_y = 0
        self.rect_x = 200
        self.rect_y = 300

    def update(self):
      self.rect_x = self.rect_x + self.change_x

    def go_left(self):
        self.change_x = -6
 
    def go_right(self):
        self.change_x = 6


# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 
# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        player = Player()
        all_sprite_list = pygame.sprite.Group()
        all_sprite_list.add(player)

    # --- Game logic should go here
        if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player.go_left()
                if event.key == pygame.K_RIGHT:
                    player.go_right()
    # --- Screen-clearing code goes here
 
    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
 
    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(WHITE)
 
    # --- Drawing code should go here
    
    all_sprite_list.update()
    all_sprite_list.draw(screen)

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
 
# Close the window and quit.
pygame.quit()
