import math
okregi = open('okregi.txt').read().splitlines()
for i, x in enumerate(okregi):
    tmp = []
    for o in x.split():
        tmp.append(float(o))
    okregi[i] = tmp
#print(okregi)


#zad 1
print('zad 1')
pierwsza = druga = trzecia = czwarta = pozostale = 0
for o in okregi:
    if o[0] - o[2] > 0 and o[1] - o[2] > 0 and o[0] > 0 and o[1] > 0:
        pierwsza += 1
    elif o[0] + o[2] < 0 and o[1] - o[2] > 0 and o[0] < 0 and o[1] > 0:
        druga += 1
    elif o[0] + o[2] < 0 and o[1] + o[2] < 0 and o[0] < 0 and o[1] < 0:
        trzecia += 1
    elif o[0] - o[2] > 0 and o[1] + o[2] < 0 and o[0] > 0 and o[1] < 0:
        czwarta += 1
    else:
        pozostale += 1
print('pierwsza:', pierwsza)
print('druga:', druga)
print('trzecia:', trzecia)
print('czwarta:', czwarta)
print('nie zawierajacych sie w calosci w zadnej cwiartce:', pozostale)

#zad 2
print('\nzad 2')
pary = []
for i in range(len(okregi)):
    for j in range(i, len(okregi)):
        if ((okregi[i][0] == -okregi[j][0] and okregi[i][1] == okregi[j][1]) or (okregi[i][1] == -okregi[j][1] and okregi[i][0] == okregi[j][0])) and okregi[i][2] == okregi[j][2] :
            pary.append(sorted([okregi[i], okregi[j]]))
print('ilosc par lustrzanych',len(pary))

#zad 3
print('\nzad 3')
prostopadle = []
for i in range(len(okregi)):
    for j in range(i, len(okregi)):
        if (okregi[i][0] == -okregi[j][1] or okregi[i][1] == -okregi[j][0]) and okregi[i][2] == okregi[j][2]:
            prostopadle.append([okregi[i],okregi[j]])
print('ilosc par prostopadlych:', len(prostopadle))

#zad 4
print('\nzad 4')
def isChain(a,b):
    #print(a,b)
    d = ((a[0]-b[0])**2 + (a[1] - b[1])**2)**0.5
    if (a[2] + b[2]) >= d and a[2] + d >= b[2] and b[2] + d >= a[2]:
        return True
    else:
        return False

chains = []
counter = 1
for i in range(1000):
    if isChain(okregi[i], okregi[i+1]):
        counter += 1
    else:
        chains.append(counter)
        counter = 1
wynik = ''
for x in chains:
    wynik += str(x) + ', '
print(wynik)
print(max(chains))