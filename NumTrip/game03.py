from random import*
spielfeld = [[],[],[],[],[]]

def printfield():
    global spielfeld
    spielfeldnice = [[],[],[],[],[]]
    print('\X    0         1         2         3         4   ')
    print('Y+---------+---------+---------+---------+---------+')
    for i in range(5):
        for j in range(5):
            if spielfeld[i][j] < 10:
                spielfeldnice[i].append(f"    {spielfeld[i][j]}    ")
            elif spielfeld[i][j] < 100:
                spielfeldnice[i].append(f"   {spielfeld[i][j]}    ")
    for k in range(5):
        print(' |         |         |         |         |         |')
        print(f"{k}|{spielfeldnice[k][0]}|{spielfeldnice[k][1]}|{spielfeldnice[k][2]}|{spielfeldnice[k][3]}|{spielfeldnice[k][4]}|")
        print(' |         |         |         |         |         |')
        print(' +---------+---------+---------+---------+---------+')

def generatefield():
    for l in range(5):
        for m in range(5):
            randomnumber = 2**(randint(1,4))
            spielfeld[l].append(randomnumber)

def playerinputcheck(inp):
    if not inp.isnumeric():
        print('Is not Numeric')
        return False
    inp = int(inp)
    if 0 <= inp and inp <= 4:
        return True
    print('Number out of range')
    return False

def gameloop():
    printfield()
    playerinputX = input('X-Axis you want to choose: ')
    while not playerinputcheck(playerinputX):
        playerinputX = input('X-Axis you want to choose: ')
        playerinputcheck(playerinputX)
    playerinputX = int(playerinputX)
    playerinputY = input('Y-Axis you want to choose: ')
    while not playerinputcheck(playerinputY):
        playerinputY = input('Y-Axis you want to choose: ')
        playerinputcheck(playerinputY)
    playerinputY = int(playerinputY)

    checkandremove(playerinputY, playerinputX, spielfeld[playerinputY][playerinputX], 0)
    gameloop()

def checkandremove(y, x, oldvalue, newvalue):
    spielfeld[y][x] = newvalue
    print('should be removed')
    if x < 0 or x >= 4 or y < 0 or y >= 4:
        return
    if spielfeld[y][x] != oldvalue:
        return
    checkandremove(y,x+1,oldvalue,newvalue)
    checkandremove(y,x-1,oldvalue,newvalue)
    checkandremove(y+1,x,oldvalue,newvalue)
    checkandremove(y-1,x,oldvalue,newvalue)
    return

generatefield()
gameloop()
