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
        self.entity_list = []

    def handle_tick(self, game):
        self.player.handle_tick(game)
        for i in range(len(self.entity_list) - 1, -1, -1):
            self.entity_list[i].handle_tick(game)

    def render(self, game):
        self.player.render(game)
        for i in range(len(self.entity_list)):
            self.entity_list[i].render(game)