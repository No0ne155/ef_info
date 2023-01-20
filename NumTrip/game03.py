from random import*
#spielfeld = [[16,16,4,8,16],[2,4,8,16,1],[4,8,16,1,2],[8,16,1,2,4],[16,1,2,4,8]]
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
            elif spielfeld[i][j] < 1000:
                spielfeldnice[i].append(f'   {spielfeld[i][j]}   ')
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
        print('Is not an Integer')
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
        print('YOU LOST!!!!!!')
        quit()
    printfield()
    playerinputX = input('X-Axis you want to choose: ')
    while not playerinputcheck(playerinputX):
        playerinputX = input('X-Axis you want to choose: ')
    playerinputX = int(playerinputX)
    playerinputY = input('Y-Axis you want to choose: ')
    while not playerinputcheck(playerinputY):
        playerinputY = input('Y-Axis you want to choose: ')
    playerinputY = int(playerinputY)
    wert = spielfeld[playerinputY][playerinputX]
    if validateneighbour(playerinputX, playerinputY) == True:
        checkandremove(playerinputY, playerinputX, spielfeld[playerinputY][playerinputX], 0)       
        spielfeld[playerinputY][playerinputX] = wert*2
    elif validateneighbour(playerinputX, playerinputY) == False:
        print('no Neighbour fields')
        gameloop()
    movedown()
    while win() is not True:
        gameloop()
    if win() == True:
        printfield()
        print(f'You Won. You scored {goal} Points in one Field')
        quit()

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

def validateneighbour(y,x):
    if x >= 1:
        if spielfeld[x-1][y] == spielfeld[x][y]:
            return True
    if x <= 3:
        if spielfeld[x+1][y] == spielfeld[x][y]:
            return True
    if y >= 1:
        if spielfeld[x][y-1] == spielfeld[x][y]:
            return True
    if y <= 3:
        if spielfeld[x][y+1] == spielfeld[x][y]:
            return True
    return False

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
    falsecounter = 0
    for zeile in range(5):
        for spalte in range(5):
            if validateneighbour(zeile, spalte) == False:
                falsecounter = falsecounter +1
    if falsecounter == 25:
        return False
    return True
    '''
    if spielfeld[zeile][spalte] == spielfeld[zeile +1][spalte]:
        return True
    elif spielfeld[zeile][spalte] == spielfeld[zeile -1][spalte]:
        return True
    elif spielfeld[zeile][spalte] == spielfeld[zeile +1][spalte-1]:
        return True
    elif spielfeld[zeile][spalte] == spielfeld[zeile][spalte+1]:
        return True
    return False'''

def win():
    for zeile in range(5):
        if goal in spielfeld[zeile]:
            return True
            
generatefield()
gameloop()