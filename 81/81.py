wierzcholki = [x.split() for x in open('wspolrzedne.txt').read().splitlines()]
for i, line in enumerate(wierzcholki):
    wierzcholki[i] = [int(x) for x in line]

trojkaty = [x.split() for x in open('wspolrzedneTR.txt').read().splitlines()]
for i, line in enumerate(trojkaty):
    trojkaty[i] = [int(x) for x in line]



#zad 1
print('zad 1')
pierwsza = 0
for line in wierzcholki:
    if line[0] > 0 and line[1] > 0 and line[2] > 0 and line[3] > 0 and line[4] > 0 and line[5] > 0:
        pierwsza += 1
print(pierwsza)

#zad 2
print('\nzad 2')


liniowe = 0
for line in wierzcholki:
    ab = [line[2]-line[0], line[3]-line[1]]
    ac = [line[4]-line[0], line[5]-line[1]]
    if (ab[1] == 0 and ac[1] == 0) or (ab[0] == 0 and ac[0] == 0):
        liniowe += 1
    elif ab[0] != 0 and ac[0] != 0 and  ab[1]/ab[0] == ac[1]/ac[0]:
        liniowe += 1

print(liniowe)

#zad 3
print('\nzad 3')
#print(trojkaty)


def dist(xa,ya,xb,yb):
    return ((xa-xb)**2 + (ya-yb)**2)**0.5

wsp = []
max_obw = 0
for line in trojkaty:
    ab = dist(line[0],line[1],line[2],line[3])
    ac = dist(line[0],line[1],line[4],line[5])
    bc = dist(line[2],line[3],line[4],line[5])
    if ab + ac > bc and ab + bc > ac and bc + ac > ab:
        obw = ab + ac + bc
        if obw > max_obw:
            max_obw = obw
            wsp = line
print(wsp)
print(round(max_obw,2))

#zad 4
print('\nzad 4')



prostokatne = 0
for line in trojkaty:
    ab = (line[2]-line[0])**2 + (line[3] - line[1])**2
    ac = (line[4]-line[0])**2 + (line[5] - line[1])**2
    bc = (line[4]-line[2])**2 + (line[5] - line[3])**2
    x = sorted([ab,ac,bc])
    if x[0] + x[1] == x[2]:
        prostokatne +=1
print(prostokatne)

#zad 5
print('\nzad 5')
for line in trojkaty:
    A = [line[0], line[1]]
    B = [line[2], line[3]]
    C = [line[4], line[5]]
    ba = [A[0]-B[0], A[1]-B[1]]
    bc = [C[0]-B[0], C[1]-B[1]]
    bd = [ba[0]+bc[0],ba[1]+bc[1]]
    D = [B[0]+bd[0],B[1]+bd[1]]
    if D[0] == D[1]:
        print('A=('+str(A[0])+','+str(A[1])+') B=('+str(B[0])+','+str(B[1])+') C=('+str(C[0])+','+str(C[1])+') D=('+str(D[0])+','+str(D[1])+')')