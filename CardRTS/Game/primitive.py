import math

class Vector2D():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, vec):
        return math.sqrt((vec.x - self.x) ** 2 + (vec.y - self.y) ** 2)
    
    def inside_rect(self, rect):
        return self.position.x > rect.position.x - rect.size.x / 2 and self.position.x < rect.position.x + rect.size.x / 2 and self.position.y > rect.position.y - rect.size.y / 2 and self.position.y < rect.position.y + rect.size.y / 2

    def inside_circle(self, circle):
        return self.distance(circle.position) < circle.radius

class Rect2D():
    def __init__(self, x, y, w, h):
        self.position = Vector2D(x, y)
        self.size = Vector2D(w, h)

class Circle2D():
    def __init__(self, x, y, r):
        self.position = Vector2D(x, y)
        self.radius = r