import pygame

card = [101, 102, 103, 201]

class Color():
    transparent = [0, 0, 0, 0]
    black = [0, 0, 0, 255]
    red = [255, 0, 0, 255]
    green = [0, 255, 0, 255]
    blue = [0, 0, 255, 255]
    yellow = [255, 255, 0, 255]
    magenta = [255, 0, 255, 255]
    cyan = [0, 255, 255, 255]
    white = [255, 255, 255, 255]

class Font():
    pass

class Image():
    pass

def load_font():
    Font.neodgm_32 = pygame.font.Font('font/neodgm.ttf', 32)
    Font.neodgm_16 = pygame.font.Font('font/neodgm.ttf', 16)

def load_image():
    Image.select_frame_160 = pygame.image.load('image/selectframe160.png')
    Image.select_frame_200 = pygame.image.load('image/selectframe200.png')
    Image.select_frame_long =  pygame.image.load('image/selectframelong.png')
    Image.icon = {
        0: pygame.image.load('image/iconfire.png'),
        1: pygame.image.load('image/iconwater.png'),
        2: pygame.image.load('image/iconwind.png'),
        3: pygame.image.load('image/iconearth.png'),
        4: pygame.image.load('image/iconlight.png'),
        5: pygame.image.load('image/icondark.png'),
        6: pygame.image.load('image/iconall.png')
    }
    Image.crystal = {
        1: pygame.image.load('image/crystalnormal.png'),
        2: pygame.image.load('image/crystalfire.png'),
        3: pygame.image.load('image/crystalwater.png'),
        4: pygame.image.load('image/crystalwind.png'),
        5: pygame.image.load('image/crystalearth.png'),
        6: pygame.image.load('image/crystallight.png'),
        7: pygame.image.load('image/crystaldark.png'),
        8: pygame.image.load('image/crystalrainbow.png')
    }
    Image.button = {
        'play': pygame.image.load('image/buttonplay.png'),
        'pause': pygame.image.load('image/buttonpause.png'),
        'menu': pygame.image.load('image/buttonmenu.png'),
        'battle': pygame.image.load('image/buttonbattle.png'),
        'elite': pygame.image.load('image/buttonelite.png'),
        'boss': pygame.image.load('image/buttonboss.png'),
        'shop': pygame.image.load('image/buttonshop.png'),
        'event': pygame.image.load('image/buttonevent.png'),
    }

    Image.card = {}
    Image.unit = {}

    for i in card:
        Image.card[i] = pygame.image.load(f'image/card/card{str(i).zfill(3)}.png').convert_alpha()
    for i in card:
        Image.unit[i] = pygame.image.load(f'image/card/card{str(i).zfill(3)}.png').convert_alpha()

    Image.unit[1001] = pygame.image.load(f'image/hero/hero1001.png').convert_alpha()
    Image.unit[1002] = pygame.image.load(f'image/hero/hero1001.png').convert_alpha()
    Image.unit[1003] = pygame.image.load(f'image/hero/hero1001.png').convert_alpha()
    Image.unit[1004] = pygame.image.load(f'image/hero/hero1001.png').convert_alpha()
    Image.unit[1005] = pygame.image.load(f'image/hero/hero1001.png').convert_alpha()
    Image.unit[1006] = pygame.image.load(f'image/hero/hero1001.png').convert_alpha()
    Image.unit[1007] = pygame.image.load(f'image/hero/hero1001.png').convert_alpha()
    Image.unit[1101] = pygame.image.load(f'image/hero/hero1101.png').convert_alpha()

    Image.hero = {

    }