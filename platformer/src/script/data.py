import json

class Data():
    level = {}

def load_data():
    Data.level = {}
    f = open('data/level1.json', 'r')
    tmp = {}
    Data.level[1] = json.loads(f.read())
