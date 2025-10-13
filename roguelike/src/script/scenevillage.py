import pygame, sys

from script.ui import *
from script.res import *
from script.render import *

def loop(game):
    if game.menu == False:
        if game.state == '':
            game.village.handle_tick(game)
    render(game)

def render(game):
    game.surface.fill(Color.white)
    game.village.render(game.surface, game)

def key_down(game, key):
    pass
