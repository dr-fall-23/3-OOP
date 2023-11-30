from typing import Any
import pygame
import time
import random
from pygame.locals import (
    K_UP, K_DOWN, K_LEFT, K_RIGHT, K_ESCAPE, QUIT, KEYDOWN, K_a, K_s, K_w, K_d
)

SCREEN_HEIGHT = 600
SCREEN_WIDTH = 900

screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])     # (x, y)

running = True
while running:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
        elif event.type == QUIT:
            running = False

    # Render
    screen.fill((0, 255, 255))
    pygame.display.flip()
