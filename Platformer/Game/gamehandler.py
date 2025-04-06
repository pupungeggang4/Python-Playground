import module as m
import pygame, sys, json

class Game():
    screen = None
    resolution = [1280, 800]
    fps = 60
    clock = None

    scene = 'title'
    state = ''
    menu = False
    key_pressed = {'left': False, 'right': False}

    player = m.Player()
    camera = m.Camera2D()

    save = []

    def __init__(self):
        pygame.init()
        pygame.font.init()
        m.res.font_neodgm_32 = pygame.font.Font('Font/neodgm.ttf', 32)
        self.screen = pygame.display.set_mode(self.resolution, pygame.SCALED, vsync = 1)
        self.clock = pygame.time.Clock()
        self.load_data()

    def run(self):
        while True:
            self.clock.tick(self.fps)
            self.handle_input()
            self.handle_scene()

    def handle_scene(self):
        if self.scene == 'title':
            m.scenetitle.loop(self)

        elif self.scene == 'game':
            m.scenegame.loop(self)

    def handle_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                key = event.key
                if key == pygame.K_a:
                    self.key_pressed['left'] = True
                if key == pygame.K_d:
                    self.key_pressed['right'] = True

                if self.scene == 'title':
                    m.scenetitle.key_down(self, key)

                elif self.scene == 'game':
                    m.scenegame.key_down(self, key)

            if event.type == pygame.KEYUP:
                key = event.key
                if key == pygame.K_a:
                    self.key_pressed['left'] = False
                if key == pygame.K_d:
                    self.key_pressed['right'] = False

                if self.scene == 'game':
                    m.scenegame.key_up(self, key)

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