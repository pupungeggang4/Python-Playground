import pygame, sys

from script.fieldplayer import *
from script.coin import *
from script.wall import *
from script.platform import *
from script.belt import *

class Field():
    def __init__(self):
        self.camera = Rect2(0, 0, 1280, 720)
        self.player = FieldPlayer()
        self.entity_list = [Wall()]

    def handle_tick(self, game):
        pass

    def render(self, game):
        self.player.render(game)
        for i in range(len(self.entity_list)):
            self.entity_list[i].render(game)