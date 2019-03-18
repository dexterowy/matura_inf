def szukaj(plik, base):
    file = open(plik)
    data = file.readlines()
    for i, line in enumerate(data):
        data[i] = line.rstrip().split(' ')
    #print(data)
    tempMin = int(data[0][1], base)
    for line in data:
        if tempMin > int(line[1], base):
            tempMin = int(line[1], base)
    print(plik ,'{0:08b}'.format(tempMin), tempMin)


szukaj('dane_systemy1.txt', 2)
szukaj('dane_systemy2.txt', 4)
szukaj('dane_systemy3.txt', 8)