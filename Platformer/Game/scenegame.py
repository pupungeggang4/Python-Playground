import pygame, sys
import module as m

def loop(game):
    render(game)

def render(game):
    game.screen.fill(m.res.COLOR_WHITE)
    game.player.render(game)
    pygame.display.flip()

def key_down(game, key):
    if game.menu == False:
        if game.state == 'start':
            if key == pygame.K_RETURN:
                game.state = ''