plik = open('trojki.txt')
data = plik.read().splitlines()
for i, line in enumerate(data):
    data[i] = line.split(' ')

for line in data:
    suma = 0
    for cyfra in line[0]:
        suma += int(cyfra)
    for cyfra in line[1]:
        suma += int(cyfra)
    if suma == int(line[2]):
        print(line)
