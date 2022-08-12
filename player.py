import pygame
from settings import *

class Player(pygame.sprite.Sprite):

  def __init__(self, position, groups):
    super().__init__(groups)

    self.image = pygame.Surface((TILE_SIZE // 2, TILE_SIZE))
    self.image.fill(PLAYER_COLOR)    
    self.rect = self.image.get_rect(topleft = position)

    self.direction = pygame.math.Vector2()
    self.speed = PLAYER_SPEED

    self.gravity = GRAVITY_SPEED
    self.jump_speed = PLAYER_JUMP_SPEED
    
  def input(self):
    keys = pygame.key.get_pressed()

    if keys[pygame.K_RIGHT]:
      self.direction.x = 1
    elif keys[pygame.K_LEFT]:
      self.direction.x = -1
    else:
      self.direction.x = 0

    if keys[pygame.K_SPACE]:
      # print("jump")
      self.direction.y = -self.jump_speed

  def apply_gravity(self):
    self.direction.y += self.gravity
    self.rect.y += self.direction.y

  def update(self):
    self.input()
    self.rect.x += self.direction.x * self.speed

    self.apply_gravity()

