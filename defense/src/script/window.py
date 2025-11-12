import pygame, sys

class Window():
    def __init__(self, game):
        self.surface = pygame.surface.Surface(game.resolution, pygame.SRCALPHA)

    def render_static(self):
        pass

    def render(self, game):
        game.surface.blit(self, [0, 0])
