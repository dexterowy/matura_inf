plik = open('ciagi.txt')
data = plik.read().splitlines()
ciagi = []

for i, line in enumerate(data):
    if(i%2 == 1):
        ciagi.append(line.split(' '))

print(ciagi)
max_szescian = []
for ciag in ciagi:
    max_local = 0
    for liczba in ciag:
        x = int(liczba)**(1/3)
        if x%1 == 0.0 and max_local < int(liczba):
            max_local = int(liczba)
    if(max_local != 0):
        max_szescian.append(max_local)

print(max_szescian)
