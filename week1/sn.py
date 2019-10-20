N = int(input())
A = N // 1000
B = (N // 100) % 10
C = (N // 10) % 10
D = N % 10
print(A * C - B * D + 1)
