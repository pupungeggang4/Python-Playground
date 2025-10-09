import pygame, sys

from script.UI import *
from script.res import *

from script.render import *
from script.func import *

def loop(game):
    render(game)

def render(game):
    game.surface.fill(Color.white)
    game.surface.blit(Font.neodgm_32.render('Auto Card Battle', False, Color.black), UI.Title.text_title)
    pygame.draw.rect(game.surface, Color.black, UI.Title.button_start, 2)
    game.surface.blit(Font.neodgm_32.render('Start Game', False, Color.black), UI.Title.text_start)
    pygame.draw.rect(game.surface, Color.black, UI.Title.button_collection, 2)
    game.surface.blit(Font.neodgm_32.render('Collection', False, Color.black), UI.Title.text_collection)
    pygame.draw.rect(game.surface, Color.black, UI.Title.button_quit, 2)
    game.surface.blit(Font.neodgm_32.render('Quit', False, Color.black), UI.Title.text_quit)

def mouse_up(game, pos, button):
    if button == 1:
        if point_inside_rect_ui(pos, UI.Title.button_start):
            game.scene = 'ready'
            game.state = ''
            game.selected_character = -1
        elif point_inside_rect_ui(pos, UI.Title.button_quit):
            pygame.quit()
            sys.exit()
