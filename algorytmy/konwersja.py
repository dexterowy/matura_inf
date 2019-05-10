def zamiana(n ,p):
    if n > 0:
        zamiana(n//p,p)
        if n%p > 9:
            x = n%p
            if x == 10:
                print("A", end='')
            if x == 11:
                print("B", end='')
            if x == 12:
                print("C", end='')
            if x == 13:
                print("D", end='')
            if x == 14:
                print("E", end='')
            if x == 15:
                print("F", end='')
        print(n%p, end='')

zamiana(254, 2)