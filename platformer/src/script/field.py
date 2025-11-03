import pygame, sys

from script.shape import *
from script.res import *
from script.render import *

class Field():
    def __init__(self):
        self.camera = Rect2(0, 0, 1280, 720)
        self.player = FieldPlayer()
        self.entity_list = [Coin()]
        self.mech_list = [Wall()]

    def handle_tick(self, game):
        self.player.handle_tick(game)
        for i in range(len(self.entity_list) - 1, -1, -1):
            self.entity_list[i].handle_tick(game)
        for i in range(len(self.mech_list) - 1, -1, -1):
            self.mech_list[i].handle_tick(game)

    def render(self, game):
        self.player.render(game)
        for i in range(len(self.entity_list)):
            self.entity_list[i].render(game)
        for i in range(len(self.mech_list)):
            self.mech_list[i].render(game)

class Entity():
    def __init__(self):
        self.rect = Rect2(0, 0, 80, 80)

class Wall(Entity):
    def __init__(self):
        self.rect = Rect2(0, 80, 160, 40)
        self.surface = None
        
    def handle_tick(self, game):
        pass

    def render(self, game):
        Render.draw_rect_center_cam(game.surface, self.rect, game.field.camera)

class Platform(Entity):
    pass

class Belt(Entity):
    pass

class Coin(Entity):
    def __init__(self):
        self.rect = Rect2(160, 0, 40, 40)
        self.surface = Image.sprite['coin']
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
        sprite = self.surface.subsurface(self.frame_coord[self.frame_current])
        Render.render_center_cam(game.surface, sprite, self.rect, field.camera)

class FieldPlayer(Entity):
    def __init__(self):
        super().__init__()
        self.surface = Image.player
        self.speed = 200.0
        self.jump_num = 1; self.jump_power = 40.0; self.jump_time = 0; self.jump_time_max = 0.2
        self.gravity = 800.0; self.terminal_speed = 800.0
        self.stepping = None

    def handle_tick(self, game):
        if game.key_pressed['left'] == True:
            self.rect.pos.x -= 320 / game.fps
        if game.key_pressed['right'] == True:
            self.rect.pos.x += 320 / game.fps

    def render(self, game):
        field = game.field
        Render.render_center_cam(game.surface, self.surface, self.rect, field.camera)