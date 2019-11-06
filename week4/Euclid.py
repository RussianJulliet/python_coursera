def gcd(a, b):
    if b > a:
        return gcd(b, a)
    elif a % b == 0:
        return b
    else:
        return gcd(b, a % b)


a = int(input())
b = int(input())
print(gcd(a, b))
