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
        pass

class Player():
    hand = []
    deck = []

    def __init__(self):
        self.hand = [Card(data.card[1]), Card(data.card[2])]

    def render(self):
        print('== Player ==')
        print('== Hand ==')
        for i in range(len(self.hand)):
            self.hand[i].render()

class FieldElement():
    pass

class Unit(FieldElement):
    pass

class Leader(FieldElement):
    pass

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
