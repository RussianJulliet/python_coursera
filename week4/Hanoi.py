def Hanoi(n, x, y, c):
    if n > 0:
        Hanoi(n - 1, x, c, y)
        print(n, x, y)
        Hanoi(n - 1, c, y, x)
    return n, x, y


n = int(input())
x = 1
y = 3
c = 2
Hanoi(n, x, y, c)
