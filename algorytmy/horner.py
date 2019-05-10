def wielomian(x):
    return(2*x**2+3*x-5)

print(wielomian(3))

tab = [2,3,-5]
def horner(x,n,t):
    if n == 0:
        return t[0]
    return x * horner(x, n-1, t) + t[n]

print(horner(3,2,tab))


binary = [1,0,1,0,0,1,1,0]
print(horner(2, len(binary)-1, binary))