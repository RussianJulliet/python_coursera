p = int(input())
x = int(input())
y = int(input())
k = int(input())
summa = 100 * x + y
while k != 0:
    summa = int(summa + summa * p / 100)
    k -= 1
rub = summa // 100
cop = summa % 100
print(rub, cop)
