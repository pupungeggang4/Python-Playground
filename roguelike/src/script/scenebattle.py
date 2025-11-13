import pygame, sys

from script.ui import *
from script.res import *
from script.shape import *
from script.render import *
from script.func import *

from script.window.windowadventurestart import *
from script.window.windowmenubattle import *

from script.scenetitle import *
from script.scenevillage import *

class SceneBattle():
    def __init__(self, game):
        self.window_adventure_start = WindowAdventureStart(game)
        self.window_adventure_start.render_static(game)
        self.window_menu_battle = WindowMenuBattle(game)

    def loop(self, game):
        if game.menu == False:
            if game.state == '':
                game.field.handle_tick(game)
        self.render(game)

    def render(self, game):
        game.surface.fill(Color.white)
        game.field.render(game)
        game.surface.blit(Image.button_menu, UI.Battle.button_menu)

        Render.render_battle_ui_upper(game)
        Render.render_battle_ui_lower(game)

        if game.state == 'adventure_start':
            self.window_adventure_start.render(game)

        if game.state == 'game_over':
            Render.render_game_over(game)

        if game.menu == True:
            self.window_menu_battle.render(game)

    def key_down(self, game, key):
        if game.menu == False:
            if key == pygame.K_ESCAPE or key == pygame.K_q:
                game.menu = True
                self.window_menu_battle.render_static(game)
                game.selected_menu_battle = 0
            if game.state == 'adventure_start':
                self.handle_key_adventure_start(game, key)
            elif game.state == '':
                self.handle_key_battle(game, key)
            elif game.state == 'game_over':
                if key == pygame.K_RETURN:
                    game.scene = SceneTitle(game)
                    game.state = ''
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
                    game.scene = SceneVillage(game)
                    game.state = ''
                elif game.selected_menu_battle == 2:
                    game.menu = False
                    game.scene = SceneTitle(game)
                    game.state = ''
                elif game.selected_menu_battle == 3:
                    pygame.quit()
                    sys.exit()

    def handle_key_adventure_start(self, game, key):
        if key == pygame.K_a:
            game.selected_adventure_start = (game.selected_adventure_start + 2) % 3
        if key == pygame.K_d:
            game.selected_adventure_start = (game.selected_adventure_start + 1) % 3
        if key == pygame.K_RETURN:
            game.state = ''
            game.field.player.adventure_start(game)

    def handle_key_battle(self, game, key):
        if key == pygame.K_SPACE:
            game.field.player.dash(game)

    def mouse_up(self, game, pos, button):
        if button == 1:
            if game.menu == False:
                if point_inside_rect_ui(pos, UI.Battle.button_menu):
                    game.menu = True
                    self.selected_menu_battle = 0
                    game.window_menu_battle.render_static(game)
                if game.state == 'adventure_start':
                    self.handle_mouse_up_adventure_start(game, pos, button)
                elif game.state == '':
                    self.mouse_up_battle(game, pos, button)
                elif game.state == 'game_over':
                    if point_inside_rect_ui(pos, UI.Window_Small.button_ok):
                        game.scene = SceneTitle(game)
                        game.state = ''
            elif game.menu == True:
                if point_inside_rect_ui(pos, UI.Battle.button_menu) or point_inside_rect_ui(pos, UI.Menu_Battle.button_resume):
                    game.menu = False
                elif point_inside_rect_ui(pos, UI.Menu_Battle.button_surrender):
                    game.menu = False
                    game.scene = SceneVillage(game)
                    game.state = ''
                elif point_inside_rect_ui(pos, UI.Menu_Battle.button_exit):
                    game.menu = False
                    game.scene = SceneTitle(game)
                    game.state = ''
                elif point_inside_rect_ui(pos, UI.Menu_Battle.button_quit):
                    pygame.quit()
                    sys.exit()

    def handle_mouse_up_adventure_start(self, game, pos, button):
        for i in range(3):
            if point_inside_rect_ui(pos, UI.Window.button_weapon[i]):
                game.selected_adventure_start = i
            if point_inside_rect_ui(pos, UI.Window.button_ok):
                game.state = ''
                game.field.player.adventure_start(game)

    def mouse_up_battle(self, game, pos, button):
        field = game.field
        player = game.field.player
        if not point_inside_rect_ui(pos, UI.Battle.button_menu):
            field_click = Vec2(pos[0] - field.camera.size.x / 2 + field.camera.pos.x, pos[1] - field.camera.size.y / 2 + field.camera.pos.y)
            if Vec2.distance(player.rect.pos, field_click) > 10:
                game.field.player.shoot(game, field_click)