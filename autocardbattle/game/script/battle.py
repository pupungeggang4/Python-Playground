class Battle():
    def __init__(self):
        self.field = [
            None, None, None, None, None, None, None, None, None, None
        ]
        self.player = BattlePlayer()
        self.enemy = BattlePlayer()
        self.turn = 0
        self.turn_who = 0

class BattlePlayer():
    def __init__(self):
        self.crystal_num = 0
        self.hand_crystal = []
        self.deck_crystal = []
        self.hand = []
        self.deck = []