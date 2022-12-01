## SDD ASSIGNMENT 2 ##

def mainmenu():  # MAIN MENU FUNCTION ##
    print('1. Start new game')
    print('2. Load game')
    print('3. Show high scores')
    print()
    print('0. Exit')


# while loop to run the game
i = 1
while (i > 0):
    mainmenu()
    choice = int(input("What is your choice? "))
    if choice == 1:
        print('Game started!')
    elif choice == 2:
        print("Game Loaded!")
    elif choice == 3:
        print("Here are your high scores!")
    else:
        break
