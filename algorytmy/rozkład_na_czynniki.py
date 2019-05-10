# def czy_pierwsza(n):
#     i = 2
#     while i*i <= n:
#         if n % i == 0:
#             return False
#         i += 1
#     return True
#
# def rozklad(n):
#     i = 2
#     x = n
#     while x != 1:
#         if czy_pierwsza(i) and x % i == 0:
#             x = x/i
#             print(i, end=',')
#         else:
#             i += 1

def rozklad(n):
    k = 2
    while n > 1:
        while n % k == 0:
            print(k, end=',')
            n /= k
        k += 1

rozklad(24654)