### Erste Versuche das Game zu Coden, aus diesem Code wurde neu das Dokument game.py geschrieben

from random import*

def numtrip():
    v = 16          #0¦, 1gap, 2v, 3gap, 4|, 5gap, 6w, 7gap, 8|
    w = 2**(randint(1,4))
    x = 2**(randint(1,4))
    y = 2**(randint(1,4))
    z = 2**(randint(1,4))

    line = ['+---------+---------+---------+---------+---------+']
    middleline = ['|         |         |         |         |         |']
    downline = ['|','    ',v,'    ','|','    ',w,'    ','|','    ',x,'    ','|','    ',y,'    ','|','    ',z,'    ','|']
    for i in range(5):
        print(line[0])
        print(middleline[0])                            
        for k in range(len(downline)):
            if k < 150:
                print(downline[k], end="")
                v = 16
                w = 2**(randint(1,3))
                x = 2**(randint(1,3))
                y = 2**(randint(1,3))
                z = 2**(randint(1,3))
                downline = ['|','    ',v,'    ','|','    ',w,'    ','|','    ',x,'    ','|','    ',y,'    ','|','    ',z,'    ','|']
            elif k > 15:
                print('too large')
        print("")
        print(middleline[0])
    print(line[0])

def again():
    playagain = input("Play again? (y/n)")
    if playagain == 'y':
        numtrip()
    while playagain != 'n':
        again()
again()