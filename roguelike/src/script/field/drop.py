import pygame, sys, random

from script.res import *

from script.shape import *
from script.render import *

class Drop():
    def __init__(self):
        self.rect = Rect2(0, 0, 40, 40)
        self.type = 'coin'
        self.amount = 10

    def set_data(self, type, amount):
        self.type = type
        self.amount = amount

    def handle_tick(self, game):
        player = game.field.player
        if Vec2.distance(self.rect.pos, player.rect.pos) < 60:
            if self.type == 'coin':
                player.gold += self.amount
            elif self.type == 'exporb':
                player.exp += self.amount
                if player.exp >= player.exp_max:
                    player.exp -= player.exp_max
                    player.level += 1
            game.field.drop.pop(game.field.drop.index(self))

    def render(self, game):
        if self.type == 'coin':
            Render.render_center_cam(game.surface, Image.coin, self.rect, game.field.camera)
        elif self.type == 'exporb':
            Render.render_center_cam(game.surface, Image.exporb, self.rect, game.field.camera)