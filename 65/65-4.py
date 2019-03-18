plik = open('dane_ulamki.txt')
data = plik.read().splitlines()
for i, line in enumerate(data):
    data[i] = data[i].split(' ')
    data[i][0] = int(data[i][0])
    data[i][1] = int(data[i][1])


b = 2**2*3**2*5**2*7**2*13

suma = 0
for ulamek in data:
    suma += (ulamek[0]*b)//ulamek[1]
print(suma)