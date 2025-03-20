import pygame

import res
import var
import const
from ui import UI
from primitive import *
import gamehandler

from render import *
from physics import point_inside_rect_ui

def loop():
    if var.menu == False:
        if var.state == '':
            var.game.handle_tick()

    display()

def display():
    var.screen.fill(res.COLOR_WHITE)
    draw_rect(res.COLOR_BLACK, UI.Battle.button_menu, 2)
    var.camera.adjust(var.player)
    var.field.render()
    var.player.render()

    if var.menu == True:
        render_menu()
        
    pygame.display.flip()

def key_down(key):
    if var.menu == False:
        if var.state == '':
            pass

def key_up(key):
    pass

def mouse_up(pos, button):
    if button == 1:
        if var.menu == False:
            if point_inside_rect_ui(pos, UI.Battle.button_menu):
                var.menu = True

        elif var.menu == True:
            if point_inside_rect_ui(pos, UI.Menu.button_resume):
                var.menu = False

            elif point_inside_rect_ui(pos, UI.Menu.button_exit):
                var.menu = False
                var.scene = 'title'
                var.state = ''