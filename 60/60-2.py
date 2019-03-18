import math
plik = open('liczby.txt')
# data = plik.read().splitlines()
data = [999037]
liczby = []
for line in data:
    x = int(line)
    dzielniki = []
    for i in range(1,math.ceil(x**0.5)):
        if(x%i == 0):
            dzielniki.append(i)
            dzielniki.append(x//i)
    # if(len(dzielniki) == 18):
    #     dzielniki.sort()
    #
    print(x, dzielniki)