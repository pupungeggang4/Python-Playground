class Player():
    hand = []
    deck = []
    energy = []

    energy_turn = 1
    power = 0
    hardness = 0
    energy_extra = 0
    draw_extra = 0
    hand_max = 8

    def draw_card(self):
        if len(self.deck) > 0 and len(self.hand) < self.hand_max:
            self.hand.append(self.deck.pop())

class Game():
    turn = 0

class Card():
    name = ''
    attack = 0
    hp = 0
    energy = []

    def __init__(self, data):
        self.name = data['name']
        self.energy = data['energy']
        self.attack = data['stat'][0]
        self.hp = data['stat'][1]
        self.play = data['play']

class Field():
    unit = []

class FieldThing():
    pass

class Empty(FieldThing):
    pass

    def __init__(self):
        pass

class Unit(FieldThing):
    attack = 0
    hp = 0

    def __init__(self):
        self.attack = 0
        self.hp = 2

class Leader(FieldThing):
    attack = 0
    hp = 30

    def __init__(self):
        self.attack = 0
        self.hp = 30
