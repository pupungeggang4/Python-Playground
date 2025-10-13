import pygame, sys, json
from script.ui import *
from script.res import *
from script.shape import *
from script.render import *

class Village():
    def __init__(self):
        self.player = VillagePlayer()
        self.camera = Rect2(0, 0, 1280, 720)
        self.thing = [VillagePortal(), VillagePortal()]
        self.thing[0].rect = Rect2(0, -400, 80, 80)

    def handle_tick(self, game):
        self.player.handle_tick(self, game)

    def render(self, surface, game):
        self.player.render(surface, self, game)
        for i in range(len(self.thing)):
            self.thing[i].render(surface, self, game)

class VillagePlayer():
    def __init__(self):
        self.rect = Rect2(0, 0, 80, 80)
        self.speed = 320.0
        self.surface = pygame.surface.Surface([self.rect.size.x, self.rect.size.y], pygame.SRCALPHA)

    def handle_tick(self, village, game):
        self.move_player(village, game)

    def move_player(self, village, game):
        if game.key_pressed['left'] == True:
            self.rect.pos.x -= self.speed / game.fps
        if game.key_pressed['right'] == True:
            self.rect.pos.x += self.speed / game.fps
        if game.key_pressed['up'] == True:
            self.rect.pos.y -= self.speed / game.fps
        if game.key_pressed['down'] == True:
            self.rect.pos.y += self.speed / game.fps

    def render(self, surface, village, game):
        self.surface.fill(Color.black)
        Render.render_center_cam(surface, self.surface, self.rect, village.camera)

class VillagePortal():
    def __init__(self):
        self.rect = Rect2(0, 0, 80, 80)
        self.surface = pygame.surface.Surface([self.rect.size.x, self.rect.size.y], pygame.SRCALPHA)
        self.surface.blit(Image.portal, [0, 0])

    def render(self, surface, village, game):
        Render.render_center_cam(surface, self.surface, self.rect, village.camera)
