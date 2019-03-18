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

naprawialne = []
xy =[]
for k in range(200):
    col = 0
    row = 0
    row_index = -1
    col_index = -1
    obraz = obrazki[k]
    for i in range(20):
        x = obraz[i][:-1].count('1')%2
        y = int(obraz[i][-1])
        if x != y:
            row += 1
            row_index = i
        suma = 0
        for j in range(20):
            suma += int(obraz[j][i])
        if suma%2 != int(obraz[-1][i]):
            col += 1
            col_index = i
    if col == 1 and row == 1:
        print('obrazek:',k+1, ', wiersz:',row_index+1, ', kolumna:',col_index+1)
    if col == 1 and row == 0:
        print('obrazek:',k+1, ', wiersz:',21, ', kolumna:',col_index+1)
    if col == 0 and row == 1:
        print('obrazek:',k+1, ', wiersz:',row_index+1,', kolumna:', 21)