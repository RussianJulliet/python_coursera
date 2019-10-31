x = int(input())
summa = x
summa_kv = x ** 2
count = 0
while x != 0:
    x = int(input())
    count += 1
    summa += x
    summa_kv += x ** 2
s = (summa / count)
res1 = summa_kv - 2 * s * summa + s * s * count
res2 = (res1 / (count - 1)) ** 0.5
print(res2)
