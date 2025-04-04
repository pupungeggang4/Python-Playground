import pygame, sys
import module as m

class Player():
    def __init__ (self):
        self.rect = m.Rect2D(10, 20, 80, 80)

    def render(self, game):
        pygame.draw.rect(game.screen, m.res.COLOR_BLACK, [self.rect.position.x, self.rect.position.y, self.rect.size.x, self.rect.size.y], 2)