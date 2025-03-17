import pygame

def render_rect(sur, color, rect):
    pygame.draw.rect(sur, color, [rect.position.x - rect.size.x / 2, rect.position.y - rect.size.y / 2, rect.size.x, rect.size.y])

def render_text(sur, font, color, text, pos):
    sur.blit(font.render(text, False, color), [pos[0], pos[1]])