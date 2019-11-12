def IsAscending(numList):
    count = 0
    i = 1
    while i < len(numList) and numList[i] > numList[i - 1]:
        i += 1
        count += 1
    return count


numList = list(map(int, input().split()))
if IsAscending(numList) == len(numList) - 1:
    print('YES')
else:
    print('NO')
