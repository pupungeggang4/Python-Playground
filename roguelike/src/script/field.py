import pygame, sys, random

from script.res import *

from script.shape import *
from script.render import *
from script.weapon import *

class Field():
    def __init__(self):
        self.camera = Rect2(0, 0, 1280, 720)
        self.player = FieldPlayer()
        self.unit = []
        self.proj = []
        self.effect = []
        self.drop = []

    def adventure_start(self, game):
        self.camera = Rect2(0, 0, 1280, 720)
        self.player = FieldPlayer()
        self.unit = []
        self.unit.append(Unit())
        self.proj = []
        self.effect = []
        self.drop = []
        self.player.adventure_start(game)

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
        self.rect = Rect2(0, 0, 40, 40)
        self.type = 'coin'
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
        self.rect = Rect2(400, 0, 80, 80)
        self.temp_pos = Vec2(0, 0)
        self.speed = 160.0
        self.hp = 60
        self.hp_max = 60
        self.attack = 120
        self.attack_type = 0
        self.attack_cool = 1.0
        self.state = 'chase'
        self.gold = 10
        self.exp = 10

        self.frames = 4; self.frame_current = 0; self.frame_interval = 0.2; self.frame_time = 0
        self.frame_coord = [[0, 0], [80, 0], [160, 0], [240, 0]]

    def handle_tick(self, game):
        field = game.field
        player = game.field.player

        self.move_and_attack(game)
        self.handle_death(game)

    def move_and_attack(self, game):
        field = game.field
        player = game.field.player
        diff = player.rect.pos - self.rect.pos

        if self.state == 'chase':
            if diff.length() < 80:
                self.state = 'attack'
                self.attack_cool = 1.0
            else:
                diff_n = diff.normalized()
                self.rect.pos += diff_n * (self.speed / game.fps)
        elif self.state == 'attack':
            if self.attack_cool <= 0:
                if diff.length() < 80:
                    player.hp -= self.attack
                    self.attack_cool -= 1.0
                self.state = 'chase'
            else:
                self.attack_cool -= 1 / game.fps

    def handle_death(self, game):
        field = game.field

        if self.hp <= 0:
            coin = Drop()
            exporb = Drop()
            coin.set_data('coin', self.gold)
            coin.rect.pos = Vec2(self.rect.pos.x + random.randint(-10, 10), self.rect.pos.y + random.randint(-10, 10))
            exporb.set_data('exporb', self.exp)
            exporb.rect.pos = Vec2(self.rect.pos.x  + random.randint(-10, 10), self.rect.pos.y + random.randint(-10, 10))
            field.drop.append(coin)
            field.drop.append(exporb)
            field.unit.pop(field.unit.index(self))

    def render(self, game):
        self.frame_time += 1.0 / game.fps
        self.frame_current = int(self.frame_time / self.frame_interval) % self.frames
        surface = Image.unit.subsurface(pygame.Rect(self.frame_coord[self.frame_current][0], self.frame_coord[self.frame_current][1], self.rect.size.x, self.rect.size.y))
        Render.render_center_cam(game.surface, surface, self.rect, game.field.camera)
        tl = Render.find_top_left(self.rect, game.field.camera)
        pygame.draw.rect(game.surface, Color.green_dark, [tl[0], tl[1], self.hp / self.hp_max * 80, 10])

class FieldPlayer(Unit):
    def __init__(self):
        super().__init__()
        self.level = 0
        self.exp = 0
        self.exp_max = 10
        self.gold = 0
        self.energy = 0
        self.energy_max = 1

        self.speed = 320.0
        self.speed_dash = 1200.0
        self.dash_time = 0.2
        self.dash_time_left = 0
        self.dash_cool = 1.5
        self.dash_cool_left = 1.5
        self.attack = 10
        self.attack_speed = 1.0
        self.weapon = Weapon()

        self.hand = []
        self.deck = []
        self.deck_discarded = []

        self.rect = Rect2(0, 0, 80, 80)

    def adventure_start(self, game):
        self.rect = Rect2(0, 0, 80, 80)
        self.hp = 120
        self.hp_max = 120
        self.level = 1
        self.exp = 0
        self.exp_max = 20
        self.energy = 0
        self.energy_max = 8
        self.weapon.set_data(1)

    def shoot(self, game, pos):
        if self.weapon.attack_cool <= 0:
            direction = (pos - self.rect.pos).normalized()
            proj = Projectile()
            proj.damage = self.attack * self.weapon.attack_mul
            proj.rect.pos.x = self.rect.pos.x
            proj.rect.pos.y = self.rect.pos.y
            proj.v_unit = direction
            game.field.proj.append(proj)
            self.weapon.attack_cool = 1 / (self.attack_speed * self.weapon.attack_speed)

    def dash(self, game):
        if self.dash_cool_left <= 0:
            self.dash_cool_left = self.dash_cool
            self.dash_time_left = self.dash_time

    def handle_tick(self, game):
        self.move(game)
        self.handle_weapon(game)
        if self.hp <= 0:
            game.state = 'game_over'

    def move(self, game):
        pos = self.rect.pos
        self.temp_pos.x = pos.x
        self.temp_pos.y = pos.y
        speed = self.speed

        if self.dash_time_left >= 0:
            speed = self.speed_dash
            self.dash_time_left -= 1 / game.fps
        else:
            if self.dash_cool_left >= 0:
                self.dash_cool_left -= 1 / game.fps

        if game.key_pressed['left'] == True:
            self.temp_pos.x -= speed / game.fps
        if game.key_pressed['right'] == True:
            self.temp_pos.x += speed / game.fps
        if game.key_pressed['up'] == True:
            self.temp_pos.y -= speed / game.fps
        if game.key_pressed['down'] == True:
            self.temp_pos.y += speed / game.fps

        pos.x = self.temp_pos.x
        pos.y = self.temp_pos.y

    def handle_weapon(self, game):
        if self.weapon.attack_cool >= 0:
            self.weapon.attack_cool -= 1.0 / game.fps

    def render(self, game):
        Render.render_center_cam(game.surface, Image.player, self.rect, game.field.camera)
