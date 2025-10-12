import pygame, sys, ctypes
from OpenGL.GL import *

from script.res import *
from script.locale import *
import script.scenetitle as scenetitle
import script.scenefield as scenefield

class Game():
    def __init__(self):
        pygame.init()
        self.scene = 'title'
        self.state = ''
        self.menu = False
        self.lang = 'en'
        self.locale = Locale.data[self.lang]
        self.selected_title = 0
        self.selected_menu = 0

        self.monitor = pygame.display.Info()
        self.scale = 1
        self.resolution = [1280, 720]
        self.fps = 60
        self.clock = pygame.time.Clock()

        if self.monitor.current_w > 2560:
            self.scale = 2
        elif self.monitor.current_w > 2000:
            self.scale = 1.5
        else:
            self.scale = 1

        self.window = pygame.display.set_mode([self.resolution[0] * self.scale, self.resolution[1] * self.scale], pygame.OPENGL)
        pygame.display.set_caption('Platformer Game')
        self.surface = pygame.surface.Surface(self.resolution, pygame.SRCALPHA)

        self.load_image()
        self.load_font()
        self.GL_init()

    def load_image(self):
        Image.arrow = pygame.image.load('image/arrow.png')

    def load_font(self):
        pygame.font.init()
        Font.neodgm_32 = pygame.font.Font('font/neodgm.ttf', 32)

    def GL_init(self):
        self.v_coord = [-1.0, -1.0, 1.0, -1.0, 1.0, 1.0, -1.0, 1.0]
        self.t_coord = [0.0, 1.0, 1.0, 1.0, 1.0, 0.0, 0.0, 0.0]
        self.texture = glGenTextures(1)
        glEnable(GL_TEXTURE_2D)
        glBindTexture(GL_TEXTURE_2D, self.texture)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
        glClearColor(0.0, 0.0, 0.0, 1.0)

    def run(self):
        while True:
            self.clock.tick(self.fps)
            self.handle_input()
            self.handle_scene()
            self.GL_render()

    def handle_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                key = event.key
                if self.scene == 'title':
                    scenetitle.key_down(self, key)
                elif self.scene == 'field':
                    scenefield.key_down(self, key)

    def handle_scene(self):
        if self.scene == 'title':
            scenetitle.loop(self)
        elif self.scene == 'field':
            scenefield.loop(self)

    def GL_render(self):
        glClear(GL_COLOR_BUFFER_BIT)
        glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, self.resolution[0], self.resolution[1], 0, GL_BGRA, GL_UNSIGNED_BYTE, ctypes.c_void_p(self.surface._pixels_address))
        glVertexPointer(2, GL_FLOAT, 0, self.v_coord)
        glTexCoordPointer(2, GL_FLOAT, 0, self.t_coord)
        glEnableClientState(GL_VERTEX_ARRAY)
        glEnableClientState(GL_TEXTURE_COORD_ARRAY)
        glDrawArrays(GL_QUADS, 0, 4)
        glFlush()
