import module as m
import pygame, sys, json

class Game():
    screen = None
    resolution = [1280, 800]
    fps = 60
    clock = None

    scene = 'title'
    state = ''

    save = []

    def __init__(self):
        pygame.init()
        pygame.font.init()
        self.screen = pygame.display.set_mode(self.resolution, pygame.SCALED)
        self.clock = pygame.time.Clock()
        self.load_data()

    def run(self):
        while True:
            self.clock.tick(self.fps)
            self.handle_input()
            self.handle_scene()

    def handle_scene(self):
        if self.scene == 'title':
            m.scenetitle.loop()

        if self.scene == 'game':
            m.scenegame.loop()

    def handle_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    def save_data(self):
        f = open('save.txt', 'w')
        f.write(json.dumps(self.save))
        f.close()

    def load_data(self):
        try:
            f = open('save.txt', 'r')
            self.save_data = json.loads(f.read())
            f.close()

        except:
            f = open('save.txt', 'w')
            f.write(json.dumps([]))
            f.close()

            f = open('save.txt', 'r')
            self.save_data = json.loads(f.read())
            f.close()

game = None