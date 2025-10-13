import pygame

from script.ui import *
from script.res import *
from script.shape import *

class Render():
    @staticmethod
    def render_center_cam(surface, source, rect, cam):
        pos = [
            rect.pos.x - rect.size.x / 2 - cam.pos.x + cam.size.x / 2,
            rect.pos.y - rect.size.y / 2 - cam.pos.y + cam.size.y / 2
        ]
        surface.blit(source, pos)
