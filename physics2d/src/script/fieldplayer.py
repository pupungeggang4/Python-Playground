import pygame, sys

from script.render import *
from script.shape import *

from script.entity import *

class FieldPlayer(Entity):
    def __init__(self):
        self.rect = Rect2(0, 0, 80, 80)

    def handle_tick(self, game):
        pass

    def render(self, game):
        field = game.field
        Render.draw_rect_center_cam(game.surface, self.rect, field.camera)