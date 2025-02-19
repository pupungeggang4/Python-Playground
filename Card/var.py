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

    def draw_card():
        if len(self.deck) > 0 and len(self.hand) < self.hand_max:
            self.hand.append(self.deck.pop())

class Field():
    unit = []

class Game():
    turn = 0
