class UI:
    class Title:
        text_title = [24, 24]
        button_start = [160, 160, 960, 80]
        text_start = [184, 184]
        button_collection = [160, 240, 960, 80]
        text_collection = [184, 264]

    class Ready:
        text_title = [24, 24]
        button_back = [1180, 20, 80, 80]
        character = [
            [20, 140, 160, 160], [220, 140, 160, 160], [420, 140, 160, 160], [20, 340, 160, 160], [220, 340, 160, 160], [420, 340, 160, 160], [20, 540, 160, 160]
        ]
        description_box = [700, 140, 560, 360]
        description_text = [704, 144, 0, 40]
        button_start = [1100, 620, 160, 80]
        text_start = [1124, 644]

    class Battle:
        text_title = [24, 24]
        button_menu = [1180, 20, 80, 80]
        field = [
            [20, 110, 160, 160], [200, 20, 160, 160], [200, 200, 160, 160], [380, 20, 160, 160], [380, 200, 160, 160],
            [1100, 110, 160, 160], [920, 20, 160, 160], [920, 200, 160, 160], [740, 20, 160, 160], [740, 200, 160, 160]
        ]
        unit_size = [160, 160]
        button_proceed = [560, 280, 160, 80]
        text_proceed = [584, 304]
        button_play = [560, 20, 80, 80]
        button_pause = [640, 20, 80, 80]
        
        player_card_start = [400, 420]
        player_card_interval = [-40, 0]
        enemy_card_start = [680, 420]
        enemy_card_interval = [40, 0]

        player_crystal_box = [20, 420, 160, 280]
        enemy_crystal_box = [1100, 420, 160, 280]

    class Window:
        rect = [160, 40, 960, 640]

    class Card:
        rect = [0, 0, 200, 280]
        crystal_start = [0, 0]
        crystal_text_start = [4, 4]
        crystal_interval = [40, 0]
        image = [60, 40, 80, 80]
        text_name = [4, 124]
        text_description = [4, 144, 0, 20]
        text_attack = [4, 244]
        text_hp = [164, 244]

    class Unit:
        rect = [0, 0, 160, 160]
        size = [160, 160]
        text_attack = [4, 124]
        text_hp = [124, 124]

    class Collection:
        text_title = [24, 24]
        button_back = [1180, 20, 80, 80]

    class Menu:
        rect = [320, 240, 640, 240]
        text_paused = [344, 264]
        button_resume = [320, 320, 640, 80]
        text_resume = [344, 344]
        button_exit = [320, 400, 640, 80]
        text_exit = [344, 424]

    crystal_size = [40, 40]