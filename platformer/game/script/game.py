import pygame, sys, ctypes
from OpenGL.GL import *
from OpenGL.GLU import *

import script.scenetitle as scenetitle

class Game():
    def __init__(self):
        self.scene = 'title'
        self.state = ''
        self.menu = False
        self.resolution = [1280, 720]

        self.screen = pygame.display.set_mode(self.resolution, pygame.OPENGL)
        self.surface = pygame.surface.Surface(self.resolution, pygame.SRCALPHA)
        self.fps = 60
        self.clock = pygame.time.Clock()

        glClearColor(0.0, 0.0, 1.0, 1.0)
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
            self.handle_input()
            self.handle_scene()

            glClear(GL_COLOR_BUFFER_BIT)
            glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, self.surface.width, self.surface.height, 0, GL_RGBA, GL_UNSIGNED_BYTE, ctypes.c_void_p(self.surface._pixels_address))
            glBegin(GL_QUADS)
            glTexCoord2f(0.0, 1.0)
            glVertex2f(-1.0, -1.0)
            glTexCoord2f(1.0, 1.0)
            glVertex2f(1.0, -1.0)
            glTexCoord2f(1.0, 0.0)
            glVertex2f(1.0, 1.0)
            glTexCoord2f(0.0, 0.0)
            glVertex2f(-1.0, 1.0)
            glEnd()

            pygame.display.flip()

    def handle_input(self):
        if self.scene == 'title':
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

    def handle_scene(self):
        if self.scene == 'title':
            scenetitle.loop(self)