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
            glDisable(GL_TEXTURE_2D)
            glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
            glClear(GL_COLOR_BUFFER_BIT)
            glBegin(GL_TRIANGLES)
            glColor3f(1.0, 0.0, 0.0)
            glVertex2f(0.0, 0.0)
            glColor3f(0.0, 1.0, 0.0)
            glVertex2f(1.0, 0.0)
            glColor3f(0.0, 0.0, 1.0)
            glVertex2f(1.0, 1.0)
            glEnd()

            glEnable(GL_TEXTURE_2D)
            glBindTexture(GL_TEXTURE_2D, self.texture)
            glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, self.ui.get_width(), self.ui.get_height(), 0, GL_RGBA, GL_UNSIGNED_BYTE, pygame.image.tobytes(self.ui, 'RGBA'))
            glBegin(GL_QUADS)
            glColor3f(1.0, 1.0, 1.0)
            glTexCoord2f(0.0, 1.0)
            glVertex2f(-1.0, -1.0)
            glTexCoord2f(1.0, 1.0)
            glVertex2f(1.0, -1.0)
            glTexCoord2f(1.0, 0.0)
            glVertex2f(1.0, 1.0)
            glTexCoord2f(0.0, 0.0)
            glVertex2f(-1.0, 1.0)
            glEnd()
            pygame.display.flip()

if __name__ == '__main__':
    game = Game()
    game.run()
