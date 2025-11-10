import pygame, sys

from script.res import *

from script.shape import *
from script.entity import *
from script.physics import *

from script.render import *

class Unit(Entity):
    def __init__(self):
        self.rect = Rect2(0, 0, 80, 80)
        self.velocity = Vec2(0, 0)
        self.gravity = 800.0
        self.terminal_speed = 800.0
        self.fall = True
        self.ground = True

    def handle_tick(self, game):
        self.ground = False
        if self.fall == True:
            if self.velocity.y < self.terminal_speed:
                self.velocity.y += self.gravity / game.fps
        self.rect.pos.y += self.velocity.y / game.fps
        if self.fall == True:
            self.support(game)

    def support(self, game):
        entity_list = game.field.entity_list
        for i in range(len(entity_list)):
            if entity_list[i] is not self:
                entity = entity_list[i]
                f = Physics.check_fall(entity.rect, self.rect)
                if f > 0:
                    self.ground = True
                    self.velocity.y = 0
                    self.rect.pos.y -= f

    def render(self, game):
        Render.draw_rect_center_cam(game.surface, self.rect, game.field.camera, Color.black, 2)