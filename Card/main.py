import card
import var
import data
import game
import display

import json

def init():
    game.game_init()

def main():
    var.state = ''
    var.card_playing = {}

    while True:
        i = input(f'({var.state})Enter Command: ')

        if var.state == '':
            if i == 'quit':
                break

            elif i == 'player':
                display.display_player()

            elif i == 'hand':
                display.display_hand()

            elif i == 'deck':
                display.display_deck()

            elif i == 'field':
                display.display_field()

            elif i == 'all':
                display.display_all()

            elif i == 'draw':
                var.player.draw_card()

            elif i == 'play':
                var.state = 'play'
        
        elif var.state == 'play':
            if i.isdecimal():
                if int(i) < len(var.player.hand):
                    var.card_playing = var.player.hand[int(i)]
                    card.process_stack = []
                    card.process_stack.append(json.loads(json.dumps(var.card_playing.play)))
                    card.card_var = {}
                    card.process_statement(var.player, var.field)

        elif var.state == 'playing':
            if i.isdecimal():
                l = card.card_literal.pop()
                card_var[l] = int(i)

if __name__ == '__main__':
    init()
    main()
