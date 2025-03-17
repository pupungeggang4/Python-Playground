import math

class Vector2D():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, vec):
        return math.sqrt((vec.x - self.x) ** 2 + (vec.y - self.y) ** 2)

class Rect2D():
    def __init__(self, x, y, w, h):
        self.position = Vector2D(x, y)
        self.size = Vector2D(w, h)