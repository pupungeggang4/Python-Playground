import pygame, sys

from script.UI import *
from script.res import *

from script.render import *
from script.func import *

def loop(game):
    render(game)
    if game.menu == False:
        if game.state == '':
            game.battle.handle_tick(game)

def render(game):
    game.screen.fill(Color.white)
    game.screen.blit(Image.button['menu'], UI.Battle.button_menu)

    Render.render_field(game.screen, game)
    Render.render_card(game.screen, game)
    Render.render_crystal(game.screen, game)

    if game.state == 'reward':
        Render.render_reward_window(game.screen, game)
    if game.state == 'next':
        Render.render_next_window(game.screen, game)

    if game.menu == True:
        Render.render_menu(game.screen)

    pygame.display.flip()

def mouse_up(game, pos, button):
    if button == 1:
        if game.menu == False:
            if point_inside_rect_ui(pos, UI.Battle.button_menu):
                game.menu = True

            if game.state == '':
                mouse_up_normal(game, pos, button)
            elif game.state == 'reward':
                mouse_up_reward(game, pos, button)
            elif game.state == 'next':
                mouse_up_next(game, pos, button)
        elif game.menu == True:
            if point_inside_rect_ui(pos, UI.Menu.button_resume):
                game.menu = False

            elif point_inside_rect_ui(pos, UI.Menu.button_exit):
                game.menu = False
                game.scene = 'title'
                game.state = ''
                game.battle.__init__()

def mouse_up_normal(game, pos, button):
    if point_inside_rect_ui(pos, UI.Battle.button_proceed):
        if game.battle.paused == True:
            game.battle.proceed(game)
    elif point_inside_rect_ui(pos, UI.Battle.button_play):
        game.battle.paused = False
    elif point_inside_rect_ui(pos, UI.Battle.button_pause):
        game.battle.paused = True

def mouse_up_reward(game, pos, button):
    for i in range(3):
        if point_inside_rect_ui(pos, UI.Window.reward[i]):
            game.adventure.reward_selected = i

    if point_inside_rect_ui(pos, UI.Window.button_confirm):
        if game.adventure.reward_selected != -1:
            if game.adventure.reward_type == 'card':
                card = game.adventure.reward[game.adventure.reward_selected].clone()
                game.player.deck.append(card)

def mouse_up_next(game, pos, button):
    for i in range(3):
        if point_inside_rect_ui(pos, UI.Window.next_cell[i]):
            game.adventure.next_selected = i

    if point_inside_rect_ui(pos, UI.Window.button_confirm):
        if game.adventure.next_selected != -1:
            if game.adventure.layout[game.adventure.floor][game.adventure.next_selected] == 'battle':
                game.state = ''
                game.battle.start_battle(game)