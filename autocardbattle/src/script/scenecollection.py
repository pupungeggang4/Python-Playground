import pygame, sys

from script.UI import *
from script.res import *

from script.render import *
from script.func import *

def loop(game):
    render(game)

def render(game):
    game.surface.fill(Color.white)
    game.surface.blit(Font.neodgm_32.render('Collection', False, Color.black), UI.Collection.text_title)
    pygame.draw.rect(game.surface, Color.black, UI.Collection.button_back)

def mouse_up(game, pos, button):
    if button == 1:
        if point_inside_rect_ui(pos, UI.Collection.button_back):
            game.scene = 'title'
            game.state = ''
