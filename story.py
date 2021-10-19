from monologue import opening_1
import time
import sys
from termcolor import colored
import os

global rejection

rejection = ("A simple Yes or No would be appreciated.")

def print_slow(str):
    for char in str:
        time.sleep(.09)
        sys.stdout.write(char)
        sys.stdout.flush()

def start():
    os.system('cls')
    time.sleep(1)
    intro_1 = input('Would you like to play a game? (Yes) or (No): ')
    if intro_1.lower() == 'yes':
        intro_2 = input("Would you like a hear story? (Yes) or (No): ")
        if intro_2.lower() == 'yes':
            time.sleep(1)
            print("Very Good. Welcome to Theoritical Judgement.")
            time.sleep(0.2)
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
    os.system('cls')
    os.system('color 70')
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
intro_1()