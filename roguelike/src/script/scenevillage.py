import pygame, sys

from script.ui import *
from script.res import *
from script.render import *
from script.func import *

def loop(game):
    if game.menu == False:
        if game.state == '':
            game.village.handle_tick(game)
    render(game)

def render(game):
    game.surface.fill(Color.white)
    game.village.render(game)
    game.surface.blit(Font.neodgm_32.render(game.locale['control'], False, Color.black), UI.Village.text_control)
    
    if game.state == 'battle_confirm':
        Render.render_battle_confirm(game)

    if game.menu == True:
        Render.render_menu_village(game)

def key_down(game, key):
    if game.menu == False:
        if key == pygame.K_ESCAPE or key == pygame.K_q:
            game.menu = True
            game.selected_menu_village = 0

        if game.state == '':
            if key == pygame.K_RETURN:
                game.village.player.handle_interact(game)
        elif game.state == 'battle_confirm':
            if key == pygame.K_a or key == pygame.K_d:
                game.selected_battle_confirm = 1 - game.selected_battle_confirm
            if key == pygame.K_RETURN:
                if game.selected_battle_confirm == 0:
                    game.scene = 'battle'
                    game.state = 'adventure_start'
                    game.selected_adventure_start = 0
                else:
                    game.state = ''

    elif game.menu == True:
        if key == pygame.K_ESCAPE or key == pygame.K_q:
            game.menu = False
        if key == pygame.K_w:
            game.selected_menu_village = (game.selected_menu_village + 2) % 3
        if key == pygame.K_s:
            game.selected_menu_village = (game.selected_menu_village + 1) % 3
        if key == pygame.K_RETURN:
            if game.selected_menu_village == 0:
                game.menu = False
            elif game.selected_menu_village == 1:
                game.menu = False
                game.scene = 'title'
                game.state = ''
            elif game.selected_menu_village == 2:
                pygame.quit()
                sys.exit()

def mouse_up(game, pos, button):
    if button == 1:
        if game.menu == False:
            if point_inside_rect_ui(pos, UI.Village.button_menu):
                game.menu = True
                game.selected_menu_village = 0
            if game.state == '':
                game.village.player.handle_interact(game)
            elif game.state == 'battle_confirm':
                if point_inside_rect_ui(pos, UI.Window_Battle_Confirm.button_yes):
                    game.scene = 'battle'
                    game.state = 'adventure_start'
                    game.selected_adventure_start = 0
                elif point_inside_rect_ui(pos, UI.Window_Battle_Confirm.button_no):
                    game.state = ''
        elif game.menu == True:
            if point_inside_rect_ui(pos, UI.Menu_Village.button_resume) or point_inside_rect_ui(pos, UI.Village.button_menu):
                game.menu = False
            elif point_inside_rect_ui(pos, UI.Menu_Village.button_exit):
                game.menu = False
                game.scene = 'title'
                game.state = ''
            elif point_inside_rect_ui(pos, UI.Menu_Village.button_quit):
                pygame.quit()
                sys.exit()