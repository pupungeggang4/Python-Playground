import pygame, sys

from script.UI import *
from script.res import *

class Render():
    @staticmethod
    def render_menu(screen):
        pygame.draw.rect(screen, Color.white, UI.Menu.rect)
        pygame.draw.rect(screen, Color.black, UI.Menu.rect, 2)
        screen.blit(Font.neodgm_32.render('Paused', False, Color.black), UI.Menu.text_paused)
        pygame.draw.rect(screen, Color.black, UI.Menu.button_resume, 2)
        screen.blit(Font.neodgm_32.render('Resume', False, Color.black), UI.Menu.text_resume)
        pygame.draw.rect(screen, Color.black, UI.Menu.button_exit, 2)
        screen.blit(Font.neodgm_32.render('Exit', False, Color.black), UI.Menu.text_exit)

    @staticmethod
    def render_field(screen, game):
        screen.blit(Font.neodgm_32.render(f'Turn : {game.battle.turn}', False, Color.black), UI.Battle.text_turn_num)
        if game.battle.turn_who == 0:
            screen.blit(Font.neodgm_32.render('Your turn', False, Color.black), UI.Battle.text_whose_turn)
        else:
            screen.blit(Font.neodgm_32.render('Enemy turn', False, Color.black), UI.Battle.text_whose_turn)
        for i in range(10):
            if game.battle.field[i] != None:
                game.battle.field[i].render(game.screen, game, UI.Battle.field[i])
            pygame.draw.rect(screen, Color.black, UI.Battle.field[i], 2)

        screen.blit(Image.button['play'], UI.Battle.button_play)
        screen.blit(Image.button['pause'], UI.Battle.button_pause)
        screen.blit(Image.button['menu'], UI.Battle.button_menu)
        pygame.draw.rect(screen, Color.black, UI.Battle.button_proceed, 2)
        screen.blit(Font.neodgm_32.render('Proceed', False, Color.black), UI.Battle.text_proceed)

    @staticmethod
    def render_crystal(screen, game):
        pygame.draw.rect(screen, Color.black, UI.Battle.player_crystal_box, 2)
        for i in range(len(game.battle.player.crystal_hand)):
            row = i // 4
            col = i % 4
            pos = [UI.Battle.player_crystal_start[0] + UI.Battle.player_crystal_interval[0] * col, UI.Battle.player_crystal_start[1] + UI.Battle.player_crystal_interval[1] * row]
            game.battle.player.crystal_hand[i].render(screen, game, pos)
        pygame.draw.rect(screen, Color.black, UI.Battle.enemy_crystal_box, 2)
        for i in range(len(game.battle.enemy.crystal_hand)):
            row = i // 4
            col = i % 4
            pos = [UI.Battle.enemy_crystal_start[0] + UI.Battle.enemy_crystal_interval[0] * col, UI.Battle.enemy_crystal_start[1] + UI.Battle.enemy_crystal_interval[1] * row]
            game.battle.enemy.crystal_hand[i].render(screen, game, pos)

    @staticmethod
    def render_reward_window(screen, game):
        pygame.draw.rect(screen, Color.white, UI.Window.rect)
        pygame.draw.rect(screen, Color.black, UI.Window.rect, 2)
        
        screen.blit(Font.neodgm_32.render('Select Reward', False, Color.black), UI.Window.text_title)

        for i in range(3):
            game.adventure.reward[i].render(screen, game, UI.Window.reward[i])
        pygame.draw.rect(screen, Color.black, UI.Window.button_confirm, 2)
        screen.blit(Font.neodgm_32.render('Confirm', False, Color.black), UI.Window.text_confirm)

    @staticmethod
    def render_card(screen, game):
        player_deck = game.battle.player.deck
        enemy_deck = game.battle.enemy.deck

        for i in range(4, -1, -1):
            if i < len(player_deck):
                pos = [UI.Battle.player_card_start[0] + UI.Battle.player_card_interval[0] * i, UI.Battle.player_card_start[1]]
                player_deck[i].render(screen, game, pos)

        for i in range(4, -1, -1):
            if i < len(enemy_deck):
                pos = [UI.Battle.enemy_card_start[0] + UI.Battle.enemy_card_interval[0] * i, UI.Battle.enemy_card_start[1]]
                enemy_deck[i].render(screen, game, pos)