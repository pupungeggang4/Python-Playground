import pygame, sys

from script.ui import *
from script.res import *

from script.window.window import *

class WindowMenuBattle(Window):
    def __init__(self, game):
        super().__init__(game)

    def render_static(self, game):
        surface = self.surface_static
        pygame.draw.rect(surface, Color.white, UI.Menu_Battle.rect)
        pygame.draw.rect(surface, Color.black, UI.Menu_Battle.rect, 2)
        surface.blit(Font.neodgm_32.render(game.locale['paused'], False, Color.black), UI.Menu_Battle.text_paused)
        pygame.draw.rect(surface, Color.black, UI.Menu_Battle.button_resume, 2)
        surface.blit(Font.neodgm_32.render(game.locale['resume'], False, Color.black), UI.Menu_Battle.text_resume)
        pygame.draw.rect(surface, Color.black, UI.Menu_Battle.button_surrender, 2)
        surface.blit(Font.neodgm_32.render(game.locale['surrender'], False, Color.black), UI.Menu_Battle.text_surrender)
        pygame.draw.rect(surface, Color.black, UI.Menu_Battle.button_exit, 2)
        surface.blit(Font.neodgm_32.render(game.locale['exit_to_title'], False, Color.black), UI.Menu_Battle.text_exit)
        pygame.draw.rect(surface, Color.black, UI.Menu_Battle.button_quit, 2)
        surface.blit(Font.neodgm_32.render(game.locale['exit'], False, Color.black), UI.Menu_Battle.text_quit)

    def render(self, game):
        self.surface.fill(Color.transparent)
        self.surface.blit(self.surface_static, [0, 0])
        self.surface.blit(Image.arrow, UI.Menu_Battle.arrow[game.selected_menu_battle])
        game.surface.blit(self.surface, [0, 0])