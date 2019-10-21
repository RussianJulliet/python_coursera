a, b, c = int(input()), int(input()), int(input())
if b <= a:
    (a, b) = (b, a)
if c <= a:
    (a, c) = (c, a)
if c <= b:
    (b, c) = (c, b)
if a == b == c:
    print(3)
elif (a == b) or (b == c):
    print(2)
else:
    print(0)
