import pygame, sys
import module as m

def loop(game):
    render(game)

def render(game):
    game.screen.fill(m.res.COLOR_WHITE)
    game.screen.blit(m.res.font_neodgm_32.render('Platformer Demo', False, m.res.COLOR_BLACK), m.UI.Title.text_title)
    game.screen.blit(m.res.font_neodgm_32.render('Press Enter to Start', False, m.res.COLOR_BLACK), m.UI.Title.text_start)
    pygame.display.flip()

def key_down(game, key):
    if key == pygame.K_RETURN:
        game.scene = 'game'
        game.state = 'start'