def pierwiastek(n, p, i):
    a = 1
    b = n
    j = 0
    while j < i and abs(a-n/a) > p:
        print(a, abs(a-n/a))
        b = (a+b)/2
        a = n/b
        j += 1
    print(a)





pierwiastek(25, 0.0000000001, 7)