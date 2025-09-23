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
        for i in range(10):
            pygame.draw.rect(screen, Color.black, UI.Battle.field[i], 2)

        pygame.draw.rect(screen, Color.black, UI.Battle.button_proceed, 2)
        screen.blit(Font.neodgm_32.render('Proceed', False, Color.black), UI.Battle.text_proceed)

    @staticmethod
    def render_crystal(screen, game):
        pygame.draw.rect(screen, Color.black, UI.Battle.player_crystal_box, 2)
        pygame.draw.rect(screen, Color.black, UI.Battle.enemy_crystal_box, 2)

    @staticmethod
    def render_card(screen, game):
        for i in range(3, -1, -1):
            pos = [UI.Battle.player_card_start[0] + UI.Battle.player_card_interval[0] * i, UI.Battle.player_card_start[1]]
            game.card.render(screen, game, pos)

        for i in range(3, -1, -1):
            pos = [UI.Battle.enemy_card_start[0] + UI.Battle.enemy_card_interval[0] * i, UI.Battle.enemy_card_start[1]]
            game.card.render(screen, game, pos)