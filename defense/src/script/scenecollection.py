import pygame, sys

from script.res import *
from script.scenetitle import *

class SceneCollection():
    def loop(self, game):
        self.render(game)

    def render(self, game):
        game.surface.fill(Color.white)

    def mouse_up(self, game, pos, button):
        pass
