from primitive import *

class Field():
    pass

class Camera():
    def __init__(self):
        self.position = Vector2D(0, 0)

    def adjust(self, target):
        self.position.x = target.rect.position.x - 640
        self.position.y = target.rect.position.y - 400