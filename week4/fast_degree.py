def power(x, n):
    if n == 0:
        return 1
    elif n % 2 == 0:
        return power(x ** 2, n // 2)
    else:
        return x * power(x, n - 1)


x = float(input())
n = float(input())
print(power(x, n))
