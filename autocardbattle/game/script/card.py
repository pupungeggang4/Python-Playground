import pygame, json

from script.res import *
from script.UI import *
from script.data import *

class Card():
    def __init__(self):
        self.ID = 0
        self.name = ''
        self.type = 'unit'
        self.element = ''
        self.crystal = []
        self.stat = []
        self.effect = []
        self.description = []

        self.surface = pygame.surface.Surface([UI.Card.rect[2], UI.Card.rect[3]], pygame.SRCALPHA)

    def set_data(self, ID):
        data = json.loads(json.dumps(Data.card[ID]))
        data_e = json.loads(json.dumps(Data.card_d[ID]))
        data_d = json.loads(json.dumps(Data.card_e[ID]))
        self.ID = ID
        self.name = data['name']
        self.type = data['type']
        self.element = data['element']
        self.crystal = data['crystal']
        self.stat = data['stat']
        self.effect = data_e
        self.description = data_d

    def render(self, screen, game, pos):
        self.surface.fill(Color.white)
        pygame.draw.rect(self.surface, Color.black, UI.Card.rect, 2)
        screen.blit(self.surface, pos)