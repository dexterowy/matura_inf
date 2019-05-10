tab = [7,2,4,5,0,9,15,24,-2,1]

def wstawianie(d):
    l = 0
    p = d - 1
    while l < p:
        i = l
        min = l
        while i <= p:
            if tab[min] > tab[i]:
                min = i
            i += 1
        t = tab[l]
        tab[l] = tab[min]
        tab[min] = t
        l += 1
    print(tab)

wstawianie(len(tab))