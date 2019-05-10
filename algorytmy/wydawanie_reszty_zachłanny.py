monety = [50000, 20000, 10000, 5000, 2000, 1000, 500, 200, 100, 50, 20, 10, 5, 2, 1]
ilosc = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

def reszta(n):
    i = 0
    x = n*100
    while x > 0:
        ilosc[i] =  x//monety[i]
        x = x - ilosc[i]*monety[i]
        i += 1

    for j, x in enumerate(ilosc):
        print(int(ilosc[j]), "razy po:", monety[j]/100,'zl')

reszta(174.37)