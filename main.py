import story as s
import os
import time
import story as s
from termcolor import colored


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


def story():
    print(s.d_intro[0])
    print(colored("What is your name?", 'green'))


story()
