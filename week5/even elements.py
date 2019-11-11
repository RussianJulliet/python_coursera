numList = list(map(int, input().split()))
for i in tuple(numList):
    if i % 2 == 0:
        print(i, end=' ')
