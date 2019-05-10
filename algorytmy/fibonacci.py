def fib(n):
    i = 0
    a = b = 1
    while i < n:
        print(a)
        b += a
        a = b - a
        i += 1


fib(5)

# nie wydajne rozwiazanie rekurencyjne!
# def rfib(n):
#     if n < 3:
#         return 1
#     return rfib(n-1)+rfib(n-2)
#
# def n_rfib(n):
#     for i in range(1,n+1):
#         print(rfib(i))
#
