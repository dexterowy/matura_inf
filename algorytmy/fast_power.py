def power(a,n):
    wynik = 1
    while n>0:
        if n%2 == 1:
          wynik *= a
        a = a**2
        n= n//2
    print(wynik)


def rek_power(a,n):
    if n == 0:
        return 1
    if n % 2 == 1:
        return a * rek_power(a, n-1)
    w =  rek_power(a, n/2)
    return w * w


power(2,3)
print(rek_power(2,3))