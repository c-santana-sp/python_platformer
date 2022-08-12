import pygame
from settings import *

class Level:

  def __init__(self):
    self.display_surface = pygame.display.get_surface()

    self.visible_sprites = pygame.sprite.Group()
    self.active_sprites = pygame.sprite.Group()
    self.collision_sprites = pygame.sprite.Group()

  def run(self):
    pass
