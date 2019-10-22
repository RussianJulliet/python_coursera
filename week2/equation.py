a, b = int(input()), int(input())
c, d = int(input()), int(input())
if (a == 0) and (b == 0):
    print('INF')
elif (c != 0) and (d != 0) and (a / c == b / d):
    print('NO')
else:
    answer = (-1) * b // a
    ans = (-1) * b / a
    if answer == ans:
        print(answer)
    else:
        print('NO')
