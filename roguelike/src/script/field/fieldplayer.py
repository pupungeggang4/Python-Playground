import pygame, sys, random

from script.res import *

from script.shape import *
from script.weapon import *

from script.render import *

from script.field.unit import *
from script.field.projectile import *

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