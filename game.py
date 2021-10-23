from gtext import *
from termcolor import colored
import time
import sys


# writes the given value to savedata
def save(s):
    with open('savedata.txt', 'w') as f:
        f.write(s)


def print_slow(string):
    for char in string:
        time.sleep(.05)
        sys.stdout.write(char)
        sys.stdout.flush()


class Player:
    def __init__(self, persuasion=5, spirit=5, maturity=10, pride=5, love=1):
        self.persuasion = persuasion
        self.spirit = spirit
        self.maturity = maturity
        self.pride = pride
        self.love = love

    def event_1(self):
        save('9')
        for x in event_01:
            print_slow(colored(x, 'red'))
        for x in event_01_op:
            print_slow(colored(x, 'red'))
        ans = input('')
        if ans.lower() == 'a':
            print('a')
        elif ans.lower() == 'b':
            print('b')
        elif ans.lower() == 'c':
            print('c')
        else:
            return Player.event_1(self)
