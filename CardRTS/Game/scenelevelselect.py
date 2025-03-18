import pygame

from render import *
from primitive import *
from ui import UI

import physics

import res
import var
import const

def loop():
    display()

def display():
    var.screen.fill(res.COLOR_WHITE)
    draw_rect(res.COLOR_BLACK, UI.Level_Select.button_back, 2)
    pygame.display.flip()

def key_down(key):
    pass

def key_up(key):
    pass

def mouse_up(pos, button):
    pass