n = int(input())
k = 0
s = n
while n != 0:
    n = int(input())
    if n > s:
        k += 1
    s = n
print(k)
