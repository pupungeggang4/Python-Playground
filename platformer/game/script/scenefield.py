import pygame, sys
from script.ui import *
from script.res import *
from script.func import *

def loop(game):
    render(game)

def render(game):
    game.screen.fill(Color.white)
    game.coin.render(game, game.screen)
    pygame.display.flip()

def key_down(game, key):
    pass

def key_up(game, key):
    pass
