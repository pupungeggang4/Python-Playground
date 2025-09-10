import pygame
from script.res import *
from script.shape import *

class FieldThing():
    def __init__(self):
        pass

class Wall(FieldThing):
    def __init__(self):
        pass

class Player(FieldThing):
    def __init__(self):
        pass

class Collectible(FieldThing):
    def __init__(self):
        pass

class Coin(Collectible):
    def __init__(self):
        self.surface = pygame.surface.Surface([40, 40], pygame.SRCALPHA)
        self.render_time = 0
        self.render_frame = 0
        self.render_frame_max = 4
        self.render_interval = 200

    def render(self, game, screen):
        self.render_time += int(1000 / game.fps)
        self.render_frame = self.render_time // self.render_interval % self.render_frame_max
        self.surface.fill(Color.transparent)
        self.surface.blit(Image.Sprite.coin, [0, 0], [self.render_frame * 40, 0, 40, 40])
        screen.blit(self.surface, [0, 0])

