from random import*
spielfeld = [[], [], [], [], []]
def game():
    print('     01        02        03        04        05   ')
    print(' +---------+---------+---------+---------+---------+')
    for i in range(5):
        for j in range(5):
            randomnumber = 2**(randint(1,4))
            if randomnumber < 10:
                spielfeld[i].append(f"    {randomnumber}    ")
            elif randomnumber < 100:
                spielfeld[i].append(f"   {randomnumber}    ")
    for k in range(5):
        print(' |         |         |         |         |         |')
        print(f"{k}|{spielfeld[k][0]}|{spielfeld[k][1]}|{spielfeld[k][2]}|{spielfeld[k][3]}|{spielfeld[k][4]}|")
        print(' |         |         |         |         |         |')
        print(' +---------+---------+---------+---------+---------+')

game()