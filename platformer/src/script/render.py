import pygame

from script.res import *
from script.ui import *

class Render():
    @staticmethod
    def draw_rect_center_cam(surface, rect, camera, color = Color.black, thickness = 2):
        r = [rect.pos.x - rect.size.x / 2 - camera.pos.x + camera.size.x / 2, rect.pos.y - rect.size.y / 2 - camera.pos.y + camera.size.y / 2, rect.size.x, rect.size.y]
        pygame.draw.rect(surface, color, r, thickness)

    @staticmethod
    def render_center_cam(surface, img, rect, camera):
        pos = [rect.pos.x - rect.size.x / 2 - camera.pos.x + camera.size.x / 2, rect.pos.y - rect.size.y / 2 - camera.pos.y + camera.size.y / 2]
        surface.blit(img, pos)
