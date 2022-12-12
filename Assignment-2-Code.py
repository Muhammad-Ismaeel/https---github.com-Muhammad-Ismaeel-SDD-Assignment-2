## SDD ASSIGNMENT 2 ##
import random
import sys


def generatebuildings():
    buildings_1 = ['R  ', 'I  ', 'C  ', 'O  ', '*  ']
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


def placebuildings(selected, turn):
    x = 1
    while x > 0:
        to_build = input("Where do you want to build? ")
        to_build = to_build.upper()
        if to_build[0] not in letters:
            print("You have selected an invalid location.\n")
            continue
        else:
            player_column = letters.index(to_build[0])
            if to_build[-2] in letters:
                player_row = int(to_build[-1]) - 1
            else:
                player_row = int(to_build[-2:]) - 1
            if turn > 1:
                if map[player_row][player_column-1] != '   ' or map[player_row][player_column+1] != '   ' or map[player_row-1][player_column] != '   ' or map[player_row+1][player_column] != '   ':
                    if map[player_row][player_column] == '   ':
                        map[player_row][player_column] = selected
                        break
                    else:
                        print(
                            "You have selected a location with a building already.\n")
                        continue
                else:
                    print("You must build next to an existing building.\n")
                    continue
            else:
                if map[player_row][player_column] == '   ':
                    map[player_row][player_column] = selected

                    break
                else:
                    print("You have selected a location with a building already.\n")
                    continue
    return map


def printmap(map):
    print('{:5}{:5}{:5}{:5}{:5}{:5}{:5}{:5}{:5}{:5}{:5}{:5}{:5}{:5}{:5}{:5}{:5}{:5}{:5}{:5}{:5}'.format(
        ' ', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T'))
    print('-------------------------------------------------------------------------------------------------------')
    for row in range(0, 20):  # only printing row 1 to 4 so range is between (1,5)
        if row < 9:
            print(row + 1, ' ', end='| ')
        else:
            print(row + 1, '', end='| ')
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


def playgame(turn):
    printmap(map)
    while turn > 0:
        generatebuildings()
        placebuildings(selectbuilding(generatebuildings()), turn)
        turn += 1
        printmap(map)


# while loop to run the game
i = 1
mainmenu()
choice = int(input("What is your choice? "))
while (i > 0):
    if choice == 1:
        print('Game started!')
        print()
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

        buildings = ['R  ', 'I  ', 'C  ', 'O  ', '*  ']
        letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I',
                   'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T']
        turn = 1
        playgame(turn)
    elif choice == 2:
        print("Game Loaded!")
        print()
    elif choice == 3:
        print("Here are your high scores!")
        print()
    elif choice == 0:
        print("Goodbye!")
        break
    else:
        print("Please input a valid input")
        continue

def parkscore():
    totalparkscore = 0
    parkposition = []
    parklist = []
    for column in range(len(map)):
        for row in range(len(map)):
            if map[row][column] == "O":
                parkposition.append([row,column])
    for n in parkposition:
        if map[n[0] + 1][n[1]] == "O":
            totalparkscore += 1
        if map[n[0]][n[1] + 1] == "O":
            totalparkscore += 1
        if map[n[0] - 1][n[1]] == "O":
            totalparkscore += 1
        if map[n[0]][n[1] - 1] == "O":
            totalparkscore += 1
    return totalparkscore

def highwayscore():
        totalhighwayscore = 0;
        highwayposition = []
        highwaylist = []
        for column in range(len(map)):
            for row in range(len(map)):
                if map[row][column] == "*":
                    highwayposition.append([row,column])
                    for h in highwayposition:
                        HWYcount = 0
                        while map[player_row][player_column+HWYcount] == "*":
                            HWYcount_score += 1
                            HWY_score = HWYcount
                    totalhighwayscore = totalhighwayscore + HWY_score
        return totalhighwayscore

def commercialscore():
    totalcommercialcoin = 0
    totalcommercialscore = 0
    commercialposition = []
    commerciallist = []
    for column in range(len(map)):
        for row in range(len(map)):
            if map[row][column] == "C":
                commercialposition.append([row,column])
    for n in commercialposition:
        if map[n[0] + 1][n[1]] == "C":
            totalcommercialscore += 1
        if map[n[0]][n[1] + 1] == "C":
            totalcommercialscore += 1
        if map[n[0] - 1][n[1]] == "C":
            totalcommercialscore += 1
        if map[n[0]][n[1] - 1] == "C":
            totalcommercialscore += 1
    for x in commercialposition:
        if map[n[0] + 1][n[1]] == "R":
            totalcommercialcoin += 1
        if map[n[0]][n[1] + 1] == "R":
            totalcommercialcoin += 1
        if map[n[0] - 1][n[1]] == "R":
            totalcommercialcoin += 1
        if map[n[0]][n[1] - 1] == "R":
            totalcommercialcoin += 1
    return totalcommercialcoin,totalcommercialscore
