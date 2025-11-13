import pygame, sys, random

from script.res import *

from script.shape import *
from script.render import *

from script.field.fieldplayer import *
from script.field.unit import *
from script.field.projectile import *
from script.field.drop import *

from script.weapon import *

class Field():
    def __init__(self):
        self.camera = Rect2(0, 0, 1280, 720)
        self.player = FieldPlayer()
        self.unit = []
        self.proj = []
        self.effect = []
        self.drop = []

    def adventure_start(self, game):
        self.camera = Rect2(0, 0, 1280, 720)
        self.player = FieldPlayer()
        self.unit = []
        self.unit.append(Unit())
        self.proj = []
        self.effect = []
        self.drop = []
        self.player.adventure_start(game)

    def handle_tick(self, game):
        self.player.handle_tick(game)

        for i in range(len(self.unit) - 1, -1, -1):
            self.unit[i].handle_tick(game)

        for i in range(len(self.proj) - 1, -1, -1):
            self.proj[i].handle_tick(game)

        for i in range(len(self.drop) - 1, -1, -1):
            self.drop[i].handle_tick(game)

    def render(self, game):
        self.player.render(game)
        
        for i in range(len(self.unit)):
            self.unit[i].render(game)

        for i in range(len(self.proj)):
            self.proj[i].render(game)

        for i in range(len(self.drop)):
            self.drop[i].render(game)
