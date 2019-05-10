def hanoi(n, a, b, c):
    if n>0:
        hanoi(n-1,a,c,b)
        print(a,"na", b)
        hanoi(n-1,c,b,a)

hanoi(4,'a','b','c')