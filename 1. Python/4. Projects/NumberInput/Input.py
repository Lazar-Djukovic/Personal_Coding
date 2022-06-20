import pygame

file = open('numbers.txt', 'w')

pygame.init()
 
font = pygame.font.SysFont("Verdana",25)

white = (255,255,255)
black = (0,0,0)
red = (200,0,0)
light_red = (255,0,0)
green = (0,155,0)
light_green = (0,255,0)
yellow = (200,200,0)
light_yellow = (255,255,0)

size = (700, 500)
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("My Game")
 
done = False

clock = pygame.time.Clock()
 

class button():
  
  def __init__(self,msg,color,x,y,font):
     self.msg = msg
     self.color = color
     self.buttonx = x 
     self.buttony = y
     self.width = 50
     self.height = 30
     self.font = font
    
  def draw(self):




while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
 




    screen.fill(white)

    pygame.display.flip()

    clock.tick(60)
 
pygame.quit()

