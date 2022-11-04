from random import*
playcounter = 0
counter1 = 1
counter2 = 2
playagain = input("Play? (y/n)")
def numtrip():
    global counter1
    global counter2
    v = 2**(randint(1,4))          #randomized die werte für die Tabele
    w = 2**(randint(1,4))
    x = 2**(randint(1,4))
    y = 2**(randint(1,4))
    z = 2**(randint(1,4))
    line = ['+---------+---------+---------+---------+---------+']          #design der Tabelle
    middleline = ['|         |         |         |         |         |']    #design der Tabelle
    for i in range(5):
        downline = ['|    ',v,'    ',w,'    ',x,'    ',y,'    ',z,'    ','|']
        print(line[0])                  #spaghetticode für erkennung von länge jeder zahl, und anpassung von Leerzeichen
        print(middleline[0])            #wird noch verbessert
        print(downline[0], end="")
        print(downline[1], end="")
        if downline[1] < 13:
            downline[2] = '    '
            print(downline[2], end="")
        elif downline[1] > 14:
            downline[2] = '   '
            print(downline[2], end="")
        print(downline[0], end="")
        print(downline[3], end="")
        if downline[3] < 13:
            downline[4] = '    '
            print(downline[4], end="")
        elif downline[3] > 14:
            downline[4] = '   '
            print(downline[4], end="")
        print(downline[0], end="")
        print(downline[5], end="")
        if downline[5] < 13:
            downline[6] = '    '
            print(downline[6], end="")
        elif downline[5] > 14:
            downline[6] = '   '
            print(downline[6], end="")
        print(downline[0], end="")
        print(downline[7], end="")
        if downline[7] < 13:
            downline[8] = '    '
            print(downline[8], end="")
        elif downline[7] > 14:
            downline[8] = '   '
            print(downline[8], end="")
        print(downline[0], end="")
        print(downline[9], end="")
        if downline[9] < 13:
            downline[10] = '    '
            print(downline[10], end="")
        elif downline[9] > 14:
            downline[10] = '   '
            print(downline[10], end="")
        print(downline[11])
        print(middleline[0])
        v = 2**(randint(1,4))               #generiert neue werte für neue zeilen
        w = 2**(randint(1,4))
        x = 2**(randint(1,4))
        y = 2**(randint(1,4))
        z = 2**(randint(1,4))
    print(line[0])

def again():                                #fragt den Spieler ob er spielen (generieren) will
    global playagain                        #nach 1x spielen fragt er ob man erneut spielen will
    global playcounter
    if playagain == 'y':
        numtrip()
        playcounter = playcounter + 1
        if playcounter > 0:
            playagain = input("Play again (y/n)")
    while playagain != 'n':
        again()
        if playcounter > 0:
            playagain = input("Play again (y/n)")
again()