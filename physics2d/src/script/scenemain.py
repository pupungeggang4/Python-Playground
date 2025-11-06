import pygame, sys

from script.res import *

def loop(game):
    render(game)

def render(game):
    game.surface.fill(Color.white)
    game.field.render(game)

def key_down(game, key):
    pass

def key_up(game, key):
    pass