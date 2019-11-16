numList = list(map(int, input().split()))
cnt = -1
for i in numList:
    if numList.count(i) > cnt:
        cnt = numList.count(i)
        k = i
print(k)
