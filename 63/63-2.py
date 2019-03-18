plik = open('ciagi.txt')
data = plik.read().splitlines()
ile = 0
for ciag in data:
    powtarza = False
    for i in range(len(ciag)-1):
        if ciag[i] == '1' and ciag[i+1] == '1':
            powtarza = True
    if not(powtarza):
        ile += 1
print(ile)