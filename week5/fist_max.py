def first_max(numList):
    k = 0
    m = numList[0]
    for i in range(1, len(numList)):
        if numList[i] > m:
            m = numList[i]
            k = i
    print(m, k)


numList = list(map(int, input().split()))
first_max(numList)
