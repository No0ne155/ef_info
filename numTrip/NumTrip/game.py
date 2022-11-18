from random import*
spielfeld = [[], [], [], [], []]
checklist = []
removed = []
def printfield():
    global spielfeld
    print('\Y    0         1         2         3         4   ')
    print('X+---------+---------+---------+---------+---------+')
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
    if len(checklist) > 0:
        check(checklist[0], checklist[1])
        checklist.pop(1)
        checklist.pop(0)
    printfield()
    playerinputX = int(input("X-Axis you want to choose: "))
    playerinputY = int(input("Y-Axis you want to choose: "))
    check(playerinputX, playerinputY)

def check(X, Y):
    if spielfeld[X][Y] != '         ':
        if spielfeld[X][Y] == spielfeld[X+1][Y]:
           # spielfeld[X+1][Y] = '         '
            checklist.append(X+1)
            checklist.append(Y)
            removed.append(X+1)
            removed.append(Y)
            print(checklist)
        if spielfeld[X][Y] == spielfeld[X][Y+1]:
          #  spielfeld[X][Y+1] = '         '
            checklist.append(X)
            checklist.append(Y+1)
            removed.append(X)
            removed.append(Y+1)
            print(checklist)
        if spielfeld[X][Y] == spielfeld[X][Y-1]:
           # spielfeld[X][Y-1] = '         '
            checklist.append(X)
            checklist.append(Y-1)
            removed.append(X)
            removed.append(Y-1)
            print(checklist)
        if spielfeld[X][Y] == spielfeld[X-1][Y]:
            #spielfeld[X-1][Y] = '         '
            checklist.append(X-1)
            checklist.append(Y)
            removed.append(X-1)
            removed.append(Y)
            print(checklist)
        #spielfeld[X][Y] = '         '
        removed.append(X)
        removed.append(Y)
        print(f'removed:{removed}')
        game()


game()