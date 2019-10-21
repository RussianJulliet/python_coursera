x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
ost1 = x1 % 2
ost2 = y1 % 2
if x2 % 2 == (ost1 + 1) % 2:
    if y2 % 2 == ost2:
        print('NO')
    else:
        print('YES')
elif x2 % 2 == ost1:
    if y2 % 2 == (ost2 + 1) % 2:
        print('NO')
    else:
        print('YES')
