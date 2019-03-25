def splitgenes(gens):
    results = []
    start = 0
    end = 0
    begining = True
    for i in range(len(gens) - 1):
        if gens[i] == 'A' and gens[i + 1] == 'A' and begining:
            start = i
            begining = False
        if not begining  and gens[i] == 'B' and gens[i + 1] == 'B':
            end = i + 2
            results.append(gens[start:end])
            begining = True
    return results


plik = open('dane_geny.txt')
data = plik.read().splitlines()

gatunek_max = 0
gatunki = []
gatunki_all = []
for genotyp in data:
    if not(len(genotyp) in gatunki):
        gatunki.append(len(genotyp))
    gatunki_all.append(len(genotyp))
for g in gatunki:
    count = gatunki_all.count(g)
    if count > gatunek_max:
        gatunek_max = count

print('zad 1')
print('liczba gatunkow:', len(gatunki))
print('najwieksza liczba osobnikow z tego samego gatunku:', gatunek_max)


print('zad 2')
osobniki = []
mutated = 0

for line in data:
    osobniki.append(splitgenes(line))

for osobnik in osobniki:
    mutate = False
    for gen in osobnik:
        if 'BCDDC' in gen:
            mutate = True
    if mutate:
        mutated += 1

print('ilosc osobnikow z mutacją:',mutated)

print('zad 3')
gens_osobnik_max = 0
longest_gen = 0
for osobnik in osobniki:
    if len(osobnik) > gens_osobnik_max:
        gens_osobnik_max = len(osobnik)
    for gen in osobnik:
        if len(gen) > longest_gen:
            longest_gen = len(gen)
print('najwieksza ilosc genow u jednego osobnika:', gens_osobnik_max)
print('najwieksza dlugosc genu:', longest_gen)

print('zad 4')
strong = 0
for genotyp in data:
    j = len(genotyp)-1
    i = 0
    palindrom = True
    while i <= j:
        if genotyp[i] != genotyp[j]:
            palindrom = False
            break
        i += 1
        j -= 1
    if palindrom:
        strong += 1
print('silnie odporne genotypy:',strong)
odporne = 0
for line in data:

    #print('Line: ', line)
    #print('Rev: ', line[::-1])
    geny_osobnika = splitgenes(line)
    geny_osobnika_rev = splitgenes(line[::-1])

    if sorted(geny_osobnika) == sorted(geny_osobnika_rev):
        #print('A: ', geny_osobnika)
        #print('B: ', geny_osobnika_rev)
        odporne += 1
print('odporne genotypy:', odporne)
