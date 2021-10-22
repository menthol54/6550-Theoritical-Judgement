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
            if act == '1':
                for x in functions:
                    time.sleep(2)
                    x()
            elif act == '2':
                for x in functions[1:]:
                    time.sleep(2)
                    x()
            elif act == '3':
                for x in functions[2:]:
                    time.sleep(2)
                    x()
            elif act == '4':
                for x in functions[3:]:
                    time.sleep(2)
                    x()
            elif act == '5':
                for x in functions[4:]:
                    time.sleep(2)
                    x()
            elif act == '6':
                for x in functions[5:]:
                    time.sleep(2)
                    x()
            elif act == '7':
                for x in functions[6:]:
                    time.sleep(2)
                    x()
            elif act == '8':
                for x in functions[7:]:
                    time.sleep(2)
                    x()
            elif act == '9':
                for x in functions[8:]:
                    time.sleep(2)
                    x()
    except KeyboardInterrupt:
        os.system('color')
        os.system('cls')


if __name__ == '__main__':
    main()
input('\n...')
