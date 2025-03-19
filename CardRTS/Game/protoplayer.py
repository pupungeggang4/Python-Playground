import pygame

import var
import res

from render import *

from protounit import Unit

class Player(Unit):
    def __init__(self):
        super().__init__()

    def render(self):
        render_rect_center_cam(res.COLOR_BLACK, self.rect, var.camera)