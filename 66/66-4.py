plik = open('trojki.txt')
data = plik.read().splitlines()
for i, line in enumerate(data):
    data[i] = line.split(' ')

data = [[int(j) for j in i] for i in data]

longest = 0
tmp_longest = 0
count = 0
for line in data:
    if (line[0]+line[1] > line[2]
    and line[0]+line[2] > line[1]
    and line[1]+line[2] > line[0]):
        tmp_longest +=1
        count += 1
        if tmp_longest > longest:
            longest = tmp_longest
    else:
        tmp_longest = 0

print('liczba trojkatow:', count)
print('najdluzszy ciag:', longest)