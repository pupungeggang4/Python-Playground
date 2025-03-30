import module as m
import pygame, sys

class Game():
    screen = None
    resolution = [1280, 800]
    fps = 60
    clock = None

    scene = 'main'
    state = ''

    def __init__(self):
        pygame.init()
        pygame.font.init()
        self.screen = pygame.display.set_mode(self.resolution, pygame.SCALED)
        self.clock = pygame.time.Clock()

    def run(self):
        while True:
            self.clock.tick(self.fps)
            self.handle_input()
            self.handle_scene()

    def handle_scene(self):
        if self.scene == 'main':
            m.scenemain.loop()

    def handle_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

game = None