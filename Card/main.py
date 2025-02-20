import json
import platform
import sys
import os

import var
import prototype as p

def init():
    var.state = ''
    var.field = p.Field()
    var.player = p.Player()
    var.statement_stack = []
    var.temp_var = {}

def main():
    while True:
        var.field.render()
        var.player.render()
        print(var.state)
        print(var.statement_stack)
        i = input('Enter Command: ')
        handle_command(i)

def handle_command(i):
    if i == 'exit':
        sys.exit(0)

    if var.state == '':
        c = i.split(' ')
        if len(c) == 2:
            if c[0] == 'play' and c[1].isdigit():
                if int(c[1]) < len(var.player.hand):
                    var.temp_card = var.player.hand[int(c[1])]
                    for i in range(len(var.player.hand[int(c[1])].play)):
                        var.statement_stack.append(json.loads(json.dumps(var.player.hand[int(c[1])].play[i])))
                var.state = 'process'
                var.temp_var = {}
                handle_statement(var.player, var.field)

    elif var.state == 'input':
        if var.temp_var_cond == 'empty_player':
            if i.isdigit():
                if int(i) >= 7 and int(i) <= 12 and type(var.field.unit[int(i)]) == p.FieldElement:
                    var.temp_var[var.temp_var_name] = int(i)
                    var.state = ''
                    handle_statement(var.player, var.field)

def handle_card():
    pass

def handle_statement(player, field):
    while len(var.statement_stack) > 0:
        first = var.statement_stack[0]

        if first[0] == 'summon':
            if first[1] == 'empty':
                print('placing')
                for i in range(7, 13):
                    if type(var.field.unit[i]) == p.FieldElement:
                        var.field.unit[i] = p.Unit({'stat': [first[2][0], first[2][1]]})
                        break

            else:
                if first[2][0] == -1:
                    var.field.unit[var.temp_var[first[1]]] = p.Unit({'stat': [var.temp_card.attack, var.temp_card.hp]})

        elif first[0] == 'input':
            var.state = 'input'
            var.temp_var_name = first[1]
            var.temp_var_cond = first[2]
            var.statement_stack.pop(0)
            return

        var.statement_stack.pop(0)
    var.state = ''

if __name__ == '__main__':
    init()
    main()
