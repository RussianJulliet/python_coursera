n = int(input())
i = 1
while i < n:
    if n // i == n / i:
        res = n // i
    i = i + 1
print(res)
