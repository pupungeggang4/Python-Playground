import pygame, sys

class Color():
    transparent = [0, 0, 0, 0]
    black = [0, 0, 0]
    white = [255, 255, 255]

class Font():
    pass

class Image():
    sprite = {}

def load_image():
    Image.arrow = pygame.image.load('image/arrow.png')
    Image.sprite['coin'] = pygame.image.load('image/sprite/spritecoin.png')
