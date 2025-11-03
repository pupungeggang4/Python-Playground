class Adventure():
    def __init__(self):
        self.player = AdventurePlayer()
        self.floor = 0
        self.layout = [
            ['plain', 'plain', 'plain'],
            ['plain', 'plain', 'plain'],
            ['plain', 'plain', 'plain'],
            ['plain', 'plain', 'plain'],
            ['plain', 'plain', 'plain'],
            ['plain', 'plain', 'plain'],
            ['plain', 'plain', 'plain'],
            ['plain', 'plain', 'plain'],
            ['plain', 'plain', 'plain'],
            ['plain', 'plain', 'plain'],
            ['plain', 'plain', 'plain'],
        ]

class AdventurePlayer():
    def __init__(self):
        self.gold = 0
        self.deck = []
        self.equipment = []