class Data():
    card = {
        801: {'ID': 1, 'name': 'Simple 1', 'type': 'unit', 'element': 'normal', 'crystal': [[1, 1]], 'crystal_list': [1], 'stat': [1, 2], 'effect': []},
        802: {'ID': 2, 'name': 'Simple 2', 'type': 'unit', 'element': 'normal', 'crystal': [[1, 2]], 'crystal_list': [1, 1], 'stat': [2, 3], 'effect': []},
        803: {'ID': 3, 'name': 'Simple 3', 'type': 'unit', 'element': 'normal', 'crystal': [[1, 3]], 'crystal_list': [1, 1, 1], 'stat': [3, 4], 'effect': []},
        401: {'ID': 501, 'name': 'Guard', 'type': 'spell', 'element': 'earth', 'crystal': [[5, 1]], 'crystal_list': [5], 'stat': [0, 0], 'effect': []}
    }
    card_p = {
        801: [['summon']],
        802: [['summon']],
        803: [['summon']],
        401: [['armor', 5]],
    }
    card_d = {
        801: [],
        802: [],
        803: [],
        401: ['Gain 5 armor'],
    }
    crystal = {
        1: {'ID': 1, 'name': 'normal crystal', 'element': 1, 'effect': []},
        2: {'ID': 2, 'name': 'fire crystal', 'element': 2, 'effect': []},
        3: {'ID': 3, 'name': 'water crystal', 'element': 3, 'effect': []},
        4: {'ID': 4, 'name': 'wind crystal', 'element': 4, 'effect': []},
        5: {'ID': 5, 'name': 'earth crystal', 'element': 5, 'effect': []},
        6: {'ID': 6, 'name': 'light crystal', 'element': 6, 'effect': []},
        7: {'ID': 7, 'name': 'dark crystal', 'element': 7, 'effect': []},
        8: {'ID': 8, 'name': 'rainbow crystal', 'element': 8, 'effect': []}
    }
    crystal_d = {
        1: [],
        2: [],
        3: [],
        4: [],
        5: [],
        6: [],
        7: [],
        8: []
    }
    equipment = {

    }
    equipment_d = {

    }
    character = {
        1001: {'deck': [801, 801, 801, 801, 802, 802, 802, 802, 803, 803, 803, 803], 'crystal': [1, 1, 1, 1, 2, 2, 2, 2]},
        1002: {'deck': [801, 801, 801, 801, 802, 802, 802, 802, 803, 803, 803, 803], 'crystal': [1, 1, 1, 1, 3, 3, 3, 3]},
        1003: {'deck': [801, 801, 801, 801, 802, 802, 802, 802, 803, 803, 803, 803], 'crystal': [1, 1, 1, 1, 4, 4, 4, 4]},
        1004: {'deck': [401, 401, 401, 401, 802, 802, 802, 802, 803, 803, 803, 803], 'crystal': [1, 1, 1, 1, 5, 5, 5, 5]},
        1005: {'deck': [801, 801, 801, 801, 802, 802, 802, 802, 803, 803, 803, 803], 'crystal': [1, 1, 1, 1, 6, 6, 6, 6]},
        1006: {'deck': [801, 801, 801, 801, 802, 802, 802, 802, 803, 803, 803, 803], 'crystal': [1, 1, 1, 1, 7, 7, 7, 7]},
        1007: {'deck': [801, 801, 801, 801, 802, 802, 802, 802, 803, 803, 803, 803], 'crystal': [1, 1, 1, 1, 1, 1, 8, 8]}
    }
    character_d = {
        1001: ['Fire Character', 'Gain more energy.'],
        1002: ['Water Character', 'Do random things.'],
        1003: ['Wind Character', 'Play mode card.'],
        1004: ['Earth Character', 'Gain defense.'],
        1005: ['Light Character', 'Heal units.'],
        1006: ['Dark Character', 'Gain power.'],
        1007: ['All Character', 'Use all cards.']
    }
    enemy = {
        1001: {'deck': [801, 801, 801, 801, 801, 801, 801, 801], 'crystal': [1, 1, 1, 1, 1, 1, 1, 1], 'hp': 15}
    }
    reward_pool = {
        1001: [],
        1002: [],
        1003: [],
        1004: [],
        1005: [],
        1006: [],
        1007: [],
    }
    enemy_pool = {

    }
    elite_pool = {

    }
    boss_pool = {

    }
