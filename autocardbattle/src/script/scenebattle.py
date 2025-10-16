import pygame, sys

from script.UI import *
from script.res import *

from script.render import *
from script.func import *

from script.card import *

def loop(game):
    render(game)
    if game.menu == False:
        if game.state == '':
            game.battle.handle_tick(game)

def render(game):
    game.surface.fill(Color.white)
    game.surface.blit(Image.button['menu'], UI.Battle.button_menu)

    Render.render_field(game.surface, game)
    Render.render_card(game.surface, game)
    Render.render_crystal(game.surface, game)

    if game.state == 'reward':
        Render.render_reward_window(game.surface, game)
    if game.state == 'next':
        Render.render_next_window(game.surface, game)
    if game.state == 'win' or game.state == 'lose':
        Render.render_end_window(game.surface, game)

    if game.menu == True:
        Render.render_menu(game.surface)

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
            elif game.state == 'lose':
                mouse_up_lose(game, pos, button)
            elif game.state == 'win':
                mouse_up_win(game, pos, button)

        elif game.menu == True:
            if point_inside_rect_ui(pos, UI.Menu.button_resume):
                game.menu = False

            elif point_inside_rect_ui(pos, UI.Menu.button_exit):
                game.menu = False
                game.scene = 'title'
                game.state = ''

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
        game.state = 'next'
        game.adventure.floor += 1
        game.adventure.next_selected = -1

def mouse_up_next(game, pos, button):
    for i in range(3):
        if point_inside_rect_ui(pos, UI.Window.next_cell[i]):
            game.adventure.next_selected = i

    if point_inside_rect_ui(pos, UI.Window.button_confirm):
        if game.adventure.next_selected != -1:
            if game.adventure.layout[game.adventure.floor][game.adventure.next_selected] == 'battle':
                game.state = ''
                game.battle.start_battle(game)

def mouse_up_lose(game, pos, button):
    if point_inside_rect_ui(pos, UI.Window_End.button_ok):
        game.scene = 'title'
        game.state = ''

def mouse_up_win(game, pos, button):
    if point_inside_rect_ui(pos, UI.Window_End.button_ok):
        if game.adventure.floor >= len(game.adventure.layout) - 1:
            game.scene = 'title'
            game.state = ''
        else:
            game.state = 'reward'
            game.adventure.reward_type = 'card'
            game.adventure.reward_selected = -1
            #game.adventure.reward = [Card(), Card(), Card()]