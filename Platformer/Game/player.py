import pygame, sys
import module as m

class Player():
    def __init__ (self):
        self.rect = m.Rect2D(80, 700, 80, 80)
    
    def handle_tick(self, game):
        self.move(game)

    def move(self, game):
        if game.key_pressed['left'] == True:
            self.rect.position.x -= 200 / game.fps

        if game.key_pressed['right'] == True:
            self.rect.position.x += 200 / game.fps

    def render(self, game):
        pygame.draw.rect(game.screen, m.res.COLOR_BLACK, [self.rect.position.x - self.rect.size.x / 2 - game.camera.position.x, self.rect.position.y - self.rect.size.y / 2 - game.camera.position.y, self.rect.size.x, self.rect.size.y], 2)