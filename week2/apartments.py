x = int(input())
y = int(input())
if x <= y:
    count = y - x + 1
    if (x - 1) % count == 0:
        print('YES')
    else:
        print('NO')
else:
    print('NO')
