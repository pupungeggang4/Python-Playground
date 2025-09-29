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
        self.turn_phase = 'start'
        self.paused = True

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

    def proceed(self, game):
        if self.turn_phase == 'start':
            if self.turn_who == 0:
                self.player.turn_start()
                self.turn += 1
            else:
                self.enemy.turn_start()
            self.turn_phase = 'play'
        elif self.turn_phase == 'play':
            self.turn_phase = 'battle'
        elif self.turn_phase == 'battle':
            self.turn_phase = 'end'
        elif self.turn_phase == 'end':
            if self.turn_who == 0:
                self.player.turn_end()
                self.turn_who = 1
            else:
                self.enemy.turn_end()
                self.turn_who = 0
            self.turn_phase = 'start'

class BattlePlayer():
    def __init__(self):
        self.crystal_num = 0
        self.crystal_deck = []
        self.crystal_hand = []
        self.deck = []
        self.attack = 0
        self.hardness = 0
        self.leadership = 0
        self.acceler = 0
        self.extra_crystal = 0

    def start_battle_player(self, player):
        self.crystal_num = 0
        self.deck = []
        self.crystal_deck = []
        self.crystal_hand = []
        self.attack = 0
        self.hardness = 0
        self.acceler = 0
        self.extra_crystal = 0

        for i in range(len(player.deck)):
            self.deck.append(player.deck[i].clone())
        
        for i in range(len(player.crystal_deck)):
            self.crystal_deck.append(player.crystal_deck[i].clone())

        random.shuffle(self.deck)
        random.shuffle(self.crystal_deck)

    def start_battle_enemy(self, ID):
        self.crystal_num = 0
        self.attack = 0
        self.hardness = 0
        self.acceler = 0
        self.extra_crystal = 0

        data_deck = json.loads(json.dumps(Data.enemy[ID]['deck']))
        data_crystal = json.loads(json.dumps(Data.enemy[ID]['crystal']))

        self.deck = []
        self.crystal_deck = []
        self.crystal_hand = []

        for i in range(len(data_deck)):
            card = Card()
            card.set_data(data_deck[i])
            self.deck.append(card)

        for i in range(len(data_crystal)):
            crystal = Crystal()
            crystal.set_data(data_crystal[i])
            self.crystal_deck.append(crystal)

        random.shuffle(self.deck)
        random.shuffle(self.crystal_deck)

    def turn_start(self):
        if self.crystal_num < 8:
            self.crystal_num += 1
        self.draw_crystal(self.crystal_num + self.extra_crystal)

    def play_card(self):
        pass

    def battle(self):
        pass

    def turn_end(self):
        pass

    def draw_crystal(self, num):
        for i in range(num):
            if len(self.crystal_deck) > 0:
                self.crystal_hand.append(self.crystal_deck.pop(0))