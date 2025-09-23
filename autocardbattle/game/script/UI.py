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
            [20, 160, 160, 160], [220, 160, 160, 160], [20, 360, 160, 160], [220, 360, 160, 160]
        ]
        button_start = [1100, 620, 160, 80]
        text_start = [1124, 644]

    class Battle:
        text_title = [24, 24]
        button_menu = [1180, 20, 80, 80]

    class Window:
        rect = [160, 40, 960, 640]

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