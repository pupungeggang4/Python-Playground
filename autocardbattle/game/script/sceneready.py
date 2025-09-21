import pygame, sys

from script.UI import *
from script.res import *

from script.render import *
from script.func import *

def loop(game):
    render(game)

def render(game):
    game.screen.fill(Color.white)
    pygame.display.flip()

def mouse_up(game, pos, button):
    pass