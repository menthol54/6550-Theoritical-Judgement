from dialouge import d_intro
import os
import time
from termcolor import colored
import sys
os.system('color')

global rejection, running

rejection = ("A simple Yes or No would be appreciated.")

running = False

def print_slow(str):
    for char in str:
        time.sleep(.09)
        sys.stdout.write(char)
        sys.stdout.flush()


def intros():
    os.system('cls')
    time.sleep(1)
    intro_1 = input('Would you like to play a game? (Yes) or (No): ')
    if intro_1.lower() == 'yes':
        intro_2 = input("Would you like a hear story? (Yes) or (No): ")
        if intro_2.lower() == 'yes':
            time.sleep(1)
            print("Very Good. Welcome to Theoritical Judgement.")
            time.sleep(0.5)
            os.system('cls')
            return True
        elif intro_2.lower() == 'no':
            print("Use Control + C to end the game. So long... user.")
        else:
            print(rejection)
            time.sleep(1)
            intros()
    elif intro_1.lower() == 'no':
        print("Use Control + C to end the game. So long... user.")
    else:
        print(rejection)
        time.sleep(1)
        intros()

def intro_dialogue():
    os.system('cls')
    print_slow(colored(d_intro[0], 'red'))

