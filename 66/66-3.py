plik = open('trojki.txt')
data = plik.read().splitlines()
for i, line in enumerate(data):
    data[i] = line.split(' ')

data = [[int(j) for j in i] for i in data]

for i in range(len(data)-1):
    data[i] = sorted(data[i])
    data[i+1] = sorted(data[i+1])
    if ((data[i][0]**2 + data[i][1]**2) == data[i][2]**2
    and (data[i+1][0]**2 + data[i+1][1]**2) == data[i+1][2]**2):
        print(data[i])
        print(data[i+1])
        print('\n')