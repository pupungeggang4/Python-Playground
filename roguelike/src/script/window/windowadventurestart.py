import pygame, sys

from script.ui import *
from script.res import *

from script.window.window import *

class WindowAdventureStart(Window):
    def __init__(self, game):
        super().__init__(game)

    def render_static(self, game):
        surface = self.surface_static
        pygame.draw.rect(surface, Color.white, UI.Window.rect)
        pygame.draw.rect(surface, Color.black, UI.Window.rect, 2)
        surface.blit(Font.neodgm_32.render(game.locale['select_weapon'], False, Color.black), UI.Window.text_title)

        for i in range(3):
            pygame.draw.rect(surface, Color.black, UI.Window.button_weapon[i], 2)

        pygame.draw.rect(surface, Color.black, UI.Window.button_ok, 2)
        surface.blit(Font.neodgm_32.render(game.locale['ok'], False, Color.black), UI.Window.text_ok)

    def render(self, game):
        self.surface.fill(Color.transparent)
        self.surface.blit(self.surface_static, [0, 0])
        self.surface.blit(Image.arrow_down, UI.Window.arrow_weapon[game.selected_adventure_start])
        game.surface.blit(self.surface, [0, 0])