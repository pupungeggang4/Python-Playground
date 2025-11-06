import pygame

class Color():
    black = [0, 0, 0]
    green = [0, 255, 0]
    white = [255, 255, 255]

class Image():
    sprite = {}

def load_image():
    Image.sprite['coin'] = pygame.image.load('image/sprite/spritecoin.png')