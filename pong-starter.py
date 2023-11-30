from typing import Any
import pygame
import time
import random
from pygame.locals import (
    K_UP, K_DOWN, K_LEFT, K_RIGHT, K_ESCAPE, QUIT, KEYDOWN, K_a, K_s, K_w, K_d
)

# These will come in handy!
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 900


# Player 1 uses up and down arrow keys
class Player1(pygame.sprite.Sprite):
    def __init__(self) -> None:
        super(Player1, self).__init__()
        self.surf = pygame.Surface()          # Input an (x, y) tuple to give it a width and height
        self.surf.fill()                      # Input an (R, G, B) tuple to give it a color
        self.rect = self.surf.get_rect()
        # Right now, Player1 spawns in at (0,0). Set the x and y values of self.rect to some other numbers to change this

    # Updates this player's position
    def update(self, pressed_keys):
        pass


# Player2 uses W and S keys
class Player2(Player1):
    def __init__(self) -> None:
        super().__init__()

    # Updates this player's position
    def update(self, pressed_keys):
        pass


class Ball(pygame.sprite.Sprite):
    def __init__(self) -> None:
        super().__init__()

    def update(self) -> None:
        pass


screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])     # (x, y)

# Create objects for player1, player2, and the ball here

all_sprites = pygame.sprite.Group()
players = pygame.sprite.Group()

# Add those objects to all_sprites and/or players, respectively


running = True
while running:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
        elif event.type == QUIT:
            running = False
    
    # Update positions
    pressed_keys = pygame.key.get_pressed()
    for player in players:
        player.update(pressed_keys)
    # Call update() on the ball here

    # Render
    screen.fill((0, 0, 0))
    # Use blit() to draw each sprite on the screen here
    pygame.display.flip()
