plik = open('ciagi.txt')
data = plik.read().splitlines()
ciagi = []

for i, line in enumerate(data):
    if(i%2 == 1):
        ciagi.append(line.split(' '))

roznice = []
for i, ciag in enumerate(ciagi):
    arytmetyczny = True
    r = int(ciag[1]) - int(ciag[0])
    for j in range(0, len(ciag)-1):
        if(int(ciag[j+1]) - int(ciag[j]) != r):
            arytmetyczny = False
            break
    if arytmetyczny:
        roznice.append([i, r])

print('ile',len(roznice))
print(roznice)
maxr= [0, 0]
for x in roznice:
    if(int(x[1]) > maxr[1]):
        maxr[1] = int(x[1])
        maxr[0] = int(x[0])

print('max r',maxr[1])
print('ciag z max r', ciagi[maxr[0]])