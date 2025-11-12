import pygame, sys

from script.ui import *
from script.res import *

class Render():
    @staticmethod
    def render_battle_static(surface, game):
        pass

    @staticmethod
    def render_window_start(surface, game):
        pass
    
    @staticmethod
    def render_menu(surface, game):
        surface.fill(Color.transparent)
        pygame.draw.rect(surface, Color.white, UI.Menu.rect)
        pygame.draw.rect(surface, Color.black, UI.Menu.rect, 2)
        surface.blit(Font.neodgm_32.render(game.locale['paused'], False, Color.black), UI.Menu.text_paused)
        pygame.draw.rect(surface, Color.black, UI.Menu.button_resume, 2)
        surface.blit(Font.neodgm_32.render(game.locale['resume'], False, Color.black), UI.Menu.text_resume)
        pygame.draw.rect(surface, Color.black, UI.Menu.button_save_and_exit, 2)
        surface.blit(Font.neodgm_32.render(game.locale['save_and_exit'], False, Color.black), UI.Menu.text_save_and_exit)
        pygame.draw.rect(surface, Color.black, UI.Menu.button_quit, 2)
        surface.blit(Font.neodgm_32.render(game.locale['quit'], False, Color.black), UI.Menu.text_quit)
