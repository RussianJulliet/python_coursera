a = int(input())
b = int(input())
c = int(input())
t = a ** 2 + b ** 2 + c ** 2
if a >= b and a >= c:
    maxim = a
elif b >= c:
    maxim = b
else:
    maxim = c

if not ((a < b + c) and (b < a + c) and (c < b + a)):
    print('impossible')
elif maxim ** 2 < t - maxim ** 2:
    print('acute')
elif maxim ** 2 > t - maxim ** 2:
    print('obtuse ')
elif maxim ** 2 == t - maxim ** 2:
    print('rectangular')
