import pygame, json

from script.wall import *
from script.belt import *
from script.platform import *
from script.coin import *

from script.field import *

class Level():
    @staticmethod
    def load_level(game, data):
        data_parsed = json.loads(json.dumps(data))
        field = game.field
        field.entity_list = []
        field.player.pos = Vec2(data_parsed['start_pos'][0], data_parsed['start_pos'][1])
        for i in range(len(data_parsed['entity'])):
            e = data_parsed['entity'][i]
            if e[0] == 'wall':
                wall = Wall()
                wall.rect = Rect2(e[1][0], e[1][1], e[1][2], e[1][3])
                field.entity_list.append(wall)
            if e[0] == 'coin':
                coin = Coin()
                coin.rect.pos = Vec2(e[1][0], e[1][1])
                field.entity_list.append(coin)
            if e[0] == 'unit':
                unit = Unit()
                unit.rect = Rect2(e[1][0], e[1][1], e[1][2], e[1][3])
                field.entity_list.append(unit)