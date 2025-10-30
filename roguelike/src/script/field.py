import pygame, sys, random

from script.res import *

from script.shape import *
from script.render import *

class Field():
    def __init__(self):
        self.camera = Rect2(0, 0, 1280, 720)
        self.player = FieldPlayer()
        self.unit = []
        self.proj = []
        self.drop = [Drop(), Drop(), Drop(), Drop()]

    def handle_tick(self, game):
        self.player.handle_tick(game)

        for i in range(len(self.unit) - 1, -1, -1):
            self.unit[i].handle_tick(game)

        for i in range(len(self.proj) - 1, -1, -1):
            self.proj[i].handle_tick(game)

        for i in range(len(self.drop) - 1, -1, -1):
            self.drop[i].handle_tick(game)

    def render(self, game):
        self.player.render(game)
        
        for i in range(len(self.unit)):
            self.unit[i].render(game)

        for i in range(len(self.proj)):
            self.proj[i].render(game)

        for i in range(len(self.drop)):
            self.drop[i].render(game)

class Drop():
    def __init__(self):
        self.rect = Rect2(random.randint(120, 240), random.randint(-60, 60), 40, 40)
        self.type = 'coin' if random.randint(1, 2) == 1 else 'exporb'
        self.amount = 10
        self.surface = pygame.surface.Surface([40, 40], pygame.SRCALPHA)

    def set_data(self, type, amount):
        self.type = type
        self.amount = amount

    def handle_tick(self, game):
        player = game.field.player
        if Vec2.distance(self.rect.pos, player.rect.pos) < 60:
            if self.type == 'coin':
                player.gold += self.amount
            elif self.type == 'exporb':
                player.exp += self.amount
                if player.exp >= player.exp_max:
                    player.exp -= player.exp_max
                    player.level += 1
            game.field.drop.pop(game.field.drop.index(self))

    def render(self, game):
        self.surface.fill(Color.transparent)
        if self.type == 'coin':
            self.surface.blit(Image.coin, [0, 0])
        elif self.type == 'exporb':
            self.surface.blit(Image.exporb, [0, 0])
        Render.render_center_cam(game.surface, self.surface, self.rect, game.field.camera)

class Projectile():
    def __init__(self):
        pass

    def handle_tick(self, game):
        pass

    def render(self, game):
        pass

class Unit():
    def __init__(self):
        self.rect = Rect2(0, 0, 40, 40)
        self.temp_pos = Vec2(0, 0)
        self.speed = 320.0
        self.hp = 0
        self.hp_max = 1
        self.attack = 0
        self.attack_type = 0
        self.attack_cool = 0
        self.state = []
        self.attack_target = 0
        self.surface = pygame.surface.Surface([40, 40], pygame.SRCALPHA)

    def handle_tick(self, game):
        pass

    def render(self, game):
        pass

class FieldPlayer(Unit):
    def __init__(self):
        super().__init__()
        self.level = 0
        self.exp = 0
        self.exp_max = 10
        self.gold = 0
        self.energy = 0
        self.energy_max = 1
        self.rect = Rect2(0, 0, 80, 80)
        self.card = []
        self.surface = pygame.surface.Surface([80, 80], pygame.SRCALPHA)

    def adventure_start(self):
        self.hp = 120
        self.hp_max = 120
        self.level = 1
        self.exp = 0
        self.exp_max = 20
        self.energy = 0
        self.energy_max = 8

    def handle_tick(self, game):
        self.move(game)

    def move(self, game):
        pos = self.rect.pos
        self.temp_pos.x = pos.x
        self.temp_pos.y = pos.y

        if game.key_pressed['left'] == True:
            self.temp_pos.x -= self.speed / game.fps
        if game.key_pressed['right'] == True:
            self.temp_pos.x += self.speed / game.fps
        if game.key_pressed['up'] == True:
            self.temp_pos.y -= self.speed / game.fps
        if game.key_pressed['down'] == True:
            self.temp_pos.y += self.speed / game.fps

        pos.x = self.temp_pos.x
        pos.y = self.temp_pos.y

    def render(self, game):
        self.surface.fill(Color.transparent)
        self.surface.blit(Image.player, [0, 0])
        Render.render_center_cam(game.surface, self.surface, self.rect, game.field.camera)
