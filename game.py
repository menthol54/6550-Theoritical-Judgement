from gtext import *
from termcolor import colored
import time
import sys
import os


# checks is savadata exists
def save_check():
    x = os.path.isfile('savedata.txt')
    return x


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
    def __init__(self, persuasion=5, spirit=5, maturity=10, pride=5, empathy=5):
        self.persuasion = persuasion
        self.spirit = spirit
        self.maturity = maturity
        self.pride = pride
        self.empathy = empathy

    def event_1(self):
        for key, value in event01_op.items():
            print_slow(colored(key + ' => ' + value, 'yellow'))
        ans = input('')
        if ans.lower() == 'a':
            print_slow(colored(list(event01_op.values())[0], 'red'))
            self.maturity += 1
        elif ans.lower() == 'b':
            print_slow(colored(list(event01_op.values())[1], 'red'))
            self.spirit += 1
        elif ans.lower() == 'c':
            print_slow(colored(list(event01_op.values())[2], 'red'))
            self.maturity -= 1
            self.spirit -= 1
        else:
            return Player.event_1(self)
    
    def event_2(self):
        for key, value in event02_op.items():
            print_slow(colored(key + '=>' + value, 'yellow'))    
        ans = input('')
        if ans.lower() == 'a':
            print_slow(colored(list(event02_op.values())[0], 'red'))
            self.empathy += 1
            self.maturity += 1
        elif ans.lower() == 'b':
            print_slow(colored(list(event02_op.values())[1],'red'))
            self.empathy -= 1
        elif ans.lower() == 'c':
            print_slow(colored(list(event02_op.values())[2], 'red'))
            self.empathy -= 3
        else:
            return Player.event_2(self)
