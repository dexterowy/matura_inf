import math
def isPrime(x):
    if(x < 2):
        return False
    for i in range(2, math.ceil(x**1/2)):
        if x%i == 0:
            return False
    return True

plik = open('liczby.txt')

data = plik.read().splitlines()
#data = [32,210,1331,1157625,105,429,1287,3465,255255]
counter = 0
for number in data:
    x = int(number)
    primes = []
    i = 2
    while i*i <= x:
        if(x%i == 0):
            if(not(i in primes)):
                primes.append(i)
            x //= i
        else:
            i += 1
    if(x > 1 and not(x in primes)):
        primes.append(x)
    even = False
    for digit in primes:
        if(digit%2 == 0):
            even = True
            break
    if(len(primes) == 3 and not even):
        counter += 1
    print(number,primes)

print(counter)

