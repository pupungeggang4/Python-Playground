import pygame, sys
from pygame._sdl2 import video

from script.UI import *
from script.render import *
from script.res import *

def loop(game):
    render(game)

def render(game):
    game.renderer.draw_color = Color.white
    game.renderer.clear()
    game.renderer.draw_color = Color.black
    Render.render_text(game.renderer, Font.neodgm_32, 'Auto Card Battle', Color.black, UI.Title.text_title)
    Render.draw_image(game.renderer, Image.test, [500, 0])
    Render.stroke_rect(game.renderer, 2, UI.Title.button_start)
    Render.render_text(game.renderer, Font.neodgm_32, 'Start', Color.black, UI.Title.text_start)
    Render.stroke_rect(game.renderer, 2, UI.Title.button_collection)
    Render.render_text(game.renderer, Font.neodgm_32, 'Collection', Color.black, UI.Title.text_collection)
    game.renderer.present()

def mouse_up(game, pos):
    pass