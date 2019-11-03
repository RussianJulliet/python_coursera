def min4(a, b, c, d):
    minim = min(a, b)
    minim = min(minim, c)
    minim = min(minim, d)
    return minim


a, b, c, d = int(input()), int(input()), int(input()), int(input())
print(min4(a, b, c, d))
