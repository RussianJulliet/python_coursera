def isPointInArea(x, y):
    return ((x + 1) ** 2 + (y - 1) ** 2 <= 4 and y >= -x and (
            y >= 2 * x + 2)) or (
            (x + 1) ** 2 + (y - 1) ** 2 >= 4 and y <= -x and y <= 2 * x + 2)


x, y = float(input()), float(input())
if isPointInArea(x, y):
    print('YES')
else:
    print('NO')
