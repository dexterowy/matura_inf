plik = open('liczby2.txt')
data = plik.read().splitlines()
for i,x in enumerate(data):
    data[i] = int(x)

max_ciag = [0,0]
for i, x in enumerate(data):
    j = i
    dlugosc = 1

    while j+1 < len(data):
        if data[j] < data[j+1]:
            dlugosc += 1
            j += 1
        else:
            break
    if(max_ciag[1] < dlugosc):
        max_ciag = [i, dlugosc]

print('pierwszy element: ',data[max_ciag[0]])
print('dlugosc: ', max_ciag[1])