import pygame

import var
import res

from render import *

from protounit import Unit

class Player(Unit):
    hand = []
    deck = []

    def __init__(self):
        super().__init__()