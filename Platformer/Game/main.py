import pygame
import sys

import var

def init():
    pygame.init()
    pygame.display.set_mode(var.resolution, pygame.SCALED, vsync = 1)
    pygame.display.set_caption('Platformer')
    var.clock = pygame.time.Clock()

def main():
    while True:
        var.clock.tick(var.FPS)
        handle_input()

def handle_input():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

if __name__ == '__main__':
    init()
    main()