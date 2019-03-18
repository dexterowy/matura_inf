def rekordy(plik, base):
    file = open(plik)
    data = file.readlines()
    for i, line in enumerate(data):
        data[i] = line.rstrip().split(' ')
    #print(data)
    rekordDays = [1]
    rekord = int(data[0][1], base)
    for i, line in enumerate(data):
        if i != 1:
            if rekord < int(line[1], base):
                rekord = int(line[1], base)
                rekordDays.append(1)
            else:
                rekordDays.append(0)
    return rekordDays


counter = 0
r1 = rekordy('dane_systemy1.txt', 2)
r2 = rekordy('dane_systemy2.txt', 4)
r3 = rekordy('dane_systemy3.txt', 8)

for i in range(0, len(r1)-1):
    if( r1[i] or r2[i] or r3[i]):
        counter += 1

print(counter)