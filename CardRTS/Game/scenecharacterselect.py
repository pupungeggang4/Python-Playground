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
    var.screen.blit(res.font_neodgm_32.render('Select Character', False, res.COLOR_BLACK), UI.Character_Select.text_title)

    draw_rect(res.COLOR_BLACK, UI.Character_Select.button_back, 2)

    for i in range(6):
        draw_rect(res.COLOR_BLACK, UI.Character_Select.button_character[i], 2)
    
    pygame.display.flip()

def key_down(key):
    pass

def key_up(key):
    pass

def mouse_up(pos, button):
    if button == 1:
        if point_inside_rect_ui(pos, UI.Character_Select.button_back):
            var.scene = 'level_select'
            var.state = ''

        for i in range(6):
            if point_inside_rect_ui(pos, UI.Character_Select.button_character[i]):
                var.scene = 'battle'
                var.state = ''
                break
                #var.state = 'start'