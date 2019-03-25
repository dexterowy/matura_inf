plik = open('funkcja.txt')
data = plik.read().splitlines()
for i, line in enumerate(data):
    data[i] = line.split()
    data[i] = [float(x) for x in data[i]]
def fi(x, arr):
    return arr[0]+x*arr[1]+arr[2]*x**2+arr[3]*x**3

def f(x):
    if x >= 0 and x < 1:
        return fi(x, data[0])
    if x >= 1 and x < 2:
        return fi(x, data[1])
    if x >= 2 and x < 3:
        return fi(x, data[2])
    if x >= 3 and x < 4:
        return fi(x, data[3])
    if x >= 4 and x < 5:
        return fi(x, data[4])

#zad 1
print(round(f(1.5), 5))

#zad 2
i = 0
maxf = 0
maxx = 0
while i<5:
    if maxf < f(i):
        maxf = f(i)
        maxx = i
    i += 0.0001
print(round(maxf, 5), round(maxx, 3))

#zad 3
i = 0
x0 = []
while i<5:
    if round(f(i), 5) == 0:
        x0.append(str(round(i, 5)))
    i += 0.000001

print(sorted(set(x0)))