import pygame, json
from script.data import *
from script.card import *
from script.crystal import *

class Player():
    def __init__(self):
        self.hp = 0
        self.hp_max = 0
        self.deck = []
        self.crystal_deck = []
        self.equipment = []

    def create_player(self, ID):
        self.hp = 20
        self.deck = []
        self.crystal_deck = []

        data_deck = json.loads(json.dumps(Data.character[ID]['deck']))
        for i in range(len(data_deck)):
            card = Card()
            card.set_data(data_deck[i])
            self.deck.append(card)

        data_crystal_deck = json.loads(json.dumps(Data.character[ID]['crystal']))
        for i in range(len(data_crystal_deck)):
            crystal = Crystal()
            crystal.set_data(data_crystal_deck[i])
            self.crystal_deck.append(crystal)

class Adventure():
    def __init__(self):
        self.layout = [
            ['battle', 'battle', 'battle'],
            ['shop', 'shop', 'shop'],
            ['battle', 'battle', 'battle'],
            ['shop', 'shop', 'shop'],
            ['boss', 'boss', 'boss']
        ]
        self.round = 0

    def start_adventure(self):
        self.round = 0