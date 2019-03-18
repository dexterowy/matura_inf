#zad 1
print('zad 1')
x = 1
fib = [1,1]
for i in range(2,40):
    fib.append(fib[i-2] + fib[i-1])

print('F10',fib[9])
print('F20',fib[19])
print('F30',fib[29])
print('F40',fib[39])

#zad 2
print('zad 2')
def isPrime(x):
    i = 2
    if x >= 2:
        while i < x:
            if x%i == 0:
                return False
            i += 1
        return True
    else:
        return False
for number in fib:
    if isPrime(number):
        print(number)

#zad 3
print('zad 3')
for number in fib:
    print(format(number,'0b'))
#zad 4
print('zad 4')
for x in fib:
    number = str(bin(x)[2:])
    if number.count('1') == 6:
        print(number)