plik = open('trojki.txt')
data = plik.read().splitlines()
for i, line in enumerate(data):
    data[i] = line.split(' ')

def isPrime(x):
    if x == 2:
        return True
    i = 2
    while i < x:
        if x%i == 0:
            return False
        i += 1
    return True

for line in data:
    if (isPrime(int(line[0])) and isPrime(int(line[1]))
        and int(line[2]) == int(line[0]) * int(line[1])):
        print(line)