import pygame, sys

def loop(game):
    render(game)

def render(game):
    game.surface.fill([255, 255, 255])
    pygame.draw.rect(game.surface, [0, 0, 0], [80, 80, 80, 80])