import pygame, sys

from script.res import *

from script.shape import *
from script.entity import *

from script.render import *

class Coin(Entity):
    def __init__(self):
        self.rect = Rect2(0, 0, 40 ,40)
        self.rigid = False
        self.fall = False
        
        self.surface = Image.sprite['coin']
        self.frame_time = 0
        self.frame_interval = 0.2
        self.frames = 4
        self.frame_current = 0
        self.frame_coord = [[0, 0, 40, 40], [40, 0, 40, 40], [80, 0, 40, 40], [120, 0, 40, 40]]

    def handle_tick(self, game):
        entity_list = game.field.entity_list
        player = game.field.player
        if Rect2.collision_check_simple(self.rect, player.rect):
            entity_list.pop(entity_list.index(self))

    def render(self, game):
        self.frame_time += 1 / game.fps
        self.frame_current = int(self.frame_time / self.frame_interval) % self.frames
        sub_surface = self.surface.subsurface(self.frame_coord[self.frame_current])
        Render.render_center_cam(game.surface, sub_surface, self.rect, game.field.camera)