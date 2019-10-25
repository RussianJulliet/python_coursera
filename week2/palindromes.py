k = int(input())
i = 1
count = 0
while i <= k:
    string = ''
    s = i
    while s > 0:
        string += str(s % 10)
        s //= 10
    if int(string) == i:
        count += 1
    i += 1
print(count)
