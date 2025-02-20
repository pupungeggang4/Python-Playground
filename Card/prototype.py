import data

class Field():
    unit = []

    def __init__(self):
        self.unit = [
            Leader(),
            FieldElement(), FieldElement(), FieldElement(), FieldElement(), FieldElement(), FieldElement(),
            FieldElement(), FieldElement(), FieldElement(), FieldElement(), FieldElement(), FieldElement(),
            Leader()
        ]

    def render(self):
        print('== Field ==')
        for i in range(14):
            unit = self.unit[i]
            print('|', end='')
            if type(unit) == Leader or type(unit) == Unit:
                print(f'{unit.attack}/{unit.hp}'.ljust(20, ' '), end='')
            else:
                print(''.ljust(20, ' '), end='')
            if i == 0 or i == 6 or i == 12 or i == 13:
                print('|')

class Player():
    hand = []
    deck = []

    def __init__(self):
        self.hand = [Card(data.card[1]), Card(data.card[2]), Card(data.card[3]), Card(data.card[4])]

    def render(self):
        print('== Player ==')
        print('== Hand ==')
        for i in range(len(self.hand)):
            self.hand[i].render()
        print('== Deck ==')
        for i in range(len(self.deck)):
            self.deck[i].render()

class FieldElement():
    attack = 0
    hp = 0

class Unit(FieldElement):
    def __init__(self, info):
        self.attack = info['stat'][0]
        self.hp = info['stat'][1]

class Leader(FieldElement):
    def __init__(self):
        self.attack = 0
        self.hp = 30

class Card():
    name = 'card'
    attack = 0
    hp = 0
    play = []

    def __init__(self, data):
        self.name = data['name']
        self.attack = data['stat'][0]
        self.hp = data['stat'][1]
        self.play = data['play']

    def render(self):
        if self.hp > 0:
            print(f'{self.name} | {self.attack}/{self.hp} | {self.play}')
        else:
            print(f'{self.name} | {self.play}')
