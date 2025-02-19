import card
import var
import data
import game
import display

def init():
    game.game_init()

def main():
    while True:
        i = input('Enter Command: ')

        if i == 'quit':
            break

        elif i == 'player':
            display.display_player()

        elif i == 'hand':
            display.display_hand()

        elif i == 'field':
            display.display_field()

        elif i == 'all':
            display.display_all()

if __name__ == '__main__':
    init()
    main()
