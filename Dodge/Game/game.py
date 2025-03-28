import m
import pygame, sys

game_i = None

class Game():
    screen = None
    resolution = [1280, 800]
    fps = 60
    clock = None

    scene = 'main'
    state = ''

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(self.resolution)
        pygame.display.set_caption('Dodge Game')
        self.clock = pygame.time.Clock()

    def run(self):
        while True:
            self.game_loop()

    def game_loop(self):
        self.clock.tick(self.fps)
        self.handle_input()
        self.handle_scene()

    def handle_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse = pygame.mouse.get_pos()
                print(mouse)

    def handle_scene(self):
        if self.scene == 'main':
            m.scenemain.loop()

if __name__ == '__main__':
    game_i = Game()
    game_i.run()