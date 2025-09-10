import pygame
import sys

class Game():
    screen = None
    resolution = [1280, 800]
    FPS = 60
    clock = None

def init():
    pygame.init()
    Game.screen = pygame.display.set_mode(Game.resolution)
    pygame.display.set_caption('Test')
    Game.clock = pygame.time.Clock()

def main():
    while True:
        Game.clock.tick(Game.FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

if __name__ == '__main__':
    init()
    main()
