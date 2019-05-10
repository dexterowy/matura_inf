def nwd(a,b):
    while b != 0:
        p = b
        b = a%p
        a = p

    return a

x = nwd(24,4455)
print(x)