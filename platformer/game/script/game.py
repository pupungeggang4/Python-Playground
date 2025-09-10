import pygame, sys
from script.res import *
from script.field import *
from script.fieldthing import *

import script.scenetitle as scenetitle
import script.scenefield as scenefield

class Game():
    def __init__(self):
        self.scene = 'title'
        self.state = ''
        self.menu = False
        self.screen = pygame.display.set_mode([1280, 720])
        pygame.display.set_caption('Platformer Game')

        self.fps = 60
        self.clock = pygame.time.Clock()
        self.load_image()
        self.load_font()

        self.field = Field()
        self.coin = Coin()

    def load_image(self):
        Image.Sprite.coin = pygame.image.load('image/spritecoin.png')

    def load_font(self):
        pygame.font.init()
        Font.neodgm_32 = pygame.font.Font('font/neodgm.ttf', 32)

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

            elif event.type == pygame.KEYDOWN:
                key = event.key
                if self.scene == 'title':
                    scenetitle.key_down(self, key)
                elif self.scene == 'field':
                    scenefield.key_down(self, key)

            elif event.type == pygame.KEYUP:
                key = event.key
                if self.scene == 'title':
                    scenetitle.key_up(self, key)
                elif self.scene == 'field':
                    scenefield.key_up(self, key)

    def handle_scene(self):
        if self.scene == 'title':
            scenetitle.loop(self)
        elif self.scene == 'field':
            scenefield.loop(self)
