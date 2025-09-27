import json, random

from script.data import *
from script.card import *
from script.crystal import *
from script.unit import *

class Battle():
    def __init__(self):
        self.field = [
            None, None, None, None, None, None, None, None, None, None
        ]
        self.player = BattlePlayer()
        self.enemy = BattlePlayer()
        self.turn = 0
        self.turn_who = 0

    def start_battle(self, game):
        self.turn = 0
        self.turn_who = 0
        self.field = [
            None, None, None, None, None, None, None, None, None, None
        ]
        self.player.start_battle_player(game.player)
        self.enemy.start_battle_enemy(1)
        unit_p = Unit()
        unit_p.set_unit_from_player(game.player)
        self.field[0] = unit_p
        unit_e = Unit()
        unit_e.set_unit_from_enemy(1)
        self.field[5] = unit_e

class BattlePlayer():
    def __init__(self):
        self.crystal_num = 0
        self.crystal_deck = []
        self.deck = []

    def start_battle_player(self, player):
        self.crystal_num
        self.deck = []
        self.crystal_deck = []

        deck_list = []
        crystal_list = []

        for i in range(len(player.deck)):
            deck_list.append(player.deck[i].clone())
        
        for i in range(len(player.crystal_deck)):
            crystal_list.append(player.crystal_deck[i].clone())

        while len(deck_list) > 0:
            i = random.randint(0, len(deck_list) - 1)
            self.deck.append(deck_list.pop(i))

        while len(crystal_list) > 0:
            i = random.randint(0, len(crystal_list) - 1)
            self.crystal_deck.append(crystal_list.pop(i))

    def start_battle_enemy(self, ID):
        data_deck = json.loads(json.dumps(Data.enemy[ID]['deck']))
        data_crystal = json.loads(json.dumps(Data.enemy[ID]['crystal']))

        self.deck = []
        self.crystal_deck = []

        for i in range(len(data_deck)):
            card = Card()
            card.set_data(data_deck[i])
            self.deck.append(card)

        for i in range(len(data_crystal)):
            crystal = Crystal()
            crystal.set_data(data_crystal[i])
            self.crystal_deck.append(crystal)
