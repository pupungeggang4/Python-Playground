class Vector2D():
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Rect2D():
    def __init__(self, x, y, w, h):
        self.position = Vector2D(x, y)
        self.size = Vector2D(w, h)