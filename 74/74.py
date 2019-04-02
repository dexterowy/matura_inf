file = open('hasla.txt')
data = file.read().splitlines()

#zad 1
print('zad 1')
count = 0
for password in data:
    if password.isdigit():
        count += 1
print(count)

#zad 2
print('zad 2')
doubled = []
for password in data:
    if data.count(password) > 1:
        if not(password in doubled):
            doubled.append(password)
for password in sorted(doubled):
    print(password)

#zad 3
print('zad 3')
counter = 0
for password in data:
    if len(password) >= 4:
        for i in range(0, len(password) - 3):
            subword = password[i:i + 4]
            x = []
            for j in subword:
                x.append(ord(j))
            x = sorted(x)
            if x[0] + 1 == x[1] and x[0] + 2 == x[2] and x[0] + 3 == x[3]:
                #print(x, password)
                counter += 1
                break
print(counter)

#zad 4
print('zad 4')
counter = 0
for password in data:
    digit = False
    upper = False
    lower = False
    for char in password:
        if char.isdigit():
            digit = True
        if char.islower():
            lower=True
        if char.isupper():
            upper=True
    if lower and upper and digit:
        counter += 1

print(counter)

