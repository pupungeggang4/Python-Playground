import pygame, sys

from script.UI import *
from script.res import *

from script.render import *
from script.func import *

def loop(game):
    render(game)

def render(game):
    game.screen.fill(Color.white)
    pygame.draw.rect(game.screen, Color.black, UI.Battle.button_menu, 2)

    Render.render_field(game.screen, game)
    Render.render_card(game.screen, game)
    Render.render_crystal(game.screen, game)

    if game.state == 'reward':
        Render.render_reward_window(game.screen, game)

    if game.menu == True:
        Render.render_menu(game.screen)

    pygame.display.flip()

def mouse_up(game, pos, button):
    if button == 1:
        if game.menu == False:
            if point_inside_rect_ui(pos, UI.Battle.button_menu):
                game.menu = True

            if game.state == 'reward':
                mouse_up_reward(game, pos, button)
        elif game.menu == True:
            if point_inside_rect_ui(pos, UI.Menu.button_resume):
                game.menu = False

            elif point_inside_rect_ui(pos, UI.Menu.button_exit):
                game.menu = False
                game.scene = 'title'
                game.state = ''

def mouse_up_reward(game, pos, button):
    if point_inside_rect_ui(pos, UI.Window.button_confirm):
        game.state = ''
        game.battle.start_battle(game)