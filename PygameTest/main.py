import pygame
import sys

class Var():
    screen = None

def init():
    pygame.init()
    Var.screen = pygame.display.set_mode((1280, 800), pygame.SCALED)
    pygame.display.set_caption("Test")

def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

if __name__ == '__main__':
    init()
    main()