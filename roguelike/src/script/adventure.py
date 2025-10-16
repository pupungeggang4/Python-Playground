class Adventure():
    def __init__(self):
        self.floor = 0
        self.layout = [
            ['rest', 'rest', 'rest'],
            ['battle', 'battle', 'battle'],
            ['battle', 'battle', 'battle'],
            ['shop', 'event', 'rest'],
            ['battle', 'battle', 'battle'],
            ['boss', 'boss', 'boss']
        ]
        self.player = AdventurePlayer()

    def start_adventure(self):
        self.floor = 0

class AdventurePlayer():
    def __init__(self):
        self.deck = []