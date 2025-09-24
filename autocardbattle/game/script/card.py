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

        for i in range(len(self.crystal)):
            rect_crystal = [UI.Card.crystal_start[0] + UI.Card.crystal_interval[0] * i, UI.Card.crystal_start[1], UI.crystal_size[0], UI.crystal_size[1]]
            pos_crystal = [UI.Card.crystal_text_start[0] + UI.Card.crystal_interval[0] * i, UI.Card.crystal_text_start[1]]
            pygame.draw.rect(self.surface, Color.black, rect_crystal, 2)
            self.surface.blit(Font.neodgm_32.render(f'{self.crystal[i][1]}', False, Color.black), pos_crystal)

        pygame.draw.rect(self.surface, [255, 255, 0], UI.Card.image)
        self.surface.blit(Font.neodgm_16.render(self.name, False, Color.black), UI.Card.text_name)

        if self.type == 'unit':
            self.surface.blit(Font.neodgm_32.render(f'{self.stat[0]}', False, Color.black), UI.Card.text_attack)
            self.surface.blit(Font.neodgm_32.render(f'{self.stat[1]}', False, Color.black), UI.Card.text_hp)

        screen.blit(self.surface, pos)
