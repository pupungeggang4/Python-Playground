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
        self.crystal_list = []
        self.stat = []
        self.effect = []
        self.played = []
        self.description = []

        self.surface = pygame.surface.Surface([UI.Card.rect[2], UI.Card.rect[3]], pygame.SRCALPHA)

    def set_data(self, ID):
        data = json.loads(json.dumps(Data.card[ID]))
        data_d = json.loads(json.dumps(Data.card_d[ID]))
        data_p = json.loads(json.dumps(Data.card_p[ID]))
        self.ID = ID
        self.name = data['name']
        self.type = data['type']
        self.element = data['element']
        self.crystal = data['crystal']
        self.crystal_list = data['crystal_list']
        self.stat = data['stat']
        self.effect = data['effect']
        self.played = data_p
        self.description = data_d

    def render(self, screen, game, pos):
        self.surface.fill(Color.white)
        pygame.draw.rect(self.surface, Color.black, UI.Card.rect, 2)

        for i in range(len(self.crystal)):
            pos_crystal = [UI.Card.crystal_start[0] + UI.Card.crystal_interval[0] * i, UI.Card.crystal_start[1], UI.crystal_size[0], UI.crystal_size[1]]
            pos_crystal_text = [UI.Card.crystal_text_start[0] + UI.Card.crystal_interval[0] * i, UI.Card.crystal_text_start[1]]
            self.surface.blit(Image.crystal[self.crystal[i][0]], pos_crystal)
            self.surface.blit(Font.neodgm_32.render(f'{self.crystal[i][1]}', False, Color.black), pos_crystal_text)

        self.surface.blit(Image.card[self.ID], UI.Card.image)
        self.surface.blit(Font.neodgm_16.render(self.name, False, Color.black), UI.Card.text_name)

        for i in range(len(self.description)):
            pos_d = [UI.Card.text_description[0], UI.Card.text_description[1] + UI.Card.text_description[3] * i]
            self.surface.blit(Font.neodgm_16.render(self.description[i], False, Color.black), pos_d)

        if self.type == 'unit':
            self.surface.blit(Font.neodgm_32.render(f'{self.stat[0]}', False, Color.black), UI.Card.text_attack)
            self.surface.blit(Font.neodgm_32.render(f'{self.stat[1]}', False, Color.black), UI.Card.text_hp)

        screen.blit(self.surface, pos)

    def clone(self):
        card = Card()
        card.ID = self.ID
        card.name = self.name
        card.type = self.type
        card.element = self.element
        card.crystal = json.loads(json.dumps(self.crystal))
        card.crystal_list = json.loads(json.dumps(self.crystal_list))
        card.stat = json.loads(json.dumps(self.stat))
        card.effect = json.loads(json.dumps(self.effect))
        card.played = json.loads(json.dumps(self.played))
        card.description = json.loads(json.dumps(self.description))
        return card
