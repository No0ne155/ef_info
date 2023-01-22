from random import*
#spielfeld = [[16,16,4,8,16],[2,4,8,16,1],[4,8,16,1,2],[8,16,1,2,4],[16,1,2,4,8]]
spielfeld = [[],[],[],[],[]]
goal = 128 #setzt den zielwert
def printfield(): #Funktion die das Spielfeld mit den Aktuellen werten der Spielfeld-Liste ausgibt
    global spielfeld
    spielfeldnice = [[],[],[],[],[]]
    print('\033[94m'+f'∖'+'\033[0m'+'\033[96m'+'X    0         1         2         3         4   '+'\033[0m')
    print('\033[96m'+f'Y'+'\033[0m'+'\033[94m'+f'+---------+---------+---------+---------+---------+'+'\033[0m')
    for i in range(5): #wiederholt für jede zeile
        for j in range(5): #wiederholt für jede spalte
            if spielfeld[i][j] < 10: #überprüft die länge, und fügt entsprechend Leerzeichen an.⇱◢◤∖
                spielfeldnice[i].append(f"    {spielfeld[i][j]}    ")
            elif spielfeld[i][j] < 100:
                spielfeldnice[i].append(f"   {spielfeld[i][j]}    ")
            elif spielfeld[i][j] < 1000:
                spielfeldnice[i].append(f'   {spielfeld[i][j]}   ')
    for k in range(5): #gibt das schöne feld aus
        print('\033[94m'+f' |         |         |         |         |         |'+'\033[0m')
        print('\033[96m'+f'{k}'+'\033[0m'+'\033[94m'+f'|'+'\033[0m'+f'{spielfeldnice[k][0]}'+'\033[94m'+f'|'+'\033[0m'+f'{spielfeldnice[k][1]}'+'\033[94m'+f'|'+'\033[0m'+f'{spielfeldnice[k][2]}'+'\033[94m'+f'|'+'\033[0m'+f'{spielfeldnice[k][3]}'+'\033[94m'+f'|'+'\033[0m'+f'{spielfeldnice[k][4]}'+'\033[94m'+f'|'+'\033[0m')
        print('\033[94m'+f' |         |         |         |         |         |'+'\033[0m')
        print('\033[94m'+f' +---------+---------+---------+---------+---------+'+'\033[0m')

def generatefield(): #füllt das Spielfeld mit Zufallszahlen
    for l in range(5):
        for m in range(5):
            randomnumber = 2**(randint(1,4))
            spielfeld[l].append(randomnumber)

def playerinputcheck(inp): #überprüft ob der Spielerinput Valide ist
    if not inp.isnumeric(): #Zahl?
        print('Is not an Integer')
        return False
    inp = int(inp)
    if 0 <= inp and inp <= 4: #im bereich der Liste?
        return True
    print('Number out of range')
    return False

def gameloop(): #die Main Game Funktion
    if loose() == False: #überprüft ob verloren
        print('You Lost.')
        printfield()
        print('\033[91m'+'YOU LOST!!' +'\033[0m')
        quit()
    printfield() #gibt Spielfeld aus
    playerinputX = input('X-Axis you want to choose: ') #fragt nach Playerinputs bis valide
    while not playerinputcheck(playerinputX):
        playerinputX = input('X-Axis you want to choose: ')
    playerinputX = int(playerinputX)
    playerinputY = input('Y-Axis you want to choose: ')
    while not playerinputcheck(playerinputY):
        playerinputY = input('Y-Axis you want to choose: ')
    playerinputY = int(playerinputY)
    wert = spielfeld[playerinputY][playerinputX]
    if validateneighbour(playerinputX, playerinputY) == True: #überprüft ob ein nachbar vorhanden ist
        checkandremove(playerinputY, playerinputX, spielfeld[playerinputY][playerinputX], 0)       
        spielfeld[playerinputY][playerinputX] = wert*2 #verdoppelt den Wert des ausgewählten Feldes
    elif validateneighbour(playerinputX, playerinputY) == False: #wenn kein nachbar dann:
        print('no Neighbour fields')
        gameloop()
    movedown()#bewegt alles nach unten
    while win() is not True: #solange nicht gewonnen, wird der Gameloop wiederholt
        gameloop()
    if win() == True: #wenn gewonnen dann wird das Feld noch einmal ausgegeben
        printfield()
        print('\033[96m '+f'You Won. You scored {goal} Points in one Field'+'\033[0m') #und eine Gewinnernachricht ausgegeben
        quit() #beendet das Programm sofort

def checkandremove(y, x, oldvalue, newvalue): #überprüft nachbaren, und setzt diese zu 0
    if x < 0 or x > 4 or y < 0 or y > 4: #überprüft ob die Zahl im rahmen ist
        return
    if spielfeld[y][x] != oldvalue: # überprüft ob die zahl den gleichen wert hat
        return
    spielfeld[y][x] = newvalue #setzt die Zahl zu 0
    checkandremove(y,x+1,oldvalue,newvalue) #wiederholt den gleichen loop für alle gleichen rundherum
    checkandremove(y,x-1,oldvalue,newvalue)
    checkandremove(y+1,x,oldvalue,newvalue)
    checkandremove(y-1,x,oldvalue,newvalue)
    return

def validateneighbour(y,x): #überprüft ob ein Nachbar vorhanden ist.
    if x >= 1: #überprüft, dass x-1 nicht aus der Liste ist
        if spielfeld[x-1][y] == spielfeld[x][y]: #wenn nachbar in x-1 richtung vorhanden return
            return True                          #gleiches für alle richtungen.
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

def movedown(): #ersetzt alle Nullen durch die zahl obendran, und das Feld obendran zu 0
    for zeile in range(4,-1,-1):
        for spalte in range(4,-1,-1):
            if spielfeld[zeile][spalte] == 0:
                if spielfeld[0][spalte] == 0:
                    spielfeld[zeile][spalte] = 2**(randint(1,4))
                elif spielfeld[zeile-1][spalte] == 0: # in der obersten Zeile werden neue Zahlen generiert
                    spielfeld[zeile][spalte] = 2**(randint(1,4))
                else:
                    spielfeld[zeile][spalte] = spielfeld[zeile -1][spalte]
                    spielfeld[zeile-1][spalte] = 0

def loose(): #überprüft ob noch eine Kombination spielbar ist
    falsecounter = 0
    for zeile in range(5):
        for spalte in range(5): #überprüft jedes feld
            if validateneighbour(zeile, spalte) == False: #falls das feld keinen nachbar hat
                falsecounter = falsecounter +1            #wird der counter um 1 erhöht
    if falsecounter == 25: #wenn alle 25 felder keinen nachbar haben gibt es False zurück
        return False       #was das Spiel beendet.
    return True

def win(): #überprüft alle Zeilen ob der Zielwert vorhanden ist
    for zeile in range(5):
        if goal in spielfeld[zeile]:
            return True #gibt True zurück, was das Spiel beendet.
            
generatefield() #generiert ein Feld
gameloop() #startet den Gameloop
#colorcode : https://gist.github.com/Prakasaka/219fe5695beeb4d6311583e79933a009
#'\033[x;xxm'+ 'text'+'\033[0m'