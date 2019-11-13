def swap(numList):
    for i in range(len(numList) // 2):
        k = len(numList) - 1 - i
        numList[i], numList[k] = numList[k], numList[i]
    print(*numList)


numList = list(map(int, input().split()))
swap(numList)
