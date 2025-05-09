import math
import os
import sys

import numpy as np
import moderngl
from OpenGL.GL import *
import pygame

pygame.init()
pygame.display.gl_set_attribute(pygame.GL_CONTEXT_MAJOR_VERSION, 4)
pygame.display.gl_set_attribute(pygame.GL_CONTEXT_MINOR_VERSION, 1)
pygame.display.gl_set_attribute(pygame.GL_CONTEXT_PROFILE_MASK, pygame.GL_CONTEXT_PROFILE_CORE)
pygame.display.gl_set_attribute(pygame.GL_CONTEXT_FORWARD_COMPATIBLE_FLAG, True)
pygame.display.set_mode((800, 800), flags=pygame.OPENGL | pygame.DOUBLEBUF, vsync=True)
print(glGetString(GL_VERSION))

class Scene:
    def __init__(self):
        self.ctx = moderngl.get_context()
        self.program = self.ctx.program(
            vertex_shader='''
                #version 330
                in vec2 in_vert;
                uniform vec2 a;
                void main() {
                    gl_Position = vec4(in_vert + a, 0.0, 1.0);
                }
            ''',
            fragment_shader='''
                #version 330
                out vec4 f_color;
                void main() {
                    f_color = vec4(1.0, 0.0, 0.0, 1.0);
                }
            ''',
        )

        self.vertices = np.array([-0.1, -0.1, 0.1, 0.1, 0.1, -0.1], dtype='f4')
        self.vbo = self.ctx.buffer(self.vertices)
        self.vao = self.ctx.simple_vertex_array(self.program, self.vbo, 'in_vert')
        self.a = self.program['a']
        self.b = [0, 0]

    def render(self):
        self.b[0] += 0.005
        self.b[1] += 0.005
        self.a.value = self.b[0], self.b[1]
        self.ctx.clear()
        self.vao.render()

scene = Scene()
clock = pygame.time.Clock()

while True:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    scene.render()

    pygame.display.flip()