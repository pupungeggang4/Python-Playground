import math

class Vec2():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @staticmethod
    def distance(v1, v2):
        return math.sqrt((v1.x - v2.x) ** 2 + (v1.y - v2.y) ** 2)

class Rect2():
    def __init__(self, x, y, w, h):
        self.pos = Vec2(x, y)
        self.size = Vec2(w, h)
