import pygame, sys

from script.shape import *
from script.res import *
from script.render import *

class Field():
    def __init__(self):
        self.camera = Rect2(0, 0, 1280, 720)
        self.player = FieldPlayer()
        self.entity_list = [Coin()]

    def handle_tick(self, game):
        self.player.handle_tick(game)
        for i in range(len(self.entity_list) - 1, -1, -1):
            self.entity_list[i].handle_tick(game)

    def render(self, game):
        self.player.render(game)
        for i in range(len(self.entity_list)):
            self.entity_list[i].render(game)

class Entity():
    def __init__(self):
        self.rect = Rect2(0, 0, 80, 80)
        self.surface = pygame.surface.Surface([self.rect.size.x, self.rect.size.y], pygame.SRCALPHA)

class Wall(Entity):
    pass

class Platform(Entity):
    pass

class Belt(Entity):
    pass

class Coin(Entity):
    def __init__(self):
        self.rect = Rect2(160, 0, 40, 40)
        self.surface = pygame.surface.Surface([self.rect.size.x, self.rect.size.y], pygame.SRCALPHA)
        self.frame_time = 0
        self.frame_interval = 0.2
        self.frames = 4
        self.frame_current = 0
        self.frame_coord = [[0, 0, 40, 40], [40, 0, 40, 40], [80, 0, 40, 40], [120, 0, 40, 40]]

    def handle_tick(self, game):
        field = game.field
        player = game.player
        player_field = game.field.player
        if Vec2.distance(self.rect.pos, player_field.rect.pos) < 40:
            player.coin += 1
            field.entity_list.pop(field.entity_list.index(self))

    def render(self, game):
        field = game.field
        self.frame_time += 1 / game.fps
        self.frame_current = int((self.frame_time / self.frame_interval)) % self.frames
        self.surface.fill(Color.transparent)
        self.surface.blit(Image.sprite['coin'], [0, 0], self.frame_coord[self.frame_current])
        Render.render_center_cam(game.surface, self.surface, self.rect, field.camera)

class FieldPlayer(Entity):
    def __init__(self):
        super().__init__()

    def handle_tick(self, game):
        if game.key_pressed['left'] == True:
            self.rect.pos.x -= 320 / game.fps
        if game.key_pressed['right'] == True:
            self.rect.pos.x += 320 / game.fps

    def render(self, game):
        field = game.field
        self.surface.fill(Color.transparent)
        self.surface.blit(Image.player, [0, 0])
        Render.render_center_cam(game.surface, self.surface, self.rect, field.camera)