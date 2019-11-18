S, N = [int(s) for s in input().split()]
users = []
i = 0
while i < N:
    x = int(input())
    users.append(x)
    i += 1
users.sort()
k = 0
summ = 0
count = 0
for k in users:
    if summ + k <= S:
        summ += k
        count += 1
print(count)
