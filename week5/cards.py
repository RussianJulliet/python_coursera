n = int(input())
s = 0
for i in range(1, n + 1):
    s = s + i
for t in range(1, n):
    x = int(input())
    s = s - x
print(s)
