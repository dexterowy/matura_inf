plik = open('liczby1.txt')
data = plik.read().splitlines()
min = data[0]
max = data[0]
for x in data:
    if int(min,8) > int(x,8):
        min = x
    if int(max, 8) < int(x, 8):
        max = x
print('min', min)
print('max', max)