plik = open('dane_obrazki.txt')
data = plik.read().splitlines()
obrazki = []
obrazek = []
rekurencyjne = []
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
    rekurencyjny = True
    if len(obraz) != len(obraz[0]) or len(obraz)%2 != 0 or len(obraz[0])%2 != 0:
        continue
    #print(obraz)
    d = len(obraz)//2
    for i in range(d):
        for j in range(d):
            if obraz[i][j] != obraz[i+d][j] or obraz[i][j] != obraz[i][j+d] or obraz[i][j] != obraz[i+d][j+d]:
                rekurencyjny = False
    if rekurencyjny:
        rekurencyjne.append(obraz)

print('ilosc rekurencyjnych obrazkow:', len(rekurencyjne))
for row in rekurencyjne[0]:
    print(row)
