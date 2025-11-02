import pygame, sys, random

from script.res import *

from script.shape import *
from script.render import *

class Field():
    def __init__(self):
        self.camera = Rect2(0, 0, 1280, 720)
        self.player = FieldPlayer()
        self.unit = [Unit()]
        self.proj = [Projectile()]
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
        if self.type == 'coin':
            Render.render_center_cam(game.surface, Image.coin, self.rect, game.field.camera)
        elif self.type == 'exporb':
            Render.render_center_cam(game.surface, Image.exporb, self.rect, game.field.camera)

class Projectile():
    def __init__(self):
        self.rect = Rect2(0, 0, 40, 40)
        self.side = 0
        self.speed = 640.0
        self.damage = 5
        self.life_time = 1
        self.v_unit = Vec2(1.0, 0.0)

    def handle_tick(self, game):
        self.collide_check(game)
        self.handle_life_time(game)
        self.move(game)

    def collide_check(self, game):
        field = game.field
        if self.side == 0:
            for i in range(len(field.unit) - 1, -1, -1):
                if Vec2.distance(field.unit[i].rect.pos, self.rect.pos) < 60:
                    field.unit[i].hp -= self.damage
                    field.proj.pop(field.proj.index(self))

    def move(self, game):
        self.rect.pos.x += self.speed * self.v_unit.x / game.fps
        self.rect.pos.y += self.speed * self.v_unit.y / game.fps

    def handle_life_time(self, game):
        field = game.field
        if self.life_time <= 0:
            field.proj.pop(field.proj.index(self))
        else:
            self.life_time -= 1.0 / game.fps

    def render(self, game):
        Render.render_center_cam(game.surface, Image.projectile, self.rect, game.field.camera)

class Unit():
    def __init__(self):
        self.rect = Rect2(160, -80, 80, 80)
        self.temp_pos = Vec2(0, 0)
        self.speed = 320.0
        self.hp = 60
        self.hp_max = 60
        self.attack = 0
        self.attack_type = 0
        self.attack_cool = 0
        self.state = 'attack'
        self.attack_target = 0

        self.frames = 4; self.frame_current = 0; self.frame_interval = 0.2; self.frame_time = 0
        self.frame_coord = [[0, 0], [80, 0], [160, 0], [240, 0]]

    def handle_tick(self, game):
        field = game.field
        if self.hp <= 0:
            field.unit.pop(field.unit.index(self))

    def render(self, game):
        self.frame_time += 1.0 / game.fps
        self.frame_current = int(self.frame_time / self.frame_interval) % self.frames
        surface = Image.unit.subsurface(pygame.Rect(self.frame_coord[self.frame_current][0], self.frame_coord[self.frame_current][1], self.rect.size.x, self.rect.size.y))
        Render.render_center_cam(game.surface, surface, self.rect, game.field.camera)

class FieldPlayer(Unit):
    def __init__(self):
        super().__init__()
        self.level = 0
        self.exp = 0
        self.exp_max = 10
        self.gold = 0
        self.energy = 0
        self.energy_max = 1

        self.hand = []
        self.deck = []
        self.deck_discarded = []

        self.rect = Rect2(0, 0, 80, 80)

    def adventure_start(self):
        self.hp = 120
        self.hp_max = 120
        self.level = 1
        self.exp = 0
        self.exp_max = 20
        self.energy = 0
        self.energy_max = 8

    def shoot(self, game, pos):
        direction = (pos - self.rect.pos).normalized()
        proj = Projectile()
        proj.rect.pos.x = self.rect.pos.x
        proj.rect.pos.y = self.rect.pos.y
        proj.v_unit = direction
        game.field.proj.append(proj)

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
        Render.render_center_cam(game.surface, Image.player, self.rect, game.field.camera)
