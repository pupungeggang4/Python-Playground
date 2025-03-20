from primitive import *
from protounit import Unit

class Field():
    unit_list = []
    
    def __init__(self):
        self.unit_list = [Unit(), Unit()]
        self.unit_list[0].rect.position.x = 200
        self.unit_list[0].rect.position.y = 200
        self.unit_list[1].rect.position.x = -200
        self.unit_list[1].rect.position.y = -200

    def render(self):
        for i in range(len(self.unit_list)):
            self.unit_list[i].render()

class Camera():
    def __init__(self):
        self.position = Vector2D(0, 0)

    def adjust(self, target):
        self.position.x = target.rect.position.x - 640
        self.position.y = target.rect.position.y - 400