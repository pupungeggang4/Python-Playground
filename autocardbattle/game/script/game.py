import pygame, pygame._sdl2, sys
import script.scenetitle as scenetitle
import script.sceneready as sceneready
import script.scenebattle as scenebattle

class Game():
    def __init__(self):
        self.scene = 'title'
        self.state = ''
        self.menu = False

        self.resolution = [1280, 720]
        self.window = pygame._sdl2.video.Window(title = "Auto Card Battle", size = self.resolution)
        #self.renderer = pygame._sdl2.video.Renderer.from_window(self.window)

    def run(self):
        while True:
            self.handle_input()
            self.handle_scene()

    def handle_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                if self.scene == 'title':
                    scenetitle.mouse_up(self, pos)
                elif self.scene == 'ready':
                    sceneready.mouse_up(self, pos)
                elif self.scene == 'battle':
                    scenebattle.mouse_up(self, pos)

    def handle_scene(self):
        if self.scene == 'title':
            scenetitle.loop(self)
        elif self.scene == 'ready':
            sceneready.loop(self)
        elif self.scene == 'battle':
            scenebattle.loop(self)