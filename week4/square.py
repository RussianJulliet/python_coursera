import math


def isPointInSquare(x, y):
    return distance(x, y) <= math.sqrt(2)


def distance(x1, y1):
    r = x1 ** 2 + y1 ** 2
    return math.sqrt(r)


x, y = float(input()), float(input())
if isPointInSquare(x, y):
    print('YES')
else:
    print('NO')
