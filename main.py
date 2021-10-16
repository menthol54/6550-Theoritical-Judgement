from dialouge import d_intro
import os
import time
from termcolor import colored
import sys
os.system('color')


def print_slow(str):
    for char in str:
        time.sleep(.09)
        sys.stdout.write(char)
        sys.stdout.flush()


def intros():
    os.system('cls')
    time.sleep(1)
    intro_1 = input('Would you like to play a game? (Yes) or (No): ')
    rejection = ("A simple Yes or No would be appreciated.")
    if intro_1 == 'yes' or intro_1 == 'Yes':
        intro_2 = input("Would you like a hear story? (Yes) or (No): ")
        if intro_2 == 'yes' or intro_2 == 'Yes':
            time.sleep(1)
            print("Very Good. Welcome to Theoritical Judgement.")
            return True
            os.system('cls')
        elif intro_2 == 'No' or intro_2 == 'no':
            print("Use Control + C to end the game. So long... user.")
        else:
            print(rejection)
            return
    elif intro_1 == 'No' or intro_1 == 'no':
        print("Use Control + C to end the game. So long... user.")
    else:
        print(rejection)
        return intros()


def intro_dialogue():
    print_slow(colored(d_intro[0], 'red'))


intro_dialogue()
