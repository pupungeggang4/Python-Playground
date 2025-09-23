import pygame, sys

from script.UI import *
from script.res import *

class Render():
    @staticmethod
    def render_menu(screen):
        pygame.draw.rect(screen, Color.white, UI.Menu.rect)
        pygame.draw.rect(screen, Color.black, UI.Menu.rect, 2)
        screen.blit(Font.neodgm_32.render('Paused', False, Color.black), UI.Menu.text_paused)
        pygame.draw.rect(screen, Color.black, UI.Menu.button_resume, 2)
        screen.blit(Font.neodgm_32.render('Resume', False, Color.black), UI.Menu.text_resume)
        pygame.draw.rect(screen, Color.black, UI.Menu.button_exit, 2)
        screen.blit(Font.neodgm_32.render('Exit', False, Color.black), UI.Menu.text_exit)

    @staticmethod
    def render_field(screen, game):
        pass

    @staticmethod
    def render_crystal(screen, game):
        pass

    @staticmethod
    def render_card(screen, game):
        pass