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
    Image.coin = pygame.image.load('image/coin.png').convert_alpha()
    Image.player = pygame.image.load('image/player.png').convert_alpha()
    Image.arrow = pygame.image.load('image/arrow.png').convert_alpha()
    Image.exporb = pygame.image.load('image/exporb.png').convert_alpha()
    Image.portal = pygame.image.load('image/portal.png').convert_alpha()