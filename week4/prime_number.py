import math


def IsPrime(n):
    k = 2
    mind = n
    while k <= math.sqrt(n):
        if n / k == n // k:
            mind = k
            break
        else:
            k += 1
    return mind == n


n = int(input())
if IsPrime(n):
    print('Yes')
else:
    print('No')
