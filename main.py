import pygame, sys
from settings import *
from level import Level

pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Python Platformer')
clock = pygame.time.Clock()

level = Level()

while True:

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      sys.exit()
  
  window.fill(BG_COLOR)

  level.run()

  pygame.display.update()
  clock.tick(FPS)
