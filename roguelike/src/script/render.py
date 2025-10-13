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
    def render_menu_village(surface, game):
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
    def render_battle_confirm(surface, game):
        pygame.draw.rect(surface, Color.white, UI.Window_Battle_Confirm.rect)
        pygame.draw.rect(surface, Color.black, UI.Window_Battle_Confirm.rect, 2)
        surface.blit(Font.neodgm_32.render(game.locale['start_battle'], False, Color.black), UI.Window_Battle_Confirm.text_title)
        surface.blit(Font.neodgm_32.render(game.locale['yes'], False, Color.black), UI.Window_Battle_Confirm.text_yes)
        surface.blit(Font.neodgm_32.render(game.locale['no'], False, Color.black), UI.Window_Battle_Confirm.text_no)
        surface.blit(Image.arrow, UI.Window_Battle_Confirm.arrow[game.selected_battle_confirm])
