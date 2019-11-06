import math


def distance(x1, x2, y1, y2):
    dx = x2 - x1
    dy = y2 - y1
    r = dx ** 2 + dy ** 2
    return math.sqrt(r)


def perimeter(a, b, c):
    p = a + b + c
    return p


x1, y1 = float(input()), float(input())
x2, y2 = float(input()), float(input())
x3, y3 = float(input()), float(input())
a = distance(x1, x2, y1, y2)
b = distance(x1, x3, y1, y3)
c = distance(x2, x3, y2, y3)
print(perimeter(a, b, c))
