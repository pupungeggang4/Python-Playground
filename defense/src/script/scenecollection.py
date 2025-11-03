import pygame, sys

from script.res import *

def loop(game):
    render(game)

def render(game):
    game.surface.fill(Color.white)

def mouse_up(game, pos, button):
    pass