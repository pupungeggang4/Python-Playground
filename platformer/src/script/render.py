import pygame

from script.res import *
from script.ui import *

class Render():
    @staticmethod
    def render_menu(surface, game):
        pygame.draw.rect(surface, Color.white, UI.Menu.rect)
        pygame.draw.rect(surface, Color.black, UI.Menu.rect, 2)
        surface.blit(Font.neodgm_32.render(game.locale['paused'], False, Color.black), UI.Menu.text_paused)
        pygame.draw.rect(surface, Color.black, UI.Menu.button_resume, 2)
        surface.blit(Font.neodgm_32.render(game.locale['resume'], False, Color.black), UI.Menu.text_resume)
        pygame.draw.rect(surface, Color.black, UI.Menu.button_exit, 2)
        surface.blit(Font.neodgm_32.render(game.locale['exit'], False, Color.black), UI.Menu.text_exit)
        surface.blit(Image.arrow, UI.Menu.arrow[game.selected_menu])
