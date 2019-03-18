plik = open('ciagi.txt')
data = plik.read().splitlines()
for ciag in data:
    if len(ciag)%2 == 0:
        if ciag[:len(ciag)//2] == ciag[len(ciag)//2:]:
            print(ciag)
