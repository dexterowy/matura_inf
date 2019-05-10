tab = [7,2,4,3,0,1]

def bubble(l):
    d = l -1
    while d > 0:
        i = 0
        while i < d:
            if tab[i] > tab[i+1]:
                tmp = tab [i]
                tab[i] = tab[i+1]
                tab[i+1] = tmp
            i += 1
        d -= 1
    print(tab)

bubble(len(tab))