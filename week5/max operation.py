numList = list(map(int, input().split()))
if len(numList) > 2:
    max1 = max(numList)
    numList.pop(numList.index(max1))
    max2 = max(numList)
    min1 = min(numList)
    numList.pop(numList.index(min1))
    min2 = min(numList)
    if max1 * max2 > min1 * min2:
        print(max2, max1)
    else:
        print(min1, min2)
else:
    a = max(numList)
    b = min(numList)
    print(b, a)
