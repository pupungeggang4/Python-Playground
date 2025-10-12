import pygame, sys

from script.ui import *
from script.res import *
from script.locale import *
from script.render import *

def loop(game):
    render(game)

def render(game):
    game.surface.fill(Color.white)

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
            game.selected_menu = (game.selected_menu + 1) % 2
        elif key == pygame.K_DOWN:
            game.selected_menu = (game.selected_menu + 1) % 2
        elif key == pygame.K_RETURN:
            if game.selected_menu == 0:
                game.menu = False
            elif game.selected_menu == 1:
                game.menu = False
                game.scene = 'title'
                game.state = ''
