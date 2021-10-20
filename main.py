import os
import time
from termcolor import colored
import sys
import story as s
os.system('color')

rejection = ("A simple Yes or No would be appreciated.")

running = False

def print_slow(str):
    for char in str:
        time.sleep(.05)
        sys.stdout.write(char)
        sys.stdout.flush()
def main():
    if s.start() == True:
        running = True
    if running == True:
        try:
            time.sleep(2)
            s.intro_1()
            time.sleep(2)
            s.intro_2()
            time.sleep(2)
            s.intro_3()
            time.sleep(2)
            s.intro_4()
            time.sleep(2)
            s.intro_5()
        except KeyboardInterrupt:
            os.system('cls')
            os.system('color')
        
if __name__ == '__main__': main()