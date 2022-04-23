import random
import pygame
 
# Global constants
 
# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (50, 50, 255)
GREEN = (0,172,32)
GRAY = (175,175,175)

ms = 2
#the global move speed

# Screen dimensions
SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 720

PlayerImgR = pygame.image.load("Photos/PlayerR.png")
PlayerImgD = pygame.image.load("Photos/PlayerD.png")
PlayerImgL = pygame.image.load("Photos/PlayerL.png")
PlayerImgU = pygame.image.load("Photos/PlayerU.png")

 
class Player(pygame.sprite.Sprite):
 
    # Constructor function
    def __init__(self, x, y):
        # Call the parent's constructor
        super().__init__()
 
        # Set height, width
        
        self.image = PlayerImgR
 
        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x
 
        # Set speed vector
        self.change_x = 0
        self.change_y = 0
        self.walls = None
 
    def changespeed(self, x, y):
        self.change_x += x
        self.change_y += y
 
    def update(self):
        # Move left/right
        self.rect.x += self.change_x
 
        # Did this update cause us to hit a wall?
        block_hit_list = pygame.sprite.spritecollide(self, self.walls, False)
        for block in block_hit_list:
            # If we are moving right, set our right side to the left side of
            # the item we hit
            if self.change_x > 0:
                self.rect.right = block.rect.left
            else:
                # Otherwise if we are moving left, do the opposite.
                self.rect.left = block.rect.right
 
        # Move up/down
        self.rect.y += self.change_y
 
        # Check and see if we hit anything
        block_hit_list = pygame.sprite.spritecollide(self, self.walls, False)
        for block in block_hit_list:
 
            # Reset our position based on the top/bottom of the object.
            if self.change_y > 0:
                self.rect.bottom = block.rect.top
            else:
                self.rect.top = block.rect.bottom

    def direction(self,dir):
      if dir == 'Right':
        self.image = PlayerImgR
      if dir == 'Left':
        self.image = PlayerImgL
      if dir == 'Up':
        self.image = PlayerImgU
      if dir == 'Down':
        self.image = PlayerImgD


 
 
class Wall(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        # Call the parent's constructor
        super().__init__()
 
        # Make a gray wall, of the size specified in the parameters
        self.image = pygame.Surface([width, height])
        self.image.fill(GRAY)
 
        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x
 
 
# Call this function so the Pygame library can initialize itself
pygame.init()
 
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
 
# Set the title of the window
pygame.display.set_caption('MyAdventure')
 
# List to hold all the sprites
all_sprite_list = pygame.sprite.Group()
 
# Make the walls. (x_pos, y_pos, width, height)
wall_list = pygame.sprite.Group()
 
wall = Wall(0, 0, 10, 720)
wall_list.add(wall)
all_sprite_list.add(wall)
 
wall = Wall(10, 0, 1080, 10)
wall_list.add(wall)
all_sprite_list.add(wall)
 
wall = Wall(10, 200, 200, 10)
wall_list.add(wall)
all_sprite_list.add(wall)

wall = Wall(150,0,10,150)
wall_list.add(wall)
all_sprite_list.add(wall)

wall = Wall(1014,10,10,720)
wall_list.add(wall)
all_sprite_list.add(wall)
 
# Create the player object
player = Player(32, 32)
player.walls = wall_list
 
all_sprite_list.add(player)

clock = pygame.time.Clock()
 
done = False
 
while not done:
 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
 
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.changespeed(-ms, 0)
                player.direction('Left')
            elif event.key == pygame.K_RIGHT:
                player.changespeed(ms, 0)
                player.direction('Right')
            elif event.key == pygame.K_UP:
                player.changespeed(0, -ms)
                player.direction('Up')
            elif event.key == pygame.K_DOWN:
                player.changespeed(0, ms)
                player.direction('Down')
 
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                player.changespeed(ms, 0)
            elif event.key == pygame.K_RIGHT:
                player.changespeed(-ms, 0)
            elif event.key == pygame.K_UP:
                player.changespeed(0, ms)
            elif event.key == pygame.K_DOWN:
                player.changespeed(0, -ms)
 
    all_sprite_list.update()

    screen.fill(GREEN)
 
    all_sprite_list.draw(screen)
 
    pygame.display.flip()
 
    clock.tick(60)
 
pygame.quit()