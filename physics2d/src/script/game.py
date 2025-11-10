import pygame, sys, ctypes, json

from script.res import *
from script.field import *

from script.level import *
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
        self.surface = pygame.surface.Surface(self.resolution, pygame.SRCALPHA)
        load_image()
        load_font()

        self.key_pressed = {'left': False, 'right': False, 'up': False}
        self.key_mapping = {'left': pygame.K_a, 'right': pygame.K_d, 'up': pygame.K_w}
        self.scene = 'main'

        self.field = Field()
        self.level_data = json.loads(open('data/level.json', 'r').read())
        Level.load_level(self, self.level_data['2'])

    def run(self):
        while True:
            self.clock.tick(self.fps)
            self.handle_input()
            self.handle_scene()
            self.window.blit(self.surface, [0, 0])
            pygame.display.flip()

    def handle_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                key = event.key
                for k in self.key_pressed:
                    if key == self.key_mapping[k]:
                        self.key_pressed[k] = True
                if key == pygame.K_r:
                    Level.load_level(self, self.level_data['2'])
                if self.scene == 'main':
                    scenemain.key_down(self, key)

            if event.type == pygame.KEYUP:
                key = event.key
                for k in self.key_pressed:
                    if key == self.key_mapping[k]:
                        self.key_pressed[k] = False
                if self.scene == 'main':
                    scenemain.key_up(self, key)

    def handle_scene(self):
        if self.scene == 'main':
            scenemain.loop(self)