import pygame, sys
from OpenGL.GL import *

class Game():
    def __init__(self):
        self.screen = pygame.display.set_mode([1280, 720], pygame.OPENGL)
        self.ui = pygame.surface.Surface([1280, 720], pygame.SRCALPHA)
        pygame.display.set_caption('RGB Mesh Test')
        self.clock = pygame.time.Clock()
        self.fps = 60

        pygame.font.init()
        self.neodgm_32 = pygame.font.Font('font/neodgm.ttf', 32)
        self.texture = glGenTextures(1)
        glBindTexture(GL_TEXTURE_2D, self.texture);
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP_TO_EDGE);
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP_TO_EDGE);
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST);
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST);

    def run(self):
        while True:
            self.clock.tick(self.fps)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.ui.fill([0, 0, 0, 0])
            self.ui.blit(self.neodgm_32.render('Hello Pygame Mesh!', False, [255, 255, 255]), [24, 24])
            
            glEnable(GL_BLEND)
            glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
            glClearColor(0.0, 0.0, 0.0, 1.0)
            glClear(GL_COLOR_BUFFER_BIT)

            glDisable(GL_TEXTURE_2D)
            gv = [0.0, 0.0, 1.0, 0.0, 1.0, 1.0]
            gc = [1.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 1.0]
            glVertexPointer(2, GL_FLOAT, 0, gv)
            glColorPointer(3, GL_FLOAT, 0, gc)
            glEnableClientState(GL_COLOR_ARRAY)
            glEnableClientState(GL_VERTEX_ARRAY)
            glDisableClientState(GL_TEXTURE_COORD_ARRAY)
            glDrawArrays(GL_TRIANGLES, 0, 3)

            glEnable(GL_TEXTURE_2D)
            glBindTexture(GL_TEXTURE_2D, self.texture)
            glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, self.ui.get_width(), self.ui.get_height(), 0, GL_RGBA, GL_UNSIGNED_BYTE, pygame.image.tobytes(self.ui, 'RGBA'))
            gv = [-1.0, -1.0, 1.0, -1.0, 1.0, 1.0, -1.0, 1.0]
            gt = [0.0, 1.0, 1.0, 1.0, 1.0, 0.0, 0.0, 0.0]
            glVertexPointer(2, GL_FLOAT, 0, gv)
            glTexCoordPointer(2, GL_FLOAT, 0, gt)
            glDisableClientState(GL_COLOR_ARRAY)
            glEnableClientState(GL_VERTEX_ARRAY)
            glEnableClientState(GL_TEXTURE_COORD_ARRAY)
            glDrawArrays(GL_QUADS, 0, 4)
            pygame.display.flip()

if __name__ == '__main__':
    game = Game()
    game.run()
