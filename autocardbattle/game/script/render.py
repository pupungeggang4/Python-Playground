import pygame
from pygame._sdl2 import video

class Render():
    @staticmethod
    def stroke_rect(renderer, thickness, rect):
        renderer.fill_rect([rect[0], rect[1], rect[2], thickness])
        renderer.fill_rect([rect[0], rect[1], thickness, rect[3]])
        renderer.fill_rect([rect[0], rect[1] + rect[3] - thickness, rect[2], thickness])
        renderer.fill_rect([rect[0] + rect[2] - thickness, rect[1], thickness, rect[3]])

    @staticmethod
    def render_text(renderer, font, text, color, pos):
        text_surface = font.render(text, False, color)
        text_texture = video.Texture.from_surface(renderer, text_surface)
        video.Texture.draw(text_texture, None, [pos[0], pos[1], text_texture.width, text_texture.height])

    @staticmethod
    def draw_image(renderer, img, pos):
        img_texture = video.Texture.from_surface(renderer, img)
        video.Texture.draw(img_texture, None, [pos[0], pos[1], img_texture.width, img_texture.height])