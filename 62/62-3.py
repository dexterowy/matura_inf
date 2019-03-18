plik1 = open('liczby1.txt')
plik2 = open('liczby2.txt')

dziesietne = plik2.read().splitlines()
osemkowe = plik1.read().splitlines()

rowne = 0
wieksza = 0
for i, x in enumerate(dziesietne):
    if int(dziesietne[i]) == int(osemkowe[i], 8):
        rowne += 1
    if int(dziesietne[i]) < int(osemkowe[i], 8):
        wieksza += 1

print('a)', rowne)
print('b)', wieksza)