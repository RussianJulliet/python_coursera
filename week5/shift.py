numList = list(map(int, input().split()))
n = len(numList)
t = numList[n - 1]
for i in range(n - 1, 0, -1):
    numList[i] = numList[i - 1]
numList[0] = t
print(*numList)
