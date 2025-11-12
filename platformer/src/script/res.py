import pygame, sys

class Color():
    transparent = [0, 0, 0, 0]
    black = [0, 0, 0]
    white = [255, 255, 255]

class Font():
    pass

class Image():
    sprite = {}

def load_font():
    Font.neodgm_32 = pygame.font.Font('font/neodgm.ttf', 32)

def load_image():
    Image.player = pygame.image.load('image/player.png').convert_alpha()
    Image.arrow = pygame.image.load('image/arrow.png').convert_alpha()
    Image.coin = pygame.image.load('image/coin.png').convert_alpha()
    Image.sprite['coin'] = pygame.image.load('image/sprite/spritecoin.png').convert_alpha()
