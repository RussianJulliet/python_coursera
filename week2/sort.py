a, b, c = int(input()), int(input()), int(input())
if b <= a:
    (a, b) = (b, a)
if c <= a:
    (a, c) = (c, a)
if c <= b:
    (b, c) = (c, b)
print(a, b, c)
