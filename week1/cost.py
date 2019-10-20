A = int(input())
B = int(input())
N = int(input())
cost = A * 100 + B
full_cost = cost * N
print(full_cost // 100, full_cost % 100)
