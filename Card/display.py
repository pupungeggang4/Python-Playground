import prototype
import var

def display_all():
    display_field()
    display_player()

def display_player():
    print(f'Power: {var.player.power}, Hardness: {var.player.hardness}')
    print(f'Extra Energy: {var.player.energy_extra}, Extra Draw: {var.player.draw_extra}')
    display_hand()
    display_deck()

def display_hand():
    print('== Hand ==')
    for i in range(len(var.player.hand)):
        card = var.player.hand[i]
        print(f'{card.name} | {card.energy} | {card.attack}/{card.hp} | {card.play}')

def display_deck():
    print('== Deck ==')
    for i in range(len(var.player.deck)):
        card = var.player.deck[i]
        print(f'{card.name} | {card.energy} | {card.attack}/{card.hp}')

def display_field():
    for i in range(len(var.field.unit)):
        unit = var.field.unit[i]
        if isinstance(unit, prototype.Leader):
            print(f'|{unit.attack}/{unit.hp}'.ljust(20), end='')
        elif isinstance(unit, prototype.Empty):
            print('|'.ljust(20), end='')
        if i == 0 or i == 6 or i == 12 or i == 13:
            print('|')
