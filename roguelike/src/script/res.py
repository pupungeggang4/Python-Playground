import pygame

class Color():
    transparent = [0, 0, 0, 0]
    black = [0, 0, 0]
    green = [0, 255, 0]
    blue = [0, 0, 255]
    cyan = [0, 255, 255]
    white = [255, 255, 255]

class Font():
    pass

class Image():
    pass

def load_font():
    Font.neodgm_32 = pygame.font.Font('font/neodgm.ttf', 32)
    Font.neodgm_24 = pygame.font.Font('font/neodgm.ttf', 24)

def load_image():
    Image.player = pygame.image.load('image/player.png').convert_alpha()
    Image.arrow = pygame.image.load('image/arrow.png').convert_alpha()
    Image.arrow_down = pygame.image.load('image/arrowdown.png').convert_alpha()
    Image.portal = pygame.image.load('image/portal.png').convert_alpha()
    Image.coin = pygame.image.load('image/coin.png').convert_alpha()
    Image.life = pygame.image.load('image/life.png').convert_alpha()
    Image.energy = pygame.image.load('image/energy.png').convert_alpha()
    Image.exporb = pygame.image.load('image/exporb.png').convert_alpha()