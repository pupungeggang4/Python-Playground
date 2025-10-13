import pygame, sys

from script.ui import *
from script.res import *
from script.render import *

def loop(game):
    if game.menu == False:
        if game.state == '':
            game.village.handle_tick(game)
    render(game)

def render(game):
    game.surface.fill(Color.white)
    game.village.render(game.surface, game)

def key_down(game, key):
    if game.menu == False:
        if key == pygame.K_ESCAPE or pygame.K_q:
            game.menu = True
            game.selected_menu_village = 0

        if game.state == '':
            if key == pygame.K_x or pygame.K_e:
                game.village.player.handle_interact(game)
        elif game.state == 'battle_confirm':
            if key == pygame.K_LEFT or key == pygame.K_RIGHT:
                game.selected_battle_confirm = 1 - game.selected_battle_confirm
            if key == pygame.K_RETURN:
                if game.selected_battle_confirm == 0:
                    game.state = ''
                else:
                    game.scene = 'battle'
                    game.state = ''

    elif game.menu == True:
        if key == pygame.K_ESCAPE or pygame.K_q:
            game.menu = False

        if key == pygame.K_UP:
            game.selected_menu_village = (game.selected_menu_village + 1)
