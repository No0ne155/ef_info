'''
Probe EF 2022
Programm 2-EMAIL.PY
'''
# üben mit z.b. Telefonnummern
# liste mit messwerten z.b. 5.6, -56, 4

verteiler = '''
caesonia.reich@gmail.com;

tulugaq.guidi@gmx.ch;

adisa23.palmisano@hispeed.ch;
chinwendu.maclean96@bluewin.ch;

foteini.faron@outlook.com;
'''

mitglieder = []

zeilen = verteiler.split()
print(zeilen)
for email in zeilen:
    name = email.split('@')[0]
    name = name.split('.')
    vorname = name[0]
    nachname = name[1]
    for zahl in '0123456789':
        vorname = vorname.replace(zahl, '')
        nachname = nachname.replace(zahl, '')
    mitglieder.append([vorname.capitalize(), nachname.capitalize()])




print(mitglieder)




def extract():
    i = 0
    while verteiler[i] != '.':
        i = i+1
        letter = verteiler[i]
        mitglieder.append(letter)
    print(mitglieder)

            
# Ziel:
# mitglieder = [                 .
#     ['Caesonia', 'Reich'],     .
#     ['Tulugaq', 'Guidi'],      .
#     ['Adisa', 'Palmisano'],    .
#     ['Chinwendu', 'MacLean'],  .
#     ['Foteini', 'Faron']       .
# ]                              .



