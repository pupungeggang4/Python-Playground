'''
Mana spending program.
A card has slots which mana must be placed.
A mana can be placed into card's slots.
When all of the slots are filled, the card can be played.
Displays result whether the card can played, mana used, mana left, and card slot status.

There are three types of slots.
1. Normal slot: Accepts all types of mana.
2. Color slot: Accepts same color of mana or rainbow mana.
3. Rainbow slot: Accepts only rainbow mana.

There are three types of mana.
1. Normal mana: Can be only placed in normal slot.
2. Color mana: Can be placed in normal and same color slot.
3. Rainbow mana: Can be placed in any slot.

Colors
0: normal, 1: fire, 2: aqua, 3: wind, 4: earth, 5: light, 6: dark, 7: rainbow.
'''

import os
import platform
import json

# Mana paying function
# Shows playable, mana used, mana left, and card mana slot status
# Card mana slot [[mana], filled]

def pay(card, mana):
    playable = True
    mana_used = []
    mana_left = mana_sort(mana)
    mana_index = 0
    card_index = 0

    print(f'Pay: {card}, {mana}')

    for card_index in range(len(card)):
        for mana_index in range(len(mana_left)):
            mana_required = card[card_index][0]
            mana_in_index = mana_left[mana_index]

            if mana_required == [0]:
                card[card_index][1] = json.loads(json.dumps(mana_in_index))
                mana_used.append(mana_left.pop(mana_index))
                break

            elif len(mana_required) == 1:
                if mana_in_index == [7] or mana_in_index == mana_required:
                    card[card_index][1] = json.loads(json.dumps(mana_in_index))
                    mana_used.append(mana_left.pop(mana_index))
                    break

    for i in range(len(card)):
        if card[i][1] == []:
            playable = False
            break

    print(f'Playable: {playable}')

    print('Used mana: ', end='')
    if len(mana_used) == 0:
        print('No mana used!', end='')
    for i in range(len(mana_used)):
        print(f'{mana_used[i]}', end='')

    print()

    print('Left mana: ', end='')
    if len(mana_left) == 0:
        print('No mana left!', end='')
    for i in range(len(mana_left)):
        print(f'{mana_left[i]}', end='')

    print()

    print(card)

    print()

    return [playable, mana_used, mana_left, card]

# Mana comparsion function
# Order: Normal mana > Color mana > Rainbow mana
def mana_compare(m1, m2):
    if m1 == m2:
        return 0
    elif m1 == [7]:
        return 1
    elif m2 == [7]:
        return -1
    elif len(m1) > len(m2):
        return 1
    elif len(m1) == len(m2):
        if m1[0] > m2[0]:
            return 1

    return -1

# Sorting mana on hand
# Order: Normal mana > Color mana > Rainbow mana
def mana_sort(m):
    for i in range(len(m)):
        for j in range(len(m) - 1):
            if mana_compare(m[j], m[j + 1]) > 0:
                tmp = m[j]
                m[j] = m[j + 1]
                m[j + 1] = tmp

    return m

def main():
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')
    
    # Test for free cards.
    pay([], [])
    pay([], [[0], [1], [2]])

    # Test for no-color mana.
    pay([ [[0], []], [[0], []] ], [[0], [0]])
    pay([ [[0], []], [[0], []], [[0], []] ], [[0], [0]])
    pay([ [[0], []] ], [[0], [0]])

    # Test for one-color mana.
    pay([ [[0], []], [[0], []], [[1], []] ], [[0], [1], [1]])
    pay([ [[0], []], [[1], []], [[1], []] ], [[0], [1], [0], [0]]),
    pay([ [[0], []], [[0], []], [[1], []] ], [[0], [0], [0], [1], [1]])

    # Test for two-color mana.
    pay([ [[0], []], [[0], []], [[1], []], [[2], []] ], [[0], [2], [0], [1]])
    pay([ [[0], []], [[1], []], [[1], []], [[2], []] ], [[1], [2], [0], [2], [0]])

    # Test for rainbow mana.
    pay([ [[0], []], [[0], []] ], [[7], [0]])
    pay([ [[0], []], [[3], []] ], [[7], [0]])
    pay([ [[0], []], [[7], []] ], [[0], [7]])
    pay([ [[1], []], [[2], []], [[3], []] ], [[7], [7], [7]])
    pay([ [[0], []], [[1], []], [[7], []] ], [[0], [7], [7]])
    pay([ [[0], []], [[1], []], [[2], []] ], [[0], [0], [7]])

    # Test for rainbow mana and one-color mana.
    pay( [ [[0], []], [[1], []], [[7], []] ], [[0], [7], [1]])
    pay( [ [[0], []], [[1], []], [[2], []], [[7], []] ], [[0], [1], [2], [7], [7]])
    pay( [ [[0], []], [[7], []], [[7], []] ], [[0], [3], [7]])
    pay( [ [[0], []], [[1], []], [[1], []], [[1], []], [[7], []] ], [[0], [0], [0], [0], [1], [7], [7]])

if __name__ == '__main__':
    main()
