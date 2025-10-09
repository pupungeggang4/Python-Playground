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
        self.proceed_time = 0.5
        self.paused = True
        self.action_queue = []

    def handle_tick(self, game):
        if self.paused == False:
            if self.proceed_time < 0:
                self.proceed(game)
                self.proceed_time = 0.5
            else:
                self.proceed_time -= 1 / game.fps

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
        if len(self.action_queue) <= 0:
            if self.turn_phase == 'start':
                if self.turn_who == 0:
                    self.player.turn_start(self)
                    self.turn += 1
                else:
                    self.enemy.turn_start(self)
                self.turn_phase = 'play'
            elif self.turn_phase == 'play':
                if self.turn_who == 0:
                    self.player.play_card_try(self)
                else:
                    self.enemy.play_card_try(self)
            elif self.turn_phase == 'battle':
                if self.turn_who == 0:
                    self.player.make_battle_list(self)
                else:
                    self.enemy.make_battle_list(self)
                self.turn_phase = 'end'
            elif self.turn_phase == 'end':
                if self.turn_who == 0:
                    self.player.turn_end()
                    self.turn_who = 1
                else:
                    self.enemy.turn_end()
                    self.turn_who = 0
                self.turn_phase = 'start'
        else:
            self.do_action()

    def do_action(self):
        front = self.action_queue[0]
        if front[0] == 'summon':
            self.field[front[2]] = front[1]
        elif front[0] == 'attack_random':
            your_field = []
            attack_list = []
            if front[1] > 0 and front[1] < 5:
                your_field = [5, 6, 7, 8, 9]
            elif front[1] > 5:
                your_field = [0, 1, 2, 3, 4]
            for i in range(len(your_field)):
                if self.field[your_field[i]] != None:
                    attack_list.append(your_field[i])
            index = random.randint(0, len(attack_list) - 1)
            self.fight_unit(front[1], attack_list[index])

        if len(self.action_queue) > 0:
            self.action_queue.pop(0)

        for i in range(1, 5):
            if self.field[i] != None:
                if self.field[i].hp <= 0:
                    self.field[i] = None

        for i in range(6, 10):
            if self.field[i] != None:
                if self.field[i].hp <= 0:
                    self.field[i] = None

    def fight_unit(self, i1, i2):
        if self.field[i1] != None and self.field[i2] != None:
            self.field[i1].hp -= self.field[i2].attack
            self.field[i2].hp -= self.field[i1].attack
            print(f'unit{i1} attacked unit{i2}')

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
        self.my_character = []
        self.my_field = []
        self.my_hero = 0
        self.your_character = []
        self.your_field = []
        self.your_hero = 0

    def start_battle_player(self, player):
        self.crystal_num = 0
        self.deck = []
        self.crystal_deck = []
        self.crystal_hand = []
        self.attack = 0
        self.hardness = 0
        self.acceler = 0
        self.extra_crystal = 0
        self.my_character = [0, 1, 2, 3, 4]
        self.my_field = [1, 2, 3, 4]
        self.my_hero = 0
        self.your_character = [5, 6, 7, 8, 9]
        self.your_field = [6, 7, 8, 9]
        self.your_hero = 5

        for i in range(len(player.deck)):
            self.deck.append(player.deck[i].clone())
        
        for i in range(len(player.crystal_deck)):
            self.crystal_deck.append(player.crystal_deck[i].clone())

        random.shuffle(self.deck)
        random.shuffle(self.crystal_deck)

    def start_battle_enemy(self, ID):
        self.crystal_num = 0
        self.deck = []
        self.crystal_deck = []
        self.crystal_hand = []
        self.attack = 0
        self.hardness = 0
        self.acceler = 0
        self.extra_crystal = 0
        self.my_character = [5, 6, 7, 8, 9]
        self.my_field = [6, 7, 8, 9]
        self.my_hero = 5
        self.your_character = [0, 1, 2, 3, 4]
        self.your_field = [1, 2, 3, 4]
        self.your_hero = 0

        data_deck = json.loads(json.dumps(Data.enemy[ID]['deck']))
        data_crystal = json.loads(json.dumps(Data.enemy[ID]['crystal']))

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

    def turn_start(self, battle):
        if self.crystal_num < 8:
            self.crystal_num += 1
        self.draw_crystal(self.crystal_num + self.extra_crystal)

        for i in range(len(self.my_field)):
            if battle.field[self.my_field[i]] != None:
                battle.field[self.my_field[i]].attack_num = 1

    def play_card_try(self, battle):
        if len(self.deck) > 0:
            top = self.deck[0]
            if self.check_playable(top):
                if self.play_card(top, battle):
                    pay_list = self.make_pay_list(top)
                    for i in range(len(pay_list)):
                        self.crystal_deck.append(self.crystal_hand.pop(pay_list[i]))
                self.deck.pop(0)
            else:
                battle.turn_phase = 'battle'
        else:
            battle.turn_phase = 'battle'

        if self.acceler > 0:
            self.acceler -= 1
        else:
            battle.turn_phase = 'battle'

    def play_card(self, card, battle):
        played = json.loads(json.dumps(card.played))
        
        while len(played) > 0:
            front = played[0]
            if front[0] == 'summon':
                for i in range(len(self.my_field)):
                    if battle.field[self.my_field[i]] == None:
                        unit = Unit()
                        unit.set_unit_from_card(card)
                        battle.action_queue.append(['summon', unit, self.my_field[i]])
                        break

                    if i == len(self.my_field) - 1:
                        return False
            played.pop(0)
        
        return True

    def check_playable(self, card):
        crystal_list = json.loads(json.dumps(card.crystal_list))
        crystal_list.sort()

        if len(crystal_list) <= 0:
            return True

        for i in range(len(self.crystal_hand)):
            if self.crystal_hand[i].element == 1:
                if crystal_list[0] == 1:
                    crystal_list.pop(0)
                    if len(crystal_list) <= 0:
                        return True
                    
        for i in range(len(self.crystal_hand)):
            if self.crystal_hand[i].element >= 2 and self.crystal_hand[i].element <= 7:
                if crystal_list[0] == self.crystal_hand[i].element or crystal_list[0] == 1:
                    crystal_list.pop(0)
                    if len(crystal_list) <= 0:
                        return True
                    
        for i in range(len(self.crystal_hand)):
            if self.crystal_hand[i].element == 8:
                crystal_list.pop(0)
                if len(crystal_list) <= 0:
                    return True

        return False

    def make_pay_list(self, card):
        crystal_list = json.loads(json.dumps(card.crystal_list))
        crystal_list.sort()
        pay_list = []

        if len(crystal_list) <= 0:
            return []

        for i in range(len(self.crystal_hand)):
            if self.crystal_hand[i].element == 1:
                if crystal_list[0] == 1:
                    crystal_list.pop(0)
                    pay_list.append(i)
                    if len(crystal_list) <= 0:
                        pay_list.sort()
                        pay_list.reverse()
                        return pay_list
                    
        for i in range(len(self.crystal_hand)):
            if self.crystal_hand[i].element >= 2 and self.crystal_hand[i].element <= 7:
                if crystal_list[0] == self.crystal_hand[i].element or crystal_list[0] == 1:
                    crystal_list.pop(0)
                    pay_list.append(i)
                    if len(crystal_list) <= 0:
                        pay_list.sort()
                        pay_list.reverse()
                        return pay_list
                    
        for i in range(len(self.crystal_hand)):
            if self.crystal_hand[i].element == 8:
                crystal_list.pop(0)
                pay_list.append(i)
                if len(crystal_list) <= 0:
                    pay_list.sort()
                    pay_list.reverse()
                    return pay_list

        pay_list.sort()
        pay_list.reverse()
        return pay_list

    def make_battle_list(self, battle):
        for i in range(len(self.my_field)):
            unit = battle.field[self.my_field[i]]
            if unit != None:
                for j in range(unit.attack_num):
                    battle.action_queue.append(['attack_random', self.my_field[i]])

    def turn_end(self):
        pass

    def draw_crystal(self, num):
        for i in range(num):
            if len(self.crystal_deck) > 0:
                self.crystal_hand.append(self.crystal_deck.pop(0))