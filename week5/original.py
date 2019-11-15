numList = list(map(int, input().split()))
count = 1
for i in range(1, len(numList)):
    if numList[i] != numList[i - 1]:
        count += 1
print(count)
