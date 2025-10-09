import pygame, sys, ctypes
from OpenGL.GL import *

import script.scenetitle as scenetitle

class Game():
    def __init__(self):
        self.scene = 'title'
        self.state = ''
        self.menu = False

        self.resolution = [1280, 720]
        self.fps = 60
        self.scale = 1

        pygame.init()
        monitor = pygame.display.Info()
        if monitor.current_w > 2560:
            self.scale = 2
        if monitor.current_w > 2000:
            self.scale = 1.5
        self.window = pygame.display.set_mode([self.resolution[0] * self.scale, self.resolution[1] * self.scale], pygame.OPENGL)
        pygame.display.set_caption('Roguelike Game')
        self.surface = pygame.surface.Surface(self.resolution, pygame.SRCALPHA)
        self.clock = pygame.time.Clock()
        self.GL_init()

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
            self.render_GL()

    def handle_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    def handle_scene(self):
        if self.scene == 'title':
            scenetitle.loop(self)

    def render_GL(self):
        glClear(GL_COLOR_BUFFER_BIT)
        glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, self.resolution[0], self.resolution[1], 0, GL_RGBA, GL_UNSIGNED_BYTE, ctypes.c_void_p(self.surface._pixels_address))
        glVertexPointer(2, GL_FLOAT, 0, self.v_coord)
        glTexCoordPointer(2, GL_FLOAT, 0, self.t_coord)
        glEnableClientState(GL_TEXTURE_COORD_ARRAY)
        glEnableClientState(GL_VERTEX_ARRAY)
        glDrawArrays(GL_QUADS, 0, 4)
        glFlush()
