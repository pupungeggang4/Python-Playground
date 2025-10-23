import pygame, sys

from script.ui import *
from script.res import *
from script.render import *

def loop(game):
    if game.menu == False:
        if game.state == '':
            game.field.handle_tick(game)
    render(game)

def render(game):
    game.surface.fill(Color.white)
    game.field.render(game)

    if game.state == 'adventure_start':
        Render.render_adventure_start(game)

    if game.menu == True:
        Render.render_menu_battle(game.surface, game)

def key_down(game, key):
    if game.menu == False:
        if key == pygame.K_ESCAPE or key == pygame.K_q:
            game.menu = True
            game.selected_menu_battle = 0
        if game.state == 'adventure_start':
            handle_adventure_start(game, key)
    else:
        if key == pygame.K_ESCAPE or key == pygame.K_q:
            game.menu = False
        if key == pygame.K_UP:
            game.selected_menu_battle = (game.selected_menu_battle + 3) % 4
        if key == pygame.K_DOWN:
            game.selected_menu_battle = (game.selected_menu_battle + 1) % 4
        if key == pygame.K_RETURN:
            if game.selected_menu_battle == 0:
                game.menu = False
            elif game.selected_menu_battle == 1:
                game.menu = False
                game.scene = 'village'
                game.state = ''
            elif game.selected_menu_battle == 2:
                game.menu = False
                game.scene = 'title'
                game.state = ''
            elif game.selected_menu_battle == 3:
                pygame.quit()
                sys.exit()

def handle_adventure_start(game, key):
    if key == pygame.K_LEFT:
        game.selected_adventure_start = (game.selected_adventure_start + 2) % 3
    if key == pygame.K_RIGHT:
        game.selected_adventure_start = (game.selected_adventure_start + 1) % 3
    if key == pygame.K_RETURN:
        game.state = ''