plik = open('dane_obrazki.txt')
data = plik.read().splitlines()
obrazki = []
obrazek = []
rewersy = []
i = 0
while i < len(data)-1:
    if data[i+1] != '':
        obrazek.append(data[i][:-1])
        i+=1
    else:
        obrazki.append(obrazek)
        obrazek = []
        i+=2
obrazki.append(obrazek)

for obraz in obrazki:
    czarne = 0
    biale = 0
    for row in obraz:
        czarne += row.count('1')
        biale += row.count('0')
    if czarne > biale:
        rewersy.append(czarne)


print('ile rewersow:', len(rewersy))
print('najwiecej czarnych pikseli:', max(rewersy))