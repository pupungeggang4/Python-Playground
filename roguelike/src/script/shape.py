class Vec2():
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Rect2():
    def __init__(self, x, y, w, h):
        self.pos = Vec2(x, y)
        self.size = Vec2(w, h)