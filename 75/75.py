file = open('tekst.txt')
data = file.read().strip().split()

letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

def szyfruj(word, a, b):
    crypted = ''
    for char in word:
        crypted += letters[(letters.index(char)*a+b)%26]
    return crypted



#zad 1
print('zad 1')
for word in data:
    if word[0] == 'd' and word[-1] =='d':
        print(word)

#zad 2
print('zad 2')
for word in data:
    if len(word) >= 10:
        print(szyfruj(word, 5, 2))

#zad 3
print('zad 3')
file2 = open('probka.txt')
data = file2.read().splitlines()
for i, line in enumerate(data):
    data[i] = line.split()

for line in data:
    szyfrujacy = []
    deszyfrujacy = []
    for a in range(0, 26):
        for b in range(0,26):
            if szyfruj(line[0],a,b) == line[1]:
                szyfrujacy = [a,b]
            if szyfruj(line[1],a,b) == line[0]:
                deszyfrujacy = [a,b]
    print(szyfrujacy, deszyfrujacy)