plik = open('dane_geny.txt')
data = plik.read().splitlines()
osobniki = []
for line in data:
    start = 0
    end = 0
    geny_osobnika = []
    for i in range(len(line)-1):
        if line[i] == 'A' and line[i+1] == 'A' and start == 0:
            start = i
        if start != 0 and line[i] == 'B' and line[i+1] == 'B':
            end = i+2
            geny_osobnika.append(line[start:end])
            start = 0
            end = 0
    osobniki.append(geny_osobnika)
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
mutated = 0
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
    i =0
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
    start = 0
    end = 0
    geny_osobnika = []
    geny_osobnika_rev = []
    for i in range(len(line)-1):
        if line[i] == 'A' and line[i+1] == 'A' and start == 0:
            start = i
        if start != 0 and line[i] == 'B' and line[i+1] == 'B':
            end = i+2
            geny_osobnika.append(line[start:end])
            start = 0
            end = 0
    line_rev = line[::-1]
    start = 0
    end = 0
    for i in range(len(line)-1):
        if line_rev[i] == 'A' and line_rev[i+1] == 'A' and start == 0:
            start = i
        if start != 0 and line_rev[i] == 'B' and line_rev[i+1] == 'B':
            end = i+2
            geny_osobnika_rev.append(line_rev[start:end])
            start = 0
            end = 0
    a = ''.join(geny_osobnika_rev)
    b = ''.join(geny_osobnika)

    if a == b and len(a) > 0:
        odporne += 1
print('odporne genotypy:',odporne)