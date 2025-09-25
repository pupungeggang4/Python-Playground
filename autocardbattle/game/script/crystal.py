import pygame, json

from script.data import *
from script.res import *
from script.UI import *

class Crystal():
    def __init__(self):
        self.ID = 0
        self.name = ''
        self.element = ''
        self.effect = []
        self.description = []

        self.surface = pygame.surface.Surface(UI.crystal_size, pygame.SRCALPHA)

    def set_data(self, ID):
        data = json.loads(json.dumps(Data.crystal[ID]))
        data_d = json.loads(json.dumps(Data.crystal_d[ID]))
        self.ID = ID
        self.name = data['name']
        self.element = data['element']
        self.effect = data['effect']
        self.description = data_d

    def render(self, surface, game, pos):
        self.surface.fill(Color.black)
        surface.blit(self.surface, pos)

    def clone(self):
        crystal = Crystal()
        crystal.ID = self.ID
        crystal.name = self.name
        crystal.element = self.element
        crystal.effect = json.loads(json.dumps(self.effect))
        crystal.description = json.loads(json.dumps(self.description))
        return crystal