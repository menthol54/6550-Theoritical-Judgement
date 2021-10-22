from gtext import *
import time
from termcolor import colored
import os
from main import print_slow


def save(s):
    file = open('savedata.txt', 'w')
    file.write(s)
    file.close()
class Player:
    def __init__(self, persuasion = 5, spirit = 5, maturity = 10, pride = 5, love = 1):
        self.persuasion = persuasion
        self.spirit = spirit
        self.maturity = maturity
        self.pride = pride
        self.love = love

    def event_1():
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
            return Player.event_1()
