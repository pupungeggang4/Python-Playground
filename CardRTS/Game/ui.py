class UI():
    class Title():
        text_title = [24, 24]
        text_start = [184, 184]
        button_start = [160, 160, 960, 80]
        text_erase = [184, 264]
        button_erase = [160, 240, 960, 80]

    class Level_Select():
        text_title = [24, 24]
        button_back = [1160, 40, 80, 80]
        button_level = [
            [160, 160, 160, 160], [400, 160, 160, 160], [640, 160, 160, 160],
            [160, 400, 160, 160], [400, 400, 160, 160], [640, 400, 160, 160]
        ]

    class Character_Select():
        text_title = [24, 24]
        button_back = [1160, 40, 80, 80]
        button_character = [
            [160, 160, 160, 160], [400, 160, 160, 160], [640, 160, 160, 160],
            [160, 400, 160, 160], [400, 400, 160, 160], [640, 400, 160, 160]
        ]

    class Battle():
        text_title = [24, 24]
        button_menu = [1160, 40, 80, 80]

    class Menu():
        rect = [320, 280, 640, 240]
        text_paused = [344, 304]
        button_resume = [320, 360, 960, 80]
        text_resume = [344, 384]
        button_exit = [320, 440, 960, 80]
        text_exit = [344, 464]