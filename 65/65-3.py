plik = open('dane_ulamki.txt')
data = plik.read().splitlines()
for i, line in enumerate(data):
    data[i] = data[i].split(' ')
    data[i][0] = int(data[i][0])
    data[i][1] = int(data[i][1])

suma = 0
for ulamek in data:
    licznik = ulamek[0]
    mianownik = ulamek[1]
    i = 2

    while i <= licznik and i <= mianownik:
        if licznik%i == 0 and mianownik%i == 0:
            licznik //= i
            mianownik //= i
        else:
            i+=1
    suma += licznik

print(suma)