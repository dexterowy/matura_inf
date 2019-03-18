plik = open('dane_ulamki.txt')
data = plik.read().splitlines()
for i, line in enumerate(data):
    data[i] = data[i].split(' ')
    data[i][0] = int(data[i][0])
    data[i][1] = int(data[i][1])

mini = data[0]
for ulamek in data:
    if mini[0]/mini[1] > ulamek[0]/ulamek[1]:
        mini = ulamek
    elif mini[0]/mini[1] == ulamek[0]/ulamek[1]:
        if mini[1] > ulamek[1]:
            mini = ulamek
print(mini)