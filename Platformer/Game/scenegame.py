import pygame, sys
import module as m

def loop(game):
    if game.menu == False:
        if game.state == '':
            game.player.handle_tick(game)

    render(game)

def render(game):
    game.screen.fill(m.res.COLOR_WHITE)
    game.player.render(game)

    if game.state == 'start':
        game.screen.blit(m.res.font_neodgm_32.render('Press Enter to Start.', False, m.res.COLOR_BLACK), m.UI.Game.text_start)
    pygame.display.flip()

def key_down(game, key):
    if game.menu == False:
        if game.state == 'start':
            if key == pygame.K_RETURN:
                game.state = ''

def key_up(game, key):
    pass