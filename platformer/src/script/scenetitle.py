import pygame, sys

from script.ui import *
from script.res import *
from script.locale import *

def loop(game):
    render(game)

def render(game):
    game.surface.fill(Color.white)
    game.surface.blit(Font.neodgm_32.render(game.locale['game_name'], False, Color.black), UI.Title.text_title)
    pygame.draw.rect(game.surface, Color.black, UI.Title.button_start, 2)
    game.surface.blit(Font.neodgm_32.render(game.locale['start_game'], False, Color.black), UI.Title.text_start)
    pygame.draw.rect(game.surface, Color.black, UI.Title.button_lang, 2)
    game.surface.blit(Font.neodgm_32.render(game.locale['lang'], False, Color.black), UI.Title.text_lang)
    pygame.draw.rect(game.surface, Color.black, UI.Title.button_hw_acceler, 2)
    if game.hw_acceler == True:
        game.surface.blit(Font.neodgm_32.render(game.locale['hw_acceler_on'], False, Color.black), UI.Title.text_hw_acceler)
    else:
        game.surface.blit(Font.neodgm_32.render(game.locale['hw_acceler_off'], False, Color.black), UI.Title.text_hw_acceler)
    pygame.draw.rect(game.surface, Color.black, UI.Title.button_erase, 2)
    game.surface.blit(Font.neodgm_32.render(game.locale['erase_data'], False, Color.black), UI.Title.text_erase)
    pygame.draw.rect(game.surface, Color.black, UI.Title.button_exit, 2)
    game.surface.blit(Font.neodgm_32.render(game.locale['quit'], False, Color.black), UI.Title.text_exit)
    game.surface.blit(Image.arrow, UI.Title.arrow[game.selected_title])

def key_down(game, key):
    if key == pygame.K_UP:
        game.selected_title = (game.selected_title + 4) % 5
    if key == pygame.K_DOWN:
        game.selected_title = (game.selected_title + 1) % 5
    if key == pygame.K_RETURN:
        if game.selected_title == 0:
            game.scene = 'field'
            game.state = ''
        elif game.selected_title == 1:
            if game.lang == 'en':
                game.lang = 'ko'
            else:
                game.lang = 'en'
            game.locale = Locale.data[game.lang]
        elif game.selected_title == 2:
            if game.hw_acceler == True:
                game.disable_hw_acceler()
            else:
                game.enable_hw_acceler()
        elif game.selected_title == 3:
            pass
        elif game.selected_title == 4:
            pygame.quit()
            sys.exit()
