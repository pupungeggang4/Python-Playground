import pygame, sys, ctypes
from OpenGL.GL import *

from script.res import *
from script.locale import *
from script.village import *
from script.field import *

import script.scenetitle as scenetitle
import script.scenevillage as scenevillage
import script.scenebattle as scenebattle

class Game():
    def __init__(self):
        pygame.init()
        pygame.font.init()
        self.resolution = [1280, 720]
        self.fps = 60
        self.scale = 1.0
        self.hw_acceler = True
        self.surface = pygame.surface.Surface(self.resolution, pygame.SRCALPHA)
        self.clock = pygame.time.Clock()
        self.enable_hw_acceler()
        load_image()
        load_font()

        self.scene = 'title'
        self.state = ''
        self.state_click = ''
        self.menu = False
        self.lang = 0
        self.locale = Locale.data[Locale.lang_list[self.lang]]

        self.selected_title = 0
        self.selected_menu_village = 0
        self.selected_menu_battle = 0
        self.selected_battle_confirm = 0
        self.selected_adventure_start = 0

        self.field = Field()
        self.village = Village()
        self.key_pressed = {
            'up': False, 'left': False, 'down': False, 'right': False
        }

    def enable_hw_acceler(self):
        self.hw_acceler = True
        monitor = pygame.display.Info()
        if monitor.current_w > 2560:
            self.scale = 2
        if monitor.current_w > 2000:
            self.scale = 1.5
        self.window = pygame.display.set_mode([self.resolution[0] * self.scale, self.resolution[1] * self.scale], pygame.OPENGL | pygame.DOUBLEBUF, vsync=1)
        pygame.display.set_caption('Roguelike Game')
        self.GL_init()

    def disable_hw_acceler(self):
        self.hw_acceler = False
        self.scale = 1.0
        self.window = pygame.display.set_mode([self.resolution[0] * self.scale, self.resolution[1] * self.scale], pygame.SCALED, vsync=1)
        pygame.display.set_caption('Roguelike Game')

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
            if self.hw_acceler == True:
                self.render_GL()
            else:
                self.window.blit(self.surface)
            pygame.display.flip()

    def handle_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                key = event.key

                if key == pygame.K_w:
                    self.key_pressed['up'] = True
                if key == pygame.K_a:
                    self.key_pressed['left'] = True
                if key == pygame.K_s:
                    self.key_pressed['down'] = True
                if key == pygame.K_d:
                    self.key_pressed['right'] = True

                if self.scene == 'title':
                    scenetitle.key_down(self, key)
                elif self.scene == 'village':
                    scenevillage.key_down(self, key)
                elif self.scene == 'battle':
                    scenebattle.key_down(self, key)

            if event.type == pygame.KEYUP:
                key = event.key

                if key == pygame.K_w:
                    self.key_pressed['up'] = False
                if key == pygame.K_a:
                    self.key_pressed['left'] = False
                if key == pygame.K_s:
                    self.key_pressed['down'] = False
                if key == pygame.K_d:
                    self.key_pressed['right'] = False

            if event.type == pygame.MOUSEBUTTONUP:
                pos = list(pygame.mouse.get_pos())
                pos[0] /= self.scale
                pos[1] /= self.scale
                button = event.button

                if self.scene == 'title':
                    scenetitle.mouse_up(self, pos, button)
                elif self.scene == 'village':
                    scenevillage.mouse_up(self, pos, button)
                elif self.scene == 'battle':
                    scenebattle.mouse_up(self, pos, button)

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
