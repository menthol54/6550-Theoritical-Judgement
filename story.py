import os
from text import *
from game import *
global ent

# reading where the game left off
with open('savedata.txt', 'r') as f:
    act = f.read()

os.system('cls')

rejection = "A simple Yes or No would be appreciated."


# Begins the opening dialogue
def start():
    global act
    ent = input('Enter to continue: ')
    os.system('cls')
    time.sleep(1)
    if act and act != '1':
        restart = input('Would you like to restart? (Yes) or (No): ').lower()
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
    for x in opening_4:
        print_slow(colored(x, 'red'))
        time.sleep(0.5)


def intro_5():
    save('5')
    os.system('color')
    for x in opening_5:
        print_slow(colored(x, 'red'))
        time.sleep(0.5)


def intro_cohort():
    save('6')
    os.system('cls')
    for x in fatherless_1:
        print_slow(colored(x, 'blue'))
        time.sleep(0.5)

def intro_6():
    save('7')
    for x in opening_6:
        print_slow(colored(x, 'red'))
        time.sleep(0.5)


def conversation_omega_1():
    save('7')
    for x in fatherless_2:
        print_slow(colored(x, 'blue'))
        time.sleep(0.5)


def intro_6():
    os.system('color')
    save('8')
    for x in opening_7:
        print_slow(colored(x, 'red'))
        time.sleep(0.5)


def intro_7():
    save('9')
    for x in opening_8:
        print_slow(colored(x, 'red'))
        time.sleep(0.5)


def intro_8():
    save('10')
    os.system('cls')
    for x in opening_9:
        print_slow(colored(x, 'blue'))
        time.sleep(0.5)


def intro_9():
    save('11')
    for x in opening_10:
        print_slow(colored(x, 'blue'))
        time.sleep(0.5)
    for x in opening_11:
        print_slow(colored(x, 'blue'))
        time.sleep(2)
    print_slow(colored("End Of Cycle 1: Emergence...", 'blue'))

#End Of Opening dialogue




functions = [
    intro_1,
    intro_2,
    intro_3,
    intro_4,
    intro_5,
    intro_cohort,
    conversation_omega_1,
    intro_6,
    intro_7,
    intro_8,
    intro_9,
]
