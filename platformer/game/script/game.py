import pygame, sys
from script.res import *

class Game():
    def __init__(self):
        self.scene = 'title'
        self.state = ''
        self.menu = False
        self.screen = pygame.display.set_mode([1280, 720])
        pygame.display.set_caption('Platformer Game')

        self.a = 0
        self.fps = 60
        self.clock = pygame.time.Clock()

    def run(self):
        while True:
            self.clock.tick(self.fps)
            self.handle_input()
            self.handle_scene()

    def handle_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    def handle_scene(self):
        self.screen.fill(Color.white)
        pygame.draw.rect(self.screen, Color.black, [self.a, self.a, 80, 80])
        self.a += 1
        print(self.clock.get_fps())
        pygame.display.flip()
