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
        print(f"{k}|{spielfeld[i][0]}|{spielfeld[i][1]}|{spielfeld[i][2]}|{spielfeld[i][3]}|{spielfeld[i][4]}|")
        print(' |         |         |         |         |         |')
        print(' +---------+---------+---------+---------+---------+')

game()