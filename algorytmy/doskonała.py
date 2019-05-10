def doskonala(n):
    suma = 1
    p = n**0.5
    i = 2
    while i <= p:
        if n % i == 0:
            suma += i
            suma += n/i
        i += 1
    if p*p == n:
        suma -= p
    if suma == n :
        return True
    else:
        return False

for x in range(500000):
    if doskonala(x):
        print(x)