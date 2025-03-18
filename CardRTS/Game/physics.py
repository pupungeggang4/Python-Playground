from primitive import *

def point_inside_rect_ui(point, rect):
    return point.x > rect[0] and point.x < rect[0] + rect[2] and point.y > rect[1] and point.y < rect[1] + rect[3]

def point_inside_rect(point, rect):
    return point.x > rect.position.x - rect.size.x / 2 and point.x > rect.position.x + rect.size.x / 2 and point.y > rect.position.y - rect.size.y / 2 and point.y > rect.position.y + rect.size.y / 2