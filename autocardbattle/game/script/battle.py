import json, random

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
        self.player.start_battle(game.player)
        #self.enemy.build_deck()

class BattlePlayer():
    def __init__(self):
        self.crystal_num = 0
        self.crystal_deck = []
        self.deck = []

    def start_battle(self, player):
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