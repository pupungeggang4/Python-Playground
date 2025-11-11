import math

class Vec2():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, v):
        return Vec2(self.x + v.x, self.y + v.y)

    def __sub__(self, v):
        return Vec2(self.x - v.x, self.y - v.y)

    def __mul__(self, a):
        return Vec2(self.x * a, self.y * a)

    def __div__(self, a):
        return Vec2(self.x / a, self.y / a)

    @staticmethod
    def length(v):
        return math.sqrt(v.x ** 2 + v.y ** 2)

    @staticmethod
    def sub(v1, v2):
        return Vec2(v1.x - v2.x, v1.y - v2.y)

    @staticmethod
    def distance(v1, v2):
        return Vec2.length(v1 - v2)

class Rect2():
    def __init__(self, x, y, w, h):
        self.pos = Vec2(x, y)
        self.size = Vec2(w, h)
