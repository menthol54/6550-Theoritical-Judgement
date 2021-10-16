from dialouge import d_intro
import os
import time
from termcolor import colored
import sys


def print_slow(str):
    for char in str:
        time.sleep(.09)
        sys.stdout.write(char)
        sys.stdout.flush()

def game_story():
    def naming():
        global name
        os.system('cls')
        print_slow(colored(d_intro[0], 'red'))
        print_slow(colored(d_intro[1], 'red'))
        print_slow(colored(d_intro[2], 'red'))
        time.sleep(0.1)
        name = input("")
        if name.lower() == 'yes':
            name = input("What is your name?\n")
            print_slow(colored("Are you sure?\n", 'red'))
            name_confirmation = input("")
            if name_confirmation.lower() == 'yes':
                return True
            if name_confirmation.lower() == 'no':
                print(name)
            else:
                print_slow(colored("Are you sure?\n", 'red'))
        
        if name.lower() == 'no':
            req_no = input("Are you sure?\n")
            if req_no.lower() == 'yes':
                return
            if req_no.lower() == 'no':
                print(name)
    naming()
game_story()