import json
from script.data import *

class Weapon():
    def __init__(self):
        self.ID = 1
        self.attack_mul = 1.0
        self.attack_speed = 1.0
        self.attack_cool = 1.0

    def set_data(self, ID):
        self.ID = 1
        data = json.loads(json.dumps(Data.weapon[ID]))
        self.attack_mul = data['stat'][0]
        self.attack_speed = data['stat'][1]
        self.attack_cool = 1 / self.attack_speed