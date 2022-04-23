import pygame 
import random
import math

# -- Global Constants 

############################################################################################

## -- Define the class snow which is a sprite 
class Invader(pygame.sprite.Sprite): 
 # Define the constructor for snow 
 def __init__(self, color, width, height, xpos, ypos, speed): 
 # Call the sprite constructor 
  super().__init__() 
 # Create a sprite and fill it with colour 
  self.ypos = ypos
  self.xpos = xpos
  self.speed = speed
  self.image = pygame.Surface([width,height]) 
  self.image.fill(color) 
 # Set the position of the sprite 
  self.rect = self.image.get_rect() 
  self.rect.x = self.xpos
  self.rect.y = self.ypos
  self.counter = 0

 def update(self):
    self.rect.x = self.rect.x + self.speed
    self.counter += 10
    if self.counter > 200:
      self.counter = 0

class Bullet(pygame.sprite.Sprite):
  #the constructor
  def __init__(self, color, speed, posx, posy):
  #sall the sprite constructor
    super().__init__()
    self.speed = speed
    self.image = pygame.Surface([3,6])
    self.image.fill(color)
    #the position of the sprite
    self.rect = self.image.get_rect()
    self.rect.x = posx + 6
    self.rect.y = posy
  
  def update(self):
    self.rect.y = self.rect.y - self.speed

class Player(pygame.sprite.Sprite):
   #the constructor
   def __init__(self, color, width, height):
      # Call the sprite constructor 
      super().__init__() 
   # Create a sprite and fill it with colour 
      self.score = 0
      self.speedx = 0
      self.speedy = 0
      self.image = pygame.Surface([width,height]) 
      self.image.fill(color) 
      # Set the position of the sprite 
      self.rect = self.image.get_rect() 
      self.rect.x = 300
      self.rect.y = 420

   def update(self):
      self.rect.x = self.rect.x + self.speedx
      self.rect.y = self.rect.y + self.speedy

   def player_set_speedx(self, speedx):
       self.speedx = speedx

   def player_set_speedy(self,speedy):
       self.speedy = speedy


 #End Procedure
#End Class

############################################################################################

# -- Colours 
BLACK = (0,0,0) 
WHITE = (255,255,255) 
BLUE = (50,50,255) 
YELLOW = (255,255,0) 
RED = (255, 50, 50)
GREEN = (0,154,23)

# -- Initialise PyGame
pygame.init() 

# -- Blank Screen 
size = (640,480) 
screen = pygame.display.set_mode(size) 

# -- Title of new window/screen 
pygame.display.set_caption("My Window") 

# -- Exit game flag set to false 
done = False

############################################################################################

# Create a list of the snow blocks 
invader_group = pygame.sprite.Group()
# Create a list of all sprites 
all_sprites_group = pygame.sprite.Group() 
# List of bullets
bullet_group = pygame.sprite.Group()

# Create the invaders 
myinvader = Invader(BLUE, 20, 20, (random.randint(40,640)), 30, 3) # invaders are white with size 5 by 5 px
invader_group.add (myinvader) # adds the new invader to the group of inavders
all_sprites_group.add (myinvader) # adds it to the group of all Sprites

#Next x
theplayer = Player(RED, 15, 25)
all_sprites_group.add (theplayer)

#defining the bullet so that the colision detection works, as the bullet is not created untill the up arrow is pressed
thebullet = Bullet(YELLOW, 5, theplayer.rect.x, theplayer.rect.y)
bullet_group.add(thebullet)
bullet_group.remove(thebullet)

# -- Manages how fast screen refreshes 
clock = pygame.time.Clock() 

############################################################################################

### -- Game Loop 
while not done: 
 # -- User input and controls 
 for event in pygame.event.get(): 
   if event.type == pygame.QUIT: 
         done = True 
#End If
 #Next event

#movement
# -- User inputs here 
   elif event.type == pygame.KEYDOWN: # - a key is down 
      if event.key == pygame.K_LEFT: # - if the left key pressed
        theplayer.player_set_speedx(-3) # speed set to -3
      elif event.key == pygame.K_RIGHT: # - if the right key pressed
        theplayer.player_set_speedx(3) # speed set to 3
      elif event.key == pygame.K_UP:
        theplayer.player_set_speedy(-3)
      elif event.key == pygame.K_DOWN:
        theplayer.player_set_speedy(3)
      #endif
   elif event.type == pygame.KEYUP: # - a key released 
     if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_UP or event.key == pygame.K_DOWN: 
      theplayer.player_set_speedx(0) # speed set to 0
      theplayer.player_set_speedy(0)
   #endif
 # -- Game logic goes after this comment
 if myinvader.counter > (random.randint(40,150)):
    thebullet = Bullet(YELLOW, -7, myinvader.rect.x, myinvader.rect.y)
    bullet_group.add(thebullet)
    myinvader.counter = 0
  
 bullet_hit_group = pygame.sprite.spritecollide(theplayer, bullet_group, True)

 #-stopping the player and enemy going off screen
 if myinvader.rect.x < 0:
   myinvader.speed = myinvader.speed * (-1)
 if myinvader.rect.x > 625:
   myinvader.speed = myinvader.speed * (-1)

 if theplayer.rect.x < 0:
   theplayer.rect.x = 0 
 if theplayer.rect.x > 625: 
   theplayer.rect.x = 625
 if theplayer.rect.y < 0:
   theplayer.rect.y = 0 
 if theplayer.rect.y > 465: 
   theplayer.rect.y = 465
 #endif
 
 # -- when invader hits the player add 5 to score. 
 #theplayer_hit_group = pygame.sprite.spritecollide(theplayer, invader_group, False)

 #-update all sprites
 all_sprites_group.update() 
 bullet_group.update()
 #-
# -- Screen background is BLACK 
 screen.fill (GREEN) 
 # Blitting the text on screen
 font2 = pygame.font.SysFont('calibri', 32)
 #-

 # -- Draw here 
 all_sprites_group.draw(screen)
 bullet_group.draw(screen)
 # -- flip display to reveal new position of objects 
 pygame.display.flip()
 # - The clock ticks over 
 clock.tick(60) 

#End While - End of game loop 
pygame.quit()

############################################################################################