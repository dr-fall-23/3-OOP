import math
import random
import pygame
from pygame import mixer

# CONSTANTS
PLAYER_IMG = pygame.image.load('player.png')
ALIEN_IMG = pygame.image.load('enemy.png')
LASER_IMG = pygame.Surface((4,20))
LASER_IMG.fill('white')
MIN_X = 0
MAX_X = 736
NUM_ALIENS = 6
LASER_RESET_Y = 380


class Player:
  pass

class PlayerLaser:
  pass

class Alien:
  pass


# Intialize the pygame
pygame.init()
screen = pygame.display.set_mode((800, 500)) # create the screen
pygame.display.set_caption("Space Invader") # Caption
clock = pygame.time.Clock()
# mixer.music.load("background.wav") # Sound
# mixer.music.play(-1)
score_font = pygame.font.Font('Pixeled.ttf', 32)
game_over_font = pygame.font.Font('Pixeled.ttf', 64)


def draw_game(screen):
  pass


running = True

# Game Loop
while running:
  clock.tick(30)
  screen.fill((0, 0, 0))

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
    if event.type == pygame.KEYDOWN:
      pass   
    if event.type == pygame.KEYUP:
      pass

  pygame.display.update()