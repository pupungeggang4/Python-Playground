import pygame, sys

from script.scenetitle import *

from script.ui import *
from script.res import *
from script.render import *

class SceneBattle():
    def __init__(self, game):
        self.surface = pygame.surface.Surface(game.resolution, pygame.SRCALPHA)
        self.surface_menu = pygame.surface.Surface(game.resolution, pygame.SRCALPHA)
        self.surface_window = pygame.surface.Surface(game.resolution, pygame.SRCALPHA)

        Render.render_menu(self.surface_menu, game)
        self.render_static()

    def render_static(self):
        pygame.draw.rect(self.surface, Color.black, UI.Battle.button_menu, 2)

    def loop(self, game):
        self.render(game)

    def render(self, game):
        game.surface.fill(Color.white)
        game.surface.blit(self.surface)

        if game.menu == True:
            game.surface.blit(self.surface_menu, [0, 0])

    def mouse_up(self, game, pos, button):
        if button == 1:
            if game.menu == False:
                if point_inside_rect_ui(pos, UI.Battle.button_menu):
                    game.menu = True
            elif game.menu == True:
                if point_inside_rect_ui(pos, UI.Battle.button_menu) or point_inside_rect_ui(pos, UI.Menu.button_resume):
                    game.menu = False

