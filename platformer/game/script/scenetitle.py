import pygame, sys
from script.ui import *
from script.res import *

def loop(game):
    render(game)

def render(game):
    game.screen.fill(Color.white)
    game.screen.blit(Font.neodgm_32.render('Platformer', False, Color.black), UI.Title.text_title)
    game.screen.blit(Font.neodgm_32.render('Press Enter to Start.', False, Color.black), UI.Title.text_lower)
    pygame.display.flip()

def key_down(game, key):
    if key == pygame.K_RETURN:
        game.scene = 'field'
        game.state = ''

def key_up(game, key):
    pass
