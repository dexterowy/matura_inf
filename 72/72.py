#134
#462

file = open('napisy.txt')
data = file.read().splitlines()
for i, line in enumerate(data):
    data[i] = line.split(' ')

#zad 1
print('zad 1')
first = []
count = 0
for line in data:
    if len(line[0]) >= 3*len(line[1]) or len(line[1]) >= 3*len(line[0]):
        count += 1
        if len(first) == 0:
            first = line

print('pierwsza para:',first[0], first[1])
print('ilosc takich par:', count)

#zad 2
print('zad 2')
count = 0
for line in data:
    if len(line[0]) < len(line[1]):
        base = line[1][0:len(line[0])]
        #print(line[0], line[1],base)
        if line[0] == base:
            count += 1
            print(line[0],line[1], line[1][len(line[0]):])

#zad 3
print('zad 3')
max_end = 0
max_end_words = []
for line in data:
    if line[0][-1] == line[1][-1]:
        if len(line[0]) < len(line[1]):
            i = len(line[0])
        else:
            i = len(line[1])
        tmp_max = 0
        j = 1
        while j <= i:
            if line[0][-j] == line[1][-j]:
                tmp_max += 1
            else:
                break
            j += 1
        if tmp_max > max_end:
            max_end = tmp_max
            max_end_words = []
            max_end_words.append(line)
        elif tmp_max == max_end:
            max_end_words.append(line)
print('maksymalna dlugosc zakonczenia:', max_end)
for word in max_end_words:
    print(word[0], word[1])
#print(data)

