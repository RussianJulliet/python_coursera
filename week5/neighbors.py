def nb(numList):
    i = 1
    count = 0
    while i < len(numList) - 1:
        if numList[i] > numList[i - 1] and numList[i] > numList[i + 1]:
            count += 1
        i += 1
    return count


numList = list(map(int, input().split()))
print(nb(numList))
