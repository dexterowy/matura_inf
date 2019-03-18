plik = open('bledne.txt')
data = plik.read().splitlines()
ciagi = []

for i, line in enumerate(data):
    if(i%2 == 1):
        ciagi.append(line.split(' '))
bledne = []
for ciag in ciagi:
    tab_r = []
    for i in range(0,len(ciag)-1):
        tab_r.append(int(ciag[i+1])-int(ciag[i]))
    #print(tab_r)
    if tab_r[0] != tab_r[1] and tab_r[1] == tab_r[2]:
        bledne.append(ciag[0])
        continue
    if tab_r[0] != tab_r[2] and tab_r[1] !=tab_r[2] and tab_r[2] == tab_r[3]:
        bledne.append(ciag[1])
        continue
    for i in range(len(tab_r)):
        if tab_r[i] != tab_r[0]:
            bledne.append(ciag[i+1])
            break

print(bledne)
wynik = open('wynik3.txt', 'w')
for liczba in bledne:
    wynik.write(liczba+'\n')
