import pygame, sys

from script.UI import *
from script.res import *

from script.render import *
from script.func import *

def loop(game):
    render(game)

def render(game):
    game.screen.fill(Color.white)
    game.screen.blit(Font.neodgm_32.render('Select Character', False, Color.black), UI.Ready.text_title)
    pygame.draw.rect(game.screen, Color.black, UI.Ready.button_back)
    pygame.draw.rect(game.screen, Color.black, UI.Ready.button_start)
    game.screen.blit(Font.neodgm_32.render('Start', False, Color.black), UI.Ready.text_start)
    pygame.display.flip()

def mouse_up(game, pos, button):
    if button == 1:
        if point_inside_rect_ui(pos, UI.Ready.button_back):
            game.scene = 'title'
            game.state = ''

        if point_inside_rect_ui(pos, UI.Ready.button_start):
            if game.selected_character != -1:
                game.scene = 'battle'
                game.state = ''