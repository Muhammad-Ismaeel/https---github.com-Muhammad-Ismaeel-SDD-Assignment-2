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


def residentialscore():
    residentialscore = 0
    totalresidentialscore = 0
    residentialposition = []
    residentiallist = []
    for column in range(len(map)):
        for row in range(len(map)):
            if map[row][column] == "R":
                residentialposition.append([row, column])
    for n in residentialposition:
        if map[n[0] + 1][n[1]] == "I" or map[n[0]][n[1] + 1] == "I" or map[n[0] - 1][n[1]] == "I" or map[n[0]][n[1] - 1] == "I":
            residentialscore = 1
        else:
            if (map[n[0] + 1][n[1]] == "R" or map[n[0] + 1][n[1]] == "C"):
                residentialscore += 1
            if map[n[0]][n[1] + 1] == "R" or map[n[0]][n[1] + 1] == "C":
                residentialscore += 1
            if map[n[0] - 1][n[1]] == "R" or map[n[0] - 1][n[1]] == "C":
                residentialscore += 1
            if map[n[0]][n[1] - 1] == "R" or map[n[0]][n[1] - 1] == "C":
                residentialscore += 1

            if map[n[0] + 1][n[1]] == "O":
                residentialscore += 2
            if map[n[0]][n[1] + 1] == "O":
                residentialscore += 2
            if map[n[0] - 1][n[1]] == "O":
                residentialscore += 2
            if map[n[0]][n[1] - 1] == "O":
                residentialscore += 2
        residentiallist.append(residentialscore)
        residentialscore -= residentialscore

    for t in residentiallist:
        totalresidentialscore += t
    residentialprint = ' + '.join(str(s) for s in residentiallist)
    if totalresidentialscore != 0:
        print('{}:{}{}{}'.format(
            buildings[0], residentialprint, ' = ', totalresidentialscore))
    elif totalresidentialscore == 0:
        print('{}:{}'.format(buildings[0], 0))

    return totalresidentialscore


def industryscore():
    industryscore = 0
    totalindustrycoin = 0
    totalindustryscore = 0
    industryposition = []
    industrylist = []
    for column in range(len(map)):
        for row in range(len(map)):
            if map[row][column] == "I":
                industryposition.append([row, column])
    for n in industryposition:
        industryscore += 1
        industrylist.append(industryscore)
        industryscore -= industryscore

    for t in industrylist:
        totalindustryscore += t
    industryprint = ' + '.join(str(s) for s in industrylist)
    if totalindustryscore != 0:
        print('{}:{}{}{}'.format(
            buildings[1], industryprint, ' = ', totalindustryscore))
    elif totalindustryscore == 0:
        print('{}:{}'.format(buildings[1], 0))

    return totalindustryscore


def commercialscore():
    commercialscore = 0
    totalcommercialscore = 0
    commercialposition = []
    commerciallist = []
    for column in range(len(map)):
        for row in range(len(map)):
            if map[row][column] == "C":
                commercialposition.append([row, column])
    for n in commercialposition:
        if map[n[0] + 1][n[1]] == "C":
            commercialscore += 1
        if map[n[0]][n[1] + 1] == "C":
            commercialscore += 1
        if map[n[0] - 1][n[1]] == "C":
            commercialscore += 1
        if map[n[0]][n[1] - 1] == "C":
            commercialscore += 1
        commerciallist.append(commercialscore)
        commercialscore -= commercialscore

    for t in commerciallist:
        totalcommercialscore += t
    commercialprint = ' + '.join(str(s) for s in commerciallist)
    if totalcommercialscore != 0:
        print('{}:{}{}{}'.format(
            buildings[2], commercialprint, ' = ', totalcommercialscore))
    elif totalcommercialscore == 0:
        print('{}:{}'.format(buildings[2], 0))

    return totalcommercialscore


def parkscore():
    parkscore = 0
    totalparkscore = 0
    parkposition = []
    parklist = []
    for column in range(len(map)):
        for row in range(len(map)):
            if map[row][column] == "O":
                parkposition.append([row, column])
    for n in parkposition:
        if map[n[0] + 1][n[1]] == "O":
            parkscore += 1
        if map[n[0]][n[1] + 1] == "O":
            parkscore += 1
        if map[n[0] - 1][n[1]] == "O":
            parkscore += 1
        if map[n[0]][n[1] - 1] == "O":
            parkscore += 1
        parklist.append(parkscore)
        parkscore -= parkscore

    for t in parklist:
        totalparkscore += t
    parkprint = ' + '.join(str(s) for s in parklist)
    if totalparkscore != 0:
        print('{}:{}{}{}'.format(
            buildings[3], parkprint, ' = ', totalparkscore))
    elif totalparkscore == 0:
        print('{}:{}'.format(buildings[3], 0))

    return totalparkscore


def roadscore():
    roadscore = 0
    totalroadscore = 0
    roadposition = []
    roadlist = []
    for column in range(len(map)):
        for row in range(len(map)):
            if map[row][column] == "*":
                roadposition.append([row, column])
    for n in roadposition:
        if map[n[0] + 1][n[1]] == "*":
            roadscore += 1
        if map[n[0] - 1][n[1]] == "*":
            roadscore += 1
        roadlist.append(roadscore)
        roadscore -= roadscore

    for t in roadlist:
        totalroadscore += t
    roadprint = ' + '.join(str(s) for s in roadlist)
    if totalroadscore != 0:
        print('{}:{}{}{}'.format(
            buildings[4], roadprint, ' = ', totalroadscore))
    elif totalroadscore == 0:
        print('{}:{}'.format(buildings[4], 0))

    return totalroadscore


def savegame():
    print('Game Saved!')


def viewcurrentscore(totalroadscore, totalparkscore, totalcommercialscore, totalindustryscore, totalresidentialscore):
    print("{:47} {}".format(
        "The score for the residential buildings is : ", totalresidentialscore))
    print("{:47} {}".format(
        "The score for the industry buildings is : ", totalindustryscore))
    print("{:47} {}".format(
        "The score for the commercial buildings is : ", totalcommercialscore))
    print("{:47} {}".format("The score for the parks is : ", totalparkscore))
    print("{:47} {}".format("The score for the roads is : ", totalroadscore))
    print()
    currentscore = totalresidentialscore + totalindustryscore + \
        totalcommercialscore + totalparkscore + totalroadscore
    print("{:47} {}".format("Your current score is : ", currentscore))


def rungame(list_options):
    p = 0
    while p < 1:
        print("{:17}{}".format("Turn Number: ", turn))
        print("{:17}{}".format("Coins Remaining: ", totalcoin))
        print()
        print("Choose one.")
        print('Select your building to place')
        print('Option 1: ', list_options[0])
        print('Option 2: ', list_options[1])
        print()
        print('Other Options:')
        print('Option 3: Save Game')
        print('Option 4: Current Score')
        print('Option 5: Exit Game')

        chosen = int(input('What option number do you wish to select? '))

        if chosen == 1:
            selected = list_options[0]
            break

        elif chosen == 2:
            selected = list_options[1]
            break

        elif chosen == 3:
            savegame()

            selected = 7
            break

        elif chosen == 4:
            viewcurrentscore(roadscore(), parkscore(
            ), commercialscore(), industryscore(), residentialscore())

            selected = 7
            break

        elif chosen == 5:
            mainmenu()
            choice = int(input("What is your choice? "))

            selected = 7

        else:
            print('You have selected an invalid option')

    return selected


def placebuildings(selected, turn, totalcoin):
    x = 1
    while x > 0:
        if selected == 7:
            break
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
                        totalcoin -= 1
                        if selected == 'C' or selected == "I":
                            if map[player_row + 1][player_column] == 'R':
                                totalcoin += 1
                            if map[player_row][player_column + 1] == 'R':
                                totalcoin += 1
                            if map[player_row - 1][player_column] == 'R':
                                totalcoin += 1
                            if map[player_row][player_column - 1] == 'R':
                                totalcoin += 1
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


def printmap():
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
    printmap()
    while turn > 0:
        placebuildings(rungame(generatebuildings()), turn, totalcoin)
        turn += 1
        printmap()


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
        totalcoin = 16
        notcountedindustrycoins = []
        notcountedcommercialcoins = []
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


def highwayscore():
    totalhighwayscore = 0
    highwayposition = []
    highwaylist = []
    for column in range(len(map)):
        for row in range(len(map)):
            if map[row][column] == "*":
                highwayposition.append([row, column])
                for h in highwayposition:
                    HWYcount = 0
                    while map[player_row][player_column+HWYcount] == "*":
                        HWYcount_score += 1
                        HWY_score = HWYcount
                totalhighwayscore = totalhighwayscore + HWY_score
    return totalhighwayscore


# def coincounter():
#     commercialcoinlist = []
#     totalcommercialcoin = 0
#     commercialcoin = 0
#     commercialposition = []
#     for column in range(len(map)):
#         for row in range(len(map)):
#             if map[row][column] == "C":
#                 commercialposition.append([row,column])
#     for n in commercialposition:
#         if map[n[0] + 1][n[1]] == "R":
#             commercialcoin += 1
#         if map[n[0]][n[1] + 1] == "R":
#             commercialcoin += 1
#         if map[n[0] - 1][n[1]] == "R":
#             commercialcoin += 1
#         if map[n[0]][n[1] - 1] == "R":
#             commercialcoin += 1
#         commercialcoinlist.append(commercialcoin)
#         notcountedcommercialcoins.append(commercialcoin)
#         commercialcoin -= commercialcoin
#     setcommercial1 = set(commercialcoinlist)
#     setcommercial2 = set(notcountedcommercialcoins)
#     commercialcoinsimilarities = setcommercial1.intersection(setcommercial2)
#     commercialcoinsimilaritieslist = list(commercialcoinsimilaritieslist)
#     for n in commercialcoinsimilaritieslist:
#         totalcommercialcoin += n
#         notcountedcommercialcoins.remove(n)
