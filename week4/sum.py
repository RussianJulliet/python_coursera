def summ(a, b):
    if b == 0:
        return a
    return summ(a + 1, b - 1)


a = int(input())
b = int(input())
print(summ(a, b))
