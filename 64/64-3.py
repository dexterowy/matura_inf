plik = open('dane_obrazki.txt')
data = plik.read().splitlines()
obrazki = []
obrazek = []
i = 0
while i < len(data):
    if len(data[i]) != 0:
        obrazek.append(data[i])
    if len(data[i]) == 20:
        obrazki.append(obrazek)
        obrazek = []
    i+=1

poprawne = 0
naprawialne = 0
nienaprawialne = 0
max_bledow = 0
napraw = []
for k in range(200):
    col = 0
    row = 0
    sum = 0
    obraz = obrazki[k]
    for i in range(20):
        x = obraz[i][:-1].count('1')%2
        y = int(obraz[i][-1])
        if x != y:
            row += 1
        sum = 0
        for j in range(20):
            sum += int(obraz[j][i])
        if sum%2 != int(obraz[-1][i]):
            col += 1





    if col > 1 or row > 1:
        nienaprawialne += 1
    elif col == 1 or row == 1:
        naprawialne += 1
        napraw.append(k)
    elif col == 0 and row == 0:
        poprawne += 1
    if  col + row > max_bledow:
        max_bledow = col + row

print('obrazki poprawne:',poprawne)
print('obrazki naprawialne:',naprawialne)
print('obrazki nienaprawialne:',nienaprawialne)
print('najwieksza ilosc bledow w obrazku:',max_bledow)
