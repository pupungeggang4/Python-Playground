import pygame, sys, random

from script.res import *

from script.shape import *
from script.render import *

class Projectile():
    def __init__(self):
        self.rect = Rect2(0, 0, 40, 40)
        self.side = 0
        self.speed = 640.0
        self.damage = 5
        self.life_time = 1
        self.v_unit = Vec2(1.0, 0.0)

    def handle_tick(self, game):
        self.collide_check(game)
        self.handle_life_time(game)
        self.move(game)

    def collide_check(self, game):
        field = game.field
        if self.side == 0:
            for i in range(len(field.unit) - 1, -1, -1):
                if Vec2.distance(field.unit[i].rect.pos, self.rect.pos) < 60:
                    field.unit[i].hp -= self.damage
                    field.proj.pop(field.proj.index(self))

    def move(self, game):
        self.rect.pos.x += self.speed * self.v_unit.x / game.fps
        self.rect.pos.y += self.speed * self.v_unit.y / game.fps

    def handle_life_time(self, game):
        field = game.field
        if self.life_time <= 0:
            field.proj.pop(field.proj.index(self))
        else:
            self.life_time -= 1.0 / game.fps

    def render(self, game):
        Render.render_center_cam(game.surface, Image.projectile, self.rect, game.field.camera)