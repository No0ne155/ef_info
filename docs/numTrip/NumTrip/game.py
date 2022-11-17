from random import*
from colorama import*
spielfeld = [[], [], [], [], []]
checklist = []
def printfield():
    global spielfeld
    print('      0         1         2         3         4   ')
    print(' +---------+---------+---------+---------+---------+')
    for i in range(5):
        for j in range(5):
            randomnumber = 2**(randint(1,4))
            if randomnumber < 10:
                spielfeld[i].append(f"    {randomnumber}    ")
            elif randomnumber < 100:
                spielfeld[i].append(f"   {randomnumber}    ")
    for k in range(5):
        print(' |         |         |         |         |         |')
        print(f"{k}|{spielfeld[k][0]}|{spielfeld[k][1]}|{spielfeld[k][2]}|{spielfeld[k][3]}|{spielfeld[k][4]}|")
        print(' |         |         |         |         |         |')
        print(' +---------+---------+---------+---------+---------+')

def game():
    global playerinputX
    global playerinputY
    global spielfeld
    printfield()
    playerinputX = int(input("X-Axis you want to choose: "))
    playerinputY = int(input("Y-Axis you want to choose: "))
    check(playerinputX, playerinputY)

def check(X, Y):
    if spielfeld[X][Y] == spielfeld[X+1][Y]:
        spielfeld[X+1][Y] = '    X    '
        checklist.append(X+1)
        checklist.append(Y)
        print(checklist)
    if spielfeld[X][Y] == spielfeld[X][Y+1]:
        spielfeld[X][Y+1] = '    X    '
        checklist.append(X)
        checklist.append(Y+1)
        print(checklist)
    if spielfeld[X][Y] == spielfeld[X][Y-1]:
        spielfeld[X][Y-1] = '    X    '
        checklist.append(X)
        checklist.append(Y-1)
        print(checklist)
    if spielfeld[X][Y] == spielfeld[X-1][Y]:
        spielfeld[X-1][Y] = '    X    '
        checklist.append(X-1)
        checklist.append(Y)
        print(checklist)
    spielfeld[X][Y] = '    Y    '
    game()
def setx():
    pass
game()