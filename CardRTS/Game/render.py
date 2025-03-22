import pygame

from ui import UI
import res
import var

def draw_rect(color, rect, width = 0):
    pygame.draw.rect(var.screen, color, rect, width)

def render_rect_center(color, rect):
    pygame.draw.rect(var.screen, color, [rect.position.x - rect.size.x / 2, rect.position.y - rect.size.y / 2, rect.size.x, rect.size.y])

def render_rect_center_cam(color, rect, camera, width = 0):
    pygame.draw.rect(var.screen, color, [rect.position.x - rect.size.x / 2 - camera.position.x + 640, rect.position.y - rect.size.y / 2 - camera.position.y + 400, rect.size.x, rect.size.y], width)

def render_battle_ui():
    render_battle_lower()

def render_battle_lower():
    draw_rect(res.COLOR_WHITE, UI.Battle.Lower.base_attack)
    draw_rect(res.COLOR_BLACK, UI.Battle.Lower.base_attack, 2)
    draw_rect(res.COLOR_WHITE, UI.Battle.Lower.hand)
    draw_rect(res.COLOR_BLACK, UI.Battle.Lower.hand, 2)

def render_menu():
    draw_rect(res.COLOR_WHITE, UI.Menu.rect)
    draw_rect(res.COLOR_BLACK, UI.Menu.rect, 2)
    var.screen.blit(res.font_neodgm_32.render('Paused', False, res.COLOR_BLACK), UI.Menu.text_paused)
    draw_rect(res.COLOR_BLACK, UI.Menu.button_resume, 2)
    var.screen.blit(res.font_neodgm_32.render('Resume', False, res.COLOR_BLACK), UI.Menu.text_resume)
    draw_rect(res.COLOR_BLACK, UI.Menu.button_exit, 2)
    var.screen.blit(res.font_neodgm_32.render('Exit', False, res.COLOR_BLACK), UI.Menu.text_exit)