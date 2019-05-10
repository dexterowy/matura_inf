tab = [7,2,4,5,0,9,15,24,2,1]
count = [0] * (max(tab)+1)
s = []
i = 0
while i < len(tab):
    count[tab[i]] += 1
    i += 1
print(tab)
i = 0
while i < len(count):
    j = count[i]
    while j > 0:
        s.append(i)
        j -= 1
    i += 1
print(s)