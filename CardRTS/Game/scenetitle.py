import pygame

import res
import var
import const
from ui import UI
from primitive import *

from render import *
from physics import point_inside_rect_ui

def loop():
    display()

def display():
    var.screen.fill(res.COLOR_WHITE)
    var.screen.blit(res.font_neodgm_32.render('Card RTS', False, res.COLOR_BLACK), UI.Title.text_title)
    draw_rect(res.COLOR_BLACK, UI.Title.button_start, 2)
    var.screen.blit(res.font_neodgm_32.render('Start Game', False, res.COLOR_BLACK), UI.Title.text_start)
    draw_rect(res.COLOR_BLACK, UI.Title.button_erase, 2)
    var.screen.blit(res.font_neodgm_32.render('Erase Data', False, res.COLOR_BLACK), UI.Title.text_erase)
    pygame.display.flip()

def key_down(key):
    pass

def key_up(key):
    pass

def mouse_up(pos, button):
    if button == 1:
        if point_inside_rect_ui(pos, UI.Title.button_start):
            var.scene = 'level_select'