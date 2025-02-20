import json
import sys
import os

import var
import prototype as p

def init():
    var.state = ''
    var.field = p.Field()
    var.player = p.Player()

def main():
    while True:
        os.system('clear')
        var.field.render()
        var.player.render()
        i = input('Enter Command: ')
        handle_command(i)

def handle_command(i):
    if i == 'exit':
        sys.exit(0)

def handle_card():
    pass

if __name__ == '__main__':
    init()
    main()
