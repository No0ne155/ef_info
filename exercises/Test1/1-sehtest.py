'''
Probe EF 2022
Programm 1-SEHTEST.PY
'''


def c(size, orientation):
    if orientation == 'r':
        print('* *' + ' *'* size + ' * *')
        print('* *' + ' *'* size + ' * *')
        for i in range(size):
            print('* *')
        print('* *' + ' *'* size + ' * *')
        print('* *' + ' *'* size + ' * *')
    if orientation == 'l':
        print('* *' + ' *'* size + ' * *')
        print('* *' + ' *'* size + ' * *')
        for i in range(size):
            print(' '*((size*2)+4) +'* *')
        print('* *' + ' *'* size + ' * *')
        print('* *' + ' *'* size + ' * *')
    playerinput()


def playerinput():
    plinput = input('Enter Your input HERE => ')
    if len(plinput) ==2:
        try:
            plinputnr = int(plinput[0])
        except:
            print('1st sign was not numeric')
            playerinput()
        plinputlt = plinput[-1]
        if plinputlt.isalpha() == True:
            c(plinputnr, plinputlt)
        else:
            print('2nd sign was not Alphabetic')
            playerinput()
    else:
        print('Wrong length')
        print('Try Again')
        playerinput()

print(f'Please enter your size and orientation in the Format "[number][l/L/r/R]".')
playerinput()