import pygame, sys

from script.ui import *
from script.res import *
from script.func import *

def loop(game):
    render(game)

def render(game):
    game.surface.fill(Color.white)
    game.surface.blit(Font.neodgm_32.render('Platformer', False, Color.black), UI.Title.text_title)
    pygame.draw.rect(game.surface, Color.black, UI.Title.button_start, 2)
    game.surface.blit(Font.neodgm_32.render('Start Game', False, Color.black), UI.Title.text_start)
    pygame.draw.rect(game.surface, Color.black, UI.Title.button_collection, 2)
    game.surface.blit(Font.neodgm_32.render('Collection', False, Color.black), UI.Title.text_collection)
    pygame.draw.rect(game.surface, Color.black, UI.Title.button_erase, 2)
    game.surface.blit(Font.neodgm_32.render('Erase', False, Color.black), UI.Title.text_erase)

def mouse_up(game, pos, button):
    if button == 1:
        if Func.point_inside_rect_ui(pos, UI.Title.button_start):
            game.scene = 'game'
            game.state = ''

def key_down(game, key):
    pass

def key_up(game, key):
    pass
