def dlt(numList, k):
    for i in range(k, len(numList) - 1):
        numList[i] = numList[i + 1]
    numList.pop()
    return numList


numList = list(map(int, input().split()))
k = int(input())
print(*dlt(numList, k))
