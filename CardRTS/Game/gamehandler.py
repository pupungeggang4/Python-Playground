import var
from protoplayer import Player
from protofield import Field, Camera
from protocard import Card
from protounit import Unit

class GameHandler():
    def __init__(self):
        var.player = Player()
        var.field = Field()
        var.camera = Camera()

    def handle_tick(self):
        var.camera.adjust(var.player)