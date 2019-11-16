numList = list(map(int, input().split()))
if len(numList) > 4:
    max1 = max(numList)
    numList.pop(numList.index(max1))
    max2 = max(numList)
    numList.pop(numList.index(max2))
    max3 = max(numList)
    min1 = min(numList)
    numList.pop(numList.index(min1))
    min2 = min(numList)
    if max1 * max2 * max3 > max1 * min2 * min1:
        print(max1, max2, max3)
    else:
        print(max1, min2, min1)
elif len(numList) == 3:
    print(*numList)
else:
    minn = 10000
    for i in numList:
        if abs(i) < minn:
            minn = i
    for i in numList:
        if i != minn:
            print(i, end=' ')
