import math

class Vector2D():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @staticmethod
    def add(vec1, vec2):
        return Vector2D(vec1.x + vec2.x, vec1.y + vec2.y)

    @staticmethod
    def sub(vec1, vec2):
        return Vector2D(vec1.x - vec2.x, vec1.y - vec2.y)

    def magnitude(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)
    
    def normalized(self):
        m = self.magnitude()
        return Vector2D(self.x / m, self.y / m)

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