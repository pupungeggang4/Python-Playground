import pygame, sys

from script.res import *

class Render():
    @staticmethod
    def draw_rect_center_cam(surface, rect, cam, color = Color.black, thickness = 0):
        r = [rect.pos.x - rect.size.x / 2 - cam.pos.x + cam.size.x / 2, rect.pos.y - rect.size.y / 2 - cam.pos.y + cam.size.y / 2, rect.size.x, rect.size.y]
        pygame.draw.rect(surface, color, r, thickness)

    def render_center_cam(surface, img, rect, cam):
        pos = [rect.pos.x - rect.size.x / 2 - cam.pos.x + cam.size.x / 2, rect.pos.y - rect.size.y / 2 - cam.pos.y + cam.size.y / 2]
        surface.blit(img, pos)

    def render_center_cam_part(surface, img, coord, rect, cam):
        sub_surface = img.subsurface(pygame.Rect(coord[0], coord[1], rect.size.x, rect.size.y))
        pos = [rect.pos.x - rect.size.x / 2 - cam.pos.x + cam.size.x / 2, rect.pos.y - rect.size.y / 2 - cam.pos.y + cam.size.y / 2]
        surface.blit(sub_surface, pos)