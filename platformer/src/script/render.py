import pygame

from script.res import *
from script.ui import *

class Render():
    @staticmethod
    def render_menu(surface, game):
        pygame.draw.rect(surface, Color.white, UI.Menu.rect)
        pygame.draw.rect(surface, Color.black, UI.Menu.rect, 2)
        surface.blit(Font.neodgm_32.render(game.locale['paused'], False, Color.black), UI.Menu.text_paused)
        pygame.draw.rect(surface, Color.black, UI.Menu.button_resume, 2)
        surface.blit(Font.neodgm_32.render(game.locale['resume'], False, Color.black), UI.Menu.text_resume)
        pygame.draw.rect(surface, Color.black, UI.Menu.button_exit, 2)
        surface.blit(Font.neodgm_32.render(game.locale['exit'], False, Color.black), UI.Menu.text_exit)
        pygame.draw.rect(surface, Color.black, UI.Menu.button_quit, 2)
        surface.blit(Font.neodgm_32.render(game.locale['quit'], False, Color.black), UI.Menu.text_quit)
        surface.blit(Image.arrow, UI.Menu.arrow[game.selected_menu])

    @staticmethod
    def render_center_cam(surface, img, rect, camera):
        pos = [rect.pos.x - rect.size.x / 2 - camera.pos.x + camera.size.x / 2, rect.pos.y - rect.size.y / 2 - camera.pos.y + camera.size.y / 2]
        surface.blit(img, pos)