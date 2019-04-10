odcinki = [int(x) for x in open('dane_trojkaty.txt').read().splitlines()]
# ^^ odkrylem to po 40h napierdalania 4 petli zeby pracowac na danych :)

#zad 1
print('zad 1')
trojki = []
for i in range(len(odcinki)-3):
    x = odcinki[i:i+3]
    sx = sorted(x)
    if sx[0]**2 + sx[1]**2 == sx[2]**2:
        trojki.append(x)
for trojka in trojki:
    print(trojka[0], trojka[1], trojka[2])

#zad 2
print('\nzad 2')
max_obw = 0
counter = 0
for a in range(len(odcinki)-2):
    for b in range(a, len(odcinki)-1):
        for c in range(b, len(odcinki)):
            if odcinki[a]+odcinki[b] > odcinki[c] \
                    and odcinki[a]+odcinki[c] > odcinki[b] \
                    and odcinki[b]+odcinki[c] > odcinki[a] \
                    and odcinki[a] != odcinki[b]\
                    and odcinki[a] != odcinki[c]\
                    and odcinki[b] != odcinki[c]:
                obw = odcinki[a]+odcinki[b]+odcinki[c]
                counter += 1
                if obw > max_obw:
                    max_obw = obw
                obw = 0
print(max_obw)

#zad 3
print('\nzad 3')
print(counter)