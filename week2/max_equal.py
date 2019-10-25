n = int(input())
maxim = 0
count = 0
while n != 0:
    if n > maxim:
        count = 0
        maxim = n
    if n == maxim:
        count += 1
    n = int(input())
print(count)
