#Script dass die anzahl augen beim Werfen von 2 Würfeln anzeigt. Wie oft geworfen wird, kann selbst entschieden werden
from random import *
often = 100000
zahl= [[],[],[],[],[],[],[],[],[],[],[]]
for i in range(often):
    x = (randint(1,6)+randint(1,6))
    zahl[x-2].append(x)
eins = 1
for i in range(11):
    nr = i
    anzahl = len(zahl[nr])
    percent = (anzahl / often)*100
    percent = round(percent, 2)
    print(f'{i+2}: ', anzahl, percent)

