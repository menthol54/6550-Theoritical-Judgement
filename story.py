import os.path
from text import *
import time
from termcolor import colored
import os
from main import print_slow

global rejection, ent

file_0 = open('savedata.txt', 'r')
act = file_0.read()
file_0.close()


def save(s):
    file = open('savedata.txt', 'w')
    file.write(s)
    file.close()


os.system('cls')

rejection = "A simple Yes or No would be appreciated."




def start():
    ent = input('Enter to continue: ')
    os.system('cls')
    time.sleep(1)
    intro_1 = input('Would you like to play a game? (Yes) or (No): ')

    if act and act != '1':
        restart = input('Would you like to restart or continue. Enter y to continue and n to restart:\n').lower()
        if restart == 'n':
            save('1')
        elif restart == 'y':
            pass
        else:
            os.system('cls')
            print('Follow the rules...')
            time.sleep(1)
            return start()
    else:
        save('1')
    if intro_1.lower() == 'yes':
        intro_2 = input("Would you like a hear story? (Yes) or (No): ")
        if intro_2.lower() == 'yes':
            time.sleep(1)
            print("Very Good. Welcome to Theoritical Judgement.")
            time.sleep(2)
            print_slow(colored(ent, 'white'))
            os.system('cls')
            return True
        elif intro_2.lower() == 'no':
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
    print_slow(colored(opening_1[1], 'red'))
    time.sleep(0.5)
    print_slow(colored(opening_1[2], 'red'))
    time.sleep(0.5)
    print_slow(colored(opening_1[3], 'red'))
    time.sleep(0.5)
    print_slow(colored(opening_1[4], 'red'))
    time.sleep(0.5)
    print_slow(colored(opening_1[5], 'red'))
    time.sleep(0.5)


def intro_2():
    save('2')
    os.system('cls')
    os.system('color')
    print_slow(colored(opening_2[0], 'red'))
    time.sleep(0.5)
    print_slow(colored(opening_2[1], 'red'))
    print_slow(colored(opening_2[2], 'red'))
    time.sleep(0.5)
    print_slow(colored(opening_2[3], 'red'))


def intro_3():
    save('3')
    os.system('cls')
    os.system('color')
    print_slow(colored(opening_3[0], 'red'))
    print_slow(colored(opening_3[1], 'red'))
    time.sleep(0.5)
    print_slow(colored(opening_3[2], 'red'))
    time.sleep(0.5)
    print_slow(colored(opening_3[3], 'red'))
    time.sleep(0.5)
    print_slow(colored(opening_3[4], 'red'))
    print_slow(colored(opening_3[5], 'red'))
    time.sleep(0.5)
    print_slow(colored(opening_3[6], 'red'))


def intro_4():
    save('4')
    os.system('cls')
    os.system('color')
    print_slow(colored(opening_4[0], 'red'))
    time.sleep(0.5)
    print_slow(colored(opening_4[1], 'red'))
    time.sleep(0.5)
    print_slow(colored(opening_4[2], 'red'))
    time.sleep(0.5)


def intro_5():
    save('5')
    os.system('cls')
    os.system('color')
    print_slow(colored(opening_5[0], 'red'))
    time.sleep(0.5)
    print_slow(colored(opening_5[1], 'red'))
    time.sleep(0.5)
    print_slow(colored(opening_5[2], 'red'))
    time.sleep(0.5)
