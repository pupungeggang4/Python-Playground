import pygame

class Color():
    transparent = [0, 0, 0, 0]
    black = [0, 0, 0]
    white = [255, 255, 255]

class Font():
    pass

class Image():
    pass

def load_font():
    Font.neodgm_32 = pygame.font.Font('font/neodgm.ttf', 32)

def load_image():
    Image.arrow = pygame.image.load('image/arrow.png').convert_alpha()
    Image.portal = pygame.image.load('image/portal.png').convert_alpha()