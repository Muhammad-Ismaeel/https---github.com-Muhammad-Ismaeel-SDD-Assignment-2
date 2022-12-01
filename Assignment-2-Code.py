## SDD ASSIGNMENT 2 ##

def mainmenu():  # MAIN MENU FUNCTION ##
    print('''Welcome, mayor of Simp City!
----------------------------
1. Start new game
2. Load saved game
3.Display High Scores

0. Exit
''')
    while True:
        try:
            answer = int(input("Your choice? "))
        except ValueError:
            print('Please enter a valid number')
            continue
        if answer > 3 or answer < 0:
            print('Make sure the number is a valid choice')
        else:
            break


mainmenu()
