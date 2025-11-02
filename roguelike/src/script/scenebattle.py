import pygame, sys

from script.ui import *
from script.res import *
from script.shape import *
from script.render import *
from script.func import *

def loop(game):
    if game.menu == False:
        if game.state == '':
            game.field.handle_tick(game)
    render(game)

def render(game):
    game.surface.fill(Color.white)
    game.field.render(game)

    Render.render_battle_ui_upper(game)

    if game.state == 'adventure_start':
        Render.render_adventure_start(game)

    if game.menu == True:
        Render.render_menu_battle(game)

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
        if key == pygame.K_w:
            game.selected_menu_battle = (game.selected_menu_battle + 3) % 4
        if key == pygame.K_s:
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
    if key == pygame.K_a:
        game.selected_adventure_start = (game.selected_adventure_start + 2) % 3
    if key == pygame.K_d:
        game.selected_adventure_start = (game.selected_adventure_start + 1) % 3
    if key == pygame.K_RETURN:
        game.state = ''
        game.field.player.adventure_start()

def mouse_up(game, pos, button):
    if button == 1:
        if game.menu == False:
            if point_inside_rect_ui(pos, UI.Battle.button_menu):
                game.menu = True
            if game.state == 'adventure_start':
                mouse_up_adventure_start(game, pos, button)
            elif game.state == '':
                mouse_up_battle(game, pos, button)
        elif game.menu == True:
            if point_inside_rect_ui(pos, UI.Battle.button_menu) or point_inside_rect_ui(pos, UI.Menu_Battle.button_resume):
                game.menu = False
            elif point_inside_rect_ui(pos, UI.Menu_Battle.button_surrender):
                game.menu = False
                game.scene = 'village'
                game.state = ''
            elif point_inside_rect_ui(pos, UI.Menu_Battle.button_exit):
                game.menu = False
                game.scene = 'title'
                game.state = ''
            elif point_inside_rect_ui(pos, UI.Menu_Battle.button_quit):
                pygame.quit()
                sys.exit()

def mouse_up_adventure_start(game, pos, button):
    for i in range(3):
        if point_inside_rect_ui(pos, UI.Window.button_weapon[i]):
            game.selected_adventure_start = i
        if point_inside_rect_ui(pos, UI.Window.button_ok):
            game.state = ''
            game.field.player.adventure_start()

def mouse_up_battle(game, pos, button):
    field = game.field
    player = game.field.player
    field_click = Vec2(pos[0] - field.camera.size.x / 2 + field.camera.pos.x, pos[1] - field.camera.size.y / 2 + field.camera.pos.y)
    #print(f'({field_click.x}, {field_click.y})')
    if Vec2.distance(player.rect.pos, field_click) > 10:
        game.field.player.shoot(game, field_click)