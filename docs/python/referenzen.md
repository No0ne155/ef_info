# Listen 2D Referenzen
Die Listen sind eigentlich die selben, jedoch mit anderem Namen. So verändert sich beim ändern der einen Liste auch die andere.
```
matrix = []

zeile = [0, 1, 0]
for i in range(3):
    matrix.append(zeile)

print(matrix)

matrix[1][1] = 0 # setzt Wert in Zeile 1 in der Mitte auf 0 Setzen

print(matrix)
```
