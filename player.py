import pygame
from settings import *

class Player(pygame.sprite.Sprite):

  def __init__(self, position, groups, collision_sprites):
    super().__init__(groups)

    self.image = pygame.Surface((TILE_SIZE // 2, TILE_SIZE))
    self.image.fill(PLAYER_COLOR)    
    self.rect = self.image.get_rect(topleft = position)

    self.direction = pygame.math.Vector2()
    self.speed = PLAYER_SPEED

    self.gravity = GRAVITY_SPEED
    self.jump_speed = PLAYER_JUMP_SPEED

    self.collision_sprites = collision_sprites

  def input(self):
    keys = pygame.key.get_pressed()

    if keys[pygame.K_RIGHT]:
      self.direction.x = 1
    elif keys[pygame.K_LEFT]:
      self.direction.x = -1
    else:
      self.direction.x = 0

    if keys[pygame.K_SPACE]:
      self.direction.y = -self.jump_speed

  def horizontal_collisions(self):
    for sprite in self.collision_sprites.sprites():
      if sprite.rect.colliderect(self.rect):
        if self.direction.x < 0:
          self.rect.left = sprite.rect.right
        if self.direction.x > 0:
          self.rect.right = sprite.rect.left

  def vertical_collisions(self):
    pass

  def apply_gravity(self):
    self.direction.y += self.gravity
    self.rect.y += self.direction.y

  def update(self):
    self.input()
    self.rect.x += self.direction.x * self.speed

    self.horizontal_collisions()
    # self.vertical_collisions()

    self.apply_gravity()

