data = open('szyfr1.txt').read().splitlines()

def szyfruj(word, key):
    crypted = list(word)
    for i in range(len(word)):
        tmp = crypted[i]
        crypted[i] = crypted[key[i%len(key)]-1]
        crypted[key[i%len(key)]-1] = tmp
    return ''.join(crypted)

#zad 1
print('zad 1')
p = data[-1].split()
for i in range(len(p)):
    p[i] = int(p[i])
words = data[0:-1]
#print(p)
for word in words:
    print(szyfruj(word, p))

#zad 2
print('zad 2')
data = open('szyfr2.txt').read().splitlines()
p = data[-1].split()
for i in range(len(p)):
    p[i] = int(p[i])
word = data[0]
print(szyfruj(word, p))

#zad 3
print('zad 3')
data = open('szyfr3.txt').read()
crypted = list(data)
key=[6,2,4,1,5,3]
for i in range(len(data)-1, -1, -1):
    tmp = crypted[i]
    crypted[i] = crypted[key[i % len(key)] - 1]
    crypted[key[i % len(key)] - 1] = tmp
print(''.join(crypted))