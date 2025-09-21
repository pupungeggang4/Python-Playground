import pygame, sys

from script.res import *
import script.scenetitle as scenetitle
import script.sceneready as sceneready
import script.scenebattle as scenebattle
import script.scenecollection as scenecollection

class Game():
    def __init__(self):
        pygame.init()
        
        self.scene = 'title'
        self.state = ''
        self.menu = False

        self.resolution = [1280, 720]
        self.screen = pygame.display.set_mode(self.resolution, pygame.SCALED)
        self.clock = pygame.time.Clock()
        self.fps = 60

        pygame.font.init()
        Font.neodgm_32 = pygame.font.Font('font/neodgm.ttf', 32)
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