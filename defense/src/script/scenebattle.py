import pygame, sys

from script.scenetitle import *

from script.res import *

class SceneBattle():
    def loop(self, game):
        self.render(game)

    def render(self, game):
        game.surface.fill(Color.white)

    def mouse_up(self, game, pos, button):
        pass
