import story as s
from story import *
import os
import time

os.system('color')


# Tests if function start was carried out properly and runs the game if it was
def main():
    global act
    try:
        if s.start():
            for x in functions[int(act) - 1:]:
                time.sleep(2)
                x()
                #os.system('cls')
    except KeyboardInterrupt:
        os.system('color')
        #os.system('cls')
        


# calls and runs the game
if __name__ == '__main__':
    main()
input('\n...')
