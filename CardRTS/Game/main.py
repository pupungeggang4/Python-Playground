import pygame
import sys

import primitive as p

import res
import var
import const

import scenetitle
import scenelevelselect
import scenebattle

def init():
    pygame.init()
    var.screen = pygame.display.set_mode(var.window_size, pygame.SCALED)
    pygame.display.set_caption('Card RTS')
    var.clock = pygame.time.Clock()

    pygame.font.init()
    res.font_neodgm_32 = pygame.font.Font('Font/neodgm.ttf', 32)

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

def handle_scene():
    if var.scene == 'title':
        scenetitle.loop()

    elif var.scene == 'level_select':
        scenelevelselect.loop()

    elif var.scene == 'battle':
        scenebattle.loop()

if __name__ == '__main__':
    init()
    main()