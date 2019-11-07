import math


def sq(c):
    n = int(input())
    if n != 0:
        if math.sqrt(n) - int(math.sqrt(n)) == 0:
            c = 1
            c = sq(c)
            print(n, end=' ')
        else:
            c = sq(c)
    return c


c = 0
k = sq(c)
if k == 1:
    print('')
else:
    print(0)
