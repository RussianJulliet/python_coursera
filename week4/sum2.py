def summ(n):
    s = n
    if n == 0:
        return 0
    else:
        n = int(input())
        return s + summ(n)


n = int(input())
print(summ(n))
