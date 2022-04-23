import pygame
import random

#ep45 - score

#initializes the pygame module
pygame.init()

display_width = 800
display_height = 600

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Tanks')

#icon = pygame.image.load("Apple.png")
#pygame.display.set_icon(icon) # best size for this is 32x32
#img = pygame.image.load("SnakeHead.png")
#appleimg = pygame.image.load("Apple.png")

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,155,0)

clock = pygame.time.Clock()
fps = 15

block_size = 20
appleThic = 30

smallfont = pygame.font.SysFont("Verdana",25)
medfont = pygame.font.SysFont("Verdana",40)
largefont = pygame.font.SysFont("Verdana",65)

def pause():
  paused = True

  message_to_screen("Paused", black, -100, size = "large")
  message_to_screen("Press C to continue or Q to quit.", black, 25)
  pygame.display.update()

  while paused:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        quit()
      
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_c:
          paused = False

        if event.key == pygame.K_q:
          pygame.quit()
          quit()
    
    #gameDisplay.fill(white)

    clock.tick(5)

def score(score):
  text = smallfont.render("Score: " +str(score) ,True, black)
  gameDisplay.blit(text, [0,0])

def randAppleGen():
  randAppleX = round(random.randrange(0, display_width-appleThic))#/10.0)*10.0
  randAppleY = round(random.randrange(0, display_height-appleThic))#/10.0)*10.0

  return randAppleX,randAppleY

def game_intro():

  intro = True

  while intro:

    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        quit()
      
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_c:
          intro = False

        if event.key == pygame.K_q:
          pygame.quit()
          quit()

    gameDisplay.fill(white)
    message_to_screen("Welcome to Tanks!", green, -100, "large")
    message_to_screen("The objective is to shoot and destroy the ", black, -30)
    message_to_screen("enemy tank before they destroy you", black, 10)
    message_to_screen("Press C to play, P to pause or Q to quit", black, 100)

    pygame.display.update()
    clock.tick(5)

def text_objects(text, color,size):
  if size == "small":
    textSurface = smallfont.render(text,True,color)
  elif size == "medium":
    textSurface = medfont.render(text,True,color)
  elif size == "large":
    textSurface = largefont.render(text,True,color)

  return textSurface, textSurface.get_rect()

def message_to_screen(msg,color, y_displace = 0, size = "small"):
  #screen_text = font.render(msg, True, color)
  #gameDisplay.blit(screen_text, [display_width/3, display_height/2])
  textSurf, textRect = text_objects(msg,color,size)
  textRect.center = (display_width/2), (display_height/2) + y_displace
  gameDisplay.blit(textSurf, textRect)

def gameLoop():
  global direction
  #leader of the blocks for snake

  gameExit = False
  gameOver = False

  while not gameExit:

    if gameOver == True:
      message_to_screen("Game over", red, -50, size="large")
      message_to_screen("Press C to play again or Q to quit", black, 50, size="medium")
      pygame.display.update()

    while gameOver == True:
      #gameDisplay.fill(white)

      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          gameOver = False
          gameExit = True

        if event.type == pygame.KEYDOWN:
          if event.key == pygame.K_q:
            gameExit = True
            gameOver = False
          if event.key == pygame.K_c:
            gameLoop()

    #events part of loop
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        gameExit = True

      #any keydown
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            pass

        elif event.key == pygame.K_RIGHT:
          pass

        elif event.key == pygame.K_UP:
          pass

        elif event.key == pygame.K_DOWN:
          pass
        
        elif event.key == pygame.K_p:
          pause()

    gameDisplay.fill(white)
    pygame.display.update()
    clock.tick(fps)

  pygame.quit()
  quit()

game_intro()
gameLoop()