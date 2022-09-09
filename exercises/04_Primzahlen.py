primzahlen = [2,3,5,7]
x = 1
for i in range(2, 100):
    if i % 2 == 0 or i %3 == 0 or i % 5 == 0 or i % 7 == 0:
        x = x +1
    else:
        primzahlen.append(i)
print(primzahlen)
