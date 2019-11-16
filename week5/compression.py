numList = list(map(int, input().split()))
count = 0
for i in range(len(numList)):
    if numList[i] == 0:
        count += 1
    else:
        print(numList[i], end=' ')
for k in range(0, count):
    print(0, end=' ')
