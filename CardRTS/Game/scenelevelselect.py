import pygame

from render import *
from primitive import *
from ui import UI

import res
import var
import const

def loop():
    display()

def display():
    var.screen.fill(res.COLOR_WHITE)
    pygame.display.flip()

def mouse_up(pos, button):
    pass