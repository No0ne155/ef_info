from random import*
spielfeld = [[],[],[],[],[]]
spielfeldnice = [[],[],[],[],[]]
checklist = []
removed = []
playerinputs = []
def printfieldstart():
    global spielfeld
    global spielfeldnice
    print('\Y    0         1         2         3         4   ')
    print('X+---------+---------+---------+---------+---------+')
    for i in range(5):
        for j in range(5):
            randomnumber = 2**(randint(1,4))
            spielfeld[i].append(randomnumber)
            if randomnumber < 10:
                spielfeldnice[i].append(f"    {randomnumber}    ")
            elif randomnumber < 100:
                spielfeldnice[i].append(f"   {randomnumber}    ")
    for k in range(5):
        print(' |         |         |         |         |         |')
        print(f"{k}|{spielfeldnice[k][0]}|{spielfeldnice[k][1]}|{spielfeldnice[k][2]}|{spielfeldnice[k][3]}|{spielfeldnice[k][4]}|")
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

def checkandremove(x, y, oldvalue, newvalue):
    if x < 0 or x >= 4 or y < 0 or y >= 4:
        return
    if spielfeld[y][x] != oldvalue:
        return
    spielfeld[y][x] = newvalue
    checkandremove(x,y+1,oldvalue,newvalue)
    checkandremove(x,y-1,oldvalue,newvalue)
    checkandremove(x+1,y,oldvalue,newvalue)
    checkandremove(x-1,y,oldvalue,newvalue)
    return

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

game()