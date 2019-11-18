N = int(input())
l1 = list(map(int, input().split()))
l1.sort()
count = 0
l2 = []
i = 0
for n in l1:
    if n >= N:
        i += 1
if i != 0:
    for n in l1:
        if n >= N:
            N = n
            break
    for n in l1:
        if n - N >= 3:
            N = n
            count += 1
    count += 1
print(count)
