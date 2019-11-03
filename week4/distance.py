import math


def distance(x1, x2, y1, y2):
    dx = x2 - x1
    dy = y2 - y1
    r = dx ** 2 + dy ** 2
    return math.sqrt(r)


x1, y1 = float(input()), float(input())
x2, y2 = float(input()), float(input())
print(distance(x1, x2, y1, y2))
