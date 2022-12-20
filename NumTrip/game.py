from random import*
spielfeld = [[], [], [], [], []]
checklist = []
removed = []
playerinputs = []
def printfieldstart():
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

def playerinputcheck(inp):
    if not inp.isnumeric():
        print('Is not Numeric')
        return False
    inp = int(inp)
    if 0 <= inp and inp <= 4:
        return True
    print('Number out of range')
    return False

def game():
    global spielfeld
    global playerinputX
    global playerinputY
    printfieldstart()
    playerinputX = input('X-Axis you want to choose: ')
    while not playerinputcheck(playerinputX):
        playerinputX = input('X-Axis you want to choose: ')
        playerinputcheck(playerinputX)
    playerinputX = int(playerinputX)
    playerinputY = input('Y-Axis you want to choose: ')
    while not playerinputcheck(playerinputY):
        playerinputY = input('X-Axis you want to choose: ')
        playerinputcheck(playerinputY)
    playerinputY = int(playerinputY)
    playerinputs.append(playerinputX)
    playerinputs.append(playerinputY)
    print(playerinputs)
    checkandremove(playerinputX, playerinputY, spielfeld[playerinputX][playerinputY], '         ')
    game()

def checkandremove(x, y, oldvalue, newvalue):
    if x < 0 or x >= len(spielfeld[0]) or y < 0 or y >= len(spielfeld):
        return
    if spielfeld[y][x] != oldvalue:
        return
    spielfeld[y][x] = newvalue
    checkandremove(x,y+1,oldvalue,newvalue)
    checkandremove(x,y-1,oldvalue,newvalue)
    checkandremove(x+1,y,oldvalue,newvalue)
    checkandremove(x-1,y,oldvalue,newvalue)
    return

def check(X, Y):
    if spielfeld[X][Y] != '         ':
        if spielfeld[X][Y] == spielfeld[X+1][Y]:
           # spielfeld[X+1][Y] = '         '
            checklist.append(X+1)
            checklist.append(Y)
            removed.append(X+1)
            removed.append(Y)
        if spielfeld[X][Y] == spielfeld[X][Y+1]:
          #  spielfeld[X][Y+1] = '         '
            checklist.append(X)
            checklist.append(Y+1)
            removed.append(X)
            removed.append(Y+1)
        if spielfeld[X][Y] == spielfeld[X][Y-1]:
           # spielfeld[X][Y-1] = '         '
            checklist.append(X)
            checklist.append(Y-1)
            removed.append(X)
            removed.append(Y-1)
        if spielfeld[X][Y] == spielfeld[X-1][Y]:
            #spielfeld[X-1][Y] = '         '
            checklist.append(X-1)
            checklist.append(Y)
            removed.append(X-1)
            removed.append(Y)
        spielfeld[X][Y] = '         '
        removed.append(X)
        removed.append(Y)
        print(checklist)
        #print(f'removed:{removed}')
        while len(checklist) > 0:
            checkandremove(checklist[0], checklist[1], spielfeld[X][Y], '         ')
            checklist.pop(1)
            checklist.pop(0)
            print(f'checklistt: {checklist}')
        game()
    if spielfeld[X][Y] == '         ':
        print("already chosen")
        game()
        

game()