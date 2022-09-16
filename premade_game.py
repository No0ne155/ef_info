from random import*
def numtrip():
    v = 2**(randint(1,3))
    w = 2**(randint(1,3))
    x = 2**(randint(1,3))
    y = 2**(randint(1,3))
    z = 2**(randint(1,3))

    line = ['+---------+---------+---------+---------+---------+']
    middleline = ['|         |         |         |         |         |']
    downline = ['|    ',x,'    |    ',y,'    |    ',z,'    |    ',w,'    |    ',v,'    |']
    for i in range(5):
        print(line[0])
        print(middleline[0])    
        for k in range(len(downline)):
            print(downline[k], end="")
            v = 2**(randint(1,3))
            w = 2**(randint(1,3))
            x = 2**(randint(1,3))
            y = 2**(randint(1,3))
            z = 2**(randint(1,3))
            downline = ['|    ',x,'    |    ',y,'    |    ',z,'    |    ',w,'    |    ',v,'    |']
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