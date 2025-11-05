import traceback
from script.game import *

def main():
    game = Game()
    game.run()

if __name__ == '__main__':
    try:
        main()
    except:
        traceback.print_exc()