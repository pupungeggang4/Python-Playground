import pygame

import var
import res

from render import *
from primitive import *

class Unit():
    def __init__(self):
        self.rect = Rect2D(0, 0, 80, 80)
        self.destination = Vector2D(0, 0)
        self.speed = 320
        self.moving = False

    def handle_tick(self):
        self.move()

    def move(self):
        if self.moving == True:
            diff = Vector2D.sub(self.destination, self.rect.position)
            if diff.magnitude() > 10:
                diffn = diff.normalized()
                self.rect.position.x += self.speed * diffn.x / var.FPS
                self.rect.position.y += self.speed * diffn.y / var.FPS
            else:
                self.moving = False 

    def render(self):
        render_rect_center_cam(res.COLOR_BLACK, self.rect, var.camera, 2)