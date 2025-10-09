import pygame, sys, ctypes
from OpenGL.GL import *
from OpenGL.GLU import *

from script.res import *
import script.scenetitle as scenetitle
import script.scenegame as scenegame

class Game():
    def __init__(self):
        self.scene = 'title'
        self.state = ''
        self.menu = False
        self.resolution = [1280, 720]
        self.fps = 60
        self.t_coord = [0.0, 1.0, 1.0, 1.0, 1.0, 0.0, 0.0, 0.0]
        self.v_coord = [-1.0, -1.0, 1.0, -1.0, 1.0, 1.0, -1.0, 1.0]
        self.scale = 1

        pygame.init()
        monitor = pygame.display.Info()
        if monitor.current_w > 2560:
            self.scale = 2
        elif monitor.current_w > 2000:
            self.scale = 1.5
        self.screen = pygame.display.set_mode([self.resolution[0] * self.scale, self.resolution[1] * self.scale], pygame.OPENGL)
        pygame.display.set_caption('Platformer')
        self.surface = pygame.surface.Surface(self.resolution, pygame.SRCALPHA)
        self.clock = pygame.time.Clock()
        self.GL_init()
        self.load_font()

    def GL_init(self):
        glClearColor(0.0, 0.0, 0.0, 1.0)
        glEnable(GL_TEXTURE_2D)
        self.texture = glGenTextures(1)
        glBindTexture(GL_TEXTURE_2D, self.texture)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)

    def load_font(self):
        pygame.font.init()
        Font.neodgm_32 = pygame.font.Font('font/neodgm.ttf', 32)

    def run(self):
        while True:
            self.clock.tick(self.fps)
            self.handle_input()
            self.handle_scene()
            self.render_window()

    def handle_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.MOUSEBUTTONUP:
                mouse_pos = pygame.mouse.get_pos()
                button = event.button
                pos = [int(mouse_pos[0] / self.scale), int(mouse_pos[1] / self.scale)]

                if self.scene == 'title':
                    scenetitle.mouse_up(self, pos, button)
                elif self.scene == 'game':
                    scenegame.mouse_up(self, pos, button)

            elif event.type == pygame.KEYDOWN:
                key = event.key
                if self.scene == 'title':
                    scenetitle.key_down(self, key)
                elif self.scene == 'game':
                    scenegame.key_down(self, key)

            elif event.type == pygame.KEYUP:
                key = event.key
                if self.scene == 'title':
                    scenetitle.key_up(self, key)
                elif self.scene == 'game':
                    scenegame.key_up(self, key)

    def handle_scene(self):
        if self.scene == 'title':
            scenetitle.loop(self)
        elif self.scene == 'game':
            scenegame.loop(self)

    def render_window(self):
        glClear(GL_COLOR_BUFFER_BIT)
        glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, self.resolution[0], self.resolution[1], 0, GL_RGBA, GL_UNSIGNED_BYTE, ctypes.c_void_p(self.surface._pixels_address))
        glVertexPointer(2, GL_FLOAT, 0, self.v_coord)
        glTexCoordPointer(2, GL_FLOAT, 0, self.t_coord)
        glEnableClientState(GL_VERTEX_ARRAY)
        glEnableClientState(GL_TEXTURE_COORD_ARRAY)
        glDrawArrays(GL_QUADS, 0, 4)
        glFlush()
