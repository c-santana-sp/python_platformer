import pygame
from settings import *
from tile import Tile
from player import Player

class Level:

  def __init__(self):
    self.display_surface = pygame.display.get_surface()

    self.visible_sprites = pygame.sprite.Group()
    self.active_sprites = pygame.sprite.Group()
    self.collision_sprites = pygame.sprite.Group()

    self.setup_level()

  def setup_level(self):
    for row_index, row in enumerate(LEVEL_MAP):
      # print(f'{row_index}:{row}-> y = {row_index * TILE_SIZE}')
      for column_index, column in enumerate(row):
        x = column_index * TILE_SIZE
        y = row_index * TILE_SIZE
        if column == 'X':
          Tile((x, y), [self.visible_sprites, self.collision_sprites])
        if column == 'P':
          Player((x, y), [self.visible_sprites, self.active_sprites], self.collision_sprites)

  def run(self):
    self.active_sprites.update()
    self.visible_sprites.draw(self.display_surface)
