data = open('dane_wybory.txt').read().splitlines()
for i,line in enumerate(data):
    data[i] = line.split()
    for j, x in enumerate(data[i]):
        if x.isdecimal():
            data[i][j] = int(x)
print(data)
wynik = open('86.4.txt', 'w')
ilosc_mandatow = 20
max_mandatow = [0,0,0,0,0]
for okrag in data:
    przyznane_mandaty = [0, 0, 0, 0, 0]
    for i in range(0, ilosc_mandatow):
        wk = [0,0,0,0,0]
        for komitet in range(0,5):
            wk[komitet] = okrag[komitet+1]/(2*przyznane_mandaty[komitet]+1)
        for j,x in enumerate(wk):
            if(wk[j] == max(wk)):
                przyznane_mandaty[j] += 1
    line = ''
    for x in przyznane_mandaty:
        line += '\t' + str(x) + '\t'
    wynik.write(okrag[0]+'\t'+line + '\n')
    for j, x in enumerate(przyznane_mandaty):
        if (przyznane_mandaty[j] > max_mandatow[j]):
            max_mandatow[j] = przyznane_mandaty[j]
print(max_mandatow)


#zad 4
data2 = open('86.4.2.txt').read().splitlines()
for i,line in enumerate(data2):
    data2[i] = line.split()
    for j, x in enumerate(data2[i]):
        if x.isdecimal():
            data2[i][j] = int(x)
ilosc_mandatow = 100
max_mandatow = [0,0,0,0,0]
regionalne = [['A',0,0,0,0,0],['B',0,0,0,0,0],['C',0,0,0,0,0],['D',0,0,0,0,0]]
for i, line in enumerate(data2):
    for x in range(1,6):
        regionalne[i%4][x] += line[x]
print(regionalne)
for okrag in data2:
    przyznane_mandaty = [0, 0, 0, 0, 0]
    for i in range(0, ilosc_mandatow):
        wk = [0,0,0,0,0]
        for komitet in range(0,5):
            wk[komitet] = okrag[komitet+1]/(2*przyznane_mandaty[komitet]+1)
        for j,x in enumerate(wk):
            if(wk[j] == max(wk)):
                przyznane_mandaty[j] += 1
    line = ''
    for x in przyznane_mandaty:
        line += '\t' + str(x) + '\t'
    wynik.write(okrag[0]+'\t'+line + '\n')

#zad 5
def zad5(ilosc_mandatow2):
    im = 2*ilosc_mandatow2
    ig = 100000
    przyznane_mandaty2 = [0, 0]
    q = 0
    while przyznane_mandaty2[0] != im/2:
        q += 1
        r = ig - q
        okrag2 = [q,r]
        przyznane_mandaty2 = [0, 0]
        for i in range(0, im):
            wk = [0,0]
            for komitet in range(0, 2):
                wk[komitet] = okrag2[komitet] / (2 * przyznane_mandaty2[komitet] + 1)
            for j, x in enumerate(wk):
                if (wk[j] == max(wk)):
                    przyznane_mandaty2[j] += 1
                    break
        #print(q,r,przyznane_mandaty2,wk)
    print(okrag2)
    # line = ''
    # for x in przyznane_mandaty:
    #     line += '\t' + str(x) + '\t'
    # wynik.write(okrag[0]+'\t'+line + '\n')
zad5(10)
zad5(20)
zad5(50)