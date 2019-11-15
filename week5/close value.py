n = int(input())
numList = list(map(int, input().split()))
x = int(input())
b = []
for i in range(n):
    cl = abs(numList[i] - x)
    b.append(cl)
k = min(b)
ind = b.index(k)
print(numList[ind])
