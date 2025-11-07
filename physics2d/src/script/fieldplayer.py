import pygame, sys

from script.render import *
from script.shape import *

from script.entity import *

class FieldPlayer(Entity):
    def __init__(self):
        self.rect = Rect2(0, 0, 80, 80)
        self.velocity = Vec2(0, 0)
        self.speed = 400.0

    def handle_tick(self, game):
        self.velocity = Vec2(0, 0)
        if game.key_pressed['left']:
            self.velocity.x -= self.speed
        if game.key_pressed['right']:
            self.velocity.x += self.speed

        self.rect.pos.x += self.velocity.x / game.fps
        self.rect.pos.y += self.velocity.y / game.fps

    def render(self, game):
        field = game.field
        Render.draw_rect_center_cam(game.surface, self.rect, field.camera)