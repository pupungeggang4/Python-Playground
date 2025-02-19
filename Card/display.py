import prototype
import var

def display_all():
    display_field()
    display_player()

def display_player():
    print(f'Power: {var.Player.power}, Hardness: {var.Player.hardness}')
    print(f'Extra Energy: {var.Player.energy_extra}, Extra Draw: {var.Player.draw_extra}')
    display_hand()

def display_hand():
    for i in range(len(var.Player.hand)):
        card = var.Player.hand[i]
        print(f'{card.name} | {card.energy} | {card.attack}/{card.hp}')

def display_field():
    for i in range(len(var.Field.unit)):
        unit = var.Field.unit[i]
        if isinstance(unit, prototype.Leader):
            print(f'|{unit.attack}/{unit.hp}'.ljust(20), end='')
        elif isinstance(unit, prototype.Empty):
            print('|'.ljust(20), end='')
        if i == 0 or i == 6 or i == 12 or i == 13:
            print('|')
