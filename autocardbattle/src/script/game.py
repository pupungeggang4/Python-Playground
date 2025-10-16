import pygame, sys, ctypes
from OpenGL.GL import *

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
        self.battle = Battle()
        self.adventure = Adventure()
        self.player = Player()

        self.scene = 'title'
        self.state = ''
        self.menu = False

        self.scale = 1

        pygame.init()
        pygame.font.init()
        monitor = pygame.display.Info()
        if monitor.current_w > 2560:
            self.scale = 2.0
        elif monitor.current_w > 2000:
            self.scale = 1.5
        self.resolution = [1280, 720]
        self.screen = pygame.display.set_mode([self.resolution[0] * self.scale, self.resolution[1] * self.scale], pygame.OPENGL | pygame.DOUBLEBUF, vsync=1)
        self.surface = pygame.surface.Surface(self.resolution)
        self.clock = pygame.time.Clock()
        self.fps = 60

        load_font()
        load_image()
        self.GL_Init()

    def GL_Init(self):
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
            self.handle_input()
            self.handle_scene()
            self.render_display()
            pygame.display.flip()

    def handle_input(self):
        for event in pygame.event.get():
            if event.type == pygame.WINDOWCLOSE:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONUP:
                mouse_pos = pygame.mouse.get_pos()
                button = event.button
                pos = [int(mouse_pos[0] / self.scale), int(mouse_pos[1] / self.scale)]

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

    def render_display(self):
        glClear(GL_COLOR_BUFFER_BIT)
        glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, self.resolution[0], self.resolution[1], 0, GL_BGRA, GL_UNSIGNED_BYTE, ctypes.c_void_p(self.surface._pixels_address))
        glVertexPointer(2, GL_FLOAT, 0, self.v_coord)
        glTexCoordPointer(2, GL_FLOAT, 0, self.t_coord)
        glEnableClientState(GL_VERTEX_ARRAY)
        glEnableClientState(GL_TEXTURE_COORD_ARRAY)
        glDrawArrays(GL_QUADS, 0, 4)
