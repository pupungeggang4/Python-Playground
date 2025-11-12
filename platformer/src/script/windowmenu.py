import pygame, sys

from script.ui import *
from script.res import *

from script.window import *

class WindowMenu(Window):
    def __init__(self, game):
        super().__init__(game)

    def render_static(self, game):
        self.surface_static.fill(Color.transparent)
        pygame.draw.rect(self.surface_static, Color.white, UI.Menu.rect)
        pygame.draw.rect(self.surface_static, Color.black, UI.Menu.rect, 2)
        self.surface_static.blit(Font.neodgm_32.render(game.locale['paused'], False, Color.black), UI.Menu.text_paused)
        pygame.draw.rect(self.surface_static, Color.black, UI.Menu.button_resume, 2)
        self.surface_static.blit(Font.neodgm_32.render(game.locale['resume'], False, Color.black), UI.Menu.text_resume)
        pygame.draw.rect(self.surface_static, Color.black, UI.Menu.button_exit, 2)
        self.surface_static.blit(Font.neodgm_32.render(game.locale['exit'], False, Color.black), UI.Menu.text_exit)
        pygame.draw.rect(self.surface_static, Color.black, UI.Menu.button_quit, 2)
        self.surface_static.blit(Font.neodgm_32.render(game.locale['quit'], False, Color.black), UI.Menu.text_quit)

    def render(self, game):
        self.surface.fill(Color.transparent)
        self.surface.blit(self.surface_static, [0, 0])
        self.surface.blit(Image.arrow, UI.Menu.arrow[game.selected_menu])
        game.surface.blit(self.surface, [0, 0])
