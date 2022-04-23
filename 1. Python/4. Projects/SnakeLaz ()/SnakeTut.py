from email import message
import pygame
import random

#ep38 - score

#initializes the pygame module
pygame.init()

display_width = 800
display_height = 600

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Snak e')

icon = pygame.image.load("Apple.png")
pygame.display.set_icon(icon) # best size for this is 32x32


img = pygame.image.load("SnakeHead.png")
appleimg = pygame.image.load("Apple.png")

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,155,0)

clock = pygame.time.Clock()
fps = 15

direction = "right"

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
    message_to_screen("Welcome to Snak e", green, -100, "large")
    message_to_screen("Eat apple to play", black, -30)
    message_to_screen("The more apples you eat the longer you get", black, 10)
    message_to_screen("Press C to play, P to pause or Q to quit", black, 100)

    pygame.display.update()
    clock.tick(5)

def snake(block_size,snakeList):

  if direction == "right":
    head = pygame.transform.rotate(img, 270)
  if direction == "left":
    head = pygame.transform.rotate(img, 90)
  if direction == "up":
    head = img
  if direction == "down":
    head = pygame.transform.rotate(img, 180)

  gameDisplay.blit(head, (snakeList[-1][0], snakeList[-1][1]))

  # :-1 everyhing up to the last element
  for XnY in snakeList [:-1]:
    pygame.draw.rect(gameDisplay, green, [XnY[0], XnY[1], block_size, block_size])

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
  direction = "right"
  lead_x = display_width/2
  lead_y = display_height/2

  lead_x_change = 10
  lead_y_change = 0

  snakeList = []
  snakeLenght = 1

  randAppleX, randAppleY = randAppleGen() 

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
            lead_x_change = -block_size
            lead_y_change = 0
            direction = "left"
        elif event.key == pygame.K_RIGHT:
          lead_x_change = block_size
          lead_y_change = 0
          direction = "right"

        elif event.key == pygame.K_UP:
          lead_y_change = -block_size
          lead_x_change = 0
          direction = "up"
        elif event.key == pygame.K_DOWN:
          lead_y_change = block_size
          lead_x_change = 0
          direction = "down"
        
        elif event.key == pygame.K_p:
          pause()


    if lead_x >= display_width or lead_x <= 0 or lead_y >= display_height or lead_y <= 0:
      gameOver = True

    lead_x += lead_x_change
    lead_y += lead_y_change

    gameDisplay.fill(white)

    #pygame.draw.rect(gameDisplay, red, [randAppleX,randAppleY, appleThic, appleThic])

    gameDisplay.blit(appleimg, (randAppleX, randAppleY))

    snakeHead = []
    snakeHead.append(lead_x)
    snakeHead.append(lead_y)
    snakeList.append(snakeHead)

    #deletes the element is the list is onger than lenght
    if len(snakeList) > snakeLenght:
      del snakeList[0]

    #Reference -1 referencing anything up to the last element (last one is head)
    for eachSegment in snakeList[:-1]:
      if eachSegment == snakeHead:
        gameOver = True

    #blit the snake
    snake(block_size,snakeList)

    #Blit the score
    score(snakeLenght -1)

    pygame.display.update()

    
    #if lead_x >= randAppleX and lead_x <= randAppleX + appleThic:
      #if lead_y >= randAppleY and lead_y <= randAppleY + appleThic:
        #randAppleX = round(random.randrange(0, display_width-appleThic))#/10.0)*10.0
        #randAppleY = round(random.randrange(0, display_height-appleThic))#/10.0)*10.0
        #snakeLenght += 1

    #collisions
    if lead_x > randAppleX and lead_x < randAppleX + appleThic or lead_x + appleThic > randAppleX and lead_x + appleThic < randAppleX + appleThic:

      if lead_y > randAppleY and lead_y < randAppleY + appleThic:
        randAppleX, randAppleY = randAppleGen() 
        snakeLenght += 1
      
      elif lead_y + appleThic > randAppleY and lead_y + appleThic < randAppleY + appleThic:
        randAppleX, randAppleY = randAppleGen() 
        snakeLenght += 1

    clock.tick(fps)

  pygame.quit()
  quit()

game_intro()
gameLoop()