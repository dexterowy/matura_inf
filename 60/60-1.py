plik = open('liczby.txt')
data = plik.read().splitlines()
counter = 0
for line in data:
    x = int(line)
    if x < 1000:
        counter += 1
        print(x)
print(counter)