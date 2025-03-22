import pygame

import var
import res

from render import *

from primitive import *
from protounit import Unit

class Player(Unit):
    hand = []
    deck = []

    def __init__(self):
        super().__init__()

    def render(self):
        render_rect_center_cam(res.COLOR_BLACK, self.rect, var.camera, 2)
        self.render_destination()

    def render_destination(self):
        if self.moving == True:
            render_rect_center_cam(res.COLOR_BLACK, Rect2D(self.destination.x, self.destination.y, 40, 40), var.camera, 2)