import pygame, sys

from script.ui import *
from script.res import *
from script.locale import *
from script.render import *

def loop(game):
    if game.menu == False:
        if game.state == '':
            game.field.handle_tick(game)
    render(game)

def render(game):
    game.surface.fill(Color.white)
    game.field.render(game)

    game.surface.blit(Image.coin, UI.Field.icon_coin)
    game.surface.blit(Font.neodgm_32.render(f'{game.player.coin}', False, Color.black), UI.Field.text_coin)

    if game.menu == True:
        Render.render_menu(game.surface, game)

def key_down(game, key):
    if game.menu == False:
        if key == pygame.K_RETURN or key == pygame.K_q:
            game.menu = True
            game.selected_menu = 0
    elif game.menu == True:
        if key == pygame.K_RETURN or key == pygame.K_q:
            game.menu = False
        if key == pygame.K_UP:
            game.selected_menu = (game.selected_menu + 2) % 3
        elif key == pygame.K_DOWN:
            game.selected_menu = (game.selected_menu + 1) % 3
        elif key == pygame.K_RETURN:
            if game.selected_menu == 0:
                game.menu = False
            elif game.selected_menu == 1:
                game.menu = False
                game.scene = 'title'
                game.state = ''
            elif game.selected_menu == 2:
                pygame.quit()
                sys.exit()
