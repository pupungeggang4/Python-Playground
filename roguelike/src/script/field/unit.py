import pygame, sys, random

from script.res import *

from script.shape import *
from script.render import *

from script.field.drop import *

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