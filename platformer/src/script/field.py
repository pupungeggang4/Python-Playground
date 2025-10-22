import pygame, sys

from script.shape import *
from script.res import *

class Field():
    def __init__(self):
        self.entity_list = [Coin()]

    def render(self, game):
        for i in range(len(self.entity_list)):
            self.entity_list[i].render(game)

class Entity():
    pass

class Wall(Entity):
    pass

class Platform(Entity):
    pass

class Coin(Entity):
    def __init__(self):
        self.rect = Rect2(0, 0, 40, 40)
        self.surface = pygame.surface.Surface([self.rect.size.x, self.rect.size.y], pygame.SRCALPHA)
        self.frame_time = 0
        self.frame_interval = 0.2
        self.frames = 4
        self.frame_current = 0
        self.frame_coord = [[0, 0, 40, 40], [40, 0, 40, 40], [80, 0, 40, 40], [120, 0, 40, 40]]

    def render(self, game):
        field = game.field
        self.frame_time += 1 / game.fps
        self.frame_current = int((self.frame_time / self.frame_interval)) % self.frames
        self.surface.fill(Color.transparent)
        self.surface.blit(Image.sprite['coin'], [0, 0], self.frame_coord[self.frame_current])
        game.surface.blit(self.surface, [80, 80])

class Player():
    def __init__(self):
        self.rect = Rect2(0, 0, 80, 80)