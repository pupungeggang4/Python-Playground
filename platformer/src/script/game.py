import pygame, sys, ctypes
from OpenGL.GL import *

from script.res import *
from script.locale import *
from script.field import *
from script.player import *
import script.scenetitle as scenetitle

class Game():
    def __init__(self):
        pygame.init()
        load_image()
        self.load_font()
        
        self.hw_acceler = False
        self.scene = scenetitle.SceneTitle()
        self.state = ''
        self.menu = False
        self.lang = 'en'
        self.locale = Locale.data[self.lang]
        self.selected_title = 0
        self.selected_menu = 0

        self.key_pressed = {'up': False, 'left': False, 'down': False, 'right': False}

        self.field = Field()
        self.player = Player()

        self.monitor = pygame.display.Info()
        self.scale = 1
        self.resolution = [1280, 720]
        self.fps = 60
        self.clock = pygame.time.Clock()

        self.window = pygame.display.set_mode(self.resolution, pygame.SCALED, vsync=1)
        pygame.display.set_caption('Platformer Game')
        self.surface = pygame.surface.Surface(self.resolution, pygame.SRCALPHA)

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

    def enable_hw_acceler(self):
        self.hw_acceler = True
        if self.monitor.current_w > 2560:
            self.scale = 2
        elif self.monitor.current_w > 2000:
            self.scale = 1.5
        else:
            self.scale = 1
        self.window = pygame.display.set_mode([self.resolution[0] * self.scale, self.resolution[1] * self.scale], pygame.OPENGL | pygame.DOUBLEBUF, vsync=1)
        self.GL_init()

    def disable_hw_acceler(self):
        self.hw_acceler = False
        self.scale = 1
        self.window = pygame.display.set_mode(self.resolution, pygame.SCALED, vsync=1)

    def run(self):
        while True:
            self.clock.tick(self.fps)
            self.handle_input()
            self.handle_scene()
            
            if self.hw_acceler == True:
                self.GL_render()
            else:
                self.window.blit(self.surface, [0, 0])
            pygame.display.flip()

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

                self.scene.key_down(self, key)

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
        self.scene.loop(self)

    def GL_render(self):
        glClear(GL_COLOR_BUFFER_BIT)
        glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, self.resolution[0], self.resolution[1], 0, GL_BGRA, GL_UNSIGNED_BYTE, ctypes.c_void_p(self.surface._pixels_address))
        glVertexPointer(2, GL_FLOAT, 0, self.v_coord)
        glTexCoordPointer(2, GL_FLOAT, 0, self.t_coord)
        glEnableClientState(GL_VERTEX_ARRAY)
        glEnableClientState(GL_TEXTURE_COORD_ARRAY)
        glDrawArrays(GL_QUADS, 0, 4)
