# Variablen
gesucht = 'test'   #

gefunden = []
falsch_geraten = []

#show() zeigt alle richtig und falsch geratenen Buchstaben an

def show():
    print('Falsche Buchstaben:', falsch_geraten)
    for buchstabe in gesucht:
        if buchstabe in gefunden:
            print(buchstabe, end=' ')
        else:
            print('_', end=' ')
    print('')

#eingabe() erfordert eine Eingabe des Spielers

def eingabe():
    buchstabe = input('Buchstabe? ')
    while not is_valid(buchstabe):
        buchstabe = input('Buchstabe? ')
    return buchstabe.lower()

#gewonnen() Wenn alle Buchstaben gefunden wurden, hat man gewonnen

def gewonnen():
    for buchstabe in gesucht:
        if buchstabe not in gefunden:
            return False
        return True

#is_valid(inp) überprüft ob eingabe erlaubt ist

def is_valid(inp):
    return inp

#auswerten() überprüft ob der Input im wort ist, und fügt den Input in die Entsprechende Liste an

def auswerten(valid_inp):
    if valid_inp in gesucht:
        gefunden.append(valid_inp)
    else:
        falsch_geraten.append(valid_inp)

def game_over():
    if len(falsch_geraten) > 10:
        print('YOU LOST')
        return True
    else:
        return False
        play()

def play():
    while not game_over():
        wort = eingabe()
        auswerten(wort)
        show()

play()