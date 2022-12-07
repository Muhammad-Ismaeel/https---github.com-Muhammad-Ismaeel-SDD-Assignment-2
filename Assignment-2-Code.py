## SDD ASSIGNMENT 2 ##
import random
import sys

map = [['   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   '],
       ['   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ',
           '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   '],
       ['   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ',
           '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   '],
       ['   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ',
           '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   '],
       ['   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ',
           '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   '],
       ['   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ',
           '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   '],
       ['   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ',
           '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   '],
       ['   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ',
           '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   '],
       ['   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ',
           '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   '],
       ['   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ',
           '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   '],
       ['   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ',
           '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   '],
       ['   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ',
           '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   '],
       ['   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ',
           '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   '],
       ['   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ',
           '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   '],
       ['   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ',
           '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   '],
       ['   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ',
           '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   '],
       ['   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ',
           '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   '],
       ['   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ',
           '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   '],
       ['   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ',
           '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   '],
       ['   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ',
           '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ', '   ']
       ]

buildings = ['R', 'I', 'C', 'O', '*']


def generatebuildings():
    buildings_1 = ['R', 'I', 'C', 'O', '*']
    first_opt = buildings[random.randint(0, 4)]
    to_pop = buildings_1.index(first_opt)
    buildings_1.pop(to_pop)
    second_opt = buildings_1[random.randint(0, 3)]
    list_options = [first_opt, second_opt]
    buildings_1 = ['R', 'I', 'C', 'O', '*']
    return list_options


def selectbuilding(list_options):
    p = 0
    while p < 1:
        print('Select your building to place')
        print('Option 1: ', list_options[0])
        print('Option 2: ', list_options[1])
        chosen = int(input('Which building do you wish to place? '))

        if chosen == 1:
            selected = list_options[0]
            break
        elif chosen == 2:
            selected = list_options[1]
            break
        else:
            print('You have selected an invalid option')
    return selected


def printmap(map):
    print('-------------------------------------------------------------------------------------------------------')
    for row in range(0, 20):  # only printing row 1 to 4 so range is between (1,5)
        if row < 9:
            print(row + 1, '', end='| ')
        else:
            print(row + 1, end='| ')
        for column in range(0, 20):  # only printing column 1 to 4 so range is between (1,5)

            # spacing for " , end= ' | ' " different for empty space and with a building
            print(map[row][column], end='| ')
        print()
        print('-------------------------------------------------------------------------------------------------------')


def mainmenu():  # MAIN MENU FUNCTION ##
    print('1. Start new game')
    print('2. Load game')
    print('3. Show high scores')
    print()
    print('0. Exit')


def playgame():
    printmap(map)
    generatebuildings()
    selectbuilding(generatebuildings())


# while loop to run the game
i = 1
while (i > 0):
    mainmenu()
    choice = int(input("What is your choice? "))
    if choice == 1:
        print('Game started!')
        playgame()
    elif choice == 2:
        print("Game Loaded!")
    elif choice == 3:
        print("Here are your high scores!")
    elif choice == 0:
        print("Goodbye!")
        break
    else:
        print("Please input a valid input")
        continue
        
