import math

class Vec2():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, v):
        return Vec2(self.x + v.x, self.y + v.y)

    def __sub__(self, v):
        return Vec2(self.x - v.x, self.y - v.y)
    
    def length(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)

class Rect2():
    def __init__(self, x, y, w, h):
        self.pos = Vec2(x, y)
        self.size = Vec2(w, h)

    @staticmethod
    def collision_check_simple(r1, r2):
        rad1 = (r1.size.x + r1.size.y) / 4
        rad2 = (r2.size.x + r2.size.y) / 4
        dist = (r1.pos - r2.pos).length()
        return dist < (rad1 + rad2)