def first_max(numList):
    k = 0
    m = numList[0]
    for i in range(1, len(numList)):
        if numList[i] > m:
            m = numList[i]
            k = i
    return k


def first_min(numList):
    k = 0
    m = numList[0]
    for i in range(1, len(numList)):
        if numList[i] < m:
            m = numList[i]
            k = i
    return k


numList = list(map(int, input().split()))
ind_maxx = first_max(numList)
ind_minn = first_min(numList)
numList[ind_maxx], numList[ind_minn] = numList[ind_minn], numList[ind_maxx]
print(*numList)
