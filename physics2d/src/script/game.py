import pygame, sys, ctypes

import script.scenemain as scenemain

class Game():
    def __init__(self):
        pygame.init()
        pygame.font.init()
        self.fps = 60
        self.clock = pygame.time.Clock()

        self.resolution = [1280, 720]
        self.window = pygame.display.set_mode(self.resolution, pygame.SCALED, vsync = 1)
        pygame.display.set_caption('platformer')
        self.scene = 'main'

    def run(self):
        while True:
            self.clock.tick(self.fps)
            self.handle_input()
            self.handle_scene()
            pygame.display.flip()

    def handle_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                key = event.key
                if self.scene == 'main':
                    scenemain.key_down(self, key)

            if event.type == pygame.KEYUP:
                key = event.key
                if self.scene == 'main':
                    scenemain.key_up(self, key)

    def handle_scene(self):
        if self.scene == 'main':
            scenemain.loop(self)