import pygame
import sys

import var

def init():
    pygame.init()
    var.screen = pygame.display.set_mode(var.window_size, pygame.SCALED)
    pygame.display.set_caption('Card RTS')
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