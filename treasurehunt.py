import pygame
import random
from pygame.locals import *
import time

# change background
def changeBackground(img):
  background = pygame.image.load(img)
  # set its size
  bg = pygame.transform.scale(background, (screen_width, screen_height))
  screen.blit(bg, (0, 0))

# initialize pygame
pygame.init()
pygame.display.set_caption("Treasure Hunt")
# set the width and height of the screen
screen_width = 900
screen_height = 700
screen = pygame.display.set_mode([screen_width, screen_height])

# player sprite for pirate
class Pirate(pygame.sprite.Sprite):
  def __init__(self):
    super().__init__()
    self.image = pygame.image.load("pirate.png").convert_alpha()
    self.image = pygame.transform.scale(self.image, (70, 100))
    self.rect = self.image.get_rect()


# stone sprite
class Stone(pygame.sprite.Sprite):
  def __init__(self, img):
    super().__init__()
    self.image = pygame.image.load(img).convert_alpha()
    self.image = pygame.transform.scale(self.image, (30, 30))
    self.rect = self.image.get_rect()

    
# soldier sprite
class Soldier(pygame.sprite.Sprite):
    def __init__(self):
      super().__init__()
      self.image = pygame.image.load("soldier.png").convert_alpha()
      self.image = pygame.transform.scale(self.image, (40, 40))
      self.rect = self.image.get_rect()


# list of stones for stone class
images = ["stone1.png", "stone2.png", "stone3.png"]

# createsprite groups
stone_list = pygame.sprite.Group()
allsprites = pygame.sprite.Group()
soldier_list = pygame.sprite.Group()

# create stone sprites
for i in range(100):
  stone = Stone(random.choice(images))
# set a random location for the stone
  stone.rect.x = random.randrange(screen_width)
  stone.rect.y = random.randrange(screen_height)
  # add to stone list
  stone_list.add(stone)
  allsprites.add(stone)

# create soldier
for i in range(20):
  soldier = Soldier()
# set a random location for the soldier
  soldier.rect.x = random.randrange(screen_width)
  soldier.rect.y = random.randrange(screen_height)
  # add to soldier list
  soldier_list.add(soldier)
  allsprites.add(soldier)


# create pirate
pirate = Pirate()
allsprites.add(pirate)


# initialise essential variables
WHITE = (255, 255, 255)
RED   = (255, 0, 0)

playing = True
score = 0
clock = pygame.time.Clock()
# start time
start_time = time.time()
myFont =  pygame.font.SysFont("Times New Roman", 20)
timingFont = pygame.font.SysFont("Times New Roman", 30)
text = myFont.render("Score ="+str(0),True,WHITE)


# --- main program loop ---
while playing:
  clock.tick(30)

  # quit the game
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      playing = False

  # check if time > 60 seconds
  timeElapsed = time.time() - start_time
  if timeElapsed >= 60:
    if score > 50:
      text=myFont.render("    Pirate loot successful    ",True,RED)
      changeBackground("winscreen.jpg")
    else:
      text=myFont.render("    Pirate loot successful    ",True,RED)
      changeBackground("losescreen.jpg")
    screen.blit(text, (250, 40))

  else:
    changeBackground("background.png")
    countDown = timingFont.render(str(60-int(timeElapsed)), True, RED)
    screen.blit(countDown, (800, 10))


    #move the glove as per key pressed
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]: # UP
        if pirate.rect.y> 0:     
              pirate.rect.y -= 5
    if keys[pygame.K_DOWN] : # DOWN
        if pirate.rect.y <630:
            pirate.rect.y += 5 
        
    if keys[pygame.K_LEFT] : # LEFT
        if pirate.rect.x> 0:    
            pirate.rect.x -= 5 
        
    if keys[pygame.K_RIGHT] : # RIGHT
        if pirate.rect.x <850:
            pirate.rect.x += 5  

    # See if stone and pirate has collided
    stone_hit_list = pygame.sprite.spritecollide(pirate, stone_list, True)
    soldier_hit_list=pygame.sprite.spritecollide(pirate, soldier_list, True)
     
    # Check the list of collisions.
    for stone in stone_hit_list:
      score += 1
      #print(score)
      text=myFont.render("Score ="+str(score),True,WHITE)
    for soldier in soldier_hit_list:
      score -= 5
      #print(score)
      text=myFont.render("Score ="+str(score),True,WHITE)

    # print the score on screen
    screen.blit(text,(730,80))

             
    # Draw all the spites
    allsprites.draw(screen)
     
        
    pygame.display.update()
     
        
pygame.quit()
