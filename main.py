from asyncio import events
import pygame, sys
from settings import *

pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Python Platformer')
clock = pygame.time.Clock()

while True:

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      sys.exit()
  
  window.fill(BG_COLOR)

  pygame.display.update()
  clock.tick(FPS)
