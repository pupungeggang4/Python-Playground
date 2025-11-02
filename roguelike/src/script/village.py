import pygame, sys, json

from script.ui import *
from script.res import *
from script.shape import *
from script.render import *

class Village():
    def __init__(self):
        self.player = VillagePlayer()
        self.camera = Rect2(0, 0, 1280, 720)
        self.portal_shop = VillagePortal()
        self.portal_battle = VillagePortal()
        self.portal_shop.rect.pos = Vec2(400, 0)
        self.portal_battle.rect.pos = Vec2(0, -400)

    def handle_tick(self, game):
        self.player.handle_tick(game)
        self.adjust_camera()

    def adjust_camera(self):
        self.camera.pos.x = self.player.rect.pos.x
        self.camera.pos.y = self.player.rect.pos.y
    
    def render(self, game):
        self.portal_shop.render(game)
        self.portal_battle.render(game)
        self.player.render(game)

class VillagePlayer():
    def __init__(self):
        self.speed = 320.0
        self.rect = Rect2(0, 0, 80, 80)
        self.surface = pygame.surface.Surface([self.rect.size.x, self.rect.size.y], pygame.SRCALPHA)

    def handle_tick(self, game):
        self.move_player(game)

    def move_player(self, game):
        if game.key_pressed['left'] == True:
            self.rect.pos.x -= self.speed / game.fps
        if game.key_pressed['right'] == True:
            self.rect.pos.x += self.speed / game.fps
        if game.key_pressed['up'] == True:
            self.rect.pos.y -= self.speed / game.fps
        if game.key_pressed['down'] == True:
            self.rect.pos.y += self.speed / game.fps

    def handle_interact(self, game):
        if Vec2.distance(self.rect.pos, game.village.portal_shop.rect.pos) < 80:
            pass
        elif Vec2.distance(self.rect.pos, game.village.portal_battle.rect.pos) < 80:
            game.state = 'battle_confirm'
            game.selected_battle_confirm = 0

    def render(self, game):
        surface = game.surface
        village = game.village
        Render.render_center_cam(surface, Image.player, self.rect, village.camera)

class VillagePortal():
    def __init__(self):
        self.rect = Rect2(0, 0, 80, 80)

    def render(self, game):
        surface = game.surface
        village = game.village
        Render.render_center_cam(surface, Image.portal, self.rect, village.camera)
