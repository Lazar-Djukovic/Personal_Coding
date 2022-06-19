from re import X
from turtle import color
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
  
  def __init__(self,msg,color,x,y,w,h,size):
     self.msg = msg
     self.color = color
     self.buttonx = x 
     self.buttony = y

  def text_to_button(self,msg, color, buttonx,buttony,buttonw,buttonh, size ="small"):
    textSurf, textRect = self.text_objects(msg,color,size)
    textRect.center = ((buttonx+(buttonw/2), buttony + (buttonh/2)))
    screen.blit(textSurf, textRect)

  def text_objects(self,text,color,size):
    if size == "small":
      textSurface = smallfont.render(text,True,color)
    elif size == "medium":
      textSurface = medfont.render(text,True,color)
    elif size == "large":
      textSurface = largefont.render(text,True,color)

    return textSurface, textSurface.get_rect()

  def message_to_screen(self,msg,color, y_displace = 0, size = "small"):
  
    textSurf, textRect = text_objects(msg,color,size)
    textRect.center = (display_width/2), (display_height/2) + y_displace
    screen.blit(textSurf, textRect)


while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
 




    screen.fill(white)

    pygame.display.flip()

    clock.tick(60)
 
pygame.quit()

def button(text, x,y,w,h,inactive_color, active_color, action = None):
  cur = pygame.mouse.get_pos()
  click = pygame.mouse.get_pressed()

  if x + w > cur[0] > x and y + h > cur[1] > y:
    pygame.draw.rect(screen, active_color, (x,y,w,h))
    if click[0] == 1 and action != None:
      if action == "quit":
        pygame.quit()
        quit()

      if action == "controls":
        game_controls()

      if action == "play":
        gameLoop()

      if action == "menu":
        game_intro()