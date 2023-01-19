from random import*
spielfeld = [[],[],[],[],[]]
goal = 128
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
    if loose() == False:
        print('You Lost.')
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
    wert = spielfeld[playerinputY][playerinputX]
    if spielfeld[playerinputY][playerinputX+1] == spielfeld[playerinputY][playerinputX] or spielfeld[playerinputY][playerinputX-1] == spielfeld[playerinputY][playerinputX] or spielfeld[playerinputY-1][playerinputX] == spielfeld[playerinputY][playerinputX] or spielfeld[playerinputY+1][playerinputX] == spielfeld[playerinputY][playerinputX]:
        checkandremove(playerinputY, playerinputX, spielfeld[playerinputY][playerinputX], 0)       
        spielfeld[playerinputY][playerinputX] = wert*2
    else:
        print('no Neighbour fields')
    movedown()
    while win() is not True:
        gameloop()
    if win() == True:
        printfield()
        print(f'You Won. You scored {goal} Points in one Field')
        pass

def checkandremove(y, x, oldvalue, newvalue):
    if x < 0 or x > 4 or y < 0 or y > 4:
        return
    if spielfeld[y][x] != oldvalue:
        return
    spielfeld[y][x] = newvalue
    checkandremove(y,x+1,oldvalue,newvalue)
    checkandremove(y,x-1,oldvalue,newvalue)
    checkandremove(y+1,x,oldvalue,newvalue)
    checkandremove(y-1,x,oldvalue,newvalue)
    return

def validateneighbour(x,y):
    pass

def movedown():
    for zeile in range(4,-1,-1):
        for spalte in range(4,-1,-1):
            if spielfeld[zeile][spalte] == 0:
                if spielfeld[0][spalte] == 0:
                    spielfeld[zeile][spalte] = 2**(randint(1,4))
                elif spielfeld[zeile-1][spalte] == 0:
                    spielfeld[zeile][spalte] = 2**(randint(1,4))
                else:
                    spielfeld[zeile][spalte] = spielfeld[zeile -1][spalte]
                    spielfeld[zeile-1][spalte] = 0

def loose():
    for zeile in range(5):
        for spalte in range(5):
            if spielfeld[zeile][spalte] == spielfeld[zeile +1][spalte]:
                return True
            elif spielfeld[zeile][spalte] == spielfeld[zeile -1][spalte]:
                return True
            elif spielfeld[zeile][spalte] == spielfeld[zeile +1][spalte-1]:
                return True
            elif spielfeld[zeile][spalte] == spielfeld[zeile][spalte+1]:
                return True
            else:
                return False

def win():
    for zeile in range(5):
        if goal in spielfeld[zeile]:
            return True
            
    

generatefield()
gameloop()