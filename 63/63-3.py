plik = open('ciagi.txt')
data = plik.read().splitlines()

halfprime = []
for ciag in data:
    liczba = int(ciag ,2)
    y = liczba
    czynniki = []
    i = 2
    while i <= y**0.5+1:
        if(y%i == 0):
            czynniki.append(i)
            y //= i
        else:
            i += 1
    if(y > 1):
        czynniki.append(y)
    if len(czynniki) == 2:
        halfprime.append(liczba)

print('ilosc:', len(halfprime))
print('minimalna:', min(halfprime))
print('maksymalna:', max(halfprime))