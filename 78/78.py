podpisy = open('podpisy.txt').read().splitlines()
wiadomosci = open('wiadomosci.txt').read().splitlines()

for i, podpis in enumerate(podpisy):
    podpisy[i] = podpis.split()
    for j,x in enumerate(podpisy[i]):
        podpisy[i][j] = int(x)

#print(podpisy)


def skrot(wiadomosc):
    klucz = 'ALGORYTM'
    s = []
    for i, char in enumerate(klucz):
        s.append(ord(char))
    #print(s)
    while len(wiadomosc) % 8 != 0:
        wiadomosc += '.'
    #print(wiadomosc)
    for j in range(len(wiadomosc)):
        s[j % 8] = (s[j % 8] + ord(wiadomosc[j])) % 128
    wynik = ''
    for char in s:
        wynik += chr( 65 + char % 26)
    return [wynik, len(wiadomosc), s]

def deszyfruj(d, n, podpis):
    p = podpis
    wynik = []
    for i, x in enumerate(podpis):
        wynik.append(chr(x * d % n))
    return ''.join(wynik)

#zad 1
print('zad 1')
wynik = skrot(wiadomosci[0])
print('a)', wynik[1])
tekst = ''
for x in wynik[2]:
    tekst += str(x) + ' '
print('b)', tekst)
print('c)', wynik[0])

#zad 2
print('\nzad 2')
for x in podpisy:
    print(deszyfruj(3, 200, x))

#zad 3
print('\nzad 3')
odpowiedzi = ''
for i in range(len(podpisy)):
    if skrot(wiadomosci[i])[0] == deszyfruj(3,200, podpisy[i]):
        odpowiedzi += str(i+1) + ' '
print(odpowiedzi)

