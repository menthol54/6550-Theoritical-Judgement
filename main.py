import story as s
from story import *
import os
import time
import sys
# duvaarn to cravin
os.system('color')

rejection = "A simple Yes or No would be appreciated."

running = False


def print_slow(string):
    for char in string:
        time.sleep(.05)
        sys.stdout.write(char)
        sys.stdout.flush()


def main():
    global running, act
    try:
        if s.start():
            running = True
            from story import act
        if running:
            for x in functions[int(act) - 1:]:
                time.sleep(2)
                x()
    except KeyboardInterrupt:
        os.system('cls')
        os.system('color')


if __name__ == '__main__':
    main()
input('\n...')
