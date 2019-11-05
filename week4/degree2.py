def power(a, n):
    deg = 1
    if n == 0:
        return 1
    elif n > 0:
        while n != 0:
            deg = deg * a
            n -= 1
    elif n < 0:
        while n != 0:
            deg = deg / a
            n += 1
    return deg


a = float(input())
n = float(input())
print(power(a, n))
