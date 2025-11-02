import sys, traceback
from script.game import *

def main():
    try:
        game = Game()
        game.run()
    except:
        traceback.print_exc()
        sys.exit()

if __name__ == '__main__':
    main()