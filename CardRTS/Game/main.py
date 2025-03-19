import pygame
import sys

from primitive import *

import res
import var
import const
import time
import gamehandler

import scenetitle
import scenelevelselect
import scenecharacterselect
import scenebattle

class Var():
    time = 0

def init():
    pygame.init()
    var.screen = pygame.display.set_mode(var.window_size, pygame.SCALED, vsync = 1)
    pygame.display.set_caption('Card RTS')
    var.clock = pygame.time.Clock()

    pygame.font.init()
    res.font_neodgm_32 = pygame.font.Font('Font/neodgm.ttf', 32)

    var.game = gamehandler.GameHandler()

def main():
    while True:
        var.clock.tick(var.FPS)
        handle_input()
        handle_scene()

def handle_input():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONUP:
            mouse = pygame.mouse.get_pos()
            pos = Vector2D(mouse[0], mouse[1])
            button = event.button

            if var.scene == 'title':
                scenetitle.mouse_up(pos, button)

            elif var.scene == 'level_select':
                scenelevelselect.mouse_up(pos, button)

            elif var.scene == 'character_select':
                scenecharacterselect.mouse_up(pos, button)

            elif var.scene == 'battle':
                scenebattle.mouse_up(pos, button)

        if event.type == pygame.KEYDOWN:
            key = event.key

            if var.scene == 'title':
                scenetitle.key_down(key)

            elif var.scene == 'level_select':
                scenelevelselect.key_down(key)

            elif var.scene == 'character_select':
                scenecharacterselect.key_down(key)

            elif var.scene == 'battle':
                scenebattle.key_down(key)

        if event.type == pygame.KEYUP:
            key = event.key

            if var.scene == 'title':
                scenetitle.key_up(key)

            elif var.scene == 'level_select':
                scenelevelselect.key_up(key)

            elif var.scene == 'character_select':
                scenecharacterselect.key_down(key)

            elif var.scene == 'battle':
                scenebattle.key_up(key)

def handle_scene():
    if var.scene == 'title':
        scenetitle.loop()

    elif var.scene == 'level_select':
        scenelevelselect.loop()

    elif var.scene == 'character_select':
        scenecharacterselect.loop()

    elif var.scene == 'battle':
        scenebattle.loop()

if __name__ == '__main__':
    init()
    main()