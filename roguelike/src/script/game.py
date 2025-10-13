import pygame, sys, ctypes
from OpenGL.GL import *

from script.res import *
from script.locale import *
from script.village import *

import script.scenetitle as scenetitle
import script.scenevillage as scenevillage
import script.scenebattle as scenebattle

class Game():
    def __init__(self):
        self.scene = 'title'
        self.state = ''
        self.menu = False
        self.lang = 'en'
        self.locale = Locale.data[self.lang]

        self.selected_title = 0

        self.resolution = [1280, 720]
        self.fps = 60
        self.scale = 1

        pygame.init()
        monitor = pygame.display.Info()
        if monitor.current_w > 2560:
            self.scale = 2
        if monitor.current_w > 2000:
            self.scale = 1.5
        self.surface = pygame.display.set_mode([self.resolution[0] * self.scale, self.resolution[1] * self.scale], pygame.OPENGL, vsync=1)
        pygame.display.set_caption('Roguelike Game')
        self.surface = pygame.surface.Surface(self.resolution, pygame.SRCALPHA)
        self.clock = pygame.time.Clock()

        self.load_image()
        self.load_font()
        self.GL_init()

        self.village = Village()
        self.key_pressed = {
            'up': False, 'left': False, 'down': False, 'right': False
        }

    def load_font(self):
        pygame.font.init()
        Font.neodgm_32 = pygame.font.Font('font/neodgm.ttf', 32)

    def load_image(self):
        Image.arrow = pygame.image.load('image/arrow.png').convert_alpha()
        Image.portal = pygame.image.load('image/portal.png').convert_alpha()

    def GL_init(self):
        glClearColor(0.0, 0.0, 0.0, 1.0)
        glEnable(GL_TEXTURE_2D)
        self.texture = glGenTextures(1)
        glBindTexture(GL_TEXTURE_2D, self.texture)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
        self.v_coord = [-1.0, -1.0, 1.0, -1.0, 1.0, 1.0, -1.0, 1.0]
        self.t_coord = [0.0, 1.0, 1.0, 1.0, 1.0, 0.0, 0.0, 0.0]

    def run(self):
        while True:
            self.clock.tick(self.fps)
            self.handle_input()
            self.handle_scene()
            #pygame.display.flip()
            self.render_GL()

    def handle_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                key = event.key

                if key == pygame.K_UP:
                    self.key_pressed['up'] = True
                if key == pygame.K_LEFT:
                    self.key_pressed['left'] = True
                if key == pygame.K_DOWN:
                    self.key_pressed['down'] = True
                if key == pygame.K_RIGHT:
                    self.key_pressed['right'] = True

                if self.scene == 'title':
                    scenetitle.key_down(self, key)
                elif self.scene == 'village':
                    scenevillage.key_down(self, key)
                elif self.scene == 'battle':
                    scenebattle.key_down(self, key)

            if event.type == pygame.KEYUP:
                key = event.key

                if key == pygame.K_UP:
                    self.key_pressed['up'] = False
                if key == pygame.K_LEFT:
                    self.key_pressed['left'] = False
                if key == pygame.K_DOWN:
                    self.key_pressed['down'] = False
                if key == pygame.K_RIGHT:
                    self.key_pressed['right'] = False

    def handle_scene(self):
        if self.scene == 'title':
            scenetitle.loop(self)
        elif self.scene == 'village':
            scenevillage.loop(self)
        elif self.scene == 'battle':
            scenebattle.loop(self)

    def render_GL(self):
        glClear(GL_COLOR_BUFFER_BIT)
        glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, self.resolution[0], self.resolution[1], 0, GL_BGRA, GL_UNSIGNED_BYTE, ctypes.c_void_p(self.surface._pixels_address))
        glVertexPointer(2, GL_FLOAT, 0, self.v_coord)
        glTexCoordPointer(2, GL_FLOAT, 0, self.t_coord)
        glEnableClientState(GL_TEXTURE_COORD_ARRAY)
        glEnableClientState(GL_VERTEX_ARRAY)
        glDrawArrays(GL_QUADS, 0, 4)
        glFlush()
