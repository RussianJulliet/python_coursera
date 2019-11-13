def min_odd(numList):
    l = []
    for i in range(1, len(numList)):
        if numList[i] % 2 == 1:
            l.append(numList[i])
    first_odd(l)


def first_odd(numList):
    m = numList[0]
    for i in range(1, len(numList)):
        if numList[i] < m:
            m = numList[i]
    print(m)


numList = list(map(int, input().split()))
min_odd(numList)
