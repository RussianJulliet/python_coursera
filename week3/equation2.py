a, b, c = float(input()), float(input()), float(input())
if a == 0 and b == 0 and c == 0:
    print(3)
elif a == 0 and b == 0:
    print(0)
elif a == 0:
    x = -c / b
    print(1, x)
else:
    D = b ** 2 - 4 * a * c
    if D > 0:
        x1 = (-b + D ** 0.5) / (2 * a)
        x2 = (-b - D ** 0.5) / (2 * a)
        if x2 - x1 > 0:
            print(2, x1, x2)
        else:
            print(2, x2, x1)
    elif D == 0:
        x1 = (-b + D ** 0.5) / (2 * a)
        print(1, x1)
    else:
        print(0)
