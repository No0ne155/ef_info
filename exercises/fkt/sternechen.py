from time import*
from random import*
def main(width, height):
    line(width)
    gap(height, width)
    line(width)
def line(width):
    print('*' * width)
def gap(height, width):
    for i in range(height -2):    
        print('*', ' ' * (width -4),'*')
for i in range(10):
    main(randint(5, 150),randint(5, 20))
    sleep(1)