def czy_pierwsza(n):
    if n < 2:
        return False
    i = 2
    while i*i <= n:
        if n%i == 0:
            return False
        i += 1
    return True

x = 19

if czy_pierwsza(x):
    print("Pierwsza")
else:
    print("Nie jest pierwsza")