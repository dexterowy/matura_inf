file = open('tekst.txt')
data = file.read().strip().split(' ')
#print(data)

#zad 1
print('zad 1')
count = 0
for word in data:
    if len(word) >= 2:
        for i in range(0, len(word) - 1):
            if word[i] == word[i+1]:
                count += 1
                break
print('wyrazy z podwojona litera:', count)

#zad 2
print('zad 2')

merged = ''.join(data)
letters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','W','X','Y','Z']
for letter in letters:
    count = merged.count(letter)
    print(letter+':', count, '('+str(round((count/len(merged))*100, 2))+ '%)')

#zad 3
print('zad 3')
samogloski = ['A','E','I','O','U','Y']
max_subword = 0
subwords = []
for word in data:
    tmp_max = 0
    for letter in word:
        if not( letter in samogloski):
            tmp_max += 1
        else:
            if max_subword <  tmp_max:
                max_subword = tmp_max
                subwords = []
                subwords.append(word)
            elif max_subword == tmp_max:
                subwords.append(word)
            tmp_max = 0
print('najwieksza dlugosc podslowa:',max_subword)
print('ilosc wyrazow z najwieksza dlugoscia podslowa:', len(subwords))
print('pierwsze slowo z najwieksza dlugoscia podslowa:',subwords[0])
