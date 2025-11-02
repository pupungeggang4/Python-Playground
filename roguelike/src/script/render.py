import pygame

from script.ui import *
from script.res import *
from script.shape import *

class Render():
    @staticmethod
    def render_center_cam(surface, source, rect, cam):
        pos = [
            rect.pos.x - rect.size.x / 2 - cam.pos.x + cam.size.x / 2,
            rect.pos.y - rect.size.y / 2 - cam.pos.y + cam.size.y / 2
        ]
        surface.blit(source, pos)

    @staticmethod
    def render_battle_confirm(game):
        surface = game.surface
        pygame.draw.rect(surface, Color.white, UI.Window_Battle_Confirm.rect)
        pygame.draw.rect(surface, Color.black, UI.Window_Battle_Confirm.rect, 2)
        surface.blit(Font.neodgm_32.render(game.locale['start_battle'], False, Color.black), UI.Window_Battle_Confirm.text_title)
        pygame.draw.rect(surface, Color.black, UI.Window_Battle_Confirm.button_yes, 2)
        surface.blit(Font.neodgm_32.render(game.locale['yes'], False, Color.black), UI.Window_Battle_Confirm.text_yes)
        pygame.draw.rect(surface, Color.black, UI.Window_Battle_Confirm.button_no, 2)
        surface.blit(Font.neodgm_32.render(game.locale['no'], False, Color.black), UI.Window_Battle_Confirm.text_no)
        surface.blit(Image.arrow, UI.Window_Battle_Confirm.arrow[game.selected_battle_confirm])

    @staticmethod
    def render_adventure_start(game):
        surface = game.surface
        pygame.draw.rect(surface, Color.white, UI.Window.rect)
        pygame.draw.rect(surface, Color.black, UI.Window.rect, 2)
        surface.blit(Font.neodgm_32.render(game.locale['select_weapon'], False, Color.black), UI.Window.text_title)

        for i in range(3):
            pygame.draw.rect(surface, Color.black, UI.Window.button_weapon[i], 2)
        surface.blit(Image.arrow_down, UI.Window.arrow_weapon[game.selected_adventure_start])

        pygame.draw.rect(surface, Color.black, UI.Window.button_ok, 2)
        surface.blit(Font.neodgm_32.render(game.locale['ok'], False, Color.black), UI.Window.text_ok)

    @staticmethod
    def render_battle_ui_upper(game):
        surface = game.surface
        player = game.field.player
        pygame.draw.rect(surface, Color.white, UI.Battle.bar_exp)
        exp_rect = [UI.Battle.bar_exp[0], UI.Battle.bar_exp[1], UI.Battle.bar_exp[2] * player.exp / max(player.exp_max, 1), UI.Battle.bar_exp[3]]
        pygame.draw.rect(surface, Color.blue, exp_rect)
        pygame.draw.rect(surface, Color.black, UI.Battle.bar_exp, 2)
        surface.blit(Image.exporb, UI.Battle.icon_exp)
        surface.blit(Font.neodgm_24.render(f'Lv.{player.level} Exp {player.exp}/{player.exp_max}', False, Color.black), UI.Battle.text_exp)
        surface.blit(Image.coin, UI.Battle.icon_gold)
        surface.blit(Font.neodgm_24.render(f'{player.gold}', False, Color.black), UI.Battle.text_gold)

        surface.blit(Image.life, UI.Battle.icon_hp)
        hp_rect = [UI.Battle.bar_hp[0], UI.Battle.bar_hp[1], UI.Battle.bar_hp[2] * player.hp / max(player.hp_max, 1), UI.Battle.bar_hp[3]]
        pygame.draw.rect(surface, Color.green, hp_rect)
        pygame.draw.rect(surface, Color.black, UI.Battle.bar_hp, 2)
        surface.blit(Font.neodgm_24.render(f'{player.hp}/{player.hp_max}', False, Color.black), UI.Battle.text_hp)

        energy_rect = [UI.Battle.bar_energy[0], UI.Battle.bar_energy[1], UI.Battle.bar_energy[2] * player.energy / max(player.energy_max, 1), UI.Battle.bar_energy[3]]
        pygame.draw.rect(surface, Color.cyan, energy_rect)
        surface.blit(Image.energy, UI.Battle.icon_energy)
        surface.blit(Font.neodgm_24.render(f'{player.energy}/{player.energy_max}', False, Color.black), UI.Battle.text_energy)
        pygame.draw.rect(surface, Color.black, UI.Battle.bar_energy, 2)

    @staticmethod
    def render_menu_village(game):
        surface = game.surface
        pygame.draw.rect(surface, Color.white, UI.Menu_Village.rect)
        pygame.draw.rect(surface, Color.black, UI.Menu_Village.rect, 2)
        surface.blit(Font.neodgm_32.render(game.locale['paused'], False, Color.black), UI.Menu_Village.text_paused)
        pygame.draw.rect(surface, Color.black, UI.Menu_Village.button_resume, 2)
        surface.blit(Font.neodgm_32.render(game.locale['resume'], False, Color.black), UI.Menu_Village.text_resume)
        pygame.draw.rect(surface, Color.black, UI.Menu_Village.button_exit, 2)
        surface.blit(Font.neodgm_32.render(game.locale['exit_to_title'], False, Color.black), UI.Menu_Village.text_exit)
        pygame.draw.rect(surface, Color.black, UI.Menu_Village.button_quit, 2)
        surface.blit(Font.neodgm_32.render(game.locale['exit'], False, Color.black), UI.Menu_Village.text_quit)
        surface.blit(Image.arrow, UI.Menu_Village.arrow[game.selected_menu_village])

    @staticmethod
    def render_menu_battle(game):
        surface = game.surface
        pygame.draw.rect(surface, Color.white, UI.Menu_Battle.rect)
        pygame.draw.rect(surface, Color.black, UI.Menu_Battle.rect, 2)
        surface.blit(Font.neodgm_32.render(game.locale['paused'], False, Color.black), UI.Menu_Battle.text_paused)
        pygame.draw.rect(surface, Color.black, UI.Menu_Battle.button_resume, 2)
        surface.blit(Font.neodgm_32.render(game.locale['resume'], False, Color.black), UI.Menu_Battle.text_resume)
        pygame.draw.rect(surface, Color.black, UI.Menu_Battle.button_surrender, 2)
        surface.blit(Font.neodgm_32.render(game.locale['surrender'], False, Color.black), UI.Menu_Battle.text_surrender)
        pygame.draw.rect(surface, Color.black, UI.Menu_Battle.button_exit, 2)
        surface.blit(Font.neodgm_32.render(game.locale['exit_to_title'], False, Color.black), UI.Menu_Battle.text_exit)
        pygame.draw.rect(surface, Color.black, UI.Menu_Battle.button_quit, 2)
        surface.blit(Font.neodgm_32.render(game.locale['exit'], False, Color.black), UI.Menu_Battle.text_quit)
        surface.blit(Image.arrow, UI.Menu_Battle.arrow[game.selected_menu_battle])
