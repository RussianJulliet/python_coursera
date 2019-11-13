def min_pos(numList):
    l = []
    for i in range(1, len(numList)):
        if numList[i] > 0:
            l.append(numList[i])
    first_min(l)


def first_min(numList):
    m = numList[0]
    for i in range(1, len(numList)):
        if numList[i] < m:
            m = numList[i]
    print(m)


numList = list(map(int, input().split()))
min_pos(numList)
