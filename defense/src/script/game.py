import pygame, sys
from OpenGL.GL import *
from script.res import *
from script.locale import *

import script.scenetitle as scenetitle

class Game():
    def __init__(self):
        pygame.init()
        self.load_font()
        self.scene = 'title'
        self.state = ''
        self.menu = False
        self.lang = 0
        self.locale = Locale.data[Locale.lang_list[self.lang]]

        self.monitor = pygame.display.Info()
        self.resolution = [1280, 720]
        self.scale = 1
        self.fps = 60
        self.clock = pygame.time.Clock()
        self.surface = pygame.surface.Surface(self.resolution)
        self.acceler = True
        self.enable_acceler()
        pygame.display.set_caption('Defense game')

    def load_font(self):
        pygame.font.init()
        Font.neodgm_32 = pygame.font.Font('font/neodgm.ttf', 32)

    def enable_acceler(self):
        self.acceler = True
        if self.monitor.current_w > 2560:
            self.scale = 2.0
        elif self.monitor.current_w > 2000:
            self.scale = 1.5
        else:
            self.scale = 1.0
        self.window = pygame.display.set_mode([self.resolution[0] * self.scale, self.resolution[1] * self.scale], pygame.OPENGL | pygame.DOUBLEBUF, vsync=1)
        self.load_GL()

    def disable_acceler(self):
        self.acceler = False
        self.scale = 1.0
        self.window = pygame.display.set_mode(self.resolution, pygame.SCALED, vsync=1)

    def load_GL(self):
        self.v_coord = [-1.0, -1.0, 1.0, -1.0, 1.0, 1.0, -1.0, 1.0]
        self.t_coord = [0.0, 1.0, 1.0, 1.0, 1.0, 0.0, 0.0, 0.0]
        glClearColor(0.0, 0.0, 0.0, 1.0)
        glEnable(GL_TEXTURE_2D)
        self.texture = glGenTextures(1)
        glBindTexture(GL_TEXTURE_2D, self.texture)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)

    def run(self):
        while True:
            self.clock.tick(self.fps)
            self.handle_scene()
            self.handle_input()
            if self.acceler == True:
                self.render_GL()
            else:
                self.window.blit(self.surface, [0, 0])
            pygame.display.flip()

    def handle_scene(self):
        if self.scene == 'title':
            scenetitle.loop(self)

    def handle_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONUP:
                pos = list(pygame.mouse.get_pos())
                pos[0] /= self.scale
                pos[1] /= self.scale
                button = event.button
                
                if self.scene == 'title':
                    scenetitle.mouse_up(self, pos, button)

    def render_GL(self):
        glClear(GL_COLOR_BUFFER_BIT)
        glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, self.resolution[0], self.resolution[1], 0, GL_BGRA, GL_UNSIGNED_BYTE, ctypes.c_void_p(self.surface._pixels_address))
        glVertexPointer(2, GL_FLOAT, 0, self.v_coord)
        glTexCoordPointer(2, GL_FLOAT, 0, self.t_coord)
        glEnableClientState(GL_VERTEX_ARRAY)
        glEnableClientState(GL_TEXTURE_COORD_ARRAY)
        glDrawArrays(GL_QUADS, 0, 4)