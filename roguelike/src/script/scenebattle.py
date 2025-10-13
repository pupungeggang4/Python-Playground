import pygame, sys

from script.ui import *
from script.res import *
from script.render import *

def loop(game):
    render(game)

def render(game):
    game.surface.fill(Color.white)

def key_down(game, key):
    pass