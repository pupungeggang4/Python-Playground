import pygame, sys

class Game():
    def __init__(self):
        self.scene = 'title'
        self.state = ''
        self.menu = False
        self.screen = pygame.display.set_mode([1280, 720])
        pygame.display.set_caption('Platformer Game')

        self.fps = 60
        self.clock = pygame.time.Clock()

    def run(self):
        while True:
            self.clock.tick(self.fps)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
