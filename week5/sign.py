def sign(numList):
    i = 1
    while i < len(numList) and numList[i - 1] * numList[i] < 0:
        i += 1
    if i != len(numList):
        print(numList[i - 1], numList[i])


numList = list(map(int, input().split()))
sign(numList)
