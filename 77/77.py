import math

letters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
data = open('dokad.txt').read().strip()

def szyfruj(input, key):
    cripted = list(input)
    pointer = 0
    for i, char in enumerate(input):
        if char != ' ' and char != ',' and char != '.':
            cripted[i] = letters[(letters.index(char) + letters.index(key[pointer%len(key)]))%len(letters)]
            pointer += 1
    return [''.join(cripted), math.ceil(pointer/len(key))]

def deszyfruj(input, key):
    cripted = list(input)
    pointer = 0
    for i, char in enumerate(input):
        if char != ' ' and char != ',' and char != '.':
            cripted[i] = letters[(letters.index(char) - letters.index(key[pointer%len(key)]))%len(letters)]
            pointer += 1
    return [''.join(cripted), math.ceil(pointer/len(key))]


#zad 1
print('zad 1')
print(szyfruj(data, 'LUBIMYCZYTAC')[1])
print(szyfruj(data, 'LUBIMYCZYTAC')[0])

#zad 2
print('zad 2')
data = open('szyfr.txt').read().splitlines()
print(deszyfruj(data[0],data[1])[0])

#zad 3
print('zad 3')
stats = []

for char in letters:
    stats.append(data[0].count(char))
    print(char+':', data[0].count(char))

k = 0
for l in stats:
    k += l*(l-1)
k/=sum(stats)*(sum(stats)-1)
d = 0.0285/(k-0.0385)

print('d =',round(d, 2))
print('dlugosc klucza w pliku:', len(data[1]))
