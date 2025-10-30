import pygame, sys

from script.ui import *
from script.res import *
from script.locale import *
from script.func import *

from script.village import *

def loop(game):
    render(game)

def render(game):
    game.surface.fill([255, 255, 255])
    game.surface.blit(Font.neodgm_32.render(game.locale['game_name'], False, Color.black), UI.Title.text_title)
    pygame.draw.rect(game.surface, Color.black, UI.Title.button_start, 2)
    game.surface.blit(Font.neodgm_32.render(game.locale['start_game'], False, Color.black), UI.Title.text_start)
    pygame.draw.rect(game.surface, Color.black, UI.Title.button_collection, 2)
    game.surface.blit(Font.neodgm_32.render(game.locale['collection'], False, Color.black), UI.Title.text_collection)
    pygame.draw.rect(game.surface, Color.black, UI.Title.button_lang, 2)
    game.surface.blit(Font.neodgm_32.render(game.locale['lang'], False, Color.black), UI.Title.text_lang)
    pygame.draw.rect(game.surface, Color.black, UI.Title.button_erase, 2)
    game.surface.blit(Font.neodgm_32.render(game.locale['erase_data'], False, Color.black), UI.Title.text_erase)
    pygame.draw.rect(game.surface, Color.black, UI.Title.button_exit, 2)
    game.surface.blit(Font.neodgm_32.render(game.locale['exit'], False, Color.black), UI.Title.text_exit)
    game.surface.blit(Image.arrow, UI.Title.arrow[game.selected_title])

def key_down(game, key):
    if key == pygame.K_UP:
        game.selected_title = (game.selected_title + 4) % 5

    if key == pygame.K_DOWN:
        game.selected_title = (game.selected_title + 1) % 5

    if key == pygame.K_RETURN:
        if game.selected_title == 0:
            game.scene = 'village'
            game.state = ''
            game.village = Village()
        elif game.selected_title == 1:
            game.scene = 'collection'
            game.state = ''
        elif game.selected_title == 2:
            game.lang = (game.lang + 1) % len(Locale.lang_list)
            game.locale = Locale.data[Locale.lang_list(game.lang)]
        elif game.selected_title == 3:
            pass
        elif game.selected_title == 4:
            pygame.quit()
            sys.exit()

def mouse_up(game, pos, button):
    if button == 1:
        if point_inside_rect_ui(pos, UI.Title.button_start):
            game.scene = 'village'
            game.state = ''
            game.village = Village()
        elif point_inside_rect_ui(pos, UI.Title.button_collection):
            game.scene = 'collection'
            game.state = ''
        elif point_inside_rect_ui(pos, UI.Title.button_lang):
            game.lang = (game.lang + 1) % len(Locale.lang_list)
            game.locale = Locale.data[Locale.lang_list(game.lang)]
        elif point_inside_rect_ui(pos, UI.Title.button_erase):
            pass
        elif point_inside_rect_ui(pos, UI.Title.button_exit):
            pygame.quit()
            sys.exit()