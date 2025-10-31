import pygame, sys
from script.ui import *
from script.res import *
from script.locale import *
from script.func import *

def loop(game):
    render(game)

def render(game):
    game.surface.fill(Color.white)
    game.surface.blit(Font.neodgm_32.render(game.locale['game_name'], False, Color.black), UI.Title.text_title)
    pygame.draw.rect(game.surface, Color.black, UI.Title.button_start, 2)
    game.surface.blit(Font.neodgm_32.render(game.locale['start_game'], False, Color.black), UI.Title.text_start)
    pygame.draw.rect(game.surface, Color.black, UI.Title.button_tutorial, 2)
    game.surface.blit(Font.neodgm_32.render(game.locale['tutorial'], False, Color.black), UI.Title.text_tutorial)
    pygame.draw.rect(game.surface, Color.black, UI.Title.button_lang, 2)
    game.surface.blit(Font.neodgm_32.render(game.locale['lang'], False, Color.black), UI.Title.text_lang)
    pygame.draw.rect(game.surface, Color.black, UI.Title.button_hw, 2)
    if game.acceler == True:
        game.surface.blit(Font.neodgm_32.render(game.locale['hw_acceler_on'], False, Color.black), UI.Title.text_hw)
    else:
        game.surface.blit(Font.neodgm_32.render(game.locale['hw_acceler_off'], False, Color.black), UI.Title.text_hw)
    pygame.draw.rect(game.surface, Color.black, UI.Title.button_erase, 2)
    game.surface.blit(Font.neodgm_32.render(game.locale['erase_data'], False, Color.black), UI.Title.text_erase)
    pygame.draw.rect(game.surface, Color.black, UI.Title.button_quit, 2)
    game.surface.blit(Font.neodgm_32.render(game.locale['quit'], False, Color.black), UI.Title.text_quit)

def mouse_up(game, pos, button):
    if point_inside_rect_ui(pos, UI.Title.button_lang):
        game.lang = (game.lang + 1) % len(Locale.lang_list)
        game.locale = Locale.data[Locale.lang_list[game.lang]]
    if point_inside_rect_ui(pos, UI.Title.button_hw):
        if game.acceler == True:
            game.disable_acceler()
        else:
            game.enable_acceler()
    if point_inside_rect_ui(pos, UI.Title.button_quit):
        pygame.quit()
        sys.exit()