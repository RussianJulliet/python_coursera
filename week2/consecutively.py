n = int(input())
count = 1
max_count = 1
while n != 0:
    s = n
    n = int(input())
    if s == n:
        count += 1
    else:
        count = 1
    if max_count < count:
        max_count = count
print(max_count)
