import math


def MinDivisor(n):
    k = 2
    mind = n
    while k <= math.sqrt(n):
        if n / k == n // k:
            mind = k
            break
        else:
            k += 1
    return mind


n = int(input())
print(MinDivisor(n))
