primzahlen = [2,3,5,7]
x = 0
y = 0
for i in range(4, 10):
    for j in range(len(primzahlen)):
        x = i % primzahlen[j]
        if x == 0:
            print('notprimenumber')
        else:
            primzahlen.append(i)
print(primzahlen)
print("done")