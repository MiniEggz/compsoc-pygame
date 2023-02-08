import sys

import pygame

from level import Level
from settings import *

# Pygame setup
pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
level = Level(level_map, screen)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill("black")
    # run loop controlled by this method
    level.run()

    # updates the display
    pygame.display.update()
    clock.tick(60)
