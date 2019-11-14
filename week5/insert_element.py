def insert(numList, kc):
    k = kc[0]
    c = kc[1]
    numList.append(c)
    for i in range(len(numList) - 2, k - 1, -1):
        numList[i + 1] = numList[i]
    numList[k] = c
    return numList


numList = list(map(int, input().split()))
kc = list(map(int, input().split()))
print(*insert(numList, kc))
