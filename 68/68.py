plik = open('dane_napisy.txt')
data = plik.read().splitlines()
for i, line in enumerate(data):
    data[i] = line.split(' ')

#zad 1
print('zad 1')
counter = 0
for row in data:
    equal = True
    if len(row[0]) == len(row[1]):
        c = row[0][0]
        if row[0].count(c) == len(row[0]) and row[1].count(c) == len(row[1]):
            counter += 1
print(counter)

#zad 2
print('zad 2')
counter = 0
for i, row in enumerate(data):
    equal = True
    if len(row[0]) == len(row[1]):
        for i in range(len(row[0])):
            c = row[0][i]
            if row[0].count(c) != row[1].count(c):
                equal = False
    else:
        equal = False
    if equal:
        counter += 1
print(counter)

#zad 3
print('zad 3')
maxk = 0
wyrazy = []
for row in data:
    wyrazy.append(row[0])
    wyrazy.append(row[1])
for i in range(len(wyrazy)):
    k = 0
    wyraz = wyrazy[i]
    for j in range(len(wyrazy)):
        test = wyrazy[j]
        equal = True
        if len(wyraz) == len(test):
            for i in range(len(wyraz)):
                c = wyraz[i]
                if wyraz.count(c) != test.count(c):
                    equal = False
        else:
            equal = False
        if equal:
            k += 1
    if k > maxk:
        maxk = k

print(maxk)