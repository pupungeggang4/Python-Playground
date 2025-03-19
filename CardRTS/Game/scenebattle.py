import pygame

from render import *
from primitive import *
from ui import UI

import physics

import res
import var
import const

class Var():
    rect = [80, 80, 80, 80]

def loop():
    Var.rect[0] += 200 / var.FPS
    display()

def display():
    var.screen.fill(res.COLOR_WHITE)
    draw_rect(res.COLOR_BLACK, Var.rect)
    pygame.display.flip()

def key_down(key):
    pass

def key_up(key):
    pass

def mouse_up(pos, button):
    pass