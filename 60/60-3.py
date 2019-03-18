import math
plik = open('liczby.txt')
data = plik.read().splitlines()
liczby = []
#data = [369362, 786999,809,384264,107595,989532]
maxPrime = 0
for line in data:
    x = int(line)
    dzielniki = []
    for i in range(2,math.ceil(x**0.5)):
        if(x%i == 0):
            dzielniki.append(i)
            dzielniki.append(x//i)
    dzielniki.append(x)
    dzielniki.sort()
    liczby.append(dzielniki)

for i ,liczba in enumerate(liczby):
    podzielna = False
    for dzielnik in liczba:
        for j, x in enumerate(liczby):
            if i == j:
                break
            if dzielnik in x:
                podzielna = True
                break
        if podzielna:
            break
        if maxPrime < liczba[-1]:
            maxPrime = liczba[-1]

print(maxPrime)