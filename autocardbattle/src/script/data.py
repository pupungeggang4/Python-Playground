class Data():
    card = {
        801: {'ID': 1, 'name': 'Simple 1', 'type': 'unit', 'element': 'normal', 'crystal': [[8, 1]], 'crystal_list': [8], 'stat': [1, 2], 'effect': []},
        802: {'ID': 2, 'name': 'Simple 2', 'type': 'unit', 'element': 'normal', 'crystal': [[8, 2]], 'crystal_list': [8, 8], 'stat': [2, 3], 'effect': []},
        803: {'ID': 3, 'name': 'Simple 3', 'type': 'unit', 'element': 'normal', 'crystal': [[8, 3]], 'crystal_list': [8, 8, 8], 'stat': [3, 4], 'effect': []},
        101: {'ID': 101, 'name': 'Attack', 'type': 'spell', 'element': 'fire', 'crystal': [[1, 1]], 'crystal_list': [1], 'stat': [0, 0], 'effect': []},
        301: {'ID': 301, 'name': 'Fast attack', 'type': 'spell', 'element': 'wind', 'crystal': [[3, 1], [8, 1]], 'crystal_list': [3, 8], 'stat': [0, 0], 'effect': []},
        401: {'ID': 501, 'name': 'Guard', 'type': 'spell', 'element': 'earth', 'crystal': [[4, 1]], 'crystal_list': [4], 'stat': [0, 0], 'effect': []}
    }
    card_p = {
        801: [['summon']],
        802: [['summon']],
        803: [['summon']],
        101: [['dmg_hero', 3]],
        301: [['dmg_random', 2], ['gain_acceler', 1]],
        401: [['gain_armor', 5]],
    }
    card_d = {
        801: [],
        802: [],
        803: [],
        101: ['Deal 3 damage to', 'enemy hero.'],
        301: ['Deal 2 damage to', 'random enemy unit.', 'Gain 1 acceler.'],
        401: ['Gain 5 armor'],
    }
    crystal = {
        1: {'ID': 1, 'name': 'fire crystal', 'element': 1, 'effect': []},
        2: {'ID': 2, 'name': 'water crystal', 'element': 2, 'effect': []},
        3: {'ID': 3, 'name': 'wind crystal', 'element': 3, 'effect': []},
        4: {'ID': 4, 'name': 'earth crystal', 'element': 4, 'effect': []},
        5: {'ID': 5, 'name': 'light crystal', 'element': 5, 'effect': []},
        6: {'ID': 6, 'name': 'dark crystal', 'element': 6, 'effect': []},
        7: {'ID': 7, 'name': 'rainbow crystal', 'element': 7, 'effect': []},
        8: {'ID': 8, 'name': 'normal crystal', 'element': 8, 'effect': []},
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
        1001: {'deck': [101, 101, 101, 101, 101, 101, 101, 101, 803, 803, 803, 803], 'crystal': [1, 1, 1, 1, 8, 8, 8, 8]},
        1002: {'deck': [801, 801, 801, 801, 802, 802, 802, 802, 803, 803, 803, 803], 'crystal': [2, 2, 2, 2, 8, 8, 8, 8]},
        1003: {'deck': [301, 301, 301, 301, 301, 301, 301, 301, 803, 803, 803, 803], 'crystal': [3, 3, 3, 3, 8, 8, 8, 8]},
        1004: {'deck': [401, 401, 401, 401, 802, 802, 802, 802, 803, 803, 803, 803], 'crystal': [4, 4, 4, 4, 8, 8, 8, 8]},
        1005: {'deck': [801, 801, 801, 801, 802, 802, 802, 802, 803, 803, 803, 803], 'crystal': [5, 5, 5, 5, 8, 8, 8, 8]},
        1006: {'deck': [801, 801, 801, 801, 802, 802, 802, 802, 803, 803, 803, 803], 'crystal': [6, 6, 6, 6, 8, 8, 8, 8]},
        1007: {'deck': [801, 801, 801, 801, 802, 802, 802, 802, 803, 803, 803, 803], 'crystal': [7, 7, 8, 8, 8, 8, 8, 8]}
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
        1001: {'deck': [801, 801, 801, 801, 801, 801, 801, 801], 'crystal': [8, 8, 8, 8, 8, 8, 8, 8], 'hp': 15}
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
