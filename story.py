import os.path
from text import *
import time
from termcolor import colored
import os
from main import print_slow

global ent

file_0 = open('savedata.txt', 'r')
act = file_0.read()
file_0.close()

# duvaarn to cravin


def save(s):
    file = open('savedata.txt', 'w')
    file.write(s)
    file.close()


os.system('cls')

rejection = "A simple Yes or No would be appreciated."


def start():
    global act
    ent = input('Enter to continue: ')
    os.system('cls')
    time.sleep(1)
    if act and act != '1':
        restart = input('Would you like to restart or continue. (Yes) or (No): ').lower()
        if restart == 'yes':
            act = '1'
            save('1')
        elif restart == 'no':
            pass
        else:
            os.system('cls')
            print('Follow the rules...')
            time.sleep(1)
            return start()
    else:
        save('1')
    intro_1 = input('Would you like to play a game? (Yes) or (No): ')
    if intro_1.lower() == 'yes':
        intro_2_ = input("Would you like a hear story? (Yes) or (No): ")
        if intro_2_.lower() == 'yes':
            time.sleep(1)
            print("Very Good. Welcome to Theoretical Judgement.")
            time.sleep(2)
            print_slow(colored(ent, 'white'))
            os.system('cls')
            return True
        elif intro_2_.lower() == 'no':
            print("Use Control + C to end the game. So long... user.")
        else:
            print(rejection)
            time.sleep(1)
            start()
    elif intro_1.lower() == 'no':
        print("Use Control + C to end the game. So long... user.")
    else:
        print(rejection)
        time.sleep(1)
        start()


def intro_1():
    save('1')
    os.system('cls')
    print_slow(colored(opening_1[0], 'blue'))
    time.sleep(0.5)
    for x in opening_1[1:]:
        print_slow(colored(x, 'red'))
        time.sleep(0.5)


def intro_2():
    save('2')
    os.system('cls')
    os.system('color')
    for x in opening_2:
        print_slow(colored(x, 'red'))
        time.sleep(0.5)


def intro_3():
    save('3')
    for x in opening_3:
        print_slow(colored(x, 'red'))
        time.sleep(0.5)


def intro_4():
    save('4')
    os.system('cls')
    os.system('color')
    for x in opening_4:
        print_slow(colored(x, 'red'))
        time.sleep(0.5)


def intro_5():
    save('5')
    os.system('cls')
    os.system('color')
    for x in opening_5:
        print_slow(colored(x, 'red'))
        time.sleep(0.5)


def intro_cohort():
    save('6')
    os.system('cls')
    os.system('color')
    for x in fatherless_1:
        print_slow(colored(x, 'red'))
        time.sleep(0.5)


functions = [
    intro_1,
    intro_2,
    intro_3,
    intro_4,
    intro_5,
    intro_cohort
]
