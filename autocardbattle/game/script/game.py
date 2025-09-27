import pygame, sys

from script.res import *
from script.card import *
from script.adventure import *
from script.battle import *
import script.scenetitle as scenetitle
import script.sceneready as sceneready
import script.scenebattle as scenebattle
import script.scenecollection as scenecollection

class Game():
    def __init__(self):
        pygame.init()
        self.selected_character = -1
        self.card = Card()
        self.card.set_data(1)
        self.battle = Battle()
        self.adventure = Adventure()
        self.player = Player()

        self.scene = 'title'
        self.state = ''
        self.menu = False

        self.resolution = [1280, 720]
        self.screen = pygame.display.set_mode(self.resolution, pygame.SCALED | pygame.RESIZABLE)
        self.clock = pygame.time.Clock()
        self.fps = 60

        self.load_font()
        self.load_image()

    def load_font(self):
        pygame.font.init()
        Font.neodgm_32 = pygame.font.Font('font/neodgm.ttf', 32)
        Font.neodgm_16 = pygame.font.Font('font/neodgm.ttf', 16)

    def load_image(self):
        Image.test = pygame.image.load('image/test.png')

    def run(self):
        while True:
            self.clock.tick(self.fps)
            self.handle_input()
            self.handle_scene()

    def handle_input(self):
        for event in pygame.event.get():
            if event.type == pygame.WINDOWCLOSE:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                button = event.button

                if self.scene == 'title':
                    scenetitle.mouse_up(self, pos, button)
                elif self.scene == 'ready':
                    sceneready.mouse_up(self, pos, button)
                elif self.scene == 'battle':
                    scenebattle.mouse_up(self, pos, button)
                elif self.scene == 'collection':
                    scenecollection.mouse_up(self, pos, button)

    def handle_scene(self):
        if self.scene == 'title':
            scenetitle.loop(self)
        elif self.scene == 'ready':
            sceneready.loop(self)
        elif self.scene == 'battle':
            scenebattle.loop(self)
        elif self.scene == 'collection':
            scenecollection.loop(self)
