from random import*
line = ['+---------+---------+---------+---------+---------+']
middleline = ['|         |         |         |         |         |']
downline = ['|    ','16','   |    ','8','    |    ','4','    |    ','2','    |    ','2','    |']

spielfeld = [[zeilen * 5 + spalten for spalten in range(5)] for zeilen in range(5)]
random_numbers = [2**i for i in range(10)]
ZEILEN = ["+---+---+---+---+---+"]

def randomizen():
    for i in range(5):
        for j in range(5):
            spielfeld[i][j] = 2**(randint(2,5))

randomizen()

def pprint(mat2d):
    for k in range(25):
        print(k)

pprint(spielfeld)