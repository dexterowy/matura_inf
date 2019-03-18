plik = open('liczby2.txt')
data = plik.read().splitlines()



ile = 0
osemkowy = 0

for x in data:
    for cyfra in x:
        if cyfra == '6':
            ile += 1
    y = oct(int(x))[2:]
    for cyfra in y:
        if cyfra == '6':
            osemkowy += 1
print('ilosc cyfr 6 jako dziesietna:',ile)
print('ilosc cyfr 6 jako osemkowa:',osemkowy)