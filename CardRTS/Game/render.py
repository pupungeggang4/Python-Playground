import pygame
import var

def draw_rect(color, rect, width = 0):
    pygame.draw.rect(var.screen, color, rect, width)

def render_rect_center(color, rect):
    pygame.draw.rect(var.screen, color, [rect.position.x - rect.size.x / 2, rect.position.y - rect.size.y / 2, rect.size.x, rect.size.y])

def render_rect_center_cam(color, rect, camera):
    pygame.draw.rect(var.screen, color, [rect.position.x - rect.size.x / 2 - camera.x, rect.position.y - rect.size.y / 2, rect.size.x, rect.size.y - camera.y])