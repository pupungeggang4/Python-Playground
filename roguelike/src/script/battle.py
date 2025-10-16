class Battle():
    def __init__(self):
        self.player = Player()
        self.unit = []
        self.proj = []

class Unit():
    def __init__(self):
        self.hp = 0
        self.hp_max = 0
        self.attack = 0
        self.attack_type = 0
        self.attack_cool = 0

class Player(Unit):
    def __init__(self):
        self.__super__()