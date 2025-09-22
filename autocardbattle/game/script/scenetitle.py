import pygame, sys

from script.UI import *
from script.res import *

from script.render import *
from script.func import *

def loop(game):
    render(game)

def render(game):
    game.screen.fill(Color.white)
    game.screen.blit(Font.neodgm_32.render('Auto Card Battle', False, Color.black), UI.Title.text_title)
    pygame.draw.rect(game.screen, Color.black, UI.Title.button_start, 2)
    game.screen.blit(Font.neodgm_32.render('Start Game', False, Color.black), UI.Title.text_start)
    pygame.draw.rect(game.screen, Color.black, UI.Title.button_collection, 2)
    game.screen.blit(Font.neodgm_32.render('Collection', False, Color.black), UI.Title.text_collection)
    pygame.display.flip()

def mouse_up(game, pos, button):
    if button == 1:
        if point_inside_rect_ui(pos, UI.Title.button_start):
            game.scene = 'ready'
            game.state = ''
            game.selected_character = -1