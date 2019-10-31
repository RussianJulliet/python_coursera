a, b, c = float(input()), float(input()), float(input())
D = b ** 2 - 4 * a * c
if D > 0:
    x1 = (-b + D ** 0.5) / (2 * a)
    x2 = (-b - D ** 0.5) / (2 * a)
    if x2 - x1 > 0:
        print(x1, x2)
    else:
        print(x2, x1)
elif D == 0:
    x1 = (-b + D ** 0.5) / (2 * a)
    print(x1)
