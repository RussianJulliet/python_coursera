numList = list(map(int, input().split()))
count = 0
for i in tuple(numList):
    if i > 0:
        count += 1
print(count)
