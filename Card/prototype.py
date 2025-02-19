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
