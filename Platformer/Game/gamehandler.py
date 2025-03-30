import pygame, sys

class Game():
    screen = None
    resolution = [1280, 800]
    fps = 60
    clock = None

    def __init__(self):
        pygame.init()
        pygame.font.init()
        self.screen = pygame.display.set_mode(self.resolution, pygame.SCALED)
        self.clock = 

    def handle_loop(self):
        pass

    def handle_input(self):
        pass

if __name__ == '__main__':
    pass