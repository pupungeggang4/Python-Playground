import pygame, sys

from script.ui import *
from script.res import *

class Window():
    def __init__(self, game):
        self.surface_static = pygame.surface.Surface(game.resolution, pygame.SRCALPHA)
        self.surface = pygame.surface.Surface(game.resolution, pygame.SRCALPHA)

    def render_static(self, game):
        pass

    def render(self, game):
        pass