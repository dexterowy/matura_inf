tab = [7,2,4,5,0,9,15,24,-2,1]

def wstawianie(l):
    i = 1
    p = 0
    while i < l:
        p = tab[i]
        j = i - 1
        while j >= 0 and tab[j] > p:
            tab[j+1] = tab[j]
            j -= 1
        tab[j+1] = p
        i += 1
    print(tab)

wstawianie(len(tab))