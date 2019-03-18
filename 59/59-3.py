plik = open('liczby.txt')
data = plik.read().splitlines()
#data = ['678', '1991']
counter = 0
tab = [[],[],[],[],[],[],[],[],[]]
for number in data:
    x = number
    i = 0
    while int(x) > 9:
        i += 1
        w = 1
        for digit in x:
            w*=int(digit)
        x = str(w)
        # print(x, i)
    tab[i].append(int(number))
    if(i >= 1 and i <= 8):
        counter+=1

# print(counter)
# print(tab)
for i, t in enumerate(tab):
    print(i,len(t))
print("min", min(tab[1]))
print("max", max(tab[1]))

