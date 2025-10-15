import pygame, sys

from script.UI import *
from script.res import *

from script.adventure import *

from script.render import *
from script.func import *

def loop(game):
    render(game)

def render(game):
    game.surface.fill(Color.white)
    game.surface.blit(Font.neodgm_32.render('Select Character', False, Color.black), UI.Ready.text_title)
    game.surface.blit(Image.button['menu'], UI.Ready.button_back)

    for i in range(7):
        game.surface.blit(Image.icon[i], UI.Ready.character[i])
        pygame.draw.rect(game.surface, Color.black, UI.Ready.character[i], 4)

    if game.selected_character != -1:
        game.surface.blit(Image.select_frame_160, UI.Ready.character[game.selected_character])
        description = Data.character_d[game.selected_character + 1]
        for i in range(len(description)):
            pos = [UI.Ready.description_text[0], UI.Ready.description_text[1] + UI.Ready.description_text[3] * i]
            game.surface.blit(Font.neodgm_32.render(description[i], 'False', Color.black), pos)

    pygame.draw.rect(game.surface, Color.black, UI.Ready.description_box, 2)
    pygame.draw.rect(game.surface, Color.black, UI.Ready.button_start, 2)
    game.surface.blit(Font.neodgm_32.render('Start', False, Color.black), UI.Ready.text_start)

def mouse_up(game, pos, button):
    if button == 1:
        if point_inside_rect_ui(pos, UI.Ready.button_back):
            game.scene = 'title'
            game.state = ''

        for i in range(7):
            if point_inside_rect_ui(pos, UI.Ready.character[i]):
                game.selected_character = i

        if point_inside_rect_ui(pos, UI.Ready.button_start):
            if game.selected_character != -1:
                game.scene = 'battle'
                game.state = 'next'
                game.menu = False

                ID = game.selected_character + 1
                game.adventure.start_adventure()
                game.player.create_player(ID)
