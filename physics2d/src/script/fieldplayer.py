import pygame, sys

from script.render import *
from script.shape import *
from script.physics import *

from script.entity import *

class FieldPlayer(Entity):
    def __init__(self):
        self.rect = Rect2(0, 0, 80, 80)
        self.velocity = Vec2(0, 0)
        self.speed = 400.0
        self.jump = -600
        self.gravity = 800
        self.terminal_speed = 800
        self.jump_num = 1
        self.jump_store = False
        self.fall = True

    def handle_tick(self, game):
        if game.key_pressed['left'] == True:
            self.rect.pos.x -= self.speed / game.fps
        if game.key_pressed['right'] == True:
            self.rect.pos.x += self.speed / game.fps
        self.ground = False
        if self.fall == True:
            if self.velocity.y < self.terminal_speed:
                self.velocity.y += self.gravity / game.fps
        self.rect.pos.y += self.velocity.y / game.fps
        if self.fall == True:
            self.support(game)
        if game.key_pressed['up'] == True:
            if self.jump_num > 0:
                self.jump_num -= 1
                self.jump_store = True
        if self.jump_store == True:
            if self.ground == True:
                self.velocity.y = self.jump
            self.jump_store = False

    def support(self, game):
        entity_list = game.field.entity_list
        for i in range(len(entity_list)):
            entity = entity_list[i]
            f = Physics.check_fall(entity.rect, self.rect)
            if f > 0:
                self.ground = True
                self.velocity.y = 0
                self.rect.pos.y -= f
                self.jump_num = 1

    def render(self, game):
        field = game.field
        Render.draw_rect_center_cam(game.surface, self.rect, field.camera)