from random import randint
gesucht = randint(0, 100)
runde = 1
geraten = ''

def to_int(geraten):
    try:
        return int(geraten)
    except:
        return -1

def is_valid(geraten):
    if geraten < 0 or geraten > 100:
        return -1
    
def abfrage(runde):
    global geraten
    geraten = -1
    while geraten < 0:
        geraten = input(f'{runde}. Versuch: Gib eine ganze Zahl zwischen 0 und 100 ein: ')
        geraten = to_int(geraten)
        is_valid(geraten)
    return geraten

def play(runde):
    while geraten != gesucht:
        abfrage(runde)
        runde = runde + 1
        if geraten > gesucht:
            print('Die eingegebene Zahl ist zu gross')
        elif geraten < gesucht:
            print('Die eingegebene Zahl ist zu klein')
    print(f'Bravo, du hast in {runde - 1} Runden die gesuchte Zahl {gesucht} gefunden.')

play(runde)
#a) Das Spiel lässt den Spieler eine zahl zwischen 1 und 100 raten. 
# Man muss eine eingabe zwischen 1 und 100 machen, diese wird Überprüft ob es eine Zahl ist.
# Sobald es eine Zahl ist, wird überprüft ob sie grösser oder kleiner als die gesuchte Zahl ist.
# Am ende wird angezeigt, wie oft man es versucht hat.