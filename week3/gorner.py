n = int(input())
x = float(input())
a1 = float(input())
tm = 0
if n == 0:
    print(a1)
else:
    while n != 0:
        a2 = float(input())
        tm = a1 * x + a2
        a1 = tm
        n -= 1
    print(tm)
