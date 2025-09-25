import pygame, json

from script.UI import *

class Unit():
    def __init__(self):
        self.ID = 0
        self.attack = 0
        self.hp = 0
        self.hp_max = 0
        self.effect = []

        self.surface = pygame.surface.Surface(UI.Field.unit_size, pygame.SRCALPHA)