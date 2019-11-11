numList = list(map(int, input().split()))
a = max(numList)
b = 0
for i in range(len(numList)):
    if numList[i] == a:
        b = i
print(a, b)
