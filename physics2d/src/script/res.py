import pygame

class Color():
    black = [0, 0, 0]
    green = [0, 255, 0]
    white = [255, 255, 255]

class Image():
    sprite = {}

class Font():
    pass

def load_image():
    Image.sprite['coin'] = pygame.image.load('image/sprite/spritecoin.png')

def load_font():
    Font.neodgm_32 = pygame.font.Font('font/neodgm.ttf', 32)