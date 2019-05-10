def W(x):
    return(2*x**2-3*x-1)

def pole(p,q,n):
    i = 0
    s = 0
    krok = (q-p)/n
    while i < n:
        x = p+i*krok
        s += abs(W((x+x+krok)/2))
        i += 1
    return s*krok

def pole2(p,q,n):
    i = 0
    s = 0
    krok = (q-p)/n
    while i < n:
        s += abs(W(p+i*krok+krok/2))
        i += 1
    return s*krok

print(pole(2,4,1000))
print(pole2(2,4,1000))