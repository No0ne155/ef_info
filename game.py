from random import*
playcounter = 0
playagain = input("Play? (y/n)")
def numtrip():
    v = 2**(randint(1,4))          #randomized die werte für die Tabele
    w = 2**(randint(1,4))
    x = 2**(randint(1,4))
    y = 2**(randint(1,4))
    z = 2**(randint(1,4))
    line = ['+---------+---------+---------+---------+---------+']          #design der Tabelle
    middleline = ['|         |         |         |         |         |']    #design der Tabelle
    for i in range(5):
        downline = ['|    ',v,'    ','|    ',w,'    ','|    ',x,'    ','|    ',y,'    ','|    ',z,'    ','|']
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
        print(downline[3], end="")
        print(downline[4], end="")
        if downline[4] < 13:
            downline[5] = '    '
            print(downline[5], end="")
        elif downline[4] > 14:
            downline[5] = '   '
            print(downline[5], end="")
        print(downline[6], end="")
        print(downline[7], end="")
        if downline[7] < 13:
            downline[8] = '    '
            print(downline[8], end="")
        elif downline[7] > 14:
            downline[8] = '   '
            print(downline[8], end="")
        print(downline[9], end="")
        print(downline[10], end="")
        if downline[10] < 13:
            downline[11] = '    '
            print(downline[11], end="")
        elif downline[10] > 14:
            downline[11] = '   '
            print(downline[11], end="")
        print(downline[12], end="")
        print(downline[13], end="")
        if downline[13] < 13:
            downline[14] = '    '
            print(downline[14], end="")
        elif downline[13] > 14:
            downline[14] = '   '
            print(downline[14], end="")
        print(downline[15])
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
    numtrip()
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