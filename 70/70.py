import math

def f(x):
    return (x**4/500.000)-(x**2/200.000)-(3/250.000)
def g(x):
    return -(x**3/30.000)+(x/20.000)+(1/6.000)

n = 0.00001 #szer. prostokąta miarowego
lewo = 2 #lewa krawędź figury
gora = f(10) #górna krawędź figury
dol = g(10) # dolna krawędź figury
p1 = 0 #pole górnego obszaru figury
p2 = 0 #pole dolnego obszaru figury

#zad 1
x = 2
while x <= 10:
    x += n
    p1 += n * (gora - f(x))
    p2 += n * (abs(dol) - abs(g(x)))

szer = 8
wys = abs(gora) + abs(dol)

p = wys * szer
print('Pozostała powierzchnia materiału: ', round(p - (p1+p2), 3))

#zad 2
n = 8/1000
kf = 0
kg = 0
x = 2
while x <= 10:
    fa = [x, f(x)]
    fb = [x+n, f(x+n)]
    ga = [x, g(x)]
    gb = [x+n, g(x+n)]
    kf += ( (fa[0]-fb[0])**2 + (fa[1]-fb[1])**2)**(1/2)
    kg += ( (ga[0]-gb[0])**2 + (ga[1]-gb[1])**2)**(1/2)
    x += n
obw = kf + kg + 2*szer + wys
print('Należy zakupić:',math.ceil(obw),'m taśmy')

#zad 3
n = 0.25
x = 10
dlugosc = 0
while x >= 0:
    x -= n
    dlugosc += math.floor(f(x) + abs(g(x)))

print('Długość pasów wyciętych z pozostałości materiału:',dlugosc,'m')
