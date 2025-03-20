import pygame

import var
import res

from render import *
from primitive import *

class Unit():
    def __init__(self):
        self.rect = Rect2D(0, 0, 80, 80)
        self.destination = Vector2D(0, 0)
        self.moving = False

    def render(self):
        render_rect_center_cam(res.COLOR_BLACK, self.rect, var.camera, 2)