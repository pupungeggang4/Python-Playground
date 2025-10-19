import pygame, json

from script.res import *
from script.UI import *
from script.data import *

class Unit():
    def __init__(self):
        self.ID = 0
        self.attack = 0
        self.hp = 0
        self.hp_max = 0
        self.effect = []
        self.attack_num = 0
        self.armor = 0

        self.surface = pygame.surface.Surface(UI.Unit.size, pygame.SRCALPHA)

    def set_unit_from_data(self, card, effect):
        self.ID = card.ID
        self.attack = card.stat[0]
        self.hp = card.stat[1]
        self.hp_max = card.stat[1]
        self.effect = json.loads(json.dumps(effect))

    def set_unit_from_player(self, player):
        self.ID = player.ID
        self.attack = 0
        self.hp = player.hp
        self.hp_max = player.hp
        self.effect = []

    def set_unit_from_enemy(self, ID):
        self.ID = ID
        self.attack = 0
        self.hp = Data.enemy[ID]['hp']
        self.hp_max = Data.enemy[ID]['hp']
        self.effect = []

    def set_unit_from_card(self, card):
        self.ID = card.ID
        self.attack = card.stat[0]
        self.hp = card.stat[1]
        self.hp_max = card.stat[1]
        self.effect = json.loads(json.dumps(card.effect))

    def take_damage(self, dmg):
        if self.armor >= dmg:
            self.armor -= dmg
        else:
            self.hp -= (dmg - self.armor)
            self.armor = 0

    def render(self, surface, game, pos):
        self.surface.fill(Color.transparent)
        self.surface.blit(Image.unit[self.ID], UI.Unit.image)
        if self.armor > 0:
            self.surface.blit(Font.neodgm_32.render(str(self.armor), False, Color.black), UI.Unit.text_armor)
        self.surface.blit(Font.neodgm_32.render(str(self.attack), False, Color.black), UI.Unit.text_attack)
        self.surface.blit(Font.neodgm_32.render(str(self.hp), False, Color.black), UI.Unit.text_hp)
        surface.blit(self.surface, pos)
