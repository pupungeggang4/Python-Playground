class UI():
    class Title():
        text_title = [24, 24]
        button_start = [160, 160, 960, 80]
        text_start = [184, 184]
        button_collection = [160, 240, 960, 80]
        text_collection = [184, 264]
        button_lang = [160, 320, 960, 80]
        text_lang = [184, 344]
        button_erase = [160, 400, 960, 80]
        text_erase = [184, 424]
        button_exit = [160, 480, 960, 80]
        text_exit = [184, 504]
        arrow = [[80, 160], [80, 240], [80, 320], [80, 400], [80, 480]]

    class Village():
        button_menu = [1180, 20, 80, 80]
        text_control = [24, 664]

    class Battle():
        button_menu = [1180, 20, 80, 80]
        icon_exp = [20, 60]
        text_exp = [64, 70]
        bar_exp = [20, 20, 1240, 20]
        icon_gold = [20, 100]
        text_gold = [64, 110]
        icon_hp = [20, 140]
        text_hp = [88, 150]
        bar_hp = [80, 144, 140, 32]
        icon_energy = [20, 180]
        text_energy = [88, 190]
        bar_energy = [80, 184, 140, 32]

    class Menu_Village():
        rect = [320, 200, 640, 320]
        text_paused = [344, 224]
        button_resume = [320, 280, 640, 80]
        text_resume = [344, 304]
        button_exit = [320, 360, 640, 80]
        text_exit = [344, 384]
        button_quit = [320, 440, 640, 80]
        text_quit = [344, 464]
        arrow = [[240, 280], [240, 360], [240, 440]]

    class Menu_Battle():
        rect = [320, 160, 640, 320]
        text_paused = [344, 184]
        button_resume = [320, 240, 640, 80]
        text_resume = [344, 264]
        button_surrender = [320, 320, 640, 80]
        text_surrender = [344, 344]
        button_exit = [320, 400, 640, 80]
        text_exit = [344, 424]
        button_quit = [320, 480, 640, 80]
        text_quit = [344, 504]
        arrow = [[240, 240], [240, 320], [240, 400], [240, 480], [240, 560]]

    class Window_Battle_Confirm():
        rect = [320, 200, 640, 240]
        text_title = [344, 224]
        arrow = [[360, 320], [680, 320]]
        text_yes = [464, 344]
        text_no = [784, 344]

    class Window():
        rect = [160, 40, 960, 640]
        text_title = [184, 64]
        button_reward = [[200, 120, 200, 280], [540, 120, 200, 280], [880, 120, 200, 280]]
        text_reward = [[204, 324], [544, 324], [884, 324]]
        button_weapon = [[200, 240, 200, 200], [540, 240, 200, 200], [880, 240, 200, 200]]
        arrow_weapon = [[260, 120], [600, 120], [940, 120]]
        button_confirm = [560, 160, 580, 80]
        text_confirm = [584, 184]