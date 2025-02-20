import var
import json

process_stack = []
card_var = {}
card_literal = []

def play_card(card, player, field):
    print(card.name)

def process_statement(player, field):
    if len(process_stack) == 0:
        var.state = ''
        return
    
    first = process_stack[0]
    
    if first[0] == 'Summon':
        card_literal = json.loads(json.dumps(first[1]))
        card_var = {}
        var.state = 'playing'

