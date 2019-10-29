p = int(input())
x = int(input())
y = int(input())
# pr = (1 + p / 100)
# print(pr)
full_cost = (x * 100 + y) * (100 + p)
rub = int(full_cost) // 10000
cop = int(full_cost) // 100 % 100
print(rub, cop)
