import pygame

import render as r

import res
import var
import const
import primitive as p

class Var():
    a = p.Rect2D(100, 100, 100, 100)

def loop():
    display()

def display():
    var.screen.fill((255, 255, 255))
    r.render_rect(var.screen, (0, 255, 0), Var.a)
    r.render_text(var.screen, res.font_neodgm_32, (0, 0, 0), 'Hello', [8, 8])
    pygame.display.flip()