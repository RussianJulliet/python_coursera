numList = list(map(int, input().split()))
n = int(input())
i = 0
while i < len(numList) and numList[i] - n >= 0:
    i += 1
print(i + 1)
