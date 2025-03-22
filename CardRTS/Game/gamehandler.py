import var
from protoplayer import Player
from protofield import Field, Camera
from protocard import Card
from protounit import Unit
from primitive import *

class GameHandler():
    def __init__(self):
        var.player = Player()
        var.field = Field()
        var.camera = Camera()

    def handle_tick(self):
        var.camera.adjust(var.player)
        var.player.handle_tick()

    def handle_right_click(self, pos):
        var.player.moving = True
        left_top = Vector2D.sub(var.camera.position, Vector2D(640, 400))
        var.player.destination = Vector2D.add(left_top, pos)