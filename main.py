# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from pygame import Color

from constants import *

def main():
  pygame.init()
  screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
  while True:
    color = (0, 0, 0)
    screen.fill(color)
    pygame.display.flip()

    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        return

if __name__ == "__main__":
  main()