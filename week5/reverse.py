def reverse(numList):
    for i in range(len(numList) - 1, -1, -1):
        print(numList[i], end=' ')


numList = list(map(int, input().split()))
reverse(numList)
