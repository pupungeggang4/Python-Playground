import json

from script.data import *
from script.shape import *

from script.field import *

class LevelHandler():
    @staticmethod
    def load_level(game, level_name):
        field = game.field
        data = json.loads(json.dumps(Data.level[level_name]))
        field.player.rect.pos = Vec2(data['start_pos'][0], data['start_pos'][1])
        for i in range(len(data['entity'])):
            entity = data['entity'][i]
            if entity[0] == 'coin':
                coin = Coin()
                coin.rect.pos = Vec2(entity[1][0], entity[1][1])
                field.entity_list.append(coin)
            if entity[0] == 'wall':
                wall = Wall()
                wall.rect = Rect2(entity[1][0], entity[1][1], entity[1][2], entity[1][3])
                field.entity_list.append(wall)
