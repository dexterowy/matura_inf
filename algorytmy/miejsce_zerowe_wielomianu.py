def wielomian(x):
    return(2*x**2+3*x-5)


def miejsce_zerowe(p, q, E):
    i = 0
    l = p
    r = q
    s = (r + l) / 2
    while abs(wielomian((l+r)/2)) >= E and wielomian(l) != 0 and wielomian(r) != 0:
        s = (r + l) / 2
        if wielomian(l)*wielomian(s) < 0:
            r = s
        else:
            l = s
        i += 1
    if wielomian(r) == 0:
        print(r)
        return
    if wielomian(l) == 0:
        print(l)
        return
    print(s)

miejsce_zerowe(-1,2, 0.001)