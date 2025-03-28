import m
import pygame, sys

game_i = None

class Game():
    screen = None
    resolution = [1280, 800]
    fps = 60
    clock = None

    scene = 'title'
    state = ''

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(self.resolution)
        pygame.display.set_caption('Dodge Game')
        self.clock = pygame.time.Clock()

    def game_loop(self):
        self.clock.tick(self.fps)
        self.handle_input()

    def handle_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()