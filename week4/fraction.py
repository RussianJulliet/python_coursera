def gcd(a, b):
    if b > a:
        return gcd(b, a)
    elif a % b == 0:
        return b
    else:
        return gcd(b, a % b)


def ReduceFraction(n, m):
    nod = gcd(n, m)
    p = n // nod
    q = m // nod
    return p, q


n = int(input())
m = int(input())
print(*ReduceFraction(n, m))
