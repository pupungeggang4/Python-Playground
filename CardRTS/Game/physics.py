from primitive import *

def point_inside_rect_ui(point, rect):
    return point.x > rect[0] and point.x < rect[0] + rect[2] and point.y > rect[1] and point.y < rect[1] + rect[3]